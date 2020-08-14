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

test_id = "139112"
def test_c139112(browser):
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
		a.close()
		login_web(browser, url=dev3)
		time.sleep(1)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp")
		time.sleep(1)
		is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(1)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp", dhcp_status2="stop",)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 13.1.1.4 255.255.255.0")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.1")
		time.sleep(1)
		result2 = a.output()
		# print(result2)
		a.close()
		time.sleep(1)
		b = Shell_SSH()
		b.connect(dev3)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_2)
		b.execute("no ip address 13.1.1.4")
		b.execute("exit")
		time.sleep(1)
		a.close()

		vlan_add_jyl(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		time.sleep(1)
		a.close()
		vlan_interface_obtain_ip_from_dhcp_jyl(browser, vlan_interface=interface_name_2+".22", work_mode="dhcp")
		time.sleep(1)
		is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(1)
		vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface=interface_name_2+".22",  dhcp_status2="stop",)
		time.sleep(1)
		b = Shell_SSH()
		b.connect(dev3)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface vlan "+interface_name_2+".22")
		b.execute("ip address 13.1.1.4 255.255.255.0")
		b.execute("exit")
		b.execute("exit")
		b.execute("ping 13.1.1.1")
		time.sleep(1)
		result4 = b.output()
		# print(result4)
		a.close()
		time.sleep(2)
		c = Shell_SSH()
		c.connect(dev3)
		c.execute("en")
		c.execute("conf t")
		c.execute("interface vlan "+interface_name_2+".22")
		c.execute("no ip address 13.1.1.4")
		c.execute("exit")
		time.sleep(1)
		a.close()
		vlan_delete_jyl(browser)

		physics_interface_change_transparent_interface(browser,  interface2=interface_name_2)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_2, bridge_interface="br_1")
		time.sleep(1)
		bridge_interface_obtain_ip_from_dhcp_jyl(browser, bridge="br_1")
		time.sleep(1)
		is_static_route_exist_wxw(browser, destination='13.1.1.0/255.255.255.0')
		time.sleep(1)
		bridge_interface_obtain_ip_dhcp_status_jyl(browser, bridge="br_1", work_mode="dhcp", dhcp_status2="stop")
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_1")
		a.execute("ip address 13.1.1.4 255.255.255.0")
		a.execute("exit")
		a.execute("exit")
		a.execute("ping 13.1.1.1")
		time.sleep(1)
		result6 = a.output()
		# print(result6)
		time.sleep(1)
		a.close()
		delete_bridge_jyl(browser)
		time.sleep(3)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		a.close()
		time.sleep(2)
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		try:
			assert "ms" in result2
			assert "ms" in result4
			assert "ms" in result6
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result2
			assert "ms" in result4
			assert "ms" in result6

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])