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
test_id = "139575"
# 重启系统后查看trace_route是否能正常工作
def test_c139575(browser):
	try:
		login_web(browser, url=dev5)
		reload(hostip=dev5, switch="重启")
		time.sleep(2)
		login_web(browser, url=dev5)
		info1 = trace_route(browser, ipadd="45.1.1.4", packersize="40", count="5", ping_wait_time="2", interface=interface_name_4, timesleep=10)

		try:
			assert "*" in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "*" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])