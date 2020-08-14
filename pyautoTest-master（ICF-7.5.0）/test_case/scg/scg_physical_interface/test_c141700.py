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
		login_web(browser, url=dev3)
		infor1 = get_physical_interface_link_station(browser, interface_id="2")
		login_web(browser, url=dev1)
		physical_interface_switch(browser, interface=interface_name_3, status="enable", interface_id="")
		login_web(browser, url=dev3)
		infor2 = get_physical_interface_link_station(browser, interface_id="2")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(5)
		result1 = a.output()
		a.close()

		try:
			assert "断开" in infor1
			assert "连接" in infor2
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "断开" in infor1
			assert "连接" in infor2
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])