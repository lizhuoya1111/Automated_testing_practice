import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
test_id = "21277"


def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		transparent_interface_change_physics_interface_jyl(browser, interface5="ge0/5")
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/5")
		a.execute("ip address 192.165.12.2 255.255.255.0")
		a.execute("exit")
		# 定位到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击DHCP
		browser.find_element_by_xpath(DHCP).click()
		# 点击DHCP设定
		browser.find_element_by_xpath(DHCP设定).click()
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		dhcp_server_add_jyl(browser, interface="ge0/5", dhcp_type="dhcp_server", dhcp_gw="192.165.12.1",
		                    dhcp_sm="255.255.255.0", dns_server1="114.114.114.114", ip_range1_1="192.165.12.3",
		                    ip_range1_2="192.165.12.13")
		time.sleep(3)
		num = Shell_SSH()
		num.connect('10.1.1.212', 'root', 'root')
		num.execute('sudo dhclient -r')
		num.execute('sudo dhclient')
		num.execute('ping 192.165.12.2 -c 2')
		time.sleep(10)
		result1 = num.output()
		print(result1)
		num.execute('ifconfig eth1 21.1.1.2 netmask 255.255.255.0')
		num.execute('exit')
		enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击关闭启用
			browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			# 点击删除
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
			time.sleep(2)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			time.sleep(2)
		else:
			# 点击删除
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
			time.sleep(2)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			time.sleep(2)
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/5")
		a.execute("no ip address 192.165.12.2")
		a.execute("exit")
		time.sleep(2)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		physics_interface_change_transparent_interface(browser, interface5="ge0/5")
		try:
			assert "ttl" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])

