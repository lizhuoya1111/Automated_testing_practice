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
test_id = "141703"


def test_c141703(browser):
	try:
		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始ping 83的13.1.1.3是不通的，因为没有回程路由，更没有snat
		ssh2.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
		result1 = ssh2.execute('ping 13.1.1.3 -c 8 -i 0.1')
		ssh2.close()
		# print(result1)

		login_web(browser, url=dev1)
		switch_physical_interface_snat(browser, interface=interface_name_3, snat="open")

		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始ping 83的13.1.1.3是不通的，因为没有回程路由，更没有snat
		result2 = ssh2.execute('ping 13.1.1.3 -c 8 -i 0.1')
		ssh2.close()
		# print(result2)



		try:
			assert "ttl" in result2 and "100% packet loss" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result2 and "100% packet loss" in result1

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")

		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始ping 83的13.1.1.3是不通的，因为没有回程路由，更没有snat
		ssh2.execute('route del -net 13.1.1.0/24 gw 20.1.1.1')
		ssh2.close()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])