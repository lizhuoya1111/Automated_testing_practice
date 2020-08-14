

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

test_id = 139367

def test_c139367(browser):
	try:
		login_web(browser, url=dev1)
		sleep(2)
		add_admin_profile(browser, profile_name='lzy')
		sleep(2)
		add_admin(browser, admin_name='lzy', temp='lzy')
		sleep(2)
		sign_out_jyl(browser)
		sleep(2)
		login_web(browser, url=dev1, username='lzy')
		log1 = get_log(browser, 系统日志)
		# print(log1)
		sleep(2)

		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		sleep(2)
		add_admin_profile(browser, profile_name='lzy1', cfg='只读', report='只读')
		sleep(2)
		add_admin(browser, admin_name='lzy', temp='lzy1')
		sleep(2)
		sign_out_jyl(browser)
		sleep(2)
		login_web(browser, url=dev1, username='lzy')

		# browser.switch_to.default_content()
		# browser.switch_to.frame("lefttree")
		# # 点击系统
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(系统管理).click()
		# # 点击物理接口
		# browser.find_element_by_xpath(管理员).click()
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		sleep(2)
		info1 = browser.find_element_by_xpath('//*[@id="text_warning"]').text
		# print(info1)
		browser.find_element_by_xpath('//*[@id="box"]/div[4]/div/input').click()
		sleep(2)

		sign_out_jyl(browser)
		sleep(2)
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)
		delete_all_admin_profile_jyl(browser)


		try:
			assert 'lzy' in log1 and '您没有权限进行此项操作' in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert 'lzy' in log1 and '您没有权限进行此项操作' in info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])

