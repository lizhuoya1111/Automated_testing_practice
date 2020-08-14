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

test_id = 21546
def test_admin_user_add(browser):
	# 登录函数
	login_web(browser)

	language_switch(browser, language="English")
	# 定位到左侧frame
	browser.switch_to.frame("lefttree")

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

	time.sleep(2)
	for y in range(1, 11):
		add_admin_profile(browser, profile_name='aaa'+str(y), desc="aaa权限", cfg="读写", report="读写")

	# 获取web页面最大profile数目
	web_profile1 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
	print(web_profile1)

	time.sleep(2)
	for x in range(1, 11):
		add_admin(browser, admin_name="bob"+str(x), auth_database="local", temp="aaa"+str(x), https="yes", telent="no", ssh="yes", console="yes", status="enable", interface="ge0/5", online_num="3", ip1="0.0.0.0/0")

	# 获取web页面最大管理员数目
	web_admin1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
	print(web_admin1)

	language_switch(browser, language="China")
	# 定位到左侧frame
	browser.switch_to.frame("lefttree")
	# 点击管理员
	browser.find_element_by_xpath(管理员).click()
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 获取web页面最大管理员数目
	web_admin2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
	print(web_admin2)

	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()

	# 获取web页面最大profile数目
	web_profile2 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
	print(web_profile2)
	language_switch(browser,language="China")
	try:
		assert web_profile1 == web_profile2
		assert web_admin1 == web_admin2
		rail_pass(178, test_id)

	except:
		assert web_profile1 == web_profile2
		assert web_admin1 == web_admin2
		rail_pass(178, test_id)


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21546.py"])
