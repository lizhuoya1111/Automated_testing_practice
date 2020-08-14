import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "141844"


def test_c141844(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="12", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2 + ".12", ipadd="12.1.1.1", mask="24")
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="11", work_mode="transprent")
		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="11", work_mode="transprent")

		bridge_add_jyl(browser, bridge_name="br_1")
		print(interface_name_3+".11")
		print(interface_name_4 + ".11")
		bri_edit_interface(browser, interface=interface_name_3+".11", bridge_interface="br_1")
		bri_edit_interface(browser, interface=interface_name_4+".11", bridge_interface="br_1")
		bridge_ip_add(browser, bridge_interface="br_1", ip="20.1.1.111", mask="24")




		# 81的命令行,将2 3口设备为access模式
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_3)
		shell_81.execute("switchmode  access")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  access")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_2)
		shell_81.execute("switchmode  access")
		shell_81.close()


		# 82上添加的路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("ip route 20.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()
		# PC2上添加的路由
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route add -net 12.1.1.0/24 gw 20.1.1.111')
		shell_pc2.close()
		# 加延迟，为了等待网桥生效
		time.sleep(6)
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('ping 12.1.1.2 -c 20 -i 0.2')

		shell_pc2.close()

		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		result = shell_pc2.execute('ping 12.1.1.2 -c 5 -i 0.5')
		print(result)
		shell_pc2.close()



		try:
			assert "ttl" in result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result


		delete_bridge(browser)
		# 删除子接口
		del_vlan_inte_all(browser)
		# 还原物理接口地址
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='13.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='24')
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_3)
		shell_81.execute("switchmode  trunk")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  trunk")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_2)
		shell_81.execute("switchmode  trunk")
		shell_81.close()

		# 82上删除的路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("no ip route 20.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()
		# PC2上删除的路由
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route del -net 12.1.1.0/24 gw 20.1.1.111')
		shell_pc2.close()




	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])