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

test_id = 141680


def test_c141680(browser):

	try:
		link_station1 = " "
		login_web(browser, url=dev1)
		if check_physical_interface_enble(browser, interface="all"):
			link_station = get_physical_interface_link_station(browser, interface_id="4")
			if link_station == "连接":
				physical_interface_switch(browser, interface=interface_name_4, status="disable")
				link_station1 = get_physical_interface_link_station(browser, interface_id="4")


		try:

			assert "断开" in link_station1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "断开" in link_station1

		physical_interface_switch(browser, interface=interface_name_4, status="enable")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])