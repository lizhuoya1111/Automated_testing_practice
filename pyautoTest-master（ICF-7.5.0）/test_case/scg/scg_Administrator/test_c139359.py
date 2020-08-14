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

test_id = 139359
# 1.使用一个读写用户登录设备
# 2.用该管理帐号去删除其他管理员帐号
# 不能删除

def test_c139359(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		add_admin(browser,
	              admin_name="bob", auth_database="local",
	              temp="log_profile",
	              https="yes", telent="yes", ssh="yes", console="yes",
	              password="admin@139", confirm_password="admin@139",
	              status="enable", interface=interface_name_1, online_num="32", ip1="0.0.0.0/0")

		add_admin(browser,
		          admin_name="bob1", auth_database="local",
		          temp="config_profile",
		          https="yes", telent="yes", ssh="yes", console="yes",
		          password="admin@139", confirm_password="admin@139",
		          status="enable", interface=interface_name_1, online_num="32", ip1="0.0.0.0/0")

		login_web(browser, url=dev1, username="bob", new="yes")
		info_bob = get_admin_name(browser)
		# print(info_bob)
		login_web(browser, url=dev1, username="bob1", new="yes")
		info_bob1 = get_admin_name(browser)
		# print(info_bob1)

		try:
			assert len(info_bob) == 1 and len(info_bob1) == 1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert len(info_bob) == 1 and len(info_bob1) == 1

		login_web(browser, url=dev1, new="yes")
		delete_all_admin_list_jyl(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])