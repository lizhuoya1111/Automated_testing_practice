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


test_id = 140471
def test_c140471(browser):
	try:
		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")
		bridge_ip_add(browser, bridge_interface="br_1", address_mode="manual", ip="134.1.1.4", mask="24")
		dhcp_server_add_jyl(browser, interface="br_1", dhcp_type="dhcp_server", dhcp_gw="134.1.1.4",
							dhcp_sm="24")

		into_fun(browser, 网桥)
		# 点击ST
		browser.find_element_by_xpath('//*[@id="refid_1"]/img').click()
		time.sleep(3)
		reference_info = browser.find_element_by_xpath('//*[@id="JT_copy"]').text
		# print(reference_info)

		dhcp_server_edit_or_delete(browser, fuction="delete")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("exit")
		try:
			assert "DHCP-Server" in reference_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "DHCP-Server" in reference_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
