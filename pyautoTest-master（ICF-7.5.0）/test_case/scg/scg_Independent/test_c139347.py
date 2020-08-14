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
test_id = 139347


def test_c139347(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		for x in range(1, 11):
			add_admin_profile(browser, profile_name='aaa'+str(x), desc="aaa权限", cfg="只读", report="只读")
		for x in range(1, 11):
			add_admin(browser, auth_database="local", admin_name="bob"+str(x), temp="aaa"+str(x), https="yes", telent="yes", ssh="yes",
				  console="yes", password="admin@139", confirm_password="admin@139", status="enable",
				  interface=interface_name_1, online_num="3", ip1="0.0.0.0/0")
		into_fun(browser, 管理员)
		# 获取web信息
		web_info1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		print(web_info1)
		into_fun(browser, 管理员)
		# 点击管理员权限
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		time.sleep(5)
		# 获取web信息
		web_info2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		print(web_info2)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)


		try:
			assert "11" in web_info1
			assert "13" in web_info2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "11" in web_info1
			assert "13" in web_info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
