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

test_id = 139264
def test_c139264(browser):
	try:
		login_web(browser, url=dev1)

		# 物理接口
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("ip address 131.1.1.1 255.255.255.0")
		a.execute("exit")
		dhcp_server_add(browser, interface=interface_name_3,
		                dhcp_type="dhcp_server", dhcp_gw="131.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="131.1.1.5", ip_range1_2="131.1.1.20")
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("ip address 132.1.1.1 255.255.255.0")
		a.execute("exit")
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]/span').text.rstrip()
		# print(webinfo1)
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 131.1.1.1")
		a.execute("no ip address 132.1.1.1")
		a.execute("exit")

		# 子接口
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="22", work_mode="route")
		time.sleep(1)
		add_vlan_inte_add(browser, interface_name=interface_name_3+".22", ipadd="131.1.1.1", mask="24")
		time.sleep(1)
		dhcp_server_add(browser, interface=interface_name_3+".22",
		                dhcp_type="dhcp_server", dhcp_gw="131.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="131.1.1.5", ip_range1_2="131.1.1.20")
		time.sleep(2)
		add_vlan_inte_add(browser, interface_name=interface_name_3+".22", ipadd="131.1.2.1", mask="24")
		time.sleep(1)
		webinfo2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(webinfo2)
		time.sleep(1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		time.sleep(1)
		del_vlan_inte_all(browser)
		time.sleep(1)

		# 网桥
		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_5)
		b.execute("work-mode transparent")
		b.execute("exit")
		bri_add(browser, bridge_name="br_1")
		time.sleep(1)
		bri_edit_interface(browser, interface=interface_name_5, bridge_interface="br_0")
		time.sleep(1)
		bridge_ip_add(browser, bridge_interface="br_0", address_mode="manual", ip="131.1.1.1", mask="24")
		time.sleep(1)
		dhcp_server_add(browser, interface="br_0",
		                dhcp_type="dhcp_server", dhcp_gw="131.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="131.1.1.5", ip_range1_2="131.1.1.20")
		time.sleep(1)
		bridge_ip_add(browser, bridge_interface="br_0", address_mode="manual", ip="132.1.1.1", mask="24")
		time.sleep(1)
		webinfo3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(webinfo3)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		time.sleep(1)
		delete_bridge(browser)
		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_5)
		b.execute("work-mode route")
		b.execute("exit")
		b.execute("interface bridge br_0")
		b.execute("no ip address 131.1.1.1")
		b.execute("no ip address 132.1.1.1")
		try:
			assert "已启用" == webinfo1
			assert "操作成功" == webinfo2
			assert "操作成功" == webinfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "已启用" == webinfo1
			assert "操作成功" == webinfo2
			assert "操作成功" == webinfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
