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


test_id = 140548
def test_c140548(browser):
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
		a.execute("interface bridge br_1")
		a.execute("bridge-member "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.execute("snat enable")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(10)
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(5)
		a.close()
		result1 = a.output()
		a.close()
		print(result1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.close()

		time.sleep(0.5)

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
