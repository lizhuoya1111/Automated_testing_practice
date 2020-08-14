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
test_id = 21609
def test_admin_user_add(browser):
	# 登录函数
	login_web(browser)
	# 点击管理员
	browser.find_element_by_xpath(管理员).click()
	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(8)
	# 获取页面配置数
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	i = 1
	while i < int(num1):
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[11]/a[2]/img').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		i += 1
	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	# 点击管理员权限
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(8)
	# 获取页面配置数
	num2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	i = 3
	while i < int(num2):
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[6]/a[2]/img').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		i += 1

	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 获取admin管理员在线数
	web_info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]').text
	print(web_info1)
	# 点击online/online num num
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
	time.sleep(5)
	# 获取实际在线管理员数
	web_info2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	print(web_info2)
	# 添加一个profile
	add_admin_profile(browser, profile_name="aaa", desc="aaa权限", cfg="读写", report="读写")
	# 添加一个管理员
	add_admin(browser, admin_name="bob", temp="aaa")
	# 登录函数
	login_web(browser, username="bob")
	# 点击管理员
	browser.find_element_by_xpath(管理员).click()
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	# 获取admin管理员在线数
	web_info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]').text
	print(web_info1)
	# 点击online/online num num
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
	time.sleep(5)
	# 获取实际在线管理员数
	web_info4 = browser.find_element_by_xpath('//*[@id="rules_count"]').text

	try:
		assert web_info2 in web_info1
		assert web_info4 in web_info3
		rail_pass(178, test_id)
	except:
		rail_fail(178, test_id)
		assert web_info2 in web_info1
		assert web_info4 in web_info3


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21609.py"])