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
test_id = 139378


def test_c139378(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin_profile(browser, profile_name='aaa', desc='描述1', cfg="读写", report="读写")
		add_admin(browser, admin_name="bob", auth_database="local", temp="aaa",
				  https="yes", telent="yes", ssh="yes", console="yes",
				  password="admin@139", confirm_password="admin@139",
				  status="enable", interface=interface_name_1, online_num="32", ip1="0.0.0.0/0")

		sign_out_jyl(browser)

		for x in range(1, 4):
			login_web_fail(browser, url=dev1, username="bob", password="admin@1399")
			time.sleep(1)

		login_web(browser, url=dev1)
		get_admin_list_look_frozen_admin(browser)
		# 点击解除冻结
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[1]').click()
		loginfo = get_log(browser, 管理日志)

		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)

		try:
			assert "解冻" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "解冻" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
