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

test_id = 139270


def test_c139270(browser):
	try:
		login_web(browser, url=dev1)
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
		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)
		dhcp_server_edit_or_delete(browser, fuction="edit", dhcp_type="server",
		                           ip_range1_1="131.1.1.6", ip_range1_2="131.1.1.15")
		time.sleep(1)
		loginfo2 = get_log_info(browser, 管理日志)
		browser.switch_to.default_content()
		# print(loginfo2)
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		loginfo3 = get_log_info(browser, 管理日志)
		# print(loginfo3)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 131.1.1.1")
		a.execute("exit")
		try:
			assert "启动DHCP成功" in loginfo1
			assert "设置DHCP成功" in loginfo2
			assert "删除DHCP成功" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "启动DHCP成功" in loginfo1
			assert "设置DHCP成功" in loginfo2
			assert "删除DHCP成功" in loginfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
