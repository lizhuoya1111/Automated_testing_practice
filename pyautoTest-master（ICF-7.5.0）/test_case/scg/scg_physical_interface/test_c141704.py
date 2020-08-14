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
test_id = "141704"


def test_c141704(browser):
	try:

		login_web(browser, url=dev1)
		switch_physical_interface_snat(browser, interface=interface_name_3, snat="open")

		a1 = Shell_SSH()
		a1.connect(hostip=dev3)
		a1.execute("en")
		a1.execute("conf t")
		time.sleep(1)
		a1.execute("ip route 20.1.1.0/24 gateway 13.1.1.1")
		# print(a1.output())
		a1.close()



		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始ping 83的13.1.1.3是不通的，因为没有回程路由，更没有snat
		ssh2.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
		ssh2.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 20.1.1.2")
		time.sleep(2)
		result1 = a.output()
		print(result1)
		a.close()



		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

		switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")

		ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
		ssh2.connect()
		# 一开始ping 83的13.1.1.3是不通的，因为没有回程路由，更没有snat
		ssh2.execute('route del -net 13.1.1.0/24 gw 20.1.1.1')
		ssh2.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		time.sleep(0.5)
		a.execute("no ip route 20.1.1.0/24 gateway 13.1.1.1")
		a.close()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])