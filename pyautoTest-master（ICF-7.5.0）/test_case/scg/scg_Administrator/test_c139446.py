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
test_id = 139446
def test_c139446(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		into_fun(browser, 管理员)
		# 点击系统设定
		browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
		# ssh设置
		# 清除默认输入内容
		browser.find_element_by_xpath('//*[@id="sshport"]').clear()
		browser.find_element_by_xpath('//*[@id="sshport"]').send_keys("22")
		# https设置
		# 清除默认输入内容
		browser.find_element_by_xpath('//*[@id="httpsport"]').clear()
		browser.find_element_by_xpath('//*[@id="httpsport"]').send_keys("22")
		# telent设置
		# 清除默认输入内容
		browser.find_element_by_xpath('//*[@id="telnetport"]').clear()
		browser.find_element_by_xpath('//*[@id="telnetport"]').send_keys("22")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(2)
		# 接受告警
		browser.switch_to_alert().accept()
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		try:
			assert "设置失败" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "设置失败" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])