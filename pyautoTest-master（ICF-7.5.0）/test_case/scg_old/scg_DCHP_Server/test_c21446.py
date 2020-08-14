import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *

test_id = "21446"
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
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
		# 获取页面配置数
		num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		if num == "0":
			configuer(browser)
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
			configuer(browser)
		time.sleep(2)
		get_log(browser, 管理日志)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		loginfo1 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(loginfo1)

		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击DHCP
		#browser.find_element_by_xpath(DHCP).click()
		# 点击DHCP设定
		browser.find_element_by_xpath(DHCP设定).click()
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击终止
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		time.sleep(2)
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		browser.find_element_by_xpath(日志).click()
		browser.find_element_by_xpath(管理日志).click()
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		loginfo2 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
		# print(loginfo2)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert "启动DHCP成功" in loginfo1
			assert "终止DHCP成功" in loginfo2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "启动DHCP成功" in loginfo1
			assert "终止DHCP成功" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False

def configuer(browser):
	dhcp_server_add_jyl(browser, interface="ge0/3", dhcp_type="dhcp_rely", dhcp_rely_server1="117.117.117.117")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])