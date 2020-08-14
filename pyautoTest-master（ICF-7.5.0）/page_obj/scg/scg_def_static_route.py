import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import sys
from page_obj.scg.scg_def import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_monitor import *


# 添加一条单网关静态路由
def add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='13.1.1.1',
								enable='yes/no'):

	""""添加一条单网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 点击单网关
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入目的ip
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="destination_ip"]').clear()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="destination_mask"]').clear()
	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(mask)
	# 选择输出接口
	# 找下拉框
	time.sleep(0.5)
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	time.sleep(1)
	# 输出网关
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)

	if enable == 'yes':
		pass
		# print("启用已开启")

	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="enable"]').click()
		# print("启用已关闭")

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()


# 改变路由的状态为enable或者disnable
def enable_static_route_single_wxw(browser, destination='20.1.1.0/255.255.255.0', enable='yes/no', disnable='yes/no'):

	"""改变路由的状态为enable或者disnable"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		if n <= 15:
			getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
		else:
			print("需要点击下一页")
			assert False
	# print(getdest)
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/input').is_selected()
	# print(status)

	if enable == "yes":
		if status == True:
			pass
			# print("状态已经是enable")
		else:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/input').click()
	if disnable == 'yes':
		if status == True:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/input').click()
		else:
			pass
			# print("状态已经是disable")


# 批量删除两个路由
def del_static_route_single_wxw(browser, destination1='20.1.1.0/255.255.255.0',
								destination2='21.1.1.0/255.255.255.0'):
	"""批量删除两个路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要删除的路由
	n = 2
	getdest1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	# print(getdest1)
	while getdest1 != destination1:
		n = n + 1
		time.sleep(1)
		getdest1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ',                                                                                                        '')
		# print(getdest1)
	# 找到元素后点击选择框
	browser.find_element_by_xpath('//*[@id="check_' + str(n - 2) + '"]').click()

	m = 2
	getdest2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[4]').text.replace(' ', '')
	while getdest2 != destination2:
		m = m + 1
		getdest2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[4]').text.replace(' ',
																												 '')
		# print(getdest2)
		# print(m)
	# 找到元素后点击选择框
	browser.find_element_by_xpath('//*[@id="check_' + str(m - 2) + '"]').click()
	time.sleep(2)
	# 选择删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()
	alert = browser.switch_to_alert()
	alert.accept()
	time.sleep(2)


# 编辑一条单网关静态路由
def edit_static_route_single_wxw(browser, destination='20.1.1.0/255.255.255.0', ip='20.1.1.0', mask='24',
								 out_device='ge0/2', gateway='13.1.1.1', enable='yes/no'):
	""""编辑一条单网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	# print(getdest)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()

	# 编辑目的ip
	browser.find_element_by_xpath('//*[@id="destination_ip"]').clear()
	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="destination_mask"]').clear()
	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(mask)
	# 选择输出接口
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	time.sleep(2)
	# 输出网关
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)

	status = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
	# print(status)

	if enable == "yes":
		if status == True:
			pass
			# print("状态已经是enable")
		else:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
	if enable == 'no':
		if status == True:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
		else:
			pass
			# print("状态已经是disable")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div[1]/input[3]').click()


# 删除一条单网关静态路由，多网关也适用，destination:ip/mask
def del_ipv4_static_route_bydestination(browser, destination=''):
	# browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 获取静态路由的总数
	rules_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	page_num = 0
	if int(rules_count) <= 15:
		# 循环遍历路由，得到直连路由的数量
		connect_num = 0
		for x in range(2, 2 + int(rules_count)):
			tmp1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text
			if tmp1 == " ":
				connect_num += 1
		# print("直连路由数量为：" + str(connect_num))
		for y in range(2 + connect_num, 2 + int(rules_count)):
			des_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[4]').text.replace(' ',
																													 '')
			if des_info == destination:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[9]/a[2]').click()
				# print("删除静态路由完成")
				break
	else:
		while 1:
			# 循环遍历路由，得到直连路由的数量 //*[@id="table"]/tbody/tr[16]/td[2]
			connect_num = 0
			# 判断一下路由总数，选择不同的直连上限 //*[@id="table"]/tbody/tr[2]/td[3]
			if 1 + int(rules_count) - page_num * 15 >= 15:
				connect_max = 17
			else:
				connect_max = 1 + int(rules_count) - page_num * 15
			for x in range(2, connect_max):
				time.sleep(0.5)
				# try:
				# 	browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
				# except:
				# 	pass
				# time.sleep(0.5)
				# print(x)
				tmp1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text
				if tmp1 == " ":
					connect_num += 1
			# print("直连路由数量为：" + str(connect_num))
			delete_flag = 0
			for y in range(2 + connect_num, 1 + int(rules_count) - page_num * 15):
				des_info = browser.find_element_by_xpath(
					'//*[@id="table"]/tbody/tr[' + str(y) + ']/td[4]').text.replace(' ', '')
				if des_info == destination:
					time.sleep(1)
					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[9]/a[2]').click()
					# print("删除静态路由完成")
					delete_flag = 1
					break
			if delete_flag == 1:
				break
			# 当前页面规则 // 15 > 0时 说明还以下一页
			if (int(rules_count) - page_num * 15) // 15 > 0:
				browser.find_element_by_xpath('//*[text()="下一页 > >"]')
				page_num += 1
			else:
				break


# 获取静态路由的状态
def get_static_route_status_wxw(browser, destination=''):

	"""获取静态路由的状态"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要查看的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	# print(getdest)
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/input').is_selected()
	# print(status)
	if status is True:
		# print("enable")
		return("enable")
	else:
		# print("disable")
		return("disable")


# 判断路由是否存在，若存在返回True,反之返回False
def is_static_route_exist_wxw(browser, destination=''):

	"""判断路由是否存在，若存在返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	# 只有第一页的情况
	if route_sum > 15:
		route_sum = 15
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', ''):
			return True
	else:
		return False


# 判断路由是否启用，若启用返回True,反之返回False
def is_static_route_enable_wxw(browser, destination=''):

	"""判断路由是否启用，若启用返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	# print(getdest)
	status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/input').is_selected()
	# print(status)
	if status is True:
		return True
	else:
		return False


# 获取静态路由的网关，找到返回网关，找不到返回None
def get_static_route_gateway_wxw(browser, destination=''):

	"""获取静态路由的网关"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	# time.sleep(2)
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', ''):
			gateway = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[5]').text.replace(' ', '')
			return gateway
	else:
		return None


# 获取静态路由的出接口，找到返回出接口，找不到返回None
def get_static_route_out_device_wxw(browser, destination=''):

	"""获取静态路由的出接口"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 获取目前有多少个路由
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据route数量,遍历一下
	# print(str(destination))
	for x in range(2, 2 + route_sum):
		if str(destination) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', ''):
			outdevice = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]').text.replace(' ', '')
			return outdevice
	else:
		return None


# 添加一条单网关静态路由（只到保存前）
def add_static_route_single_before_save_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='13.1.1.1',
								enable='yes/no'):

	""""添加一条单网关静态路由（只到保存前）"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 点击单网关
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="destination_ip"]').clear()
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="destination_mask"]').clear()
	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(mask)
	# 选择输出接口
	# 找下拉框
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	time.sleep(2)
	# 输出网关
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)

	if enable == 'yes':
		pass
		# print("启用已开启")

	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="enable"]').click()
		# print("启用已关闭")


# 添加一条多网关静态路由,grp_men是网关组的级别，输入列表
def add_static_route_multi_gateway_wxw(browser, ip='', mask='', gateway_grp='', num=4, grp_mem='',enable="yes/no",
									   save='yes/no', cancel='yes/no'):

	"""添加一条多网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 点击多网关
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask"]').clear()
	browser.find_element_by_xpath('//*[@id="mask"]').send_keys(mask)
	# 选择网关组
	# 找下拉框
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway"]'))
	# 找下拉框的内容//*[@id="mgws"]/tbody/tr[3]/td[3]/select
	s1.select_by_visible_text(gateway_grp)

	m = 2
	for n in grp_mem:
		# 找下拉框
		time.sleep(0.5)
		s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ '+str(m)+' ]/td[3]/select'))
		# 找下拉框的内容
		s1.select_by_visible_text(n)
		m = m + 1

	if enable == "yes":
		pass
		# print("状态默认为开启")
	if enable == "no":
		browser.find_element_by_xpath('//*[@id="enable"]').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()


# 编辑一条多网关静态路由
def edit_static_route_multi_gateway_wxw(browser, destination='', ip='', mask='', gateway_grp='', num=4, grp_mem='', enable="yes/no",
									   save='yes/no', cancel='yes/no'):

	"""编辑一条多网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 根据目的地址/掩码选择要编辑的路由
	n = 2
	getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	while getdest != destination:
		n = n + 1
		getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
	# print(getdest)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()

	# 编辑目的ip
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask"]').clear()
	browser.find_element_by_xpath('//*[@id="mask"]').send_keys(mask)
	# 选择输出接口
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(gateway_grp)

	m = 2
	for n in grp_mem:
		# 找下拉框
		time.sleep(1)
		s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ '+str(m)+' ]/td[3]/select'))
		# 找下拉框的内容
		s1.select_by_visible_text(n)
		m = m + 1

	status = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
	# print(status)

	if enable == "yes":
		if status is True:
			pass
		# print("状态已经是enable")
		else:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
	if enable == 'no':
		if status is True:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
		else:
			pass
	# print("状态已经是disable")

	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 添加一条多网关静态路由（只到保存前）
def add_static_route_multi_gateway_before_save_wxw(browser, ip='', mask='', gateway_grp='', num=4, grp_mem='',enable="yes/no",
									               save='yes/no', cancel='yes/no'):

	"""添加一条多网关静态路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 点击多网关
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask"]').clear()
	browser.find_element_by_xpath('//*[@id="mask"]').send_keys(mask)
	# 选择网关组
	# 找下拉框
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway"]'))
	# 找下拉框的内容//*[@id="mgws"]/tbody/tr[3]/td[3]/select
	s1.select_by_visible_text(gateway_grp)

	m = 2
	for n in grp_mem:
		# 找下拉框
		time.sleep(1)
		s1 = Select(browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ '+str(m)+' ]/td[3]/select'))
		# 找下拉框的内容
		s1.select_by_visible_text(n)
		m = m + 1

	if enable == "yes":
		pass
		# print("状态默认为开启")
	if enable == "no":
		browser.find_element_by_xpath('//*[@id="enable"]').click()


# 编辑多网关组
def edit_multi_gateway_group_wxw(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
								device=interface_name_3, gateway='24.1.1.7', ping_server='34.1.1.4', ping='yes/no', arp='yes/no',
								time_switch='7', ub="100000", db="100000"):

	"""编辑多网关组"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# time.sleep(2)
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:" + group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath(
					'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath(
						'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[3]/a').text
					# print(name_info)
					if name_info == name:
						# 点击编辑
						browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[9]/a[1]').click()

						# 修改网关组
						# 找下拉框
						s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
						# 找下拉框的内容
						s1.select_by_visible_text(group)

						if modify == "yes":
							# 点击更改
							browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
							# 输入别名
							browser.find_element_by_xpath('//*[@id="alias"]').clear()
							browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
							# 点击保存
							browser.find_element_by_xpath(
								'//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
							# 点击返回
							browser.find_element_by_xpath('//*[@id="link_but"]').click()

						# 选择设备
						s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
						# 找下拉框的内容
						s1.select_by_visible_text(device)
						# 选择网关
						time.sleep(2)
						browser.find_element_by_xpath('//*[@id="gateway"]').clear()
						browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
						# 选择ping服务器
						browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
						browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

						if ping == 'yes':
							browser.find_element_by_xpath('//*[@id="detectmethod_ping"]').click()
							# print('探测方式已为ping')
						if arp == 'yes':
							browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
						# 切换时间
						browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
						browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
						# 上传带宽
						browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
						browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
						# 下载带宽
						browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
						browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)
						# 点击保存
						browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
						return True
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return None


# 添加单网关静态路由 返回告警框内容 适用于 IP或掩码输入不规范弹出警告框时使用
def return_alert_after_add_static_route_single(browser, ip='20.1.1.0', mask='24', out_device=interface_name_1, gateway='192.168.1.2'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 静态路由)
	# 点击单网关
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入目的ip
	browser.find_element_by_xpath('//*[@id="destination_ip"]').clear()
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="destination_mask"]').clear()
	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(mask)
	# 选择输出接口
	# 找下拉框
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(out_device)
	time.sleep(2)
	# 输出网关
	browser.find_element_by_xpath('//*[@id="gateway"]').click()
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

	# 获取告警框信息
	alert = browser.switch_to_alert().text
	# print(alert)
	browser.switch_to_alert().accept()
	return alert


# 获取静态路由状态 up/down
def return_static_route_state(browser, destination=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击静态路由
	# browser.find_element_by_xpath(静态路由).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	state = "NULL"
	into_fun(browser, 静态路由)
	# 获取状态  （新添加的不正确的路由Xpath一定是//*[@id="table"]/tbody/tr[8]/td[7]）
	rules_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	page_num = 0
	if int(rules_count) <= 15:
		# 循环遍历路由，得到直连路由的数量
		connect_num = 0
		for x in range(2, 2 + int(rules_count)):
			tmp1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text
			if tmp1 == " ":
				connect_num += 1
		# print("直连路由数量为：" + str(connect_num))
		for y in range(2 + connect_num, 2 + int(rules_count)):
			des_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[4]').text.replace(
				' ',
				'')
			if des_info == destination:
				state = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[7]').text.strip()
				# print("删除静态路由完成")
				break
	else:
		while 1:
			# 循环遍历路由，得到直连路由的数量 //*[@id="table"]/tbody/tr[16]/td[2]
			connect_num = 0
			# 判断一下路由总数，选择不同的直连上限 //*[@id="table"]/tbody/tr[2]/td[3]
			if 1 + int(rules_count) - page_num * 15 >= 15:
				connect_max = 17
			else:
				connect_max = 1 + int(rules_count) - page_num * 15
			for x in range(2, connect_max):
				time.sleep(0.5)
				# try:
				# 	browser.find_element_by_xpath('//*[@id="current"]/a/span').click()
				# except:
				# 	pass
				# time.sleep(0.5)
				# print(x)
				tmp1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text
				if tmp1 == " ":
					connect_num += 1
			# print("直连路由数量为：" + str(connect_num))
			delete_flag = 0
			for y in range(2 + connect_num, 1 + int(rules_count) - page_num * 15):
				des_info = browser.find_element_by_xpath(
					'//*[@id="table"]/tbody/tr[' + str(y) + ']/td[4]').text.replace(' ', '')
				if des_info == destination:
					time.sleep(1)
					state = browser.find_element_by_xpath(
						'//*[@id="table"]/tbody/tr[' + str(y) + ']/td[7]').text.strip()
					# print("删除静态路由完成")
					delete_flag = 1
					break
			if delete_flag == 1:
				break
			# 当前页面规则 // 15 > 0时 说明还以下一页
			if (int(rules_count) - page_num * 15) // 15 > 0:
				browser.find_element_by_xpath('//*[text()="下一页 > >"]')
				page_num += 1
			else:
				break

	return state


# 返回静态路由网关信息
def return_static_route_gateway_by_destination(browser, destination=''):

	into_fun(browser, 静态路由)
	# 获取静态路由的总数
	rules_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# 循环遍历路由，得到直连路由的数量
	connect_num = 0
	for x in range(2, 2 + int(rules_count)):
		tmp1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text
		if tmp1 == " ":
			connect_num += 1
	# print("直连路由数量为：" + str(connect_num))
	for y in range(2 + connect_num, 2 + int(rules_count)):
		des_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[4]').text.replace(' ',
																												 '')
		if des_info == destination:
			gateway = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[5]').text
			return gateway
