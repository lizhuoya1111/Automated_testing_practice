

import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *

test_id = 142956
def test_c142956(browser):
	try:
		login_web(browser, url=dev1)
		add_smtp_alarm_jyl(browser, smtp_server="192.168.15.2.6", server="ip", user_name="admin", password="123456",
						   save="yes")
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info1 = alert.text
		# print(web_info1)
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "IP格式输入错误" in web_info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP格式输入错误" in web_info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
