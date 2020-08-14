import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def import *

test_id = "139492"


def test_c139492(browser):
	try:
		login_web(browser, url=dev5)
		# 点击管理员
		set_dns(browser, dns1="qwert")
		alert = browser.switch_to_alert()
		alert_info = alert.text
		time.sleep(0.5)
		alert.accept()
		# print(alert_info_list)
		try:
			assert "IP格式输入错误，请重新输入" in alert_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP格式输入错误，请重新输入" in alert_info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
