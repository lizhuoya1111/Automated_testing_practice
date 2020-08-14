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


test_id = "139465"



def test_c139465(browser):
	try:
		login_web(browser, url=dev1)
		set_timezone(browser, time_zone="(GMT+0100) Africa/Douala")
		timezone_info = get_timezone(browser)
		log_info = ""
		if "Africa/Douala" in timezone_info:
			log_info = get_log_info(browser, 管理日志)

		set_timezone(browser, time_zone="(GMT+0800) Asia/Shanghai")

		try:
			assert "成功修改[timezone]为[Africa/Douala]" in log_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改[timezone]为[Africa/Douala]" in log_info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])