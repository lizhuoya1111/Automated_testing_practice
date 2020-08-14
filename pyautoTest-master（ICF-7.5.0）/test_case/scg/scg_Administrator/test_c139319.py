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

test_id = 139319

def test_c139319(browser):
	try:
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(1)
		loginfo = get_log(browser, 管理日志)
		delete_all_admin_profile_jyl(browser)
		# print(loginfo)
		try:
			assert "添加管理员视图成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加管理员视图成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	add_admin_profile(browser, profile_name='tina1', desc='tina1权限', cfg="只读", report="无权限")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])

