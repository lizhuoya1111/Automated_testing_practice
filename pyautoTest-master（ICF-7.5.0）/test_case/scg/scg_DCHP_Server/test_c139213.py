import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.common.ssh import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *
test_id = "139213"
def test_c139213(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_10")
		a.execute("ip address 13.1.10.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_11")
		a.execute("ip address 13.1.11.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_12")
		a.execute("ip address 13.1.12.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_13")
		a.execute("ip address 13.1.13.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_14")
		a.execute("ip address 13.1.14.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_15")
		a.execute("ip address 13.1.15.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_16")
		a.execute("ip address 13.1.16.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_17")
		a.execute("ip address 13.1.17.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_18")
		a.execute("ip address 13.1.18.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface bridge br_19")
		a.execute("ip address 13.1.19.1 255.255.255.0")
		a.execute("exit")
		dhcp_server_add_jyl(browser, interface="br_10", dhcp_type="dhcp_server", dhcp_gw="13.1.10.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_11", dhcp_type="dhcp_server", dhcp_gw="13.1.11.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_12", dhcp_type="dhcp_server", dhcp_gw="13.1.12.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_13", dhcp_type="dhcp_server", dhcp_gw="13.1.13.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_14", dhcp_type="dhcp_server", dhcp_gw="13.1.14.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_15", dhcp_type="dhcp_server", dhcp_gw="13.1.15.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_16", dhcp_type="dhcp_server", dhcp_gw="13.1.16.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_17", dhcp_type="dhcp_server", dhcp_gw="13.1.17.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_18", dhcp_type="dhcp_server", dhcp_gw="13.1.18.254", dhcp_sm="24")
		time.sleep(2)
		dhcp_server_add_jyl(browser, interface="br_19", dhcp_type="dhcp_server", dhcp_gw="13.1.19.254", dhcp_sm="24")
		time.sleep(2)
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[7]/a[2]/img').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		loginfo = get_log(browser, 管理日志)
		print(loginfo)

		dhcp_server_edit_or_delete(browser, fuction="delete")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_10")
		a.execute("no interface bridge br_11")
		a.execute("no interface bridge br_12")
		a.execute("no interface bridge br_13")
		a.execute("no interface bridge br_14")
		a.execute("no interface bridge br_15")
		a.execute("no interface bridge br_16")
		a.execute("no interface bridge br_17")
		a.execute("no interface bridge br_18")
		a.execute("no interface bridge br_19")
		a.execute("exit")


		try:
			assert "删除DHCP成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "删除DHCP成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])