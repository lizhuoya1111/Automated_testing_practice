import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_physical_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141640

def test_c141640(browser):

	try:
		login_web(browser, url=dev1)
		# 物理接口获取IP地址
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		login_web(browser, url=dev3)
		time.sleep(2)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp")
		loginfo1 = get_log(browser, 管理日志)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url=dev3)
		time.sleep(2)
		physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp")

		time.sleep(1)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface=interface_name_2, work_mode="dhcp",
													 dhcp_status2="stop",)
		time.sleep(1)

		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='13.1.1.3', mask='24')
		loginfo2 = get_log(browser, 管理日志)

		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		try:
			assert "DHCP Client失败" in loginfo1
			assert "成功修改" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "DHCP Client失败" in loginfo1
			assert "成功修改" in loginfo2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])