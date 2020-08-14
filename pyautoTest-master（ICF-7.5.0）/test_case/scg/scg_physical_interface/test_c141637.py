
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141637

def test_c141637(browser):

	try:
		login_web(browser, url=dev1)
		switch_physical_interface_snat(browser, interface=interface_name_3, snat="open")
		loginfo1 = get_log(browser, 管理日志)
		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")
		loginfo2 = get_log(browser, 管理日志)
		open_physical_interface_allowping_wxw(browser, interface=interface_name_3, allow_ping="open")
		loginfo3 = get_log(browser, 管理日志)
		open_physical_interface_allowping_wxw(browser, interface=interface_name_3, allow_ping="close")
		loginfo4 = get_log(browser, 管理日志)

		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			assert "成功" in loginfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			assert "成功" in loginfo4

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")
		open_physical_interface_allowping_wxw(browser, interface=interface_name_3, allow_ping="open")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])