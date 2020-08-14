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
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140521
def test_c140521(browser):
	try:
		login_web(browser, url=dev1)
		physical_interface_switch(browser, interface=interface_name_5, status="disenable")

		ssh = SSH("10.1.1.213", 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 21.1.1.2 -c 5 -i 0.1')

		physical_interface_switch(browser, interface=interface_name_5, status="enable")

		try:
			assert "loss" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "loss" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
