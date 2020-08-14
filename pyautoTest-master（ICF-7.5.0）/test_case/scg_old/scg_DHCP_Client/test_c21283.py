import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_route import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *

test_id = 21283
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_add_jyl(browser, interface="ge0/3", dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url="10.2.2.83")
		time.sleep(2)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface="ge0/2", work_mode="dhcp")
		time.sleep(2)
		result1 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(2)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface="ge0/2", work_mode="dhcp", dhcp_status2="stop",)
		time.sleep(2)
		result2 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(2)

		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击子接口
		browser.find_element_by_xpath(子接口).click()
		vlan_add_jyl(browser, physicl_interface="ge0/2", vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("switchmode access")
		a.execute("exit")
		time.sleep(5)
		vlan_interface_obtain_ip_from_dhcp_jyl(browser, vlan_interface="ge0/2.22", work_mode="dhcp")
		time.sleep(2)
		result3 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(5)
		vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface="ge0/2.22",  dhcp_status2="stop",)
		time.sleep(2)
		result4 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(2)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击子接口
		browser.find_element_by_xpath(子接口).click()
		time.sleep(2)
		vlan_delete_jyl(browser)

		time.sleep(3)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		physics_interface_change_transparent_interface(browser,  interface2="ge0/2",)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface="ge0/2", bridge_interface="br_1")
		time.sleep(2)
		bridge_interface_obtain_ip_from_dhcp_jyl(browser, bridge="br_1")
		time.sleep(3)
		result5 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(3)
		bridge_interface_obtain_ip_dhcp_status_jyl(browser, bridge="br_1", work_mode="dhcp", dhcp_status2="stop")
		time.sleep(3)
		result6 = is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(3)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		time.sleep(3)
		delete_bridge_jyl(browser)
		time.sleep(3)
		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		time.sleep(2)
		login_web(browser, url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		try:
			assert result1 == True
			assert result2 == False
			assert result3 == True
			assert result4 == False
			assert result5 == True
			assert result6 == False
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == True
			assert result2 == False
			assert result3 == True
			assert result4 == False
			assert result5 == True
			assert result6 == False

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])