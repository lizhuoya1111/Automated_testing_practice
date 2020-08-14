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

test_id = "21386"
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		a = Shell_SSH()
		a.connect("10.2.2.81")
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
		num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		if num == "0":
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
		else:
			i = 0
			while i < int(num):
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
					i += 1
				else:
					# 点击删除
					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
					time.sleep(2)
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					time.sleep(2)
					i += 1
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
			dhcp_server_add_jyl(browser, interface="br_19", dhcp_type="dhcp_server", dhcp_gw="13.1.18.254", dhcp_sm="24")
			time.sleep(2)
			# 点击删除
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[7]/a[2]/img').click()
			time.sleep(2)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()

		get_log(browser, 管理日志)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		print(loginfo)
		i = 1
		for i in range(1, 11):
			dhcp_server_edit_or_delete(browser, fuction="delete")
			i += 1
			a = Shell_SSH()
			a.connect("10.2.2.81")
			a.execute("en")
			a.execute("conf t")
			a.execute("no interface bridge br_10")
			time.sleep(2)
			a.execute("no interface bridge br_11")
			time.sleep(2)
			a.execute("no interface bridge br_12")
			time.sleep(2)
			a.execute("no interface bridge br_13")
			time.sleep(2)
			a.execute("no interface bridge br_14")
			time.sleep(2)
			a.execute("no interface bridge br_15")
			time.sleep(2)
			a.execute("no interface bridge br_16")
			time.sleep(2)
			a.execute("no interface bridge br_17")
			time.sleep(2)
			a.execute("no interface bridge br_18")
			time.sleep(2)
			a.execute("no interface bridge br_19")
			time.sleep(2)
			a.execute("exit")

		try:
			assert "删除DHCP成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "删除DHCP失败" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])