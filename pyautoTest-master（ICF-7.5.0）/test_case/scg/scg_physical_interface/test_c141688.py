
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

test_id = 141688

def test_c141688(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("ip address 192.165.12.2 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("ip address 192.165.12.2")
		ssh_info1 = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("ip address 192.165.12.2 24")
		ssh_info2 = a.output()
		a.close()

		try:
			assert "% Unrecognized command" not in ssh_info1
			assert "口工作在透明模式" in ssh_info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "% Unrecognized command" not in ssh_info1
			assert "口工作在透明模式" in ssh_info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])