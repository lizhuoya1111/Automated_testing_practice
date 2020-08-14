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


test_id = "139478"



def test_c139478(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		for x in [":", "/", "！@#￥%%&×（）"]:
			edit_sysinfo(browser, hostname=x)
			alert = browser.switch_to_alert()
			alert_info = alert.text
			time.sleep(0.5)
			alert.accept()
			# print(alert_info)
			if "主机名只允许" in alert_info:
				result = True
			else:
				result = False
				break

		try:
			assert result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])