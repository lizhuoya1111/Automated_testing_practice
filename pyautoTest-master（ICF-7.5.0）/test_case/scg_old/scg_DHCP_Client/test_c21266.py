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
test_id = "21266"
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_add_jyl(browser, interface="ge0/3", dhcp_type="dhcp_server", dhcp_gw="13.1.1.254",
		                    dhcp_sm="255.255.255.0", dns_server1="117.117.117.117", wins_server1="",
		                    ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		login_web(browser, url="10.2.2.83")
		time.sleep(2)
		physical_interface_update_dhcp_jyl(browser, physical_interface="ge0/2")
		time.sleep(2)
		b = Shell_SSH()
		b.connect("10.2.2.83")
		b.execute("en")
		b.execute("show interface gigabitethernet ge0/2")
		time.sleep(5)
		result1 = b.output()
		print(result1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 获取界面ip
		getname = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text
		print(getname)
		physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface="ge0/2", work_mode="dhcp", dhcp_status2="stop",)
		time.sleep(5)
		add_physical_interface_static_ip_jyl(browser, interface='ge0/2', ip='13.1.1.3', mask='24')
		time.sleep(2)
		login_web(browser, url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(DHCP).click()
		# 点击物理接口
		browser.find_element_by_xpath(DHCP设定).click()
		dhcp_server_edit_or_delete_jyl(browser, fuction="delete")

		try:
			assert getname in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert getname in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])