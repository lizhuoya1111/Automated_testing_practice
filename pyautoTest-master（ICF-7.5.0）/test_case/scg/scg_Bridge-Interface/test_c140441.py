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


test_id = 140441
def test_c140441(browser):
	try:
		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode transparent")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_5)
		# print(webinfo1)
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_1", address_mode="manual", ip="192.165.12.3", mask="24")
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[2]').text.rstrip()
		# print(webinfo2)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("exit")




		try:
			assert "br_1" == webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "br_1" == webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
