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


test_id = "139455"



def test_c139455(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		edit_sysinfo(browser, location="wuhan")
		# time.sleep(1)
		result1 = get_sys_info_location(browser)

		edit_sysinfo(browser, location="武汉")
		# time.sleep(1)
		result2 = get_sys_info_location(browser)

		edit_sysinfo(browser, location="武汉市 洪山区")
		# time.sleep(1)
		result3 = get_sys_info_location(browser)

		edit_sysinfo(browser, location="华乐-1006")
		# time.sleep(1)
		result4 = get_sys_info_location(browser)

		edit_sysinfo(browser, location="huale1006")
		# time.sleep(1)
		result5 = get_sys_info_location(browser)

		edit_sysinfo(browser, location="1006-s2")
		# time.sleep(1)
		result6 = get_sys_info_location(browser)
		loginfo = get_log_info(browser, 管理日志)

		try:
			assert result1 == "wuhan" and result2 == "武汉" and result3 == "武汉市 洪山区" and result4 == "华乐-1006" and result5 == "huale1006" and result6 == "1006-s2" and "1006-s2" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == "wuhan" and result2 == "武汉" and result3 == "武汉市 洪山区" and result4 == "华乐-1006" and result5 == "huale1006" and result6 == "1006-s2" and "1006-s2" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1, reloadtime=70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])