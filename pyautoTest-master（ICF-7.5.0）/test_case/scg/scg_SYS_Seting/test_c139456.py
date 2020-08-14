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


test_id = "139456"



def test_c139456(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		edit_sysinfo(browser, description="!@")
		# time.sleep(1)
		result1 = get_sys_info_description(browser)

		edit_sysinfo(browser, description="武汉")
		# time.sleep(1)
		result2 = get_sys_info_description(browser)

		edit_sysinfo(browser, description="1234")
		# time.sleep(1)
		result3 = get_sys_info_description(browser)

		edit_sysinfo(browser, description="武汉123")
		# time.sleep(1)
		result4 = get_sys_info_description(browser)

		edit_sysinfo(browser, description="wuhan123")
		# time.sleep(1)
		result5 = get_sys_info_description(browser)

		edit_sysinfo(browser, description="123abcabcabcabcabcabcabcabcabcab")
		# time.sleep(1)
		result6 = get_sys_info_description(browser)
		loginfo = get_log_info(browser, 管理日志)

		try:
			assert result1 == "!@" and result2 == "武汉" and result3 == "1234" and result4 == "武汉123" and result5 == "wuhan123" and result6 == "123abcabcabcabcabcabcabcabcabcab" and "123abcabcabcabcabcabcabcabcabcab" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == "!@" and result2 == "武汉" and result3 == "1234" and result4 == "武汉123" and result5 == "wuhan123" and result6 == "123abcabcabcabcabcabcabcabcabcab" and "123abcabcabcabcabcabcabcabcabcab" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])