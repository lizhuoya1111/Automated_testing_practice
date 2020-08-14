import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141700

def test_c141700(browser):

	try:
		login_web(browser, url=dev1)
		physical_interface_switch(browser, interface=interface_name_3, status="disable", interface_id="")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(0.5)
		result1 = a.output()
		a.close()
		physical_interface_switch(browser, interface=interface_name_3, status="enable", interface_id="")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(0.5)
		result2 = a.output()
		a.close()

		time.sleep(0.5)
		try:
			assert "Destination" in result1
			assert "ms" in result2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Destination" in result1
			assert "ms" in result2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])