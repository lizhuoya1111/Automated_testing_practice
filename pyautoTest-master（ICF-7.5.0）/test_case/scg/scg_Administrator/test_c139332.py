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
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *

test_id = 139332
# 1.添加一个admin user，online number是3，点击save
# 2.点击编辑按钮编辑该user，修改inline number是32
# 可以修改成功,有相应的日志，shell查看的数据与UI一致

def test_c139332(browser):
	try:
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		print(loginfo)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		time.sleep(1)
		try:
			assert "修改管理员帐户成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "修改管理员帐户成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	add_admin_profile(browser, profile_name='aaa', desc="aaa权限", cfg="读写", report="读写")
	time.sleep(2)
	add_admin(browser, admin_name="bob", temp="aaa", https="yes", telent="yes", ssh="yes", console="yes",
			  auth_database="local", online_num="3", interface=interface_name_1,  password="admin@139", status="enable",
			  confirm_password="admin@139")
	edit_admin_jyl(browser,  edit_admin_name="bob", temp="aaa", https="yes", telnet="yes", ssh="yes", console="yes",
				auth_database="local", status="enable",
	          online_num="32", interface=interface_name_1,  password="admin@139", confirm_password="admin@139")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])