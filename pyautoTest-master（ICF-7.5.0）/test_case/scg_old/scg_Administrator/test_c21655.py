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
test_id = 21655
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

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
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
	get_log(browser, 管理日志)
	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
	print(loginfo)

	try:
		assert "设置失败" in loginfo
		rail_pass(178, test_id)
	except:
		rail_fail(178, test_id)
		assert "设置失败" in loginfo


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21655.py"])