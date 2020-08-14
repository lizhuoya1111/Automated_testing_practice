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
test_id = 139425
def test_c139425(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		# 添加admin profile
		add_admin_profile(browser, profile_name="aaa", desc="aaa权限", cfg="读写", report="读写")
		# 添加读写管理员
		add_admin(browser, admin_name="zxcvbnmasdfghjklqwertyuiopzxcvb", temp="aaa")

		login_web(browser, url=dev1, username="zxcvbnmasdfghjklqwertyuiopzxcvb")
		# # 点击报表
		# browser.find_element_by_xpath(报表).click()
		into_fun(browser, 报表设置)
		web_info1 = (browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text.rstrip())

		login_web(browser, url=dev1)
		# print(loginfo)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "报表" in web_info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "报表" in web_info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])



