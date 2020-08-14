import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *


#  监控过滤
def monitor_filter_wxw(browser, dest='0.0.0.0', gateway='10.2.2.1', route_type='全部', search='yes', reset='no'):

	""" 监控过滤"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击路由监控
	# browser.find_element_by_xpath(路由监控).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 路由监控)
	# 输入要过滤的目的地
	browser.find_element_by_xpath('//*[@id="destination"]').send_keys(dest)
	# 输入要过滤的网关
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	# 选择要过滤的类型
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="type"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(route_type)

	if search == 'yes':
		browser.find_element_by_xpath('//*[@id="notes"]/table/tbody/tr[2]/td[7]/input[2]').click()
	if reset == 'yes':
		browser.find_element_by_xpath('//*[@id="notes"]/table/tbody/tr[2]/td[7]/input[3]').click()


# 获得各种路由类型的数量（直连路由、静态路由等），返回整形
def get_routenum(browser, r_type='全部'):
	into_fun(browser, 路由监控)
	# 选择要过滤的类型
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="type"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(r_type)
	# 点击查询，并获得数量
	browser.find_element_by_xpath('//*[@id="notes"]/table/tbody/tr[2]/td[7]/input[2]').click()
	time.sleep(1)
	route_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	return route_num


# 获得各种路由类型的信息（直连路由、静态路由等），返回索引行的信息字符串元组（索引，目的IP/掩码，网关，输出接口，状态，启用，类型）
def get_route_monitor_info(browser, r_type='全部,policy,connected,static,ospf,isp-auto,默认', index=1):
	into_fun(browser, 路由监控)
	# 选择要过滤的类型
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="type"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(r_type)
	# 点击查询，并获得数量 //*[@id="route_monitor_table"]/tbody/tr[2]/td[2]
	browser.find_element_by_xpath('//*[@id="notes"]/table/tbody/tr[2]/td[7]/input[2]').click()
	time.sleep(1)
	route_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	r_index = r_dest_ip_mask = r_gw = r_outif = r_sataus = r_enable = r_class = ''
	for x in range(2, 2+int(route_num)):
		r_index = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[1]').text
		r_dest_ip_mask = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[2]').text
		r_gw = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[3]').text
		r_outif = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[4]').text
		r_sataus = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[5]').text
		r_enable = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[6]').text
		r_class = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[' + str(x) + ']/td[7]').text
	return r_index, r_dest_ip_mask, r_gw, r_outif, r_sataus, r_enable, r_class
