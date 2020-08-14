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
test_id = 139377
# 在admin list中点击“online”
# 可以查看到当前有几个用户用什么ip登录

def test_c139377(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		get_admin_list_look_online_admin(browser)
		# 获取总数
		num1 = browser.find_element_by_xpath(('//*[@id="rules_count"]')).text.strip()
		# print(num1)
		# 获取登陆的管理员名称
		web_info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text.rstrip()
		# 获取登陆的管理员ip
		web_info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text

		try:
			assert "admin" == web_info1
			assert "." in web_info2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "admin" == web_info1
			assert "." in web_info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
