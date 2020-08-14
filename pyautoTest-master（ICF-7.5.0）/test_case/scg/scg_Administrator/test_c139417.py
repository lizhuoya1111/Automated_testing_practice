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
test_id = 139417


def test_c139417(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(2)
		loginfo = get_log(browser, 管理日志)
		print(loginfo)
		delete_all_admin_list_jyl(browser)
		time.sleep(1)
		delete_all_admin_profile_jyl(browser)
		try:
			assert "添加管理员帐户成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "添加管理员帐户成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	for i in range(1, 6):
		add_admin_profile(browser, profile_name="aaa" + str(i), desc='aaa' + str(i) + "权限", cfg="读写", report="读写")
	for j in range(1, 6):
		add_admin(browser, admin_name="bob" + str(j), temp="aaa" + str(j), interface=interface_name_5)


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])