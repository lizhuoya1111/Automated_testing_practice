import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139716"

def test_c139716(browser):

	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3 count 10")
		a.execute("exit")
		a.close()

		get_info1 = get_dynamic_arp_all(browser)
		# print(get_info1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("ip address 13.1.1.5 24")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.3 count 10")
		a.close()

		get_info2 = get_dynamic_arp_all(browser)
		# print(get_info2)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.5")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_3+".33")
		a.execute("ip address 13.1.1.6 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("switchmode  access")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.3 count 10")
		a.close()

		get_info3 = get_dynamic_arp_all(browser)
		# print(get_info3)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".33")
		a.execute("no ip address 13.1.1.6")
		a.execute("ip address 13.1.1.7 24")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.3 count 10")
		a.close()

		get_info4 = get_dynamic_arp_all(browser)
		# print(get_info4)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_3+".33")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3)

		time.sleep(5)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_1")
		a.execute("ip address 13.1.1.10 24")
		a.execute("exit")
		a.close()

		del_dynamic_arp(browser, index_list="all")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3 count 10")
		a.execute("exit")
		a.close()

		login_web(browser, url=dev3)
		get_info5 = get_dynamic_arp_all(browser)
		# print(get_info5)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_1")
		a.execute("no ip address 13.1.1.10")
		a.execute("ip address 13.1.1.11 24")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.3 count 10")
		a.execute("exit")
		a.close()

		get_info6 = get_dynamic_arp_all(browser)
		# print(get_info6)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.1 24")
		a.close()


		try:
			assert get_info1 != get_info2
			assert get_info3 != get_info4
			assert get_info5 != get_info6
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert get_info1 != get_info2
			assert get_info3 != get_info4
			assert get_info5 != get_info6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])