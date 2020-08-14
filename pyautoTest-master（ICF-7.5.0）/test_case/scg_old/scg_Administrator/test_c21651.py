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
test_id = 21651
def test_admin_user_add(browser):
	# 登录函数
	login_web(browser)
	# 点击管理员
	browser.find_element_by_xpath(管理员).click()
	time.sleep(2)
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

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# 点击系统设定
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').clear()
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').send_keys("86401")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(3)
	# 获取web信息
	web_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	print(web_info)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	try:
		assert "冻结时间取值范围" in web_info
		rail_pass(178, test_id)
	except:
		rail_fail(178, test_id)
		assert "冻结时间取值范围" in web_info


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21651.py"])