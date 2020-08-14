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


test_id = 140550
def test_c140550(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("no ip address 20.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()
		bridge_edit_interface_jyl(browser, bridge_interface="br_0", interface=interface_name_4)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("ip address 20.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("shutdown")
		a.execute("exit")
		a.close()

		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 20.1.1.1 -c 5')
		# print(result1)
		# 关闭连接
		ssh.close()
		time.sleep(5)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("no shutdown")
		a.execute("exit")
		a.close()

		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 20.1.1.1 -c 5')
		# print(result2)
		# 关闭连接
		ssh.close()
		time.sleep(5)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("no ip address 20.1.1.1")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("work-mode route")
		a.execute("ip address 20.1.1.1 24")
		a.execute("exit")
		a.close()

		try:
			assert "loss" in result1
			assert "ms" in result2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "loss" in result1
			assert "ms" in result2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
