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
test_id = "139582"
# 在Net_Diag ip/domain中填入一个不可达的ip地址或是domain
# 接不到回应包
def test_c139582(browser):
	try:
		login_web(browser, url=dev5)
		info1 = diag_ping(browser, ipadd="45.1.1.11", packersize="40", count="5", ping_wait_time="2",
						  interface=interface_name_4, timesleep=15)


		info2 = diag_ping(browser, ipadd="www.aaa.com", packersize="40", count="5", ping_wait_time="2",
						  interface=interface_name_4, timesleep=15)


		try:
			assert "Destination" in info1
			assert "Destination" in info2

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Destination" in info1
			assert "Destination" in info2


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])