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
test_id = 139420


def test_c139420(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		# # 定位到默认frame
		# 		# browser.switch_to.default_content()
		# 		# browser.switch_to.frame("lefttree")
		# 		# # 点击系统
		# 		# browser.find_element_by_xpath(系统).click()
		# 		# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
		# 		# 	# 如果不可见，点击加号，展开元素
		# 		# 	browser.find_element_by_xpath(系统管理).click()
		# 		# # 点击物理接口
		# 		# browser.find_element_by_xpath(管理员).click()
		# 		# # 切换到默认frame
		# 		# browser.switch_to.default_content()
		# 		# # 切换到内容frame
		# 		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		# 点击管理员列表
		browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
		# 点击online/online num num
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
		time.sleep(5)
		# 获取刚刚登录的ip
		web_info1 = (browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip())
		# print(web_info1)
		time.sleep(2)
		loginfo = get_log(browser, 系统日志)


		try:
			assert web_info1 in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info1 in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
