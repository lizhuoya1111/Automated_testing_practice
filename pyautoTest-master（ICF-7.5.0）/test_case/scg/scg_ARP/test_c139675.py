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

test_id = "139675"

def test_c139675(browser):

	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3 count 10")
		a.execute("exit")
		a.close()
		mac_2 = get_dut_interface_mac_jyl(dut_name=dev1, interface=interface_name_3).lower()

		get_info1 = get_dynamic_arp_all(browser)
		# print(get_info1)

		try:
			assert ['13.1.1.1', mac_2, interface_name_2, ''] in get_info1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert ['13.1.1.1', mac_2, interface_name_2, ''] in get_info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])