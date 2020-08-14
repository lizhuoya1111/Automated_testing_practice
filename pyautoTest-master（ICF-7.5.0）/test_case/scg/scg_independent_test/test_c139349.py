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

test_id = 139349


def test_c139349(browser):
	try:
		# 登录函数
		login_web(browser, url=dev2)
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
		time.sleep(1)
		for x in range(1, 34):
			add_admin(browser, admin_name="bob"+str(x), auth_database="local", temp="aaa", https="yes",
			          telent="no", ssh="yes", console="yes", status="enable", interface=interface_name_5,
			          online_num="3", ip1="0.0.0.0/0")
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 获取页面最大管理员数
		web_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[34]/td[1]').text
		# print(web_info)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert web_info == "33"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info == "33"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])