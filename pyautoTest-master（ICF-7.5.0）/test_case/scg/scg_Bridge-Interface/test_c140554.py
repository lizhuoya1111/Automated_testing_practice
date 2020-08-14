import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140554
def test_c140554(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("ip address 192.165.12.2 24")
		a.execute("ip address 192.166.12.2 24")
		a.execute("ip address 192.167.12.2 24")
		a.close()

		webinfo1 = is_static_route_exist_wxw(browser, destination='192.165.12.0/255.255.255.0')
		info1 = str(webinfo1)
		webinfo1 = is_static_route_exist_wxw(browser, destination='192.166.12.0/255.255.255.0')
		info2 = str(webinfo1)
		webinfo1 = is_static_route_exist_wxw(browser, destination='192.167.12.0/255.255.255.0')
		info3 = str(webinfo1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("no ip address 192.165.12.2")
		a.execute("no ip address 192.166.12.2")
		a.execute("no ip address 192.167.12.2")
		a.execute("exit")
		a.close()

		try:
			assert "True" in info1
			assert "True" in info2
			assert "True" in info3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "True" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
