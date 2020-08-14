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

test_id = "139630"


def test_c139630(browser):

	try:
		login_web(browser, url=dev1)
		add_static_arp_jyl(browser, ip="192.165.12.3", interface=interface_name_4, mac_add="manual_mac",
						   mac="45:16:90:E3:80:50", host_name="manual_host", host="<>&?\#$")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info1 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		try:
			assert "只允许" in web_info1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "只允许" in web_info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])