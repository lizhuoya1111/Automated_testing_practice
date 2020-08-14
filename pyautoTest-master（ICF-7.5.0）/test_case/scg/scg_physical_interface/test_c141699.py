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
test_id = "141699"


def test_main(browser):
	try:
		login_web(browser, url=dev1)
		into_fun(browser, 网桥)
		time.sleep(1)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_5, bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface=interface_name_6, bridge_interface="br_1")
		time.sleep(3)
		ssh1 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh1.connect()
		ssh1.execute('ping 21.1.1.3 -c 8 -i 0.1')
		ssh1.close()
		ssh2 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh2.connect()
		result1 = ssh2.execute('ping 21.1.1.3 -c 8 -i 0.1')
		print(result1)
		ssh2.close()
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_1", address_mode="manual", ip="21.1.1.1", mask="255.255.255.0", )
		bridge_add_jyl(browser, bridge_name="br_2", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_6, bridge_interface="br_2")
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_2", address_mode="manual", ip="22.1.1.1", mask="255.255.255.0",)
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ifconfig eth3 22.1.1.3 netmask 255.255.255.0')
		ssh.execute('route add -net 21.1.1.0/24 gw 22.1.1.1')
		# 关闭连接
		ssh.close()
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('route add -net 22.1.1.0/24 gw 21.1.1.1')
		# 关闭连接
		ssh.close()

		try:
			assert "100% packet loss" not in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "100% packet loss" not in result1

		delete_bridge_byname(browser, br_name="all")
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ifconfig eth3 21.1.1.3 netmask 255.255.255.0')
		ssh.close()

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('route del -net 22.1.1.0/24 gw 21.1.1.1')
		# 关闭连接
		ssh.close()

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('reboot')
		time.sleep(15)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])