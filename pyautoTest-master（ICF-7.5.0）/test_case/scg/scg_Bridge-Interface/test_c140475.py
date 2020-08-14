
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


test_id = "140475"
def test_c140475(browser):
	try:
		login_web(browser, url=dev4)
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 34.1.1.4")
		a.execute("work-mode transparent")
		a.execute("exit")
		bridge_add_jyl(browser, bridge_name="br_1", snat="yes")
		bridge_ip_add(browser, bridge_interface="br_1", address_mode="manual", ip="34.1.1.4", mask="24")
		dhcp_server_add_jyl(browser, interface="br_1", dhcp_type="dhcp_server", dhcp_gw="34.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="34.1.1.5", ip_range1_2="34.1.1.20")
		bridge_ip_add(browser, bridge_interface="br_1", address_mode="manual", ip="192.165.12.2", mask="24")
		loginfo1 = get_log(browser, 管理日志)
		delete_bridge_byname(browser, br_name="br_1")
		loginfo2 = get_log(browser, 管理日志)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		delete_bridge_byname(browser, br_name="br_1")
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("ip address 34.1.1.4 24")
		a.execute("exit")

		try:
			assert "成功" in loginfo1
			assert "失败" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "失败" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev4)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
