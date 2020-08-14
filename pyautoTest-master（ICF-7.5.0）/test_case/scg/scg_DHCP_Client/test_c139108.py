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

test_id = "139108"
def test_c139108(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="",
		                    ip_range1_1="13.1.1.2", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()
		login_web(browser, url=dev3)
		time.sleep(2)
		physics_interface_from_dhcp_obtain_ip_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp",
		                                          dhcp_status1="release_recapture", dhcp_status2="click")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(5)
		result1 = a.output()
		# print(result1)
		# 点击停止
		a.close()
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()

		vlan_add_jyl(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		time.sleep(2)
		a.close()
		vlan_interface_from_dhcp_obtain_ip_jyl(browser, vlan_interface=interface_name_2+".22", work_mode="dhcp",
		                                       dhcp_status1="release_recapture", dhcp_status2="click")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(2)
		result2 = a.output()
		# print(result2)
		a.close()
		time.sleep(1)
		vlan_delete_jyl(browser)
		time.sleep(1)
		physics_interface_change_transparent_interface(browser,  interface2=interface_name_2,)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_2, bridge_interface="br_1")
		time.sleep(1)
		bridge_interface_from_dhcp_obtain_ip_jyl(browser, bridge="br_1", work_mode="dhcp",
		                                         dhcp_status1="release_recapture", dhcp_status2="click")
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.1")
		time.sleep(2)
		result3 = a.output()
		# print(result3)
		a.close()

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
		a.close()
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "ms" in result1
			assert "ms" in result2
			assert "ms" in result3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "ms" in result2
			assert "ms" in result3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])