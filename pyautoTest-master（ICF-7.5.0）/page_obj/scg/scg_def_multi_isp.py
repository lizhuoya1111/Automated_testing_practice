import pytest
import os
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
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_multi_gateway_group import *


# 添加isp后保存
def add_multi_isp_save_wxw(browser, name='', desc=''):

	""""添加isp后保存
	:rtype: object
	"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加isp后保存前
def add_multi_isp_before_save_wxw(browser, name='', desc=''):

	""""添加isp后保存前"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)


# 添加isp后取消
def add_multi_isp_cancel_wxw(browser, name='', desc=''):

	""""添加isp后取消"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)
	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除指定的isp
def del_multi_isp_wxw(browser, name=''):

	"""删除指定的isp"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(0.5)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	# print(str(name))
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(' ', ''):
			pass
			# print(str(name))

			try:
				browser.implicitly_wait(2)
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[2]').click()
			except:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a').click()


# 通过名字删除所有的ips
def del_multi_isp_byname(browser, name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(str(name))
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(' ', ''):
			# print(str(name))
			button_info = browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a/img').get_attribute("title")
			if button_info == "编辑":
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[2]').click()
				# print("删除有编辑的按钮的条目完成")
				return "ok"
			elif button_info == "删除":
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a/img').click()
				# print("删除无编辑的按钮的条目完成")
				return "ok"
			else:
				# print("error")
				return "error"


# 判断isp是否存在，若存在返回True,反之返回False
def is_multi_isp_exist_wxw(browser, name=''):

	"""判断isp是否存在，若存在返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(' ', ''):
			return True
	else:
		return False


# 给isp导入ip配置文件
def import_ip_config_file_wxw(browser, name='', save='yes/no', cancel='yes/no', file='isp.txt'):

	"""给isp导入ip配置文件"""
	# 切换到默认frame filepath+'\\'+file
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(0.5)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	getcwd = os.path.realpath(__file__)
	filepath = os.path.abspath(getcwd+r"..\\..\\..\\..\\importfile\\isp.file\\")
	# print(filepath)
	# print(filepath+'\\'+file)
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[9]/a').click()
			browser.find_element_by_xpath('//*[@id="uploadFile"]').send_keys(filepath+'\\'+file)
			if save == 'yes':
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
			if cancel == "yes":
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[5]').click()
			return True
	else:
		# print("没有找到指定isp")
		return None


# 获取isp的显示ip
def get_isp_show_ip_wxw(browser, name=''):

	"""获取isp的显示ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[8]/a').click()
			time.sleep(2)
			try:
				browser.implicitly_wait(2)
				ip = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.replace(' ', '')
				return ip
			except:
				return ("ip is null")
	else:
		print("没有找到指定isp")
		return None


# 编辑只有姓名和描述的isp
def edit_multi_isp_wxw(browser, name='', newname='', newdesc=''):

	"""编辑只有姓名和描述的isp"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[1]').click()
			# 编辑名称//*[@id="name2"]
			browser.find_element_by_xpath('//*[@id="name2"]').clear()
			browser.find_element_by_xpath('//*[@id="name2"]').send_keys(newname)
			# 编辑描述
			browser.find_element_by_xpath('//*[@id="desc"]').clear()
			browser.find_element_by_xpath('//*[@id="desc"]').send_keys(newdesc)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
			return True
	else:
		print("没有找到指定isp")
		return None


# 清除isp的ip
def clear_isp_ip_wxw(browser, name=''):

	"""清除isp的ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			# 点击清除ip
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[10]/a').click()
			time.sleep(1)
			return True
	else:
		print("没有找到指定isp")
		return None


# 添加isp路由
def add_isp_route_wxw(browser, name='', single_gateway='yes/no', device='', gateway='',
					  multi_gateway='yes/no', gateway_group='',
					  enable='yes/no', disable='yes/no'):

	"""添加isp路由"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			# 点击添加isp路由
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[11]/a').click()
			if single_gateway == 'yes':
				# 选择设备
				# 找下拉框
				s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
				# 找下拉框的内容
				s1.select_by_visible_text(device)
				# 输入网关
				time.sleep(3)
				browser.find_element_by_xpath('//*[@id="gateway"]').clear()
				browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
			if multi_gateway == 'yes':
				# 点击多网关
				browser.find_element_by_xpath('//*[@id="gw_type_m"]').click()
				# 选择多网关组：
				# 找下拉框
				s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
				# 找下拉框的内容
				s1.select_by_visible_text(gateway_group)
				# 选择主用/备用





			if enable == "yes":
				pass
				# print('默认状态为已开启')
			if disable == "yes":
				browser.find_element_by_xpath('//*[@id="enable"]')
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div/div[2]/div/input[3]').click()
			return True
	else:
		# print("没有找到指定isp")
		return None



# 删除所有isp
def del_all_multi_isp_wxw(browser):

	""""删除所有isp"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	alert = browser.switch_to_alert()
	alert.accept()


# 获取isp总数
def get_isp_sum_wxw(browser):

	""""获取isp总数"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击ISP自动选择
	# browser.find_element_by_xpath(ISP自动选择).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ISP自动选择)
	sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text.replace(' ', ''))
	return sum1



# 添加isp路由 包括多网关组的情况 根据名称
def add_isp_route_lzy(browser, name='', single_gateway='yes/no', device='', gateway='',
					  multi_gateway='yes/no', gateway_group='', grp_mem='',
					  enable='yes/no', disable='yes/no'):


	into_fun(browser, ISP自动选择)

	# 获取目前有多少个isp
	time.sleep(0.5)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据isp数量,遍历一下
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			# 点击添加isp路由
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[11]/a').click()
			if single_gateway == 'yes':
				# 选择设备
				# 找下拉框
				s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
				# 找下拉框的内容
				s1.select_by_visible_text(device)
				# 输入网关
				time.sleep(1)
				browser.find_element_by_xpath('//*[@id="gateway"]').clear()
				browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
			if multi_gateway == 'yes':
				# 点击多网关 //*[@id="gw_type_m"]
				sleep(0.5)
				browser.find_element_by_xpath('//*[@id="gw_type_m"]').click()
				# 选择多网关组：
				# 找下拉框
				s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
				# 找下拉框的内容
				s1.select_by_visible_text(gateway_group)
				# 选择主用/备用
				m = 2
				for n in grp_mem:
					# 找下拉框
					time.sleep(1)
					s1 = Select(
						browser.find_element_by_xpath('//*[@id="mgws"]/tbody/tr[ ' + str(m) + ' ]/td[3]/select'))
					# 找下拉框的内容
					s1.select_by_visible_text(n)
					m = m + 1

			if enable == 'yes':
				en = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
				if en == True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="enable"]').click()
			if disable == 'yes':
				en = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
				if en == True:
					browser.find_element_by_xpath('//*[@id="enable"]').click()
				else:
					pass
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div/div[2]/div/input[3]').click()
			return True
	else:
		# print("没有找到指定isp")
		return None


# 修改ISP启用/不启用 通过名字
def edit_isp_enable_or_disable_byname(browser, name='', enable='yes/no', disable='yes/no'):
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(1)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(str(name))  //*[@id="table"]/tbody/tr[2]/td[3]
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			if enable == 'yes':
				en = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/input').is_selected()
				if en == True:
					pass
				else:
					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/input').click()
			if disable == 'yes':
				en = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/input').is_selected()
				if en == True:
					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/input').click()
				else:
					pass
		else:
			print('无该ISP路由')


# 清除ISP路由 通过名字
def del_isp_route_byname(browser, name=''):
	into_fun(browser, ISP自动选择)
	# 获取目前有多少个isp
	time.sleep(0.5)
	isp_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(str(name))  //*[@id="table"]/tbody/tr[2]/td[3]
	for x in range(2, 2 + isp_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(
				' ', ''):
			# 点击清除
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[12]/a').click()
		# # 点击返回
		# browser.find_element_by_xpath('//*[@id="link_but"]').click()
		else:
			print('无该ISP路由')