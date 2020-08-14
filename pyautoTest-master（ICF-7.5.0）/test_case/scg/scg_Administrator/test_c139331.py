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
test_id = 139331


def test_c139331(browser):
	try:
		login_web(browser, url=dev1)
		time.sleep(1)
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
		time.sleep(2)
		for x in range(1, 32):
			add_admin(browser, admin_name="bob"+str(x), auth_database="local", temp="aaa", https="yes", telent="no",
					  ssh="yes", console="yes", status="enable", interface=interface_name_5, online_num="3", ip1="0.0.0.0/0")
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 获取web页面最大管理员数目
		web_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[33]/td[1]').text
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "添加管理员帐户成功" in loginfo
			assert web_info == "32"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert web_info == "32"
			assert "添加管理员帐户失败" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
