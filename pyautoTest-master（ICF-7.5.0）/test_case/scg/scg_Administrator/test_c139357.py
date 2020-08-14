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

test_id = 139357

def test_c139357(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		try:
			assert "修改管理员帐户成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改管理员帐户成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="只读", report="只读")
	time.sleep(2)
	add_admin(browser, admin_name="bob", auth_database="local", temp="aaa", https="yes", telent="no",
			  	password="admin@139", confirm_password="admin@139",
	              ssh="yes", console="yes", status="enable", interface="any", online_num="3", ip1="0.0.0.0/0")
	sign_out_jyl(browser)
	time.sleep(2)
	login_web(browser, username="bob")
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[text()="系统管理"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击
	# browser.find_element_by_xpath(管理员).click()
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	time.sleep(7)
	browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
	# time.sleep(7)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a/img').click()
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys("admin@1399")
	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys("admin@1399")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	sign_out_jyl(browser)
	time.sleep(2)
	login_web(browser, username="bob", password="admin@1399")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])