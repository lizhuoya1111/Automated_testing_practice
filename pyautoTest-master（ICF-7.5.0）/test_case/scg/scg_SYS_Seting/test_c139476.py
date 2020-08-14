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


test_id = "139476"



def test_c139476(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		set_dns(browser)
		cmd = Shell_SSH()
		cmd.connect(hostip=dev1)
		cmd.execute("en")
		cmd.execute("ping www.baidu.com count 2")
		# time.sleep(2)
		info = cmd.output()

		try:
			assert "Success rate is 100%" in info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Success rate is 100%" in info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])