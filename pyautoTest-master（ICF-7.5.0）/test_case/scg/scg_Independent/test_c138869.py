import pytest
import subprocess
import time
import  os
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "138869"


def test_c138869(browser):
	try:
		# ssh_cmd = Shell_SSH()
		# ssh_cmd.execute("en")
		# ssh_cmd.execute("ping 47.1.1.7 count 30")
		while True:
			login_web(browser, url="10.2.2.34")
			physical_interface_switch(browser, interface=interface_name_9, status="disable", interface_id="9")

			# 查看设备是否正常，可以ping吗？
			result_37_1 = os.popen("ping 10.2.2.37")
			result_info_37_1 = result_37_1.read()
			print(result_info_37_1)

			result_34_1 = os.popen("ping 10.2.2.34")
			result_info_34_1 = result_34_1.read()
			print(result_info_34_1)

			try:
				assert "0% 丢失" in result_info_37_1 or "0% 丢失" in result_info_34_1
				# rail_pass(test_run_id, test_id)
			except:
				assert "0% 丢失" in result_info_37_1 or "0% 丢失" in result_info_34_1
				# rail_pass(test_run_id, test_id)
				break

			physical_interface_switch(browser, interface=interface_name_9, status="enable", interface_id="9")
			# 查看设备是否正常，可以ping吗？
			result_37_2 = os.popen("ping 10.2.2.37")
			result_info_37_2 = result_37_2.read()
			print(result_info_37_2)

			result_34_2 = os.popen("ping 10.2.2.34")
			result_info_34_2 = result_34_2.read()
			print(result_info_34_2)

			try:
				assert "0% 丢失" in result_info_37_2 or "0% 丢失" in result_info_34_2
				# rail_pass(test_run_id, test_id)
			except:
				assert "0% 丢失" in result_info_37_2 or "0% 丢失" in result_info_34_2
				# rail_pass(test_run_id, test_id)
				break

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		# rail_fail(test_run_id, test_id)
		# reload(hostip="10.2.2.72", reloadtime=70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])