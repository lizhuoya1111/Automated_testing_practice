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
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 139424
def test_c139424(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		del_zone_all_batch(browser)
		time.sleep(1)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
	time.sleep(2)
	add_admin(browser, auth_database="local", admin_name="zxcvbnmlkjhgfdsaqwertyuiopzxcvb", temp="aaa", https="yes",
			  telent="yes", ssh="yes", console="yes", password="admin@139", confirm_password="admin@139",
			  status="enable", interface=interface_name_1, online_num="3", ip1="0.0.0.0/0")
	sign_out_jyl(browser)
	login_web(browser, url=dev1, username="zxcvbnmlkjhgfdsaqwertyuiopzxcvb")
	add_obj_zone(browser, "zone1", "zone测试", [interface_name_2, interface_name_3])
	time.sleep(5)
	# 切换到默认frame
	browser.switch_to.default_content()


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])