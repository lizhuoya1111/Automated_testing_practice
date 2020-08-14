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
test_id = "141776"


def test_c141776(browser):
	try:
		login_web(browser, url=dev2)
		add_physical_interface_description(browser, interface=interface_name_2, des=str_257_en)
		info1 = get_physical_interface_des(browser, interface=interface_name_2)
		print(info1)



		try:
			assert "abcabcabcabcabcabc" in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "abcabcabcabcabcabc" in info1

		clear_physical_interface_des(browser, interface=interface_name_2)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])