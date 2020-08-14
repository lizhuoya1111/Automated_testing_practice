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
test_id = 139363


def test_admin_user_add(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin(browser, admin_name="bob", auth_database="local", temp="max_profile", https="yes", telent="no",
		          ssh="yes", console="yes", status="enable", interface="any", online_num="3", ip1="192.168.18.0/24")

		browser.get("https://" + dev1)
		# 输入帐号
		browser.find_element_by_xpath("//*[@id='input_username']").send_keys("bob")
		# 输入密码
		browser.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
		# 验证码0613
		browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
			"0613")
		# 点击登入
		browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()


		info_login = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)

		login_web(browser, url=dev1)
		add_admin(browser, admin_name="bob", auth_database="local", temp="max_profile", https="yes", telent="no",
		          ssh="yes", console="yes", status="enable", interface="any", online_num="3", ip1="192.168.188.0/24",
		          ip2="10.1.1.0/24")

		login_web(browser, url=dev1, username="bob", new="yes")
		# host = get_sys_info_hostname(browser)
		# print(host)

		try:
			assert "不支持的登录ip" in info_login
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "不支持的登录ip" in info_login
		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])