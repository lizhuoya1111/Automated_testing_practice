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

test_id = "21393"
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/3")
		a.execute("ip address 13.1.2.1 255.255.255.0")
		a.execute("ip address 13.1.3.1 255.255.255.0")
		a.execute("ip address 13.1.4.1 255.255.255.0")
		a.execute("exit")
		dhcp_server_add(browser, interface="ge0/3",
		                dhcp_type="dhcp_server", dhcp_gw="13.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="13.1.1.4", ip_range1_2="13.1.1.20")
		get_log(browser, 管理日志)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		loginfo1 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(loginfo1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		time.sleep(1)
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/3")
		a.execute("no ip address 13.1.2.1")
		a.execute("no ip address 13.1.3.1")
		a.execute("no ip address 13.1.4.1")
		a.execute("exit")
		try:
			assert "启动DHCP成功" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "启动DHCP成功" in loginfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.81")
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])