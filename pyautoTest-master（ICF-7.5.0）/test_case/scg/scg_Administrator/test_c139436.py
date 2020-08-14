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
test_id = 139436

def test_c139436(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
		time.sleep(1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
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
		# 填入最大在线数
		browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
		browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys("032")
		browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys("0.0.0.0/24")
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(3)
		time.sleep(3)
		# 获取提示框信息
		alert = browser.switch_to_alert()
		print(alert.text)
		web_info = alert.text
		# 接受告警
		browser.switch_to_alert().accept()
		delete_all_admin_profile_jyl(browser)
		try:
			assert "在线数必须为数字" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "在线数必须为数字" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
