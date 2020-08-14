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
test_id = "139197"
def test_c139197(browser):
	try:
		login_web(browser, url=dev3)
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_server", dhcp_gw="34.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="34.1.1.4", ip_range1_2="34.1.1.20", senior="yes", static_ip="add",
							static_ip_add_num="2", static_ip_add2="34.1.1.21", static_mac_add2="00:10:81:E3:33:90",
							static_ip_add3="34.1.1.22", static_mac_add3="00:10:80:E3:33:70")
		get_log(browser, 管理日志)
		loginfo1 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		get_into_dhcp_server(browser, interface=interface_name_3)
		# 点击删除
		browser.find_element_by_xpath('//*[@id="del_staticip_link"]').click()
		get_log(browser, 管理日志)
		loginfo2 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert "成功" in loginfo1
			assert "管理员" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "管理员" in loginfo2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])