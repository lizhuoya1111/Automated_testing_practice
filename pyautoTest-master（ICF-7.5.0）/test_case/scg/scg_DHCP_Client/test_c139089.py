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
from page_obj.scg.scg_def import *

test_id = "139089"
def test_c139089(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="118.118.118.118",
		                    ip_range1_1="13.1.1.2", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url=dev3)
		physical_intertface_obtain_ip_address_from_dhcp1_jyl(browser, physical_interface=interface_name_2)
		time.sleep(5)
		# 获取信息
		webinfo1 = browser.find_element_by_xpath('//*[@id="dhcptr_2"]/td[1]').text
		webinfo2 = browser.find_element_by_xpath('//*[@id="dhcptr_3"]/td[1]').text
		webinfo3 = browser.find_element_by_xpath('//*[@id="dhcptr_4"]/td[1]').text

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address dhcp")

		vlan_add_jyl(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		vlan_interface_obtain_ip_fromdhcp1_jyl(browser, vlan_interface=interface_name_2+".22")
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
		webinfo4 = browser.find_element_by_xpath('//*[@id="dhcptr_2"]/td[1]').text
		webinfo5 = browser.find_element_by_xpath('//*[@id="dhcptr_3"]/td[1]').text
		webinfo6 = browser.find_element_by_xpath('//*[@id="dhcptr_4"]/td[1]').text

		time.sleep(1)
		vlan_delete_jyl(browser)

		physics_interface_change_transparent_interface(browser,  interface2=interface_name_2)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_2, bridge_interface="br_1")
		bridge_interface_obtain_ip_from_dhcp1_jyl(browser, bridge="br_1", work_mode="dhcp")
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
		webinfo7 = browser.find_element_by_xpath('//*[@id="dhcptr_2"]/td[1]').text
		webinfo8 = browser.find_element_by_xpath('//*[@id="dhcptr_3"]/td[1]').text
		webinfo9 = browser.find_element_by_xpath('//*[@id="dhcptr_4"]/td[1]').text


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
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "IP地址" in webinfo1
			assert "子网掩码" in webinfo2
			assert "网关" in webinfo3
			assert "IP地址" in webinfo4
			assert "子网掩码" in webinfo5
			assert "网关" in webinfo6
			assert "IP地址" in webinfo7
			assert "子网掩码" in webinfo8
			assert "网关" in webinfo9

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP地址" and "子网掩码" and "网关" in webinfo1
			assert "IP地址" and "子网掩码" and "网关" in webinfo2
			assert "IP地址" and "子网掩码" and "网关" in webinfo3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])