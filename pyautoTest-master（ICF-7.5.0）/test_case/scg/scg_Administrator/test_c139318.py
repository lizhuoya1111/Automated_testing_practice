import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *

test_id = 139318


def test_c129318(browser):
	try:
		login_web(browser, url=dev1)
		add_admin_profile(browser, profile_name="test1")
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "管理员视图成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "管理员视图成功" in loginfo
			print("????")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])