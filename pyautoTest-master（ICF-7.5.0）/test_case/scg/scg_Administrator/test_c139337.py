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
test_id = 139337
# 未通过测试

def test_c139337(browser):
	try:
		# 登录函数
		# login_web(browser, url=dev1)
		# language_switch(browser, language="English")
		# time.sleep(2)
		# for y in range(1, 11):
		# 	add_admin_profile(browser, profile_name='aaa'+str(y), desc="aaa权限", cfg="读写", report="读写")
		# time.sleep(2)
		# browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# # 获取web页面最大profile数目
		# web_profile1 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
		# # print(web_profile1)
		# time.sleep(2)
		# for x in range(1, 11):
		# 	add_admin(browser, admin_name="bob"+str(x), auth_database="local", temp="aaa"+str(x), https="yes",
		# 	          telent="no", ssh="yes", console="yes", status="enable", interface=interface_name_5, online_num="3",
		# 	          ip1="0.0.0.0/0")
		#
		# time.sleep(2)
		# browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# # 获取web页面最大管理员数目
		# web_admin1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
		# # print(web_admin1)
		# language_switch(browser, language="China")
		# # # 定位到左侧frame
		# # browser.switch_to.frame("lefttree")
		# # # 点击管理员
		# # browser.find_element_by_xpath(管理员).click()
		# # # 定位到默认frame
		# # browser.switch_to.default_content()
		# # # 定位到内容frame
		# # browser.switch_to.frame("content")
		#
		# into_fun(browser, 管理员)
		# # 点击管理员列表
		# browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
		# # 获取web页面最大管理员数目
		# web_admin2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[12]/td[1]').text
		# # print(web_admin2)
		# time.sleep(3)
		# browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		# # 获取web页面最大profile数目
		# web_profile2 = browser.find_element_by_xpath('// *[ @ id = "table"] / tbody / tr[14] / td[1]').text
		# # print(web_profile2)
		# language_switch(browser, language="China")
		# delete_all_admin_list_jyl(browser)
		# time.sleep(1)
		# delete_all_admin_profile_jyl(browser)
		# try:
		# 	assert web_profile1 == web_profile2
		# 	assert web_admin1 == web_admin2
		# 	rail_pass(test_run_id, test_id)
		#
		# except:
		# 	rail_fail(test_run_id, test_id)
		# 	assert web_profile1 == web_profile2
		# 	assert web_admin1 == web_admin2
		rail_fail(test_run_id, test_id)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
