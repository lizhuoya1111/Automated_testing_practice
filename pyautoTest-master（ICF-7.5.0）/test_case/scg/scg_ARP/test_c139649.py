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

test_id = "139649"


def test_c139649(browser):

	try:
		login_web(browser, url=dev1)
		set_dynamic_arp_to_static_arp_jyl(browser, dynamic_arp_ip="10.2.2.1")
		get_into_static_arp_jyl(browser)
		# 点击启用绑定同步
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		get_into_ip_mac_binding_jyl(browser)
		webinfo = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text.rstrip()
		delete_static_arp_jyl(browser, static_arp_ip="10.2.2.1")
		# 点击关闭绑定同步
		browser.find_element_by_xpath('//*[@id="status"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "00" in webinfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "00" in webinfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])