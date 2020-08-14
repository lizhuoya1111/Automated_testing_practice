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


test_id = 140547
def test_c140547(browser):
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
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.execute("interface bridge br_1")
		a.execute("exit")
		a.execute("interface bridge br_2")
		a.execute("exit")
		a.close()

		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3)

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.2")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_2+".11")
		a.execute("ip address 12.1.1.2 24")
		a.execute("exit")
		a.execute("interface gig "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_2+".11")
		a.execute("ip address 12.1.1.3 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 12.1.1.3")
		time.sleep(10)
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("ping 12.1.1.3")
		time.sleep(3)
		result1 = a.output()
		a.close()
		# print(result1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.execute("no interface bridge br_1")
		a.execute("no interface bridge br_2")
		a.execute("exit")
		a.close()


		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_2+".11")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.2 24")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_2+".11")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 13.1.1.3 24")
		a.close()

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2. dev3])
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
