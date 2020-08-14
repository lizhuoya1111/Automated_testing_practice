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
test_id = "141771"


def test_c141771(browser):
	try:
		login_web(browser, url=dev2)
		info1 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_1, ip='10.2.2.82', mask='24')
		print(info1)
		info2 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_1, ip='10.2.2.82', mask='32')
		print(info2)
		info3 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='10.2.2.82', mask='24')
		print(info3)
		info4 = add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='10.2.2.82', mask='32')
		print(info4)




		try:
			assert "IP地址已经存在于本系统" in info1 and "IP地址已经存在于本系统" in info2 and "IP地址已经存在于本系统" in info3 and "IP地址已经存在于本系统" in info4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP地址已经存在于本系统" in info1 and "IP地址已经存在于本系统" in info2 and "IP地址已经存在于本系统" in info3 and "IP地址已经存在于本系统" in info4


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev2)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])