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
test_id = "139547"
# 配置ip为10.10.10.2, Packet size为40,count为10,waittime为2s, interface选一个合适的接口
# 可以配置进去
def test_c139547(browser):
	try:
		login_web(browser, url=dev5)
		info1 = trace_route(browser, ipadd="45.1.1.4", packersize="40", count="10", ping_wait_time="2", interface=interface_name_4, timesleep=10)
		# print(info1)
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
		reload(hostip=dev5)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])