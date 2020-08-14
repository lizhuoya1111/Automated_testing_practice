import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_route import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
test_id = "139248"
def test_c139248(browser):
	try:
		login_web(browser, url=dev3)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="34.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="34.1.1.5", ip_range1_2="34.1.1.20")
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 34.1.1.4")
		a.execute("switchmode trunk")
		a.execute("exit")
		login_web(browser, url=dev4)
		time.sleep(1)
		physical_interface_update_dhcp_jyl(browser, physical_interface=interface_name_2)

		b = Shell_SSH()
		b.connect(dev5)
		b.execute("en")
		b.execute("conf t")
		b.execute("ip route 34.1.1.0/24 gateway 45.1.1.4")
		b.execute("exit")

		b = Shell_SSH()
		b.connect(dev4)
		b.execute("en")
		b.execute("ping 45.1.1.5")
		result = b.output()
		print(result)

		a = Shell_SSH()
		a.connect(dev5)
		a.execute("en")
		a.execute("no ip route 34.1.1.0/24 gateway 45.1.1.4")
		a.execute("exit")

		login_web(browser, url=dev4)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='34.1.1.4', mask='24')
		time.sleep(1)
		login_web(browser, url=dev3)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "ms" in result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload([dev3, dev4, dev5])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])