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
test_id = 21645
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

	add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击添加
	time.sleep(8)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入管理员名称
	time.sleep(5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys("bob")
	# 选认证数据库
	s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
	# 选认证数据库下拉框内容
	s1.select_by_visible_text("local")
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text("aaa")
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys("admin@139")
	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys("admin@139")
	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys("032")
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys("0.0.0.0/24")
	time.sleep(3)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(3)
	# 获取web信息
	web_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	print(web_info)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	try:
		assert "parse cli error" in web_info
		rail_pass(178, test_id)
	except:
		rail_fail(178, test_id)
		assert "parse cli error" in web_info


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c21645.py"])
