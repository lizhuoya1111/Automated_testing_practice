
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141643

def test_c141643(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("switchmode access")
		a.execute("switchmode trunk")
		a.execute("exit")
		a.close()
		result1 = a.output()
		try:

			assert "switchmode trunk" and "不能设置为接入模式" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "switchmode trunk" and "不能设置为接入模式" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])