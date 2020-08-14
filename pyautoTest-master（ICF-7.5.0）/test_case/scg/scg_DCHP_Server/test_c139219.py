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

test_id = "139219"
def test_c139219(browser):
	try:
		login_web(browser, url=dev3)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="34.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="34.1.1.4", ip_range1_2="34.1.1.20", senior="yes", static_ip="add",
							static_ip_add_num="1", static_ip_add1="34.1.1.21", static_mac_add1="00:10:81:E3:33:90",)
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
		login_web(browser, url=dev3)
		get_into_dhcp_lease(browser)
		# 主机的ip地址
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
		# print(webinfo1)
		login_web(browser, url=dev4)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='34.1.1.4', mask='24')
		time.sleep(1)
		login_web(browser, url=dev3)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		try:
			assert "34.1.1" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "34.1.1" in webinfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload([dev3, dev4])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])