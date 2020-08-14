#感觉用找Xpath的方式不太对 因为“在线”和“frozen”的用户不是固定的
#那么位置应该也不是固定的吧 Xpath不是找位置吗？
#有没有问题匹配的定位方式呀？

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

test_id = 139376

def test_c139376(browser):
	try:
		login_web(browser, url=dev1)
		sleep(2)
		sys_set_jyl(browser, frozen_time='300', retry='3')
		add_admin_profile(browser, profile_name='lzy')
		add_admin(browser, admin_name='lzy', temp='lzy')

		sign_out_jyl(browser)
		sleep(2)

		# 用新账号登录

		for i in range(1, 4):
			browser.get("https://10.2.2.81")
			# 输入帐号
			browser.find_element_by_xpath("//*[@id='input_username']").send_keys('lzy')
			# 输入密码
			browser.find_element_by_xpath("//*[@id='input_password']").send_keys('admin')
			# 验证码0613
			browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
				'0613')
			# 点击登入
			browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
			info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			# print(info1)
			sleep(5)
			# print(i)

		login_web(browser, url=dev1)
		sleep(2)
		# browser.switch_to.default_content()
		# browser.switch_to.frame("lefttree")
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
		# 	browser.find_element_by_xpath(系统管理).click()
		# browser.find_element_by_xpath(管理员).click()
		# time.sleep(2)
		# browser.switch_to.default_content()
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)

		# 点击管理员列表
		browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
		num1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[10]/a').text
		# print(num1)#frozen
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[10]/a').click()
		num2 = browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]').text
		# print(num2)#冻结信息
		time.sleep(2)

		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)

		try:
			assert 'frozen' in num1 and 'lzy' in num2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert 'frozen' in num1 and 'lzy' in num2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])

