

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

test_id = 139374

def test_c139374(browser):
	try:
		login_web(browser, url=dev1)
		sleep(2)
		sys_set_jyl(browser, frozen_time='300', retry='3')
		print(33333333333333333333333)
		time.sleep(10)
		print(111111111111111111111111)
		add_admin_profile(browser, profile_name='lzy')
		add_admin(browser, admin_name='lzy', temp='lzy')

		sign_out_jyl(browser)
		sleep(2)

		#用新账号登录
		info1 = ''
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
			info11 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			print(info11)
			info1 = info11
			sleep(5)
			print(i)

		# sleep(310)
		login_web(browser, url=dev1)
		get_admin_list_look_frozen_admin(browser)
		# 点击解除冻结
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[1]').click()
		sign_out_jyl(browser)

		login_web(browser, url=dev1, username='lzy')
		log1 = get_log(browser, 系统日志)
		print(log1)

		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		sleep(2)
		delete_all_admin_list_jyl(browser)
		delete_all_admin_profile_jyl(browser)


		try:
			assert 'lzy' in log1 and '本地认证错误(密码错误)' in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert 'lzy' in log1 and '本地认证错误(密码错误)' in info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])

