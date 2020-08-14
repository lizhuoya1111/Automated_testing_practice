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

test_id = "139592"


def test_c139592(browser):

	try:
		result1 = get_dut_interface_mac_jyl(dut_name=dev2, interface=interface_name_1).lower()
		print(result1)
		shell_cmd = Shell_SSH()
		shell_cmd.connect(hostip=dev2)
		shell_cmd.ping_cmd(ipadd=dev3)
		time.sleep(2)
		shell_cmd.close()
		login_web(browser, url=dev3)
		# arp_list = get_dynamic_arp_all(browser)
		# print(arp_list)
		set_arp_dyn_to_static(browser, ipadd=dev2)
		arp_list_static = get_static_arp_all(browser)
		del_static_arp(browser)
		try:
			assert [dev2, result1, interface_name_1, ''] in arp_list_static
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert [dev2, result1, interface_name_1, ''] in arp_list_static


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev3, dev2])
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])