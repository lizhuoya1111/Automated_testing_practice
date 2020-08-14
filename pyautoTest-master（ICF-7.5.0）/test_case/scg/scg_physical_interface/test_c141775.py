import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
test_id = "141775"


def test_c141775(browser):
	try:
		result1 = 1
		login_web(browser, url=dev2)
		info_list = []
		for x in ['#', '$', ';', '|', '#$;,|', ',']:
			info = add_physical_interface_description_alert(browser, interface=interface_name_2, des=x)
			# print(info)
			info_list.append(info)

		for y in info_list:
			if "描述格式输入错误" in y:
				result1 = 0
			else:
				result1 = 1


		try:
			assert result1 == 0
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == 0

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])