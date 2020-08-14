import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_dns import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_route import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *

test_id = "139111"
def test_c139111(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url=dev3)
		delete_dns_jyl(browser, master_dns="delete")
		time.sleep(1)
		physical_interface_update_dhcp_jyl(browser, physical_interface=interface_name_2, update_system_dns="open")
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo1 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo1)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp", dhcp_status2="stop",)
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo2 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo2)

		vlan_add_jyl(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		time.sleep(1)
		vlan_interface_from_dhcp_obtain_ip_jyl(browser, vlan_interface=interface_name_2+".22", work_mode="dhcp",
											 update_system_dns="open")
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo3 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo3)
		vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface=interface_name_2+".22",  dhcp_status2="stop",)
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo4 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo4)
		vlan_delete_jyl(browser)

		time.sleep(1)
		physics_interface_change_transparent_interface(browser,  interface2=interface_name_2)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_2, bridge_interface="br_1")
		time.sleep(1)
		bridge_interface_from_dhcp_obtain_ip_jyl(browser, bridge="br_1",  work_mode="dhcp", update_system_dns="open")
		time.sleep(1)
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo5 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo5)
		time.sleep(1)
		bridge_interface_obtain_ip_dhcp_status_jyl(browser, bridge="br_1", work_mode="dhcp", dhcp_status2="stop")
		time.sleep(1)
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo6 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo6)
		delete_bridge_jyl(browser)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		time.sleep(1)
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		try:
			assert "114.114.114.114" in webinfo1
			assert "" in webinfo2
			assert "114.114.114.114" in webinfo3
			assert "" in webinfo4
			assert "114.114.114.114" in webinfo5
			assert "" in webinfo6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "114.114.114.114" in webinfo1
			assert "" in webinfo2
			assert "114.114.114.114" in webinfo3
			assert "" in webinfo4
			assert "114.114.114.114" in webinfo5
			assert "" in webinfo6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])