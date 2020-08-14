import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_route import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
test_id = "139578"
def test_c139578(browser):
	try:
		login_web(browser, url=dev1)
		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="39", count="5", ping_wait_time="2",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info1 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="18025", count="5", ping_wait_time="2",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info2 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="40", count="4", ping_wait_time="2",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info3 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="40", count="10000", ping_wait_time="2",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info4 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="40", count="5", ping_wait_time="0",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info5 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		fail_diag_ping(browser, ipadd="13.1.1.3", packersize="40", count="5", ping_wait_time="3601",
						  interface=interface_name_3)
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info6 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()


		try:
			assert "错误" in web_info1
			assert "错误" in web_info2
			assert "错误" in web_info3
			assert "错误" in web_info4
			assert "错误" in web_info5
			assert "错误" in web_info6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "错误" in web_info1
			assert "错误" in web_info2
			assert "错误" in web_info3
			assert "错误" in web_info4
			assert "错误" in web_info5
			assert "错误" in web_info6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])