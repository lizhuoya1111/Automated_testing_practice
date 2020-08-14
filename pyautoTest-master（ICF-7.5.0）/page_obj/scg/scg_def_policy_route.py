import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *


# 添加一条单网关策略路由
def add_policy_route_single_wxw(browser, in_device='ge0/4', src_ip='', src_mask='',
								dst_ip='', dst_mask='', service='yes/no', serv='any',
								service_grp='yes/no', serv_grp='H323',
								out_device='', gateway='13.1.1.1', enable='yes/no',
								disnable='yes/no', desc='maioshu'):

	""""添加一条单网关策略路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 增加单网关路由
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(in_device)
	# 输入源ip
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(src_ip)
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(src_mask)
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(dst_ip)
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(dst_mask)

	if service == "yes":
		browser.find_element_by_xpath('//*[@id="srv_type_s"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv)
	if service_grp == 'yes':
		browser.find_element_by_xpath('//*[@id="srv_type_g"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv_grp)

	# 输出接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	# 输出网关
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	time.sleep(0.5)

	if enable == 'yes':
		pass
		# print("启用已开启")

	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="enable"]').click()
		# print("启用已关闭")

	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()


# 改变策略路由的状态为enable或者disnable
def enable_policy_route_single_wxw(browser, destination='12.1.1.0/255.255.255.0', enable='yes/no', disnable='yes/no'):

	"""改变路由的状态为enable或者disnable"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	# print(getdest)
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[10]/input').is_selected()
	# print(status)

	if enable == "yes":
		if status is True:
			pass
			# print("状态已经是enable")
		else:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[10]/input').click()
	if disnable == 'yes':
		if status is True:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[10]/input').click()
		else:
			pass
			# print("状态已经是disable")


# 编辑一条单网关策略路由
def edit_policy_route_single_wxw(browser, destination='12.1.1.0/255.255.255.0', in_device='ge0/4', src_ip='', src_mask='',
								 dst_ip='', dst_mask='', service='yes/no', serv='any',
								 service_grp='yes/no', serv_grp='H323',
								 out_device='', gateway='1', enable='yes/no',
								 disnable='yes/no', desc='maioshu'):

	""""编辑一条单网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[15]/a[1]/img').click()

	# 输入接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(in_device)
	# 编辑源ip
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="src_ip"]').clear()
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(src_ip)
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(src_mask)
	# 编辑目的ip
	browser.find_element_by_xpath('//*[@id="dst_ip"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(dst_ip)
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(dst_mask)

	if service == "yes":
		browser.find_element_by_xpath('//*[@id="srv_type_s"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv)
	if service_grp == 'yes':
		browser.find_element_by_xpath('//*[@id="srv_type_g"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv_grp)

	# 输出接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	# 输出网关
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	time.sleep(0.5)

	status = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
	# print(status)

	if enable == "yes":
		if status == True:
			pass
			# print("状态已经是enable")
		else:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
	if disnable == 'yes':
		if status == True:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
		else:
			pass
			# print("状态已经是disable")

	# 编辑描述
	browser.find_element_by_xpath('//*[@id="desc"]').clear()
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	time.sleep(0.5)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	time.sleep(0.5)


# 删除一条单网关策略路由
def del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0'):

	"""删除一条单网关策略路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要删除的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	# 删除按钮出现过找不到元素的情况，后续添加容错处理
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[15]/a[2]/img').click()


# 批量删除两个策略路由
def del_enable_policy_route_single_wxw(browser, destination1='12.1.1.0/255.255.255.0',
									   destination2='21.1.1.0/255.255.255.0'):

	"""批量删除两个策略路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要删除的路由
	n = 2
	getdest1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	# print(getdest1)
	while getdest1 != destination1:
		n = n + 1
		time.sleep(1)
		getdest1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
		# print(getdest1)
	# 找到元素后点击选择框
	browser.find_element_by_xpath('//*[@id="check_' + str(n - 2) + '"]').click()

	m = 2
	getdest2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[6]').text.replace(' ', '')
	while getdest2 != destination2:
		m = m + 1
		getdest2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[6]').text.replace(' ', '')
		# print(getdest2)
	# 找到元素后点击选择框
	browser.find_element_by_xpath('//*[@id="check_' + str(m - 2) + '"]').click()
	time.sleep(2)
	# 选择删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()
	alert = browser.switch_to_alert()
	alert.accept()
	time.sleep(2)


# 获取策略路由的状态
def get_policy_route_status_wxw(browser, destination=''):

	"""获取策略路由的状态"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要查看的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[10]/input').is_selected()
	# print(status)
	if status is True:
		# print("enable")
		return("enable")
	else:
		# print("disable")
		return("disable")


# 判断路由是否存在，若存在返回True,反之返回False
def is_policy_route_exist_wxw(browser, destination=''):

	"""判断路由是否存在，若存在返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		# 先控制在单页管用，后续考虑翻页
		if int(x) > 15:
			return False
		if str(destination) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			return True
	else:
		return False


# 获取策略路由的入接口
def get_policy_route_in_device_wxw(browser, destination=''):

	"""获取策略路由的入接口"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			indevice = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', '')
			return indevice
	else:
		return None


# 获取策略路由的源ip、掩码
def get_policy_route_source_wxw(browser, destination=''):

	"""获取策略路由的源ip、掩码"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			source = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[5]').text.replace(
				' ', '')
			return source
	else:
		return None


# 获取策略路由的服务
def get_policy_route_service_wxw(browser, destination=''):

	"""获取策略路由的服务"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			service = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[8]').text.replace(
				' ', '')
			return service
	else:
		return None


# 获取策略路由的网关
def get_policy_route_gateway_wxw(browser, destination=''):

	"""获取策略路由的网关"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下//*[@id="table"]/tbody/tr[2]/td[9]
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			gateway = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[9]').text.replace(
				' ', '')
			return gateway
	else:
		return None


# 获取策略路由得出接口
def get_policy_route_out_device_wxw(browser, destination=''):

	"""获取策略路由的出接口"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下//*[@id="table"]/tbody/tr[2]/td[9]
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', ''):
			gateway = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[7]').text.replace(
				' ', '')
			return gateway
	else:
		return None


# 判断路由是否启用，若启用返回True,反之返回False
def is_policy_route_enable_wxw(browser, destination=''):

	"""判断路由是否启用，若启用返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
	# print(getdest)
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[10]/input').is_selected()
	# print(status)
	if status is True:
		return True
	else:
		return False


# 添加一条多网关策略路由
def add_policy_route_multi_wxw(browser, in_device='ge0/4', src_ip='', src_mask='',
							   dst_ip='', dst_mask='', service='yes/no', serv='any',
							   service_grp='yes/no', serv_grp='H323',
							   gw_group='',  grp_mem='', enable='yes/no',
							   disable='yes/no', desc='maioshu', save='yes/no', cancel='yes/no'):

	""""添加一条多网关策略路由"""                                                                                                                                                                             
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 增加多网关路由
	into_fun(browser, 策略路由)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()

	# 选择输入接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(in_device)
	# 选择源ip
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(src_ip)
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(src_mask)
	# 选择目的ip
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(dst_ip)
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(dst_mask)
	time.sleep(1)

	if service == "yes":
		browser.find_element_by_xpath('//*[@id="service"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv)
	if service_grp == 'yes':
		browser.find_element_by_xpath('//*[@id="service_group"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv_grp)

	# 网关组
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="gw_group"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(gw_group)
	m = 2
	for n in grp_mem:
		# 找下拉框
		time.sleep(1)
		s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ ' + str(m) + ' ]/td[3]/select'))
		# 找下拉框的内容
		s1.select_by_visible_text(n)
		m = m + 1

	if enable == 'yes':
		pass
		# print("启用已开启")

	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="enable"]').click()
		# print("启用已关闭")

	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# time.sleep(2)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="submitbtn"]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()


# 添加一条单网关策略路由 用于输入不规范导致弹出警告框的情况  并返回告警信息
def return_alert_when_add_policy_route_single_(browser, in_device='全部', src_ip='', src_mask='',
								dst_ip='', dst_mask='', service='yes/no', serv='any',
								service_grp='yes/no', serv_grp='H323',
								out_device=interface_name_1, gateway='192.168.1.2', enable='yes/no', desc='maioshu'):

	""""添加一条单网关策略路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击策略路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 增加单网关路由
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(in_device)
	# 输入源ip
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(src_ip)
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(src_mask)
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(dst_ip)
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(dst_mask)

	if service == "yes":
		browser.find_element_by_xpath('//*[@id="srv_type_s"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv)
	if service_grp == 'yes':
		browser.find_element_by_xpath('//*[@id="srv_type_g"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv_grp)

	# 输出接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	# 输出网关
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	time.sleep(1)

	if enable == 'yes':
		pass
		# print("启用已开启")

	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="enable"]').click()
		# print("启用已关闭")

	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

	# 获取告警框信息
	alert = browser.switch_to_alert().text
	# print(alert)
	browser.switch_to_alert().accept()
	return alert


# 获取策略路由状态 up/down （页面第一条路由）
def return_policy_route_state(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(策略路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 策略路由)
	# 获取状态  （获取第一条路由的状态 ）
	state = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]').text.strip()
	return state


# 移动策略路由  根据索引号选择
def move_policy_route_by_Index_number_lzy(browser, Index_number, to_number):
	into_fun(browser, 策略路由)

	# 定位到需要移动的策略路由条目
	n = 2
	number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while number != Index_number:
		n = n + 1
		number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	# 点击移动
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[12]/a/img').click()
	# 输入移动到第几位
	browser.find_element_by_xpath('//*[@id="to_id"]').clear()
	browser.find_element_by_xpath('//*[@id="to_id"]').send_keys(to_number)
	# 点击确定
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 删除全部策略路由
def del_all_policy_route_lzy(browser):
	into_fun(browser, 策略路由)
	rule_max = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	while int(rule_max) != 0:
		# 选择全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
		# 点击删除所有
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		rule_max = browser.find_element_by_xpath('//*[@id="rules_count"]').text

# 点击向上add、向下add策略路由  根据索引号选择  目前向上向下添加单网关策略路由没出现问题  多网关还没验证
def add_policy_route_by_Index_number_upward_or_downward_lzy(browser, Index_number='', upward='yes/no',
                                                            downward='yes/no',
                                                            addmult='yes/no', m_in_device='全部', m_src_ip='',
                                                            m_src_mask='',
                                                            m_dst_ip='', m_dst_mask='', m_service='yes/no',
                                                            m_serv='any',
                                                            m_service_grp='yes/no', m_serv_grp='H323',
                                                            m_gw_group='', m_grp_mem='', m_enable='yes/no',
                                                            m_desc='maioshu', m_save='yes/no', m_cancel='yes/no',
                                                            addsingle='yes/no', s_in_device='全部', s_src_ip='',
                                                            s_src_mask='',
                                                            s_dst_ip='', s_dst_mask='', s_service='yes/no',
                                                            s_serv='any',
                                                            s_service_grp='yes/no', s_serv_grp='H323',
                                                            s_Intelligent_protocol='yes/no',
                                                            s_out_device='', s_gateway='', s_enable='yes/no',
                                                            s_desc='maioshu'):
	into_fun(browser, 策略路由)

	# 定位到需要移动的策略路由条目
	n = 2
	number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while number != Index_number:
		n = n + 1
		number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	if upward == 'yes':
		# 点击向上添加
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[14]/a[1]').click()
	if downward == 'yes':
		# 点击向下添加
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[14]/a[2]').click()
	if addmult == 'yes':
		# 点击增加多网关路由
		browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div/input[1]').click()
		# 跳转到增加多网关路由界面
		# 选择输入接口
		s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(m_in_device)
		# 选择源ip
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(m_src_ip)
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(m_src_mask)
		# 选择目的ip
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(m_dst_ip)
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(m_dst_mask)
		time.sleep(1)

		if m_service == "yes":
			browser.find_element_by_xpath('//*[@id="service"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(m_serv)
		if m_service_grp == 'yes':
			browser.find_element_by_xpath('//*[@id="service_group"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(m_serv_grp)

		# 网关组
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="gw_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(m_gw_group)
		m = 2
		for n in m_grp_mem:
			# 找下拉框
			time.sleep(1)
			s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ ' + str(m) + ' ]/td[3]/select'))
			# 找下拉框的内容
			s1.select_by_visible_text(n)
			m = m + 1

		if m_enable == 'yes':
			enable1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable1 == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable"]').click()

		if m_enable == 'no':
			enable2 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable2 == True:
				browser.find_element_by_xpath('//*[@id="enable"]').click()
			else:
				pass

		# 输入描述
		browser.find_element_by_xpath('//*[@id="desc"]').send_keys(m_desc)
		# time.sleep(2)
		if m_save == "yes":
			# 点击保存
			browser.find_element_by_xpath('//*[@id="submitbtn"]').click()
		if m_cancel == "yes":
			browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()

	if addsingle == 'yes':
		# 点击增加单网关路由
		browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div/input[2]').click()
		# 跳转到增加单网关路由界面
		# 输入接口
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_in_device)
		# 输入源ip
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(s_src_ip)
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(s_src_mask)
		# 输入目的ip
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(s_dst_ip)
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(s_dst_mask)

		if s_service == "yes":
			browser.find_element_by_xpath('//*[@id="srv_type_s"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv)
		if s_service_grp == 'yes':
			browser.find_element_by_xpath('//*[@id="srv_type_g"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv_grp)
		if s_Intelligent_protocol == 'yes':
			browser.find_element_by_xpath('///*[@id="srv_type_ipr"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="ipr"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv_grp)

		# 输出接口
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_out_device)
		# 输出网关
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gateway"]').clear()
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(s_gateway)
		time.sleep(1)

		if s_enable == 'yes':
			enable1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable1 is True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable"]').click()

		if s_enable == 'no':
			enable2 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable2 is True:
				browser.find_element_by_xpath('//*[@id="enable"]').click()
			else:
				pass

		# 输入描述
		browser.find_element_by_xpath('//*[@id="desc"]').send_keys(s_desc)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 修改多网关策略路由 根据索引号选择
def edit_policy_route_multi_by_index_number_lzy(browser, index_number='',
                                                in_device='', src_ip='', src_mask='', dst_ip='', dst_mask='',
                                                service='yes/no', serv='any',
                                                service_grp='yes/no', serv_grp='H323', gw_group='', grp_mem='',
                                                enable='yes/no', desc='maioshu', save='yes/no', cancel='yes/no'):
	into_fun(browser, 策略路由)

	# 定位到需要修改的策略路由条目
	n = 2
	number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while number != index_number:
		n = n + 1
		number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	# 点击修改
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[15]/a[1]/img').click()
	# 跳转到多网关组策略路由界面
	# 选择输入接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(in_device)
	# 选择源ip
	browser.find_element_by_xpath('//*[@id="src_ip"]').clear()
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(src_ip)
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(src_mask)
	# 选择目的ip
	browser.find_element_by_xpath('//*[@id="dst_ip"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(dst_ip)
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
	browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(dst_mask)
	time.sleep(1)

	if service == "yes":
		browser.find_element_by_xpath('//*[@id="service"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv)
	if service_grp == 'yes':
		browser.find_element_by_xpath('//*[@id="service_group"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(serv_grp)

	# 网关组
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="gw_group"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(gw_group)
	m = 2
	for n in grp_mem:
		# 找下拉框
		time.sleep(1)
		s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ ' + str(m) + ' ]/td[3]/select'))
		# 找下拉框的内容
		s1.select_by_visible_text(n)
		m = m + 1

	if enable == 'yes':
		enable1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
		if enable1 == True:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="enable"]').click()

	if enable == 'no':
		enable2 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
		if enable2 == True:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
		else:
			pass

	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').clear()
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# time.sleep(2)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()


# 克隆策略路由  根据索引号选择
def clone_policy_route_by_Index_number_lzy(browser, Index_number):
	into_fun(browser, 策略路由)

	# 定位到需要克隆的策略路由条目
	n = 2
	number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while number != Index_number:
		n = n + 1
		number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	# 点击克隆 //*[@id="table"]/tbody/tr[2]/td[13]/a
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[13]/a').click()
	# 添加描述以区分
	browser.find_element_by_xpath('//*[@id="desc"]').clear()
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys('我是克隆出来哒')
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 克隆策略路由完整 可修改参数  根据索引号选择
def clone_policy_route_by_Index_number_complete_lzy(browser, Index_number,
													clonemult='yes/no', m_in_device='全部', m_src_ip='',m_src_mask='',
													m_dst_ip='', m_dst_mask='', m_service='yes/no', m_serv='any',
													m_service_grp='yes/no', m_serv_grp='H323',
													m_gw_group='', m_grp_mem='', m_enable='yes/no',
													m_desc='maioshu', m_save='yes/no', m_cancel='yes/no',
													clonesingle='yes/no', s_in_device='全部', s_src_ip='',s_src_mask='',
													s_dst_ip='', s_dst_mask='', s_service='yes/no',s_serv='any',
													s_service_grp='yes/no', s_serv_grp='H323', s_Intelligent_protocol='yes/no',
													s_out_device='', s_gateway='', s_enable='yes/no', s_desc='maioshu'):
	into_fun(browser, 策略路由)

	# 定位到需要克隆的策略路由条目
	n = 2
	number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while number != Index_number:
		n = n + 1
		number = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	# 点击克隆
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[13]/a').click()
	if clonemult == 'yes':

		# 跳转到增加多网关路由界面
		# 选择输入接口
		s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(m_in_device)
		# 选择源ip
		browser.find_element_by_xpath('//*[@id="src_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(m_src_ip)
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(m_src_mask)
		# 选择目的ip
		browser.find_element_by_xpath('//*[@id="dst_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(m_dst_ip)
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(m_dst_mask)
		time.sleep(1)

		if m_service == "yes":
			browser.find_element_by_xpath('//*[@id="service"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(m_serv)
		if m_service_grp == 'yes':
			browser.find_element_by_xpath('//*[@id="service_group"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(m_serv_grp)

		# 网关组
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="gw_group"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(m_gw_group)
		m = 2
		for n in m_grp_mem:
			# 找下拉框
			time.sleep(1)
			s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ ' + str(m) + ' ]/td[3]/select'))
			# 找下拉框的内容
			s1.select_by_visible_text(n)
			m = m + 1

		if m_enable == 'yes':
			enable1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable1 == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable"]').click()

		if m_enable == 'no':
			enable2 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable2 == True:
				browser.find_element_by_xpath('//*[@id="enable"]').click()
			else:
				pass

		# 输入描述
		browser.find_element_by_xpath('//*[@id="desc"]').clear()
		browser.find_element_by_xpath('//*[@id="desc"]').send_keys(m_desc)
		# time.sleep(2)
		if m_save == "yes":
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
		if m_cancel == "yes":
			browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()

	if clonesingle == 'yes':

		# 跳转到增加单网关路由界面
		# 输入接口
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="in_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_in_device)
		# 输入源ip
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="src_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(s_src_ip)
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="src_mask_len"]').send_keys(s_src_mask)
		# 输入目的ip
		browser.find_element_by_xpath('//*[@id="dst_ip"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(s_dst_ip)
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_mask_len"]').send_keys(s_dst_mask)

		if s_service == "yes":
			browser.find_element_by_xpath('//*[@id="srv_type_s"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv)
		if s_service_grp == 'yes':
			browser.find_element_by_xpath('//*[@id="srv_type_g"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="service_group"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv_grp)
		if s_Intelligent_protocol == 'yes':
			browser.find_element_by_xpath('///*[@id="srv_type_ipr"]').click()
			# 找下拉框
			s1 = Select(browser.find_element_by_xpath('//*[@id="ipr"]'))
			# 找下拉框的内容
			s1.select_by_visible_text(s_serv_grp)

		# 输出接口
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_out_device)
		# 输出网关
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="gateway"]').clear()
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(s_gateway)
		time.sleep(1)

		if s_enable == 'yes':
			enable1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable1 == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="enable"]').click()

		if s_enable == 'no':
			enable2 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
			if enable2 == True:
				browser.find_element_by_xpath('//*[@id="enable"]').click()
			else:
				pass

		# 输入描述
		browser.find_element_by_xpath('//*[@id="desc"]').clear()
		browser.find_element_by_xpath('//*[@id="desc"]').send_keys(s_desc)
		# 点击保存
		sleep(1)
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()