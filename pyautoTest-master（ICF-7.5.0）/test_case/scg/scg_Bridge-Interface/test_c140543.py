import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 140543

def test_c140543(browser):

	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("shutdown")
		a.close()

		get_physical_interface_link_station(browser, interface_id="2")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no shutdown")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("shutdown")
		a.close()

		get_physical_interface_link_station(browser, interface_id="2")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no shutdown")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("ping 13.1.1.3")
		time.sleep(3)
		result1 = a.output()
		a.close()
		print(result1)

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		# reload(hostip=[dev2, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])