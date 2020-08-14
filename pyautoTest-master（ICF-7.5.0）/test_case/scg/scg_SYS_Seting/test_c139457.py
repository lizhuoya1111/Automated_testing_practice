import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "139457"



def test_c139457(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		edit_sysinfo(browser, contact="122@123.com")
		# time.sleep(1)
		result1 = get_sys_info_contact(browser)
		loginfo1 = get_log_info(browser, 管理日志)

		edit_sysinfo(browser, contact="www112@123.com")
		# time.sleep(1)
		result2 = get_sys_info_contact(browser)

		loginfo2 = get_log_info(browser, 管理日志)


		try:
			assert result1 == "122@123.com" and result2 == "www112@123.com" and "www112@123.com" in loginfo2 and "122@123.com" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == "122@123.com" and result2 == "www112@123.com" and "www112@123.com" in loginfo2 and "122@123.com" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])