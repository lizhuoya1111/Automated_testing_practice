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
from page_obj.scg.scg_def import *


test_id = "141850"


def test_c141850(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")


		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="20", work_mode="transprent")
		# add_vlan_inte_add(browser, interface_name=interface_name_2 + ".12", ipadd="12.1.1.1", mask="24")
		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="20", work_mode="transprent")
		# 将两个透明子接口加到一个网桥中
		bridge_add_jyl(browser, bridge_name="br_1")
		bri_edit_interface(browser, interface=interface_name_2+".20", bridge_interface="br_1")
		bri_edit_interface(browser, interface=interface_name_4+".20", bridge_interface="br_1")

		# 把81的5口，也加进来，设置为vlan21
		change_physical_interface_workmode_wxw(browser, interface=interface_name_5,
		                                       route="yes", trans='no')
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="21", work_mode="transprent")
		# add_vlan_inte_add(browser, interface_name=interface_name_2 + ".12", ipadd="12.1.1.1", mask="24")
		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="21", work_mode="transprent")
		# 将两个透明子接口加到一个网桥中
		bridge_add_jyl(browser, bridge_name="br_2")
		bri_edit_interface(browser, interface=interface_name_2 + ".21", bridge_interface="br_2")
		bri_edit_interface(browser, interface=interface_name_5 + ".21", bridge_interface="br_2")

		# 81的命令行,修改接口的switchmode
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  access")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_5)
		shell_81.execute("switchmode  access")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_2)
		shell_81.execute("switchmode  trunk")
		shell_81.close()

		login_web(browser, url=dev2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.2")
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="20", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2 + ".20", ipadd="20.1.1.100", mask="24")

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="21", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2 + ".21", ipadd="21.1.1.100", mask="24")
		switch_vlan_interface_snat(browser, vlan_interface=interface_name_2 + ".20", snat="open")


		# 加延迟，为了等待网桥生效
		time.sleep(5)
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('ping 20.1.1.100 -c 20 -i 0.2')
		shell_pc2.close()
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		result = shell_pc2.execute('ping 20.1.1.100 -c 5 -i 0.5')
		print(result)
		shell_pc2.close()

		shell_pc2 = SSH('10.1.1.212', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('ping 21.1.1.100 -c 20 -i 0.2')
		shell_pc2.close()

		shell_pc2 = SSH('10.1.1.212', 'root', 'root', 22)
		shell_pc2.connect()
		result1 = shell_pc2.execute('ping 21.1.1.100 -c 5 -i 0.5')
		print(result1)
		shell_pc2.execute('route add -net 20.1.1.0/24 gw 21.1.1.100')
		result2 = shell_pc2.execute('ping 20.1.1.2 -c 5 -i 0.5')
		print(result2)
		shell_pc2.close()



		try:
			assert "ttl" in result2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result2

		del_vlan_inte_all(browser)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.2', mask='24')

		login_web(browser, url=dev1)
		delete_bridge(browser)
		delete_bridge(browser)
		# 删除子接口
		del_vlan_inte_all(browser)
		# 还原物理接口地址
		# add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='13.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='24')

		change_physical_interface_workmode_wxw(browser, interface=interface_name_5,
		                                       route="no", trans='yes')

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

		shell_pc2 = SSH('10.1.1.212', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route del -net 20.1.1.0/24 gw 21.1.1.100')
		shell_pc2.close()




	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])