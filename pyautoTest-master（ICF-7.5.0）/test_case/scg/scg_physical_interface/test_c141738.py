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

test_id = 141738

def test_c141738(browser):

	try:
		login_web(browser, url=dev3)
		physical_interface_switch(browser, interface=interface_name_4, status="disable", interface_id="")
		loginfo1 = get_log(browser, 管理日志)
		physical_interface_switch(browser, interface=interface_name_4, status="enable", interface_id="")
		loginfo2 = get_log(browser, 管理日志)
		try:
			assert "成功修改" in loginfo1
			assert "成功修改" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改" in loginfo1
			assert "成功修改" in loginfo2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])