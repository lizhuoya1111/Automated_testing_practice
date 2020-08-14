import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *


# 添加acl组（只有name）
def add_acl_group_wxw(browser, name=''):

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
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


#  删除所有防火墙组，并加上一个默认组
def del_all_acl_group_wxw(browser):

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
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 删除所有组
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()

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
	time.sleep(2)
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
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 删除所有组
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()

	# 接受告警
	browser.switch_to_alert().accept()


# # 给一个防火墙组添加一条acl规则
# def add_acl_rule_complete_wxw(browser, aclgroup_name='', source_zone_interface=interface_name_4,
# 					 source_custom='no', fromip='', fromnetmask='',
# 					 source_address_object='yes', s_address_object='A:any',
# 					 mac='',
# 					 dest_custom='no', toip='', tonetmask='',
# 					 dest_address_object='yes', d_address_object='A:any',
# 					 dest_zone_interface=' ',
# 					 service='P:any', schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no'):
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
# 	browser.refresh()
# 	into_fun(browser, IPv4访问控制列表)
# 	n = 1
# 	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
# 	while getname != aclgroup_name:
# 		n = n + 1
# 		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
# 	# print(getname)
#
# 	# 添加规则
# 	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
# 	time.sleep(2)
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
# 		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
# 		# 找下拉框
# 		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
# 		# 找下拉框的内容
# 		s1.select_by_visible_text(s_address_object)
#
# 	# 点击输入mac
# 	if mac != " ":
# 		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
#
# 	# 目的
# 	# 找下拉框（目的接口）
# 	if dest_zone_interface != " ":
# 		s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
# 		# 找下拉框的内容
# 		s1.select_by_visible_text(dest_zone_interface)
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
#
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
# 	# 是否选择日志
# 	if log == "yes":
# 		browser.find_element_by_xpath('//*[@id="log"]').click()
#
# 	# 点击保存
# 	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
# 	# 点击返回
# 	browser.find_element_by_xpath('//*[@id="link_but"]').click()

# 给一个防火墙组添加一条acl规则
def add_acl_rule_complete_wxw(browser, aclgroup_name='', source_zone_interface=interface_name_4,
							  source_custom='no', fromip='', fromnetmask='',
							  source_address_object='yes', s_address_object='A:any',
							  mac='',
							  dest_custom='no', toip='', tonetmask='',
							  dest_address_object='yes', d_address_object='A:any',
							  dest_zone_interface=interface_name_2,
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
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print("222222222222222")
	# print(getname)
	while getname != aclgroup_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 添加规则
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
	time.sleep(1)

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
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(s_address_object)

	# 点击输入mac
	if mac != " ":
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)

	# 目的
	if dest_zone_interface != " ":
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
		browser.find_element_by_xpath('//*[@id="icf"]').click()

	# 是否保存
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
	# 是否取消
	if cancel == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[7]')


# 通过ID将acl到顶部
def set_acl_to_top_byid(browser, acl_id, aclgroup_name=''):
	"""将id规则放到顶端"""
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
	# print("111111111")
	time.sleep(0.5)
	# s = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a').text
	# print(s)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		# print(getname)

		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)

	# 展开这个acl组
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(n)+']/li[1]/img[2]').click()
	# print(browser.find_element_by_xpath('//*[@id="sublist_0"]').is_displayed())
	time.sleep(1)
	browser.switch_to.frame("iFrame0")
	if acl_id == "2":
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[2]/ul/li[8]/a').click()
	else:
		browser.find_element_by_xpath('//*[@id="switchid_to_'+str(acl_id)+'"]').send_keys("1")
		browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[9]/a').click()


# 通过ID删除IPV4-acl
def del_ipv4_acl_byid(browser, acl_id, aclgroup_name=''):
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
	# print("111111111")
	time.sleep(1)
	# s = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a').text
	# print(s)
	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != aclgroup_name:
		# print(getname)

		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	# print(getname)
	# 得到该ACL组里的acl规则数量
	acl_num = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[2]/span').text
	# print("该组acl的数量："+str(acl_num))

	# 展开这个acl组
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul['+str(n)+']/li[1]/img[2]').click()
	# print(browser.find_element_by_xpath('//*[@id="sublist_0"]').is_displayed())
	time.sleep(1)
	iframe_num = n-1
	browser.switch_to.frame("iFrame"+str(iframe_num))
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div['+str(acl_id)+']/ul/li[12]/a[2]').click()


