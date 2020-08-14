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

test_id = 141663

def test_c141663(browser):

	try:
		login_web(browser, url=dev3)
		infor1 = get_physical_interface_link_station(browser, interface_id="1")
		infor2 = get_physical_interface_link_station(browser, interface_id="2")
		infor3 = get_physical_interface_link_station(browser, interface_id="3")
		infor4 = get_physical_interface_link_station(browser, interface_id="4")
		infor5 = get_physical_interface_link_station(browser, interface_id="5")
		infor6 = get_physical_interface_link_station(browser, interface_id="6")

		try:
			assert "连接" in infor1
			assert "连接" in infor2
			assert "连接" in infor3
			assert "断开" in infor4
			assert "断开" in infor5
			assert "断开" in infor6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "连接" in infor1
			assert "连接" in infor2
			assert "连接" in infor3
			assert "断开" in infor4
			assert "断开" in infor5
			assert "断开" in infor6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])