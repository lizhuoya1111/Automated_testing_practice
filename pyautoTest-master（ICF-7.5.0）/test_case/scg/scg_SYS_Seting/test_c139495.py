import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def import *

test_id = "139495"


def test_c139495(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		export_cli_file(browser, mode="all", encry="no")
		time.sleep(2)
		loginfo = get_log_info(browser, 管理日志)
		try:
			assert "导出系统设置成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "导出系统设置成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
