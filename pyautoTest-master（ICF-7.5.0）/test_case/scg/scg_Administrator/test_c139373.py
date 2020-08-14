
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


test_id = 139373


def test_c139373(browser):
	try:
		login_web(browser, url=dev1)
		sleep(1)
		add_admin_profile(browser, profile_name='lzy')
		add_admin(browser, admin_name='lzy', temp='lzy')
		sys_set_lzy(browser, ssh_port="22", ssh_timeout="300", https_port="500", https_timeout="300", telent_port="23",
					telent_timeout="300", console_timeout="300")

		time.sleep(1)
		refresh(browser)
		login_web(browser, url=dev1)
		sleep(1)
		sign_out_jyl(browser)
		sleep(1)
		login_web(browser, url=dev1, username='lzy')
		time.sleep(1)
		refresh(browser)
		time.sleep(1)
		log1 = get_log(browser, 系统日志)
		# print(log1)

		sleep(0.5)
		sign_out_jyl(browser)
		sleep(0.5)
		login_web(browser, url=dev1)
		delete_all_admin_list_jyl(browser)
		delete_all_admin_profile_jyl(browser)

		try:
			assert '管理员登录成功' in log1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert '管理员登录成功' in log1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False





if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])