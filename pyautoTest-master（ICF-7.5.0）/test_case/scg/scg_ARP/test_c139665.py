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

test_id = "139665"

def test_c139665(browser):

	try:
		login_web(browser, url=dev1)
		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_3, source_mac_binding="enable",
									 policy_for_undefined_host="block")
		add_ip_mac_binding_jyl(browser, ip="13.1.1.3", interface=interface_name_3, mac_add="auto_mac",
							   host_name="manual_host", host="主机83")
		edit_ip_mac_banding_jyl(browser, banding_ip="13.1.1.3", ip="13.1.1.5", interface=interface_name_3)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(5)
		result1 = a.output()
		del_bindinglist(browser, index_list="all")
		del_static_arp(browser, index_list="all")
		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_3, source_mac_binding="disenable",
									 policy_for_undefined_host="allow")

		try:
			assert "Unreachable" in result1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "Unreachable" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])