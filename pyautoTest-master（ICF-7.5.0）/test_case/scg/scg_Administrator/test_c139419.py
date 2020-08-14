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
test_id = 139419
def test_c139419(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)

		configuer(browser)
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		login_web(browser, url=dev1)
		into_fun(browser, 系统信息)
		# 修改系统信息—描述
		# 清除默认输入内容
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		browser.find_element_by_xpath('//*[@id="description"]').send_keys("BSAFE")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div/div[2]/div/input[2]').click()
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)

		try:
			assert "成功修改系统信息" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改系统信息" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	# 添加admin profile
	add_admin_profile(browser, profile_name="aaa", desc="aaa权限", cfg="读写", report="读写")
	# 添加读写管理员
	add_admin(browser, admin_name="bob", temp="aaa")

	login_web(browser, url=dev1, username="bob")
	into_fun(browser, 系统信息)
	# 修改系统信息—描述
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="description"]').clear()
	browser.find_element_by_xpath('//*[@id="description"]').send_keys("description_description")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div/div[2]/div/input[2]').click()


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])



