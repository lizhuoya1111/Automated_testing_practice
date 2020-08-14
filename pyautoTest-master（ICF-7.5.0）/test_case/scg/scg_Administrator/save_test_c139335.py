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
test_id = 139335


def test_c139335(browser):
	try:
		login_web(browser, url=dev1)
		for y in range(1, 11):
			add_admin_profile(browser, profile_name='aaa'+str(y), desc="aaa权限", cfg="读写", report="读写")
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 获取web页面最大profile数目
		web_info1 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
		time.sleep(2)
		for x in range(1, 11):
			add_admin(browser, admin_name="bob"+str(x), auth_database="local", temp="aaa"+str(x), https="yes",
			          telent="no", ssh="yes", console="yes", status="enable", interface=interface_name_5, online_num="3",
			          ip1="0.0.0.0/0")
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 获取web页面最大管理员数目
		web_info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
		save_configer(browser)
		reload(hostip=dev1)
		login_web(browser, url=dev1)
		into_fun(browser, 管理员)
		# 点击管理员列表
		browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
		web_info4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
		# print(web_info4)
		time.sleep(3)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		web_info3 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
		# print(web_info3)

		sum1 = sum2 = 10
		while int(sum1) > 1:
			delete_all_admin_list_jyl(browser)
			time.sleep(1)
			into_fun(browser, 管理员)
			# 点击管理员列表
			browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
			sum1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		else:
			all_del_admin = "yes"

		while int(sum2) > 3:
			delete_all_admin_profile_jyl(browser)
			into_fun(browser, 管理员)
			# 点击管理员列表 //*[@id="rules_count"]
			browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
			sum2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		else:
			all_del_admin_profile = "yes"

		save_configer(browser)
		try:
			assert web_info1 == web_info3
			assert web_info2 == web_info4
			assert all_del_admin == "yes"
			assert all_del_admin_profile == "yes"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info1 == web_info3
			assert web_info2 == web_info4
			assert all_del_admin == "yes"
			assert all_del_admin_profile == "yes"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)

		delete_all_admin_list_jyl(browser)

		delete_all_admin_profile_jyl(browser)

		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
