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

test_id = "139666"

def test_c139666(browser):

	try:
		result1 = get_dut_interface_mac_jyl(dut_name=dev3, interface=interface_name_2).lower()
		login_web(browser, url=dev1)
		add_ip_mac_binding_jyl(browser, ip="13.1.1.3", interface=interface_name_3, mac_add="auto_mac",
							   host_name="manual_host", host="主机83")
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="open")
		info1 = get_static_arp_all(browser)
		print(info1)
		del_bindinglist(browser, index_list="all")
		info2 = get_static_arp_all(browser)
		print(info2)
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="close")

		del_bindinglist(browser, index_list="all")
		del_static_arp(browser, index_list="all")

		try:
			assert ['13.1.1.3', result1, interface_name_3, '主机83'] in info1
			assert ["13.1.1.3"] not in info2
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert ['13.1.1.3', result1, interface_name_3, '主机83'] in info1
			assert ["13.1.1.3"] not in info2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])