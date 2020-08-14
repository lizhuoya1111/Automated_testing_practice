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
test_id = 139430


def test_c139430(browser):
	try:
		login_web(browser, url=dev1)
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# browser.switch_to.frame("lefttree")
		# # 点击系统
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(系统管理).click()
		# # 点击物理接口
		# browser.find_element_by_xpath(管理员).click()
		# # 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
		time.sleep(3)
		browser.find_element_by_xpath('//*[@id="profilename"]').send_keys("tom")
		browser.find_element_by_xpath('//*[@id="description"]').send_keys("zxcvbnmlkjhgfdsaqwertyuiopzxcvbnmlkjhg"
		                                                                  "fdsaqwertyuiopzxcvbnmlkjhgfdsaqwertyuiop0"
		                                                                  "12345678901234567890123456789012345678901"
		                                                                  "2345678zxcvbnmlkjhgfdsaqw123ertyuiopzxcvb"
		                                                                  "nmlkjhgfdsaqwertyuiopzxcvbnmlkjhgfdsaqwert"
		                                                                  "yuiop0123456789012345678901234567890123456"
		                                                                  "789012345678")
		browser.find_element_by_xpath('//*[@id="configsystem_0"]').click()
		browser.find_element_by_xpath('//*[@id="reportsystem_0"]').click()
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 获取提示框信息
		time.sleep(2)
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		try:
			assert "描述格式输入错误" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "描述格式输入错误" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
