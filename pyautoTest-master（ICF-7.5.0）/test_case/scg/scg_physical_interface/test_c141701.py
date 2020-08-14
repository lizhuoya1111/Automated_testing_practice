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
test_id = "141701"


def test_c141701(browser):
	try:
		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始，相同网段ping，期望是可通
		result1 = ssh2.execute('ping 20.1.1.1 -c 8 -i 0.1')
		ssh2.close()
		# print(result1)

		login_web(browser, url=dev1)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='172.16.55.1', mask='24')
		# time.sleep(555)

		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 修改为不同网段，ping，期望是不通
		result2 = ssh2.execute('ping 172.16.55.1 -c 8 -i 0.1')
		# print(result2)
		ssh2.execute('ifconfig eth5 172.16.55.2 netmask 255.255.255.0')
		# 修改为同网段，ping，期望是可通
		result3 = ssh2.execute('ping 172.16.55.1 -c 8 -i 0.1')
		# print(result3)
		ssh2.execute('ifconfig eth5 20.1.1.2 netmask 255.255.255.0')
		ssh2.close()


		try:
			assert "ttl" in result1 and "100% packet loss" in result2 and "ttl" in result3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result1 and "100% packet loss" in result2 and "ttl" in result3

		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="172.16.55.1")
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])