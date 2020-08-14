import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
test_id = 139435


def test_c139435(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin(browser, auth_database="local", admin_name="bob", temp="log_profile", https="yes",
				  telent="yes", ssh="yes", console="yes", password="admin@139", confirm_password="admin@139",
				  status="enable", interface=interface_name_1, online_num="3", ip1="2.2.2.256/32")

		# 获取提示框信息
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		try:
			assert "IP格式输入错误" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "IP格式输入错误" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
