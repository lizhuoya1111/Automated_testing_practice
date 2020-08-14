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
test_id = 139448
def test_c139448(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		into_fun(browser, 管理员)
		# 点击系统设定
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a/img').click()
		# browser.find_element_by_xpath('//*[@id="name"]').clear()
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("admin123")
		admin_name = browser.find_element_by_xpath('//*[@id="name"]').get_attribute("value")

		add_admin_profile(browser, profile_name='scg', desc='zhe是yi个描述1', cfg="读写", report="读写")
		into_fun(browser, 管理员)
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[6]/a[1]/img').click()
		# browser.find_element_by_xpath('//*[@id="profilename"]').clear()
		browser.find_element_by_xpath('//*[@id="profilename"]').send_keys("admin123")
		admin_profile_name = browser.find_element_by_xpath('//*[@id="profilename"]').get_attribute("value")

		try:
			assert admin_name == "admin"
			assert admin_profile_name == "scg"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert admin_name == "admin"
			assert admin_profile_name == "scg"

		del_admin_profile_byname(browser, name="scg")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])