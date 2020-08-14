
import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "141790"

# 本测试用例包含"shell配置与UI配置的对比检查"


def test_c141790(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode route")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="55", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_5+".55", ipadd="192.165.12.3", mask="24")
		loginfo1 = get_log_info(browser, 管理日志)

		login_web(browser, url=dev3)

		dhcp_server_add_jyl(browser, interface=interface_name_2, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")

		login_web(browser, url=dev1)
		del_vlan_inte_add(browser, interface_name=interface_name_5 + ".55", ipadd="192.165.12.3")
		vlan_interface_obtain_ip_from_dhcp_jyl(browser, vlan_interface=interface_name_5+".55", work_mode="dhcp")
		time.sleep(1)
		loginfo2 = get_log(browser, 管理日志)
		# print(loginfo2)
		time.sleep(1)
		vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface=interface_name_5+".55",  dhcp_status2="stop",)
		time.sleep(1)

		del_vlan_inte_all(browser)

		login_web(browser, url=dev3)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		try:
			assert "成功" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])