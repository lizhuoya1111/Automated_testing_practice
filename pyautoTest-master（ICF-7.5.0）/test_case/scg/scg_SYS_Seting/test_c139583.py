import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_route import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
test_id = "139583"
def test_c139583(browser):
	try:
		login_web(browser, url=dev1)
		info1 = trace_route(browser, ipadd="31.1.1.3", packersize="40", count="5", ping_wait_time="2",
						  interface=interface_name_3, timesleep=15)

		info2 = trace_route(browser, ipadd="www.aaa.com", packersize="40", count="5", ping_wait_time="2",
						  interface=interface_name_3, timesleep=15)

		try:
			assert "max" in info1
			assert "max" in info2

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "max" in info1
			assert "max" in info2


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])