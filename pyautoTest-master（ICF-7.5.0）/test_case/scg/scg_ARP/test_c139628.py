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

test_id = "139628"


def test_c139628(browser):

	try:
		login_web(browser, url=dev1)
		add_static_arp_jyl(browser, ip="A.B.C.D", interface=interface_name_4, mac_add="manual_mac",
						   mac="00:16:90:E3:80:50", host_name="manual_host", host="jia_1")
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info1 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		browser.refresh()
		add_static_arp_jyl(browser, ip="X.X.X.255", interface=interface_name_4, mac_add="manual_mac",
						   mac="00:16:90:E3:80:50", host_name="manual_host", host="jia_1")
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info2 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		browser.refresh()
		add_static_arp_jyl(browser, ip="X.X.X.0", interface=interface_name_4, mac_add="manual_mac",
						   mac="00:16:90:E3:80:50", host_name="manual_host", host="jia_1")
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info3 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		try:
			assert "错误" in web_info1
			assert "错误" in web_info2
			assert "错误" in web_info3
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "错误" in web_info1
			assert "错误" in web_info2
			assert "错误" in web_info3


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])