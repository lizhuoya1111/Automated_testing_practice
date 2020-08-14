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


test_id = 140519
def test_c140519(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_2+".3")
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_3+".3")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("switchmode access")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(4)
		result1 = a.output()
		a.close()
		# print(result1)

		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("no interface vlan "+interface_name_2+".3")
		b.execute("no interface vlan "+interface_name_3+".3")
		b.execute("interface gigabitethernet "+interface_name_2)
		b.execute("ip address 12.1.1.1 24")
		b.execute("exit")
		b.execute("interface gigabitethernet "+interface_name_3)
		b.execute("ip address 13.1.1.1 24")
		b.execute("exit")
		b.close()

		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_2)
		b.execute("ip address 12.1.1.1 24")
		b.execute("exit")
		b.execute("interface gigabitethernet "+interface_name_3)
		b.execute("ip address 13.1.1.1 24")
		b.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.execute("exit")
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
		reload(hostip=[dev1, dev2, dev3])
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
