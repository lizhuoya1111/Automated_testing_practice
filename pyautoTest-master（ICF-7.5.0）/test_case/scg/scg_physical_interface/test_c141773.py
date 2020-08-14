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
test_id = "141773"


def test_c141773(browser):
	try:
		login_web(browser, url=dev2)

		# print(info3)
		info4 = add_physical_interface_static_ip_jyl_alert(browser, interface=interface_name_1, ip='中文', mask='24')
		# print(info4)
		info5 = add_physical_interface_static_ip_jyl_alert(browser, interface=interface_name_1, ip='eng', mask='24')
		# print(info5)
		info6 = add_physical_interface_static_ip_jyl_alert(browser, interface=interface_name_1, ip='！@！#！@￥', mask='24')
		# print(info6)


		if  "IP格式输入错误，请重新输入。" in info4 and "IP格式输入错误，请重新输入。" in info5 and "IP格式输入错误，请重新输入。" in info6:
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