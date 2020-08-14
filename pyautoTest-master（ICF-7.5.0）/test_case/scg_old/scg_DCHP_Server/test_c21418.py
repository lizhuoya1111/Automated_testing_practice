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
test_id = "21418"
def test_main(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add(browser, interface=interface_name_3,
		                dhcp_type="dhcp_server", dhcp_gw="13.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		time.sleep(1)
		dhcp_server_add(browser, interface=interface_name_2,
		                dhcp_type="dhcp_server", dhcp_gw="12.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="12.1.1.4", ip_range1_2="12.1.1.20")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		b = Shell_SSH()
		b.connect(dev2)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet ge0/2")
		b.execute("no ip address 12.1.1.2")
		b.execute("exit")
		time.sleep(1)
		login_web(browser, url=dev3)
		time.sleep(2)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface=interface_name_2)
		time.sleep(2)
		webinfo1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text
		# print(webinfo1)
		time.sleep(1)
		login_web(browser, url=dev2)
		time.sleep(2)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface=interface_name_2)
		time.sleep(2)
		webinfo2 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text
		# print(webinfo2)
		login_web(browser, url=dev1)
		dhcp_renting_list_jyl(browser)
		time.sleep(1)
		#82 ge0/2
		webinfo3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
		# print(webinfo3)
		time.sleep(1)
		#83 ge0/3
		webinfo4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[2]').text.rstrip()
		# print(webinfo4)
		time.sleep(1)
		login_web(browser, url=dev3)
		time.sleep(1)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp", dhcp_status2="stop",)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		login_web(browser, url=dev2)
		time.sleep(1)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp", dhcp_status2="stop",)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("work-mode route")
		a.execute("ip address 12.1.1.2 255.255.255.0")
		a.execute("exit")
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert webinfo1 == webinfo3
			assert webinfo2 == webinfo4
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert webinfo1 == webinfo3
			assert webinfo2 == webinfo4
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		reload(hostip=dev2)
		reload(hostip=dev3)
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])