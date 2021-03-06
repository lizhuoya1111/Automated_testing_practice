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

test_id = 141655

def test_c141655(browser):

	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_1)
		result1 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_2)
		result2 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_3)
		result3 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_4)
		result4 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_5)
		result5 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_6)
		result6 = a.output()
		a.close()

		time.sleep(0.5)
		try:
			assert "MTU:1500" in result1
			assert "MTU:1500" in result2
			assert "MTU:1500" in result3
			assert "MTU:1500" in result4
			assert "MTU:1500" in result5
			assert "MTU:1500" in result6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "MTU:1500" in result1
			assert "MTU:1500" in result2
			assert "MTU:1500" in result3
			assert "MTU:1500" in result4
			assert "MTU:1500" in result5
			assert "MTU:1500" in result6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])