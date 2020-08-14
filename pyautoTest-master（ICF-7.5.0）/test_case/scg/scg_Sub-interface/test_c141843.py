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


test_id = "141843"


def test_c141843(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")

		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="11", work_mode="transprent")
		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="11", work_mode="transprent")

		bridge_add_jyl(browser, bridge_name="br_1")
		# print(interface_name_3+".11")
		# print(interface_name_4 + ".11")
		bri_edit_interface(browser, interface=interface_name_3+".11", bridge_interface="br_1")
		bri_edit_interface(browser, interface=interface_name_4+".11", bridge_interface="br_1")

		login_web(browser, url=dev3)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='20.1.1.100', mask='24')


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
		shell_81.close()


		time.sleep(5)
		# PC2上添加13.1.1.0的路由
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		result = shell_pc2.execute('ping 20.1.1.100 -c 8 -i 0.1')
		shell_pc2.close()



		try:
			assert "ttl" in result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result

		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip='20.1.1.100')
		login_web(browser, url=dev1)
		delete_bridge(browser)
		# 删除子接口
		del_vlan_inte_all(browser)
		# 还原物理接口地址
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='13.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_3)
		shell_81.execute("switchmode  trunk")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  trunk")
		shell_81.close()



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])