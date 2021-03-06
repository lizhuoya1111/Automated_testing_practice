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
test_id = 139444
def test_c139444(browser):
	try:
		# 登录函数
		login_web(browser, url=dev5)
		into_fun(browser, 管理员)
		# 点击管理员权限
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		time.sleep(2)
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		into_fun(browser, 管理员)
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
		browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys("2002::3423::1")
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(3)
		# 获取提示框信息
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "格式输入错误" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "格式输入错误" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev5)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])