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
test_id = 139442
def test_c139442(browser):
	try:
		# 登录函数
		login_web(browser, url=dev5)
		into_fun(browser, 管理员)
		# 点击系统设定
		browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
		time.sleep(3)
		browser.find_element_by_xpath('//*[@id="fronzedtime"]').clear()
		browser.find_element_by_xpath('//*[@id="fronzedtime"]').send_keys("86401")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(3)
		# 获取web信息
		web_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(web_info)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		sleep(1)

		try:
			assert "冻结时间取值范围" in web_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "冻结时间取值范围" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev5)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])