
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = "140511"
def test_c140511(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("no ip address 20.1.1.1")
		a.execute("exit")
		a.execute("in vlan "+interface_name_4+".44")
		a.execute("ip address 20.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("switchmode access")
		a.execute("exit")

		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode route")
		a.execute("exit")
		a.execute("interface vlan "+interface_name_5+".44")
		a.execute("ip address 21.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("switchmode access")
		a.execute("exit")

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 20.1.1.2 -c 5')
		# 关闭连接
		ssh.close()
		time.sleep(5)

		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_4+".44")
		a.execute("no interface vlan "+interface_name_5+".44")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("ip address 20.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode transparent")
		a.execute("exit")

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
