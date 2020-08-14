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


test_id = 140499


def test_c140499(browser):
	try:
		login_web(browser, url=dev1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.execute("work-mode transparent")
		a.close()

		bridge_add_jyl(browser, bridge_name="br_1")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.close()

		get_into_bri_jyl(browser)
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text.rstrip()
		# print(webinfo1)
		# print(1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".2")
		a.execute("work-mode transparent")
		a.close()

		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3+".2")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".2")
		a.execute("work-mode route")
		a.close()

		get_into_bri_jyl(browser)
		webinfo2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
		# print(webinfo2)
		# print(2)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("no interface vlan "+interface_name_3+".2")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode transparent")
		a.close()

		get_into_bri_jyl(browser)
		webinfo3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
		# print(webinfo3)
		# print(3)
		birdge_edit_interface_delete_jyl(browser, interface=interface_name_3, bridge_interface="br_0")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		time.sleep(3)
		get_into_bri_jyl(browser)
		webinfo4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
		# print(webinfo4)
		# print(4)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.close()

		try:
			assert interface_name_3 not in webinfo1
			assert interface_name_3+".2" not in webinfo2
			assert interface_name_3 in webinfo3
			assert interface_name_3 in webinfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert interface_name_3 not in webinfo1
			assert interface_name_3 + ".2" not in webinfo2
			assert interface_name_3 in webinfo3
			assert interface_name_3 in webinfo4
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
