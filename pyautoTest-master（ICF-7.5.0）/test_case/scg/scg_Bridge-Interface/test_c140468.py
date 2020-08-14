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


test_id = 140468
def test_c140468(browser):
	try:
		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_1", address_mode="manual", ip="192.165.12.3", mask="24")
		bridge_add_jyl(browser, bridge_name="br_2")
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_2", address_mode="manual", ip="192.165.13.3", mask="24")
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]').text.rstrip()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no interface bridge br_2")
		a.execute("exit")
		try:
			assert "br_" in webinfo1
			assert "192.165.13" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "br_" in webinfo1
			assert "192.165.13" in webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
