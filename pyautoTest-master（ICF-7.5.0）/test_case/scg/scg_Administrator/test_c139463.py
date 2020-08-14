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


test_id = 139463


def test_c139463(browser):
	try:
		login_web(browser, url=dev5)
		# 点击管理员
		set_time(browser, date_input="2019-06-08", time_input="08:08:08")
		login_web(browser, url=dev5)
		time_info = get_time(browser)
		log_info = ""
		if "2019-06-08 08:08" in time_info or "2019-06-08 08:09" in time_info:
			log_info = get_log_info(browser, 管理日志)

		try:
			assert "成功修改[date frome " in log_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改[date frome " in log_info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev5)
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])