import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141625"

def test_c141625(browser):

	try:
		login_web(browser, url=dev3)
		physical_interface_switch(browser, interface=interface_name_3, status="disable", interface_id="")
		time.sleep(2)
		loginfo1 = get_log_info(browser, log_type=管理日志)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface gigabitethernet "+interface_name_3)
		result1 = a.output()
		# print(result1)
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no shutdown")
		a.close()
		time.sleep(0.5)

		try:
			assert "成功修改" in loginfo1
			assert "DOWN" in result1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功修改" in loginfo1
			assert "DOWN" in result1
		physical_interface_switch(browser, interface=interface_name_3, status="enable", interface_id="")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])