
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = "21392"
def test_main(browser):
	try:
		b = Shell_SSH()
		b.connect(dev3)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet ge0/2")
		b.execute("no ip address 13.1.1.3")
		b.execute("exit")
		login_web(browser, url=dev1)
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                    senior="yes",  static_ip_add1="13.1.1.5", static_mac_add1="00:16:31:F6:2A:1D")
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url=dev1)
		time.sleep(2)

		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击子接口
		browser.find_element_by_xpath(子接口).click()
		vlan_add_jyl(browser, physicl_interface="ge0/2", vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("switchmode access")
		a.execute("exit")
		time.sleep(5)
		vlan_interface_obtain_ip_from_dhcp_jyl(browser, vlan_interface="ge0/2.22")
		time.sleep(4)
		# 获取页面信息
		webinfo1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text
		print(webinfo1)
		time.sleep(2)
		vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface="ge0/2.22", dhcp_status2="stop")
		time.sleep(2)
		vlan_delete_jyl(browser)
		time.sleep(3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		login_web(browser, url=dev1)
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "13.1.1.5" == webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "13.1.1.5" == webinfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])