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

test_id = "139160"
def test_c139160(browser):
	try:
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url=dev3)
		time.sleep(1)
		physical_interface_update_dhcp_jyl(browser, physical_interface=interface_name_2, update_default_gateway="open")

		dhcp_server_add_jyl(browser, interface=interface_name_2, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="13.1.1.5", ip_range1_2="13.1.1.20")
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address dhcp")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "失败" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "失败" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])