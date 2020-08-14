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

test_id = "139481"
# location栏输入超过256个英文/128个中文/验证能否提交成功，查看log
# 不能提交


def test_c139481(browser):
	try:
		login_web(browser, url=dev5)
		# 点击管理员
		edit_sysinfo(browser, location=str_257_en)
		alert1 = browser.switch_to_alert().text
		time.sleep(0.5)
		browser.switch_to_alert().accept()
		# print(alert1)
		edit_sysinfo(browser, location=str_85_ch+str_85_ch)
		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(info1)




		try:
			assert "地点长度错误，请重新输入" in alert1 and "字串长度超过有效范围:[0-256]" in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "地点长度错误，请重新输入" in alert1 and "字串长度超过有效范围:[0-256]" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])