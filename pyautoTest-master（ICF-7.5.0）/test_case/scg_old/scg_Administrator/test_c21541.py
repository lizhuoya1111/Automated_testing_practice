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

test_id = 21541

def test_admin_user_add(browser):
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

	configuer(browser)

	time.sleep(2)
	get_log(browser, 管理日志)
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
	print(loginfo)

	try:
		assert "修改管理员帐户成功" in loginfo
		rail_pass(178, test_id)

	except:
		rail_fail(178, test_id)
		assert "修改管理员帐户失败" in loginfo

def configuer(browser):
	add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
	time.sleep(2)
	add_admin(browser, admin_name="bob", temp="aaa", https="yes", telent="yes", ssh="yes", console="yes",online_num="3", ip1="0.0.0.0/0")
	add_admin(browser, admin_name="bob", temp="aaa", https="yes", telent="yes", ssh="yes", console="yes",online_num="32", ip1="0.0.0.0/0")
	"""
	# 点击编辑按钮
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[11]/a[1]/img').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(32)
	# 点击保存按钮
	time.sleep(5)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(10)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	"""


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21541.py"])