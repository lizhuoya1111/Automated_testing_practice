import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140518
def test_c140518(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.2")
		a.execute("ip address 21.1.1.4 24")
		a.execute("exit")
		a.close()

		ssh = SSH("10.1.1.212", 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 21.1.1.4 -c 5 -i 0.1')

		ssh = SSH("10.1.1.213", 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 21.1.1.4 -c 5 -i 0.1')

		birdge_edit_interface_delete_jyl(browser, interface=interface_name_2, bridge_interface="br_0")

		ssh = SSH("10.1.1.212", 'root', 'root', 22)
		ssh.connect()
		result3 = ssh.execute('ping 21.1.1.4 -c 5 -i 0.1')
		# print(result3)

		ssh = SSH("10.1.1.213", 'root', 'root', 22)
		ssh.connect()
		result4 = ssh.execute('ping 21.1.1.4 -c 5 -i 0.1')
		# print(result4)

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 21.1.1.4")
		a.execute("ip address 12.1.1.2 24")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.close()

		try:
			assert "ms" in result1
			assert "ms" in result2
			assert "loss" in result3
			assert "loss" in result4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "ms" in result2
			assert "loss" in result3
			assert "loss" in result4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2])
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
