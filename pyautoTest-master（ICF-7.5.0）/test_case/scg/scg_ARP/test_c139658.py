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

test_id = "139658"

def test_c139658(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1 count 10")
		a.execute("exit")
		set_dynamic_arp_to_static_arp_jyl(browser, dynamic_arp_ip="13.1.1.3")
		get_into_static_arp_jyl(browser)
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		del_static_arp(browser, index_list="all")
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		infor1 = get_binding_all(browser)
		print(infor1)

		try:
			assert ['13.1.1.10'] not in infor1
			rail_pass(test_run_id, test_id)
		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert ['13.1.1.10'] not in infor1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])