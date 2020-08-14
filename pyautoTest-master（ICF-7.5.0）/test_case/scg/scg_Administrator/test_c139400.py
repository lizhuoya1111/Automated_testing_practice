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

test_id = 139400

def test_c139400(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		# # 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到左侧frame
		# browser.switch_to.frame("lefttree")
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[text()="系统管理"]/../ul').is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(系统管理).click()
		# browser.find_element_by_xpath(管理员).click()
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		# 点击管理员列表
		browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
		# 获取admin管理员在线数
		web_info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]').text
		# print(web_info1)
		# 点击online/online num num
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
		time.sleep(5)
		# 获取实际在线管理员数
		web_info2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		# print(web_info2)
		# 添加一个profile
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
		time.sleep(2)
		add_admin(browser, auth_database="local", admin_name="bob", temp="aaa", https="yes", telent="yes", ssh="yes",
				  console="yes", password="admin@139", confirm_password="admin@139", status="enable",
				  interface=interface_name_1, online_num="3", ip1="0.0.0.0/0")
		sign_out_jyl(browser)
		# 登录函数
		login_web(browser, url=dev1, username="bob")
		# # 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到左侧frame
		# browser.switch_to.frame("lefttree")
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[text()="系统管理"]/../ul').is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(系统管理).click()
		# browser.find_element_by_xpath(管理员).click()
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		# 点击管理员列表
		browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
		# 获取admin管理员在线数
		web_info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]').text
		# print(web_info1)
		# 点击online/online num num
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
		time.sleep(5)
		# 获取实际在线管理员数
		web_info4 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		sign_out_jyl(browser)
		# 登录函数
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert web_info2 in web_info1
			assert web_info4 in web_info3
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info2 in web_info1
			assert web_info4 in web_info3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])