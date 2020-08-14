import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_dns import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *

test_id = "139091"
def test_c139091(browser):
	try:
		login_web(browser, url=dev3)
		add_dns_jyl(browser, master_dns="114.114.114.114")
		login_web(browser, url=dev1)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="118.118.118.118",
		                    ip_range1_1="13.1.1.2", ip_range1_2="13.1.1.20", )
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()
		login_web(browser, url=dev3)
		physical_interface_update_dhcp_jyl(browser, physical_interface=interface_name_2,  update_system_dns="open")
		location_dns_jyl(browser)
		time.sleep(5)
		webinfo1 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
		# print(webinfo1)

		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='13.1.1.3', mask='24')

		login_web(browser, url=dev1)
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "114.114.114.114" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "114.114.114.114" in webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev3])
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])