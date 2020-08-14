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
test_id = 139427


def test_c139427(browser):
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
		browser.find_element_by_xpath('//*[@id="profilename"]').send_keys("权限")
		browser.find_element_by_xpath('//*[@id="description"]').send_keys("admin_profile")
		browser.find_element_by_xpath('//*[@id="configsystem_0"]').click()
		browser.find_element_by_xpath('//*[@id="reportsystem_0"]').click()
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 获取提示框信息
		web_info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(web_info1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		try:
			assert web_info1 == "不合法的profile名"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info1 == "不合法的profile名"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
