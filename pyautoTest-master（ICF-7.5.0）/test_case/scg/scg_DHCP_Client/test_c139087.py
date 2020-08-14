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

test_id = "139087"
def test_c139087(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="118.118.118.118",
		                    ip_range1_1="13.1.1.2", ip_range1_2="13.1.1.20")
		login_web(browser, url=dev3)
		time.sleep(1)
		physical_intertface_obtain_ip_address_from_dhcp1_jyl(browser, physical_interface=interface_name_2)
		time.sleep(1)
		# 获取信息
		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(webinfo1)
		# 点击返回
		time.sleep(1)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()
		vlan_add_jyl(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		time.sleep(1)
		time.sleep(5)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_2+'.22')
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		a.close()

		time.sleep(5)

		time.sleep(1)
		vlan_interface_obtain_ip_fromdhcp1_jyl(browser, vlan_interface=interface_name_2+".22")
		time.sleep(1)
		time.sleep(5)
		webinfo2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(webinfo2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()
		vlan_delete_jyl(browser)
		time.sleep(1)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()
		time.sleep(2)
		physics_interface_change_transparent_interface(browser,  interface2=interface_name_2)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_2, bridge_interface="br_1")
		time.sleep(1)
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_1", address_mode="manual", ip="13.1.1.3", mask="24")
		time.sleep(1)
		bridge_interface_obtain_ip_from_dhcp1_jyl(browser, bridge="br_1", work_mode="dhcp")
		time.sleep(1)
		webinfo3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(webinfo3)
		time.sleep(1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()

		time.sleep(1)
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
			assert "配置了静态ip地址" in webinfo1
			assert "配置了静态ip地址" in webinfo2
			assert "配置了静态ip地址" in webinfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "配置了静态ip地址" in webinfo1
			assert "配置了静态ip地址" in webinfo2
			assert "配置了静态ip地址" in webinfo3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])