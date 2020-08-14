import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_button import *
import pytest
from selenium import webdriver
import time
from page_obj.scg.scg_def_ipv4acl import *
from selenium.webdriver.support.ui import Select
from page_obj.common.my_selenium import *


# 添加acl组（只有name）
def add_acl_group_wxw(browser, name='acl_group'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 点击保存
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


#  删除所有防火墙组，并加上一个默认组
def del_all_acl_group_wxw(browser):
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# time.sleep(0.5)
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 删除所有组
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()
	time.sleep(0.5)
	# 接受告警
	browser.switch_to_alert().accept()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys("default")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul/li[4]/a').click()
	time.sleep(1)
	# 保存//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


#  删除所有防火墙组,不添加默认组
def del_all_acl_group_noadd_wxw(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 删除所有组
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()

	# 接受告警
	browser.switch_to_alert().accept()


# 给一个防火墙组添加一条acl规则
# def add_acl_rule_complete_wxw(browser, aclgroup_name='', source_zone_interface=interface_name_4,
# 							  source_custom='no', fromip='', fromnetmask='',
# 							  source_address_object='yes', s_address_object='A:any',
# 							  mac='',
# 							  dest_custom='no', toip='', tonetmask='',
# 							  dest_address_object='yes', d_address_object='A:any',
# 							  dest_zone_interface=interface_name_2,
# 							  service='P:any', schdule='-- 无 --',
# 							  accept='yes', drop='no',
# 							  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no'):
# 	"""给一个防火墙组添加一条acl规则"""
# 	# 切换到默认frame
# 	# browser.switch_to.default_content()
# 	# # 切换到左侧frame
# 	# browser.switch_to.frame("lefttree")
# 	# # 点击防火墙
# 	# browser.find_element_by_xpath(防火墙).click()
# 	# # 点击IPv4访问组列表
# 	# browser.find_element_by_xpath(IPv4访问控制列表).click()
# 	#
# 	# # 定位到默认frame
# 	# browser.switch_to.default_content()
# 	# # 定位到内容frame
# 	# browser.switch_to.frame("content")
# 	into_fun(browser, IPv4访问控制列表)
# 	n = 1
# 	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
# 	print("222222222222222")
# 	# print(getname)
# 	while getname != aclgroup_name:
# 		n = n + 1
# 		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
# 	# print(getname)
#
# 	# 添加规则
# 	time.sleep(1)
# 	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
# 	time.sleep(1)
#
# 	# 来源
# 	# 找下拉框(源接口)
# 	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
# 	# 找下拉框的内容
# 	s1.select_by_visible_text(source_zone_interface)
#
# 	if source_custom == 'yes':
# 		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
# 		browser.find_element_by_xpath('//*[@id="fromip"]').send_keys(fromip)
# 		browser.find_element_by_xpath('//*[@id="fromnetmask"]').clear()
# 		browser.find_element_by_xpath('//*[@id="fromnetmask"]').send_keys(fromnetmask)
#
# 	if source_address_object == 'yes':
# 		time.sleep(0.5)
# 		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
# 		# 找下拉框
# 		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
# 		# 找下拉框的内容
# 		s1.select_by_visible_text(s_address_object)
#
# 	# 点击输入mac
# 	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
#
# 	# 目的
# 	# 找下拉框（目的接口）
# 	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
# 	# 找下拉框的内容
# 	s1.select_by_visible_text(dest_zone_interface)
#
# 	if dest_custom == 'yes':
# 		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
# 		browser.find_element_by_xpath('//*[@id="toip"]').send_keys(toip)
# 		browser.find_element_by_xpath('//*[@id="tonetmask"]').clear()
# 		browser.find_element_by_xpath('//*[@id="tonetmask"]').send_keys(tonetmask)
#
# 	if dest_address_object == 'yes':
# 		time.sleep(1)
# 		browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
# 		# 找下拉框
# 		s1 = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
# 		# 找下拉框的内容
# 		s1.select_by_visible_text(d_address_object)
#
# 	# 服务
# 	# 找下拉框
# 	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
# 	# 找下拉框的内容
# 	s1.select_by_visible_text(service)
#
# 	# 计划任务
# 	# 找下拉框
# 	s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
# 	# 找下拉框的内容
# 	s1.select_by_visible_text(schdule)
#
# 	if accept == 'yes':
# 		browser.find_element_by_xpath('//*[@id="action_0"]').click()
# 		# 认证
# 		# 找下拉框
# 		s1 = Select(browser.find_element_by_xpath('//*[@id="auth"]'))
# 		# 找下拉框的内容
# 		s1.select_by_visible_text(auth)
#
# 	if drop == 'yes':
# 		browser.find_element_by_xpath('//*[@id="action_1"]').click()
#
# 	# 是否选择icf
# 	if icf == "yes":
# 		browser.find_element_by_xpath('//*[@id="log"]').click()
#
# 	# 是否选择日志
# 	if log == "yes":
# 		browser.find_element_by_xpath('//*[@id="icf"]').click()
#
# 	# 是否保存
# 	if save == 'yes':
# 		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
# 	# 是否取消
# 	if cancel == 'yes':
# 		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[7]')




def acl_click_group_enable_button_jyl(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	time.sleep(2)
	enable = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul/li[2]/input').is_selected()
	if enable is True:
		time.sleep(1)
		# 点击关闭启用
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul/li[2]/input').click()
	else:
		# 点击启用
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul/li[2]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 删除指定防火墙组
def del_acl_group_wxw(browser, name='acl_group'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 点击删除
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# 点击删除
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(n)+']/li[5]/a[2]/img').click()


# 添加acl组
def add_acl_group_complete(browser, name='acl_group', enable='yes/no', sour='Z:any', dest='Z:any', desc='miaoshu', save='yes', cancel='no'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	time.sleep(1)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 是否启用
	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/input').click()
	# 选择源接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(sour)
	# 选择目的接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(dest)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 点击保存/取消
	time.sleep(1)
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	if cancel == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()


# 添加acl组(到保存前)
def add_acl_group_before_save(browser, name='acl_group', enable='yes/no', sour='Z:any', dest='Z:any', desc='miaoshu'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)

	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 是否启用
	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/input').click()
	# 选择源接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(sour)
	# 选择目的接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(dest)
	# 输入描述
	# 点击保存/取消
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)


# 给一个防火墙组添加一条acl规则(到保存前)
def add_acl_rule_before_save_wxw(browser, aclgroup_name='', source_zone_interface=interface_name_4,
							  source_custom='no', fromip='', fromnetmask='',
							  source_address_object='yes', s_address_object='A:any',
							  mac='',
							  dest_custom='no', toip='', tonetmask='',
							  dest_address_object='yes', d_address_object='A:any',
							  dest_zone_interface=interface_name_2,
							  service='P:any', schdule='-- 无 --',
							  accept='yes', drop='no',
							  auth='-- 无 --', icf='no', log='no'):
	"""给一个防火墙组添加一条acl规则"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
	time.sleep(2)

	# 来源
	# 找下拉框(源接口)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(source_zone_interface)

	if source_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="fromip"]').send_keys(fromip)
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').send_keys(fromnetmask)

	if source_address_object == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_address_object)

	# 点击输入mac
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)

	# 目的
	# 找下拉框（目的接口）
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(dest_zone_interface)

	if dest_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="toip"]').send_keys(toip)
		browser.find_element_by_xpath('//*[@id="tonetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="tonetmask"]').send_keys(tonetmask)

	if dest_address_object == 'yes':
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(d_address_object)

	# 服务
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(service)

	# 计划任务
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(schdule)

	if accept == 'yes':
		browser.find_element_by_xpath('//*[@id="action_0"]').click()
		# 认证
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(auth)

	if drop == 'yes':
		browser.find_element_by_xpath('//*[@id="action_1"]').click()

	# 是否选择icf
	if icf == "yes":
		browser.find_element_by_xpath('//*[@id="log"]').click()

	# 是否选择日志
	if log == "yes":
		browser.find_element_by_xpath('//*[@id="log"]').click()


# 添加ipv6访问列表组(到保存前)
def add_ipv6_acl_group_before_save(browser, name='acl_group', enable='yes/no', sour='Z:any', dest='Z:any', desc='miaoshu'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv6访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv6访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 是否启用
	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/input').click()
	# 选择源接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(sour)
	# 选择目的接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(dest)
	# 输入描述
	# 点击保存/取消
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)


# 添加ipv6防火墙组
def add_ipv6_acl_group_complete(browser, name='acl_group', enable='yes/no', sour='Z:any', dest='Z:any', desc='miaoshu', save='yes', cancel='no'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv6访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv6访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 是否启用
	if enable == 'no':
		browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/input').click()
	# 选择源接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(sour)
	# 选择目的接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(dest)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 点击保存/取消
	time.sleep(1)
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	if cancel == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()


# 删除指定ipv6防火墙组
def del_ipv6_acl_group_wxw(browser, name='acl_group'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv6访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv6访问控制列表)
	# 点击删除
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# 点击删除
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(n)+']/li[5]/a[2]/img').click()


# 启用/禁用防火墙组
def enable_acl_group_wxw(browser, aclgroup_name='default', enable='yes/no'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 判断该条防火墙组是否被启用
	enable1 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[2]/input').is_selected()
	# print(enable1)
	if enable == "yes":
		if enable1 is True:
			# print("该防火墙组已被启用")
			pass
		else:
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[2]/input').click()

	if enable == "no":
		if enable1 is True:
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[2]/input').click()
		else:
			# print("该防火墙组已被禁用")
			pass


# 编辑acl规则,仅支持ACL组内只有一条规则的情况
def edit_acl_rule_wxw(browser, aclgroup_name='', source_zone_interface=interface_name_4,
					  source_custom='no', fromip='', fromnetmask='',
					  source_address_object='yes', s_address_object='A:any',
					  mac='',
					  dest_custom='no', toip='', tonetmask='',
					  dest_address_object='yes', d_address_object='A:any',
					  dest_zone_interface=interface_name_2,
					  service='P:any', schdule='-- 无 --',
					  accept='yes', drop='no',
					  auth='-- 无 --', icf='no', log='no',
					  save='yes', cancel='no'
					  ):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 点击展开
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到frame
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame" + str(n - 1))
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[12]/a[1]/img').click()
	time.sleep(3)

	browser.switch_to.frame("content")
	# 来源
	# 找下拉框(源接口)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(source_zone_interface)

	if source_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="fromip"]').clear()
		browser.find_element_by_xpath('//*[@id="fromip"]').send_keys(fromip)
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').send_keys(fromnetmask)

	if source_address_object == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_address_object)

	# 点击输入mac
	browser.find_element_by_xpath('//*[@id="mac"]').clear()
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)

	# 目的
	# 找下拉框（目的接口）
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(dest_zone_interface)

	if dest_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="toip"]').clear()
		browser.find_element_by_xpath('//*[@id="toip"]').send_keys(toip)
		browser.find_element_by_xpath('//*[@id="tonetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="tonetmask"]').send_keys(tonetmask)

	if dest_address_object == 'yes':
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(d_address_object)

	# 服务
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(service)
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(schdule)

	if accept == 'yes':
		browser.find_element_by_xpath('//*[@id="action_0"]').click()
		# 认证
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(auth)

	if drop == 'yes':
		browser.find_element_by_xpath('//*[@id="action_1"]').click()

	# 是否选择icf
	if icf == "yes":
		if(browser.find_element_by_xpath('//*[@id="icf"]').is_selected()) is True:
			pass
			# print("icf已经选中")
		else:
			browser.find_element_by_xpath('//*[@id="icf"]').click()

	# 是否选择日志
	if log == "yes":
		if (browser.find_element_by_xpath('//*[@id="log"]').is_selected()) is True:
			pass
			# print("log已经选中")
		else:
			browser.find_element_by_xpath('//*[@id="log"]').click()

	# 点击保存
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()
	# 点击取消
	if cancel == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()


# 移动ipv4访问控制列表,输入序列号进行移动
def move_ipc4_acl(browser, group_name, from_id="", to_id=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 定位到需要的acl组,n是组的id
	n = 1
	get_acl_sum = 0
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	get_acl_sum = int(
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
	while getname != group_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
		get_acl_sum = int(browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)

	# 获取当前组是否展开，若没有展开，需要点击展开
	# print("获取当前组是否展开，若没有展开，需要点击展开")
	image_info = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').get_attribute('src')
	if "defButton_f.gif" in image_info:
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	# print(n-1)
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到frame
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame"+str(n-1))

	# for x1 in range(1, get_acl_sum+1):
	# 当只有两条acl时，且要把第二条上移到第一条，直接点击上移
	if get_acl_sum == 2:
		if int(from_id) == 2 and int(to_id) == 1:
			browser.find_element_by_xpath(
				'//*[@id="storage_new_zone"]/div[2]/ul/li[8]/a/img').click()


	if int(from_id) <= get_acl_sum and get_acl_sum > 2:
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(from_id)+']/ul/li[10]/input').send_keys(to_id)
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(from_id)+']/ul/li[9]/a/img').click()


# 移动ipv4访问控制列表,点击上下移动,传给acl ID，和移动方式
def move_ipc4_acl_click(browser, group_name, acl_id, move="up/down"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 定位到需要的acl组,n是组的id
	n = 1
	get_acl_sum = 0
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	get_acl_sum = int(
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
	while getname != group_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
		get_acl_sum = int(browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)

	# 获取当前组是否展开，若没有展开，需要点击展开
	# print("获取当前组是否展开，若没有展开，需要点击展开")
	image_info = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').get_attribute('src')
	if "defButton_f.gif" in image_info:
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	# print(n-1)
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到frame
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame"+str(n-1))

	if int(acl_id) == 1:
		if move == "down":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[8]/a/img').click()
		else:
			print("acl组1已在顶部，无法上移")
	elif int(acl_id) == int(get_acl_sum):
		if move == "up":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[8]/a/img').click()
		else:
			print("acl组1已在底部，无法下移")
	else:
		if move == "up":
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[8]/a[1]/img').click()
		elif move == "down":
			# print("downdowndown")
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[8]/a[2]/img').click()


# 移动ipv4访问控制列表组,传给函数组ID，和移动方式
def move_ipc4_acl_group_simple(browser, group_id, move="up/down"):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# 定位到需要的acl组,n是组的id
	# print(group_id)
	# print(group_sum)
	if int(group_id) == 1:
		if move == "down":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[1]/li[3]/a/img').click()
		else:
			print("acl组1已在顶部，无法上移")
	elif int(group_id) == int(group_sum):
		if move == "up":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(group_sum)+']/li[3]/a/img').click()
		else:
			print("acl组1已在底部，无法下移")
	else:
		if move == "up":
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(group_id)+']/li[3]/a[1]/img').click()
		elif move == "down":
			# print("downdowndown")
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(group_id)+']/li[3]/a[2]/img').click()


# 获取指定组ID的组名称,返回组名称字符串
def get_groupname_byid(browser, group_id):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(group_id) + ']/li[1]/span[1]/a').text
	return getname


# 删除指定组内的acl规则，需要指定要删除的acl的id号,每次删除一条
def del_acl_byid(browser, group_name, acl_id):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 定位到需要的acl组,n是组的id
	n = 1
	get_acl_sum = 0
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	get_acl_sum = int(
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
	while getname != group_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
		get_acl_sum = int(
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)

	# 获取当前组是否展开，若没有展开，需要点击展开
	# print("获取当前组是否展开，若没有展开，需要点击展开")
	image_info = browser.find_element_by_xpath(
		'//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').get_attribute('src')
	if "defButton_f.gif" in image_info:
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	# print(n-1)
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到frame
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame" + str(n - 1))

	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[12]/a[2]/img').click()


# 删除指定组内的多个acl规则，需要指定要删除的acl的id号列表，多选后点击删除按钮,
def del_acls_byids(browser, group_name, acl_id_list=[], all_del="no"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 定位到需要的acl组,n是组的id
	n = 1
	get_acl_sum = 0
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	get_acl_sum = int(
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)
	while getname != group_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
		get_acl_sum = int(
			browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text)

	# 获取当前组是否展开，若没有展开，需要点击展开
	# print("获取当前组是否展开，若没有展开，需要点击展开")
	image_info = browser.find_element_by_xpath(
		'//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').get_attribute('src')
	if "defButton_f.gif" in image_info:
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	# print(n-1)
	time.sleep(2)
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到frame
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame" + str(n - 1))
	time.sleep(1)

	# 如果all_del='yes',则全选后选择删除
	if all_del == 'yes':
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[4]/ul/li/a[1]').click()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[4]/ul/li/a[2]').click()
		time.sleep(0.5)
		browser.switch_to_alert().accept()
	else:
		for g in acl_id_list:
			browser.find_element_by_xpath(
				'//*[@id="storage_new_zone"]/div['+str(g)+']/ul/li[1]/input[1]').click()
			time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[6]/ul/li/a[2]/img').click()
		time.sleep(0.5)
		browser.switch_to_alert().accept()


# 克隆规则
def clone_ipv4acl_lzy(browser, group_name, aclnum):
	# 切换frame,点击IPv4访问控制列表
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 切换frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 定位组  //*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a
	n = 1
	groupname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(n)+']/li[1]/span[1]/a').text
	while groupname != group_name:
		n = n+1
		groupname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# 展开组
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/img[2]').click()
	# 切换frame
	browser.switch_to.default_content()
	browser.switch_to.frame("content")
	browser.switch_to.frame("iFrame" + str(n - 1))
	time.sleep(2)
	# 定位规则
	m = 1
	num = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[' + str(m) + ']/ul/li[1]/span').text
	while num != aclnum:
		m = m+1
		num = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[' + str(m) + ']/ul/li[1]/span').text

	# 点击克隆
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[' + str(m) + ']/ul/li[11]/a[2]').click()
	time.sleep(2)
	browser.switch_to.frame("content")
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[5]').click()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 高级搜索（根据XX查找acl）
def find_ipv4acl_lzy(browser, source_zone_interface='选择项目', source_custom='no', fromip='', fromnetmask='',
					 source_address_object='yes', s_address_object='选择项目', dest_zone_interface='选择项目',
					 dest_custom='no', toip='', tonetmask='', dest_address_object='yes', d_address_object='选择项目',
					 service='选择项目', action='', accept='yes', drop=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 点击高级搜索
	browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/div/input').click()
	# 找下拉框(源接口)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(source_zone_interface)
	if source_custom == 'yes':
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="fromip"]').send_keys(fromip)
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').send_keys(fromnetmask)

	if source_address_object == 'yes':
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_address_object)
	# 目的
	# 找下拉框（目的接口）
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(dest_zone_interface)

	if dest_custom == 'yes':
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="toip"]').send_keys(toip)
		browser.find_element_by_xpath('//*[@id="tonetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="tonetmask"]').send_keys(tonetmask)

	if dest_address_object == 'yes':
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(d_address_object)
	# 服务

	# 找下拉框（服务）
	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(service)


	# 动作
	if action == 'yes':
		browser.find_element_by_xpath('//*[@id="action_ck"]').click()
		if accept == 'yes':
			browser.find_element_by_xpath('//*[@id="action_0"]').click()
		if drop == 'yes':
			browser.find_element_by_xpath('//*[@id="action_1"]').click()

	# 点击保存
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[10]').click()


# 添加acl规则 传参数记得把不是yes的no掉
def add_ipv4acl_lzy(browser, aclgroup_name='', source_zone_interface='Z:any',
							  source_custom='no', fromip='', fromnetmask='',
							  source_address_object='yes', s_address_object='A:any',
							  mac='', dest_zone_interface='Z:any',
							  dest_custom='no', toip='', tonetmask='',
							  dest_address_object='yes', d_address_object='A:any',
							  service='P:any', schdule='-- 无 --',
							  accept='yes', drop='no',
							  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no'):
	"""给一个防火墙组添加一条acl规则"""

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
	time.sleep(2)

	# 来源
	# 找下拉框(源接口)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(source_zone_interface)

	if source_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="fromip"]').send_keys(fromip)
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="fromnetmask"]').send_keys(fromnetmask)
		browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()

	if source_address_object == 'yes':
		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_address_object)

	# 点击输入mac
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)

	# 目的
	# 找下拉框（目的接口）
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(dest_zone_interface)

	if dest_custom == 'yes':
		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
		browser.find_element_by_xpath('//*[@id="toip"]').send_keys(toip)
		browser.find_element_by_xpath('//*[@id="tonetmask"]').clear()
		browser.find_element_by_xpath('//*[@id="tonetmask"]').send_keys(tonetmask)
		browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()

	if dest_address_object == 'yes':
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(d_address_object)

	# 服务
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(service)

	# 计划任务
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(schdule)

	if accept == 'yes':
		browser.find_element_by_xpath('//*[@id="action_0"]').click()
		# 认证
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="auth"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(auth)

	if drop == 'yes':
		browser.find_element_by_xpath('//*[@id="action_1"]').click()

	# 是否选择icf
	if icf == "yes":
		browser.find_element_by_xpath('//*[@id="icf"]').click()

	# 是否选择日志
	if log == "yes":
		browser.find_element_by_xpath('//*[@id="log"]').click()
	time.sleep(2)
	# 是否保存
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
	# 是否取消
	if cancel =='yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[7]')

