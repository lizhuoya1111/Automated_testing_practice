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
test_id = 139355
# 1.添加一个用户，conf system 为none
# 2.用该用户登录设备，并修改自己的口令
# 可以修改，修改后用新口令可以正常登陆
# 此处修改的密码可以为任意值 已提单

def test_admin_user_add(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="none", report="读写")
		time.sleep(2)
		add_admin(browser, admin_name="lzy", auth_database="local", temp="aaa", https="yes", telent="no",
				  ssh="yes", console="yes", status="enable", interface="any", online_num="3", ip1="0.0.0.0/0")
		sign_out_jyl(browser)
		browser.refresh()
		time.sleep(2)
		login_web(browser, url=dev1, username="lzy")
		modify_password_of_new_adminuser(browser, password="admin@1399", confirm_password="admin@1399")
		sign_out_jyl(browser)
		browser.refresh()
		time.sleep(2)
		login_web(browser, url=dev1, username="lzy", password="admin@1399")
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		print(loginfo)
		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "修改管理员帐户成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改管理员帐户成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False




if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])