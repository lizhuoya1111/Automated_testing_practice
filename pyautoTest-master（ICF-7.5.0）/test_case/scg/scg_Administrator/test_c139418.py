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
test_id = 139418


def test_c139418(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		for x in range(1, 5):
			add_admin_profile(browser, profile_name='aaa'+str(x),desc='描述1', cfg="读写", report="读写")

		add_admin(browser, admin_name="bob1", auth_database="local", temp="aaa1",
				  https="yes", telent="yes", ssh="yes", console="yes",
				  password="admin@139", confirm_password="admin@139",
				  status="enable", interface=interface_name_1, online_num="32", ip1="0.0.0.0/0")

		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)

		loginfo = get_log(browser, 管理日志)


		try:
			assert "删除" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "删除" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
