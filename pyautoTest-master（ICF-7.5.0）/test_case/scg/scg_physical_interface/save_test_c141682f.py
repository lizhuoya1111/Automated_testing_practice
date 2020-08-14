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

test_id = 141682


def test_c141682(browser):

	try:
		login_web(browser, url=dev1)
		physical_interface_switch(browser, interface=interface_name_3, status="disable")
		save_configer(browser)
		reload(hostip=dev1, switch="重启")

		login_web(browser, url=dev1)
		link_station = get_physical_interface_link_station(browser, interface_id="3")


		try:

			assert "断开" in link_station
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "断开" in link_station

		physical_interface_switch(browser, interface=interface_name_3, status="enable")
		save_configer(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])