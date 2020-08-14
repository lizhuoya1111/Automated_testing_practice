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

test_id = "21463"
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
		num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		if num == "0":
			browser.switch_to.default_content()
			# 定位到内容frame
			browser.switch_to.frame("content")
			# 选interface下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
			# 选interface下拉框内容
			s1.select_by_visible_text("ge0/3")
			# 点击增加
			browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			# 点击dhcp_server
			browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
			# 输入dhcp网关
			browser.find_element_by_xpath('//*[@id="gateway"]').send_keys("13.1.1.254")
			# 输入dhcp子网掩码
			browser.find_element_by_xpath('//*[@id="netmask"]').send_keys("24")
			# 清除dhcp 默认租约时间
			browser.find_element_by_xpath('//*[@id="day"]').clear()
			# 输入dhcp 租约时间
			browser.find_element_by_xpath('//*[@id="minute"]').send_keys("200")
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			time.sleep(2)
			webinfo = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
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
			browser.switch_to.default_content()
			# 定位到内容frame
			browser.switch_to.frame("content")
			# 选interface下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
			# 选interface下拉框内容
			s1.select_by_visible_text("ge0/3")
			# 点击增加
			browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			# 点击dhcp_server
			browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
			# 输入dhcp网关
			browser.find_element_by_xpath('//*[@id="gateway"]').send_keys("13.1.1.254")
			# 输入dhcp子网掩码
			browser.find_element_by_xpath('//*[@id="netmask"]').send_keys("24")
			# 清除dhcp 默认租约时间
			browser.find_element_by_xpath('//*[@id="day"]').clear()
			# 输入dhcp 租约时间
			browser.find_element_by_xpath('//*[@id="minute"]').send_keys("200")
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			time.sleep(2)
			webinfo = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			time.sleep(2)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert webinfo == "默认租约时间不能小于最小租约时间(5分钟)"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert webinfo == "默认租约时间不能小于最小租约时间(5分钟)"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])