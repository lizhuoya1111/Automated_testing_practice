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
test_id = 139440


def test_c139440(browser):
	try:
		# 登录函数
		login_web(browser, url=dev5)
		into_fun(browser, 管理员)
		# 点击系统设定
		browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
		time.sleep(3)
		browser.find_element_by_xpath('//*[@id="telnetport"]').clear()
		browser.find_element_by_xpath('//*[@id="telnetport"]').send_keys("65536")
		browser.find_element_by_xpath('//*[@id="telnettimeout"]').clear()
		browser.find_element_by_xpath('//*[@id="telnettimeout"]').send_keys("86401")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(3)
		# 获取提示框信息
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		alert.accept()
		sleep(1)

		try:
			assert "输入错误" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "输入错误" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev5)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
