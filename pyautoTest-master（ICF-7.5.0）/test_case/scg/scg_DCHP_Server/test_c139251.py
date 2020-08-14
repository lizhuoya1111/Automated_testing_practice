
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
from page_obj.scg.scg_def import *
test_id = "139251"
def test_c139251(browser):
	try:
		login_web(browser, url=dev4)
		dhcp_server_add_jyl(browser, interface=interface_name_2, dhcp_type="dhcp_server", dhcp_gw="34.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="34.1.1.5", ip_range1_2="34.1.1.20")
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("dhcp-relay server 45.1.1.6")
		a.execute("dhcp-relay enable")
		a.execute("exit")
		save_sys(browser)
		reload(hostip=dev4, switch="重启")

		login_web(browser, url=dev4)
		get_into_dhcp_set(browser)
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text.rstrip()
		webinfo2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[3]').text.rstrip()

		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_4)
		a.execute("no dhcp-relay enable")
		a.execute("no dhcp-relay")
		a.execute("exit")
		login_web(browser, url=dev4)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")
		save_sys(browser)

		try:
			assert "服务器" in webinfo1
			assert "中继" in webinfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "服务器" in webinfo1
			assert "中继" in webinfo2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev4)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])