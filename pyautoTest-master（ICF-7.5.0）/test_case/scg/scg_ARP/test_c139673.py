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

test_id = "139673"

def test_c139673(browser):

	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("no ip add 23.1.1.3")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()
		for x in range(1, 4):
			bridge_add_jyl(browser, bridge_name="br_"+str(x))
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_4)
		bridge_edit_interface_jyl(browser, bridge_interface="br_2", interface=interface_name_5)
		bridge_edit_interface_jyl(browser, bridge_interface="br_3", interface=interface_name_6)
		get_info1 = get_br_mac_byname(browser, br_name="br_1")
		print(get_info1)
		get_info2 = get_br_mac_byname(browser, br_name="br_2")
		print(get_info2)
		get_info3 = get_br_mac_byname(browser, br_name="br_3")
		print(get_info3)

		get_info4 = get_bri_mac_byname_jyl(browser, br_name="br_1").lower()
		print(get_info4)
		get_info5 = get_bri_mac_byname_jyl(browser, br_name="br_2").lower()
		print(get_info5)
		get_info6 = get_bri_mac_byname_jyl(browser, br_name="br_3").lower()
		print(get_info6)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("work-mode route")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode route")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("work-mode route")
		a.execute("ip add 23.1.1.3/24")
		a.execute("exit")
		a.execute("no interface bridge br_1")
		a.execute("no interface bridge br_2")
		a.execute("no interface bridge br_3")
		a.execute("exit")
		a.close()

		try:
			assert get_info1 in get_info4
			assert get_info2 in get_info5
			assert get_info3 in get_info6
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert get_info1 in get_info4
			assert get_info2 in get_info5
			assert get_info3 in get_info6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev3)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])