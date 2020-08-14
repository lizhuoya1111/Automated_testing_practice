import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_interface import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = "21428"


def test_c21428(browser):
	try:
		login_web(browser, url=dev2)
		dhcp_server_add(browser, interface=interface_name_3, dhcp_gw="24.1.1.2", ip_range1_1="24.1.1.100", ip_range1_2="24.1.1.200")
		login_web(browser, url=dev4)
		change_addrmod_physical_inte(browser, interface_name_3, "DHCP")
		ping = Shell_SSH()
		ping.connect(dev4)
		ping.execute("en")
		ping.execute("ping 24.1.1.2")
		time.sleep(5)
		ping_info = ping.output()
		# print(ping_info)
		if "Round-trip" in str(ping_info):
			login_web(browser, url=dev2)
			dhcp_server_edit_or_delete(browser, fuction="delall")
			login_web(browser, url=dev4)
			dhcp_stat = get_interface_dhcp_status(browser, interface_name_3)
			print(dhcp_stat)
			try:
				assert "断开" == str(dhcp_stat)
				rail_pass(test_run_id, test_id)

			except Exception as err1:
				print(err1)
				rail_fail(test_run_id, test_id)
				assert "断开" == str(dhcp_stat)
		else:
			# 恢复配置
			login_web(browser, url=dev2)
			dhcp_server_edit_or_delete(browser, fuction="delall")
			login_web(browser, url=dev4)
			# print("111111")
			change_addrmod_physical_inte(browser, interface_name_3, "静态")
			add_net_ineterface(browser, "24.1.1.4", "255.255.255.0", interface_name_3)

		login_web(browser, url=dev4)
		change_addrmod_physical_inte(browser, interface_name_3, "静态")
		add_net_ineterface(browser, "24.1.1.4", "255.255.255.0", interface_name_3)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev2)
		reload(hostip=dev4)
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])