import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def import *

# 添加对象zone,添加zone,添加Zone
def add_obj_zone(browser, name="",  desc="", zone_mem=""):

	"""
	a_obj_zone(browser,"zone1","ssss",["ge0/1"])
	"""

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(Zone).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, Zone)
	# 点击增加
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 成员的select对象
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	if zone_mem != [" "]:
		for n in zone_mem:
			s1.select_by_visible_text(n)
			browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 通过名字删除对象zone
def del_obj_zone_byname(browser, name):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(Zone).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, Zone)
	# 获取目前有多少个zone对象，而且要减去2，因为有两个默认存在的对象
	time.sleep(0.5)
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 2
	# 根据zone数量,遍历一下，获取要被删除的对象的层数，如果出问题了，把下面的2改成4
	for x in range(4, 4+zone_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a/span').text:
			# 点击删除该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[7]/a[2]').click()
			# if EC.alert_is_present:
			# 	alert = browser.switch_to_alert()
			# 	text = alert.text()
			# 	return text
			time.sleep(1.5)
			# print(str(name)+"删除成功")
			break


# 添加地址对象
def add_obj_address_wxw(browser, name='obj_add_1', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24'):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入地址名称
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 输入子网列表ip
	browser.find_element_by_xpath('//*[@id="subnetip0"]').send_keys(subnetip)
	# 输入子网列表mask
	browser.find_element_by_xpath('//*[@id="subnetmask0"]').clear()
	browser.find_element_by_xpath('//*[@id="subnetmask0"]').send_keys(subnetmask)
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加地址范围对象
def add_obj_address_range_wxw(browser, name='obj_add_range_1', desc='zhe是yi个描述1', fromip='12.12.12.1',toip='12.12.12.250'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击IPv4地址范围
	# browser.find_element_by_xpath(IPv4地址范围).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址范围)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入地址范围对象名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 输入地址范围
	browser.find_element_by_xpath('//*[@id="fromip0"]').send_keys(fromip)
	browser.find_element_by_xpath('//*[@id="toip0"]').send_keys(toip)

	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 修改地址对象
def change_obj_address_wxw(browser, name='obj_add_1', desc='zhe是yi个描述2', subnetip='11.11.11.10',  subnetmask='32'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击IPv4地址
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	# 点击编辑
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ '+str(n)+']/td[3]').text
	while getname != name:
		n = n+1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ '+str(n)+' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ '+str(n)+' ]/td[7]/a[1]/img').click()
	# 修改描述
	browser.find_element_by_xpath('//*[@id="comment"]').clear()
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 修改子网列表ip
	browser.find_element_by_xpath('//*[@id="subnetip0"]').clear()
	browser.find_element_by_xpath('//*[@id="subnetip0"]').send_keys(subnetip)
	# 修改子网列表mask
	browser.find_element_by_xpath('//*[@id="subnetmask0"]').clear()
	browser.find_element_by_xpath('//*[@id="subnetmask0"]').send_keys(subnetmask)
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 修改地址范围对象
def change_obj_range_wxw(browser, name='obj_add_range_1', desc='zhe是yi个描述1', fromip='12.12.12.1', toip='12.12.12.250'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	#
	# # 点击IPv4地址范围
	# browser.find_element_by_xpath(IPv4地址范围).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址范围)
	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[3]').text

	while getname != name:
		n = n+1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	# 点击
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[1]/img').click()

	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').clear()
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	# 输入地址范围
	browser.find_element_by_xpath('//*[@id="fromip0"]').clear()
	browser.find_element_by_xpath('//*[@id="fromip0"]').send_keys(fromip)

	browser.find_element_by_xpath('//*[@id="toip0"]').clear()
	browser.find_element_by_xpath('//*[@id="toip0"]').send_keys(toip)

	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 修改weekly schdule
def change_obj_weekly_schdule_wxw(browser, name='', desc='', monday='yes', schdule1='', tuesday='yes', schdule2='',
								  wednesday='yes', schdule3='', thursday='yes', schdule4='', friday='yes', schdule5='',
								  saturday='yes', schdule6='', sunday='yes', schdule7=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 找到要修改的对象
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text

	# 点击编辑
	browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').click()

	# 修改描述
	browser.find_element_by_xpath('//*[@id="comment"]').clear()
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	if monday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_mon"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule1)

	if tuesday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_tues"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule2)

	if wednesday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_wed"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule3)

	if thursday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_thur"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule4)

	if friday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_fri"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule5)

	if saturday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_sat"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule6)

	if sunday =='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_sun"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule7)

	# 点击保存//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除地址对象
def del_obj_address_wxw(browser, name='obj_add_1', alert="no"):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址)

	# 点击删除
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[2]/img').click()
	if alert == "yes":
		return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


# 删除所有地址对象
def del_all_obj_address_wxw(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击ipv4地址
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()
	# 接受告警
	browser.switch_to_alert().accept()


# 删除地址范围对象
def del_obj_range_wxw(browser, name='obj_add_range_1', alert_info="no"):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击IPv4地址范围
	# browser.find_element_by_xpath(IPv4地址范围).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址范围)
	# 点击删除
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[2]/img').click()
	if alert_info == "yes":
		return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

# 删除地址组对象
def del_obj_grp_wxw(browser, name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址组)
	# 点击删除//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[2]/img').click()


# 删除计划任务对象
def del_obj_schdule_wxw(browser, name=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击删除
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[2]/img').click()


# 一个地址对象添加多个host
def one_obj_add_more_ip_h_wxw(browser,name='obj_add_1', num =3,subnetip='11.11.',  subnetmask='24'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()
	m = 1
	while m <= num:
		# 点击增加
		browser.find_element_by_xpath('//*[@id="add_subnet_link"]').click()
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="subnetip'+str(m)+'"]').send_keys(subnetip+str(m)+'.0')
		time.sleep(2)
		# 输入子网列表mask
		browser.find_element_by_xpath('//*[@id="subnetmask' + str(m) + '"]').clear()
		browser.find_element_by_xpath('//*[@id="subnetmask'+str(m)+'"]').send_keys(subnetmask)
		m = m+1
		# print(m)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 一个地址对象添加多个subnet
def one_obj_add_more_ip_s_wxw(browser, name='obj_add_2', num=3, subnetip='11.11.11.',  subnetmask='32'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()
	m = 1
	while m <= num:
		# 点击增加
		browser.find_element_by_xpath('//*[@id="add_subnet_link"]').click()
		browser.find_element_by_xpath('//*[@id="subnetip'+str(m)+'"]').send_keys(subnetip+str(m))
		# 输入子网列表mask
		browser.find_element_by_xpath('//*[@id="subnetmask' + str(m) + '"]').clear()
		browser.find_element_by_xpath('//*[@id="subnetmask'+str(m)+'"]').send_keys(subnetmask)
		m = m+1
		# print(m)
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 一个地址对象添加多个subnet，点到增加
def one_obj_add_more_ip_s_half_wxw(browser,name='obj_add_2', num =3):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址
	# browser.find_element_by_xpath(IPv4地址).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[3]').text

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()


# 删除一个地址对象的多个ip
def del_one_obj_more_ip_wxw(browser, name='obj_add_1', num=2):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址
	# browser.find_element_by_xpath(IPv4地址).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()
	# 删除
	m = 1
	while m <= num:
		browser.find_element_by_xpath('//*[@id="del_subnet_link"]').click()
		m = m + 1
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 一个地址对象添加多个范围
def one_obj_more_range_wxw(browser, name='obj_add_range_1', num=3, fromip='12.12.', toip='12.12.'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址范围
	# browser.find_element_by_xpath(IPv4地址范围).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址范围)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[1]/img').click()
	m = 1
	while m <= num:
		# 点击增加
		browser.find_element_by_xpath('//*[@id="add_subnet_link"]').click()
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="fromip' + str(m) + '"]').send_keys(fromip + str(m)+".1")
		time.sleep(2)
		# 输入fromip
		browser.find_element_by_xpath('//*[@id="toip' + str(m) + '"]').send_keys(fromip + str(m)+".250")
		m = m + 1
		# print(m)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 一条地址对象中删除多个范围
def del_one_obj_more_range_wxw(browser, name='obj_add_range_1', num=3):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	#
	# # 点击地址范围
	# browser.find_element_by_xpath(IPv4地址范围).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址范围)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	m = 1
	while m <= num:
		# 点击删除
		browser.find_element_by_xpath('//*[@id="del_subnet_link"]').click()
		m = m + 1
		# print(m)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加一个地址组,引用一个地址对象
def add_obj_group_use_addr_obj_wxw(browser, name='', desc='zhe是yi个描述1', addr_obj='A:any'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址组)
	time.sleep(0.5)
	# 点击添加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 选择可用地址
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="a_address"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(addr_obj)
	time.sleep(0.5)
	# 右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加一个地址组,引用多个地址对象，地址对象的传参为列表，如addr_obj=['A:any','A:any1']
def add_obj_group_use_more_addr_obj_wxw(browser, name='', desc='zhe是yi个描述1', addr_obj="list"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址组)
	# 点击添加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 选择可用地址
	# 找下拉框
	for x in addr_obj:
		s1 = Select(browser.find_element_by_xpath('//*[@id="a_address"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(x)
		time.sleep(1)
		# 右移
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑一个地址组,引用一个地址对象
def edit_obj_group_use_addr_obj_wxw(browser, name='', addr_obj='A:any'):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址组)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text

	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()

	# 选择可用地址
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="a_address"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(addr_obj)
	time.sleep(1)
	# 右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 一条acl引用一个地址对象
def acl_ref_addr_obj_wxw(browser, gname='aclgroup_1', addr_obj=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	#
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	time.sleep(5)
	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(gname)
	time.sleep(5)
	# 选择对象
	browser.find_element_by_xpath('//*[@id="fromaddress"]').click()
	# 找下拉框
	time.sleep(2)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromaddress"]'))

	# 找下拉框的内容
	s1.select_by_visible_text(addr_obj)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 一条acl引用一个服务对象
def acl_ref_service_obj_wxw(browser, gname='aclgroup_s1', service_obj='C:'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	#
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(gname)

	# 选择对象
	browser.find_element_by_xpath('//*[@id="service"]').click()

	# 找下拉框//*[@id="service"]
	s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))

	# 找下拉框的内容
	s1.select_by_visible_text(service_obj)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 添加一条只有名字的防火墙组
def add_acl_grp_wxw(browser, name='aclgroup_s1'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	#
	# # 点击IPv4访问组列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)

	# 添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加一条acl规则，引用计划任务
def add_acl_rule_wxw(browser, name='', schdule_obj='S:'):

	# 切换到默认frame
	browser.switch_to.default_content()

	# 切换到内容frame
	browser.switch_to.frame("content")

	# 找与名字匹配的项//*[@id="storage_new_zone"]/ul[2]/li[1]/span[1]/a
	# //*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a
	# //*[@id="storage_new_zone"]/ul[1]/li[1]/span[1]/a

	n = 1
	getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[1]/span[1]/a').text
	print(getname)

	# 添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(n) + ']/li[4]/a').click()
	time.sleep(2)

	# 引用计划任务
	# 找下拉框//*[@id="schedule"]
	browser.find_element_by_xpath('//*[@id="schedule"]').click()

	s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(schdule_obj)
	time.sleep(2)

	# 点击保存//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 查看地址对象的引用，并返回引用类型字符串列表
def get_addr_obj_ref_wxw(browser, name='obj_add_1'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击ipv4地址
	# browser.find_element_by_xpath(IPv4地址).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	# print('getname')
	# 点击引用 //*[@id="table"]/tbody/tr[2]/td[2]
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a/img').click()
	time.sleep(0.5)
	refren_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	refren_list = []
	for x in range(2, refren_sum+2):
		ref_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text
		refren_list.append(ref_info)
	return refren_list


# 查看地址对象组的引用
def get_grp_obj_ref_wxw(browser, name='obj_grp_1'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击ipv4地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4地址组)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text
	# 点击引用
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a/img').click()
	time.sleep(0.5)
	refren_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	refren_list = []
	for x in range(2, refren_sum + 2):
		ref_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text
		refren_list.append(ref_info)
	return refren_list

# 查看服务对象的引用
def get_service_obj_ref_wxw(browser, name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text

	# 点击引用
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a/img').click()


# 查看服务组对象的引用
def get_serv_grp_obj_ref_wxw(browser, name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text

	# 点击引用//*[@id="table"]/tbody/tr[3]/td[6]/a/img
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a/img').click()


# 查看服务组对象的引用
def get_schdule_obj_ref_wxw(browser, name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击计划任务
	# browser.find_element_by_xpath(计划任务).click()
	# # 点击基础计划任务
	# browser.find_element_by_xpath('//*[@id="menu"]/div[4]/div/ul/li[5]/ul/li[1]/span/a/span').click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 计划任务)
	# 找与名字匹配的项//*[@id="namearea0"]
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text
	print(getname)
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text
	print(getname)

	# 点击引用//*[@id="table"]/tbody/tr[2]/td[7]/a/img
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n+2) + ']/td[7]/a/img').click()


# 查看周计划任务对象的引用
def get_weekly_schd_obj_wxw(browser, name=''):

	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到左侧frame
	browser.switch_to.frame("lefttree")
	# 点击对象
	browser.find_element_by_xpath(对象).click()
	# 点击计划任务
	browser.find_element_by_xpath(计划任务).click()
	# 点击周计划任务
	browser.find_element_by_xpath(周计划任务).click()

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 找与名字匹配的项//*[@id="namearea0"]
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	print(getname)
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	print(getname)

	# 点击引用
	browser.find_element_by_xpath('//*[@id="obj_schedule_weekly_table"]/tbody/tr[' + str(n + 2) + ']/td[6]/a/img').click()


# 删除所有对象组
def del_all_obj_group_wxw(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址组)
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	time.sleep(1)
	# 删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	time.sleep(1)
	browser.switch_to_alert().accept()


# 添加一个服务对象(包括前面点到自定义)
def add_obj_service_wxw(browser, name='obj_serv_7', desc='zhe是ge描shu',
						tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
						udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
						icmp='', item='ping',
						ip='', number='85'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	# 选择协议
	if tcp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_0"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dest_port_from)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dest_port_to)

	if udp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_1"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from1)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to1)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dst_port_from1)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dst_port_to1)

	if icmp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_2"]').click()
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="icmp_type"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(item)

	if ip == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_3"]').click()
		browser.find_element_by_xpath('//*[@id="ip"]').send_keys(number)
	time.sleep(0.5)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 添加一个服务对象（只从默认界面开始）
def add_obj_service_major_wxw(browser,name='', desc='zhe是ge描shu',
						# tcp端口范围：(0-65535)； udp端口范围：(0-65535)；
						# icmp(echo-reply;pong;destination-unreachable;network-unreachable;host-unreachable;protocol-unreachable;port-unreachable;
						#      fragmentation-needed;source-route-failed;network-unknown;host-unknown;network-prohibited;host-prohibited;TOS-network-unreachable;
						#      TOS-host-unreachable;communication;host-precedence-violation;precedence-cutoff;source-quench;redirect;network-redirect;host-redirect;
						#      TOS-network-redirect;TOS-host-redirect;echo-request;ping;router-advertisement;router-solicitation;time-exceeded;ttl-exceeded;
						#      ttl-zero-during-transit;ttl-zero-during-reassembly;parameter-problem;ip-header-bad;required-option-missing;timestamp-request;timestamp-reply;
						#      address-mask-request)；
						# ip协议号（0-255）
						tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
						udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
						icmp='', item='ping',
						ip='', number='85'):

	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()

	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)

	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	# 选择协议
	if tcp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_0"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dest_port_from)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dest_port_to)

	if udp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_1"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from1)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to1)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dst_port_from1)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dst_port_to1)

	if icmp == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_2"]').click()
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="icmp_type"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(item)

	if ip == 'yes':
		browser.find_element_by_xpath('//*[@id="protocol_3"]').click()
		browser.find_element_by_xpath('//*[@id="ip"]').send_keys(number)
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加一个服务组对象，引用一个服务对象
def add_obj_serv_grp_wxw(browser, name='', desc='', serv_obj=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	time.sleep(1)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="submit_button"]').click()


# 添加一个计划任务对象
def add_obj_schdule_wxw(browser, name='', desc='', recurring='yes', fromtime='01:00', totime='02:00'):

	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()

	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)

	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	if recurring == 'yes':
		# 点击循环按钮
		browser.find_element_by_xpath('//*[@id="type_0"]').click()
		# browser.find_element_by_xpath('//*[@id="recuring_time_from_btn"]').click()
		# 选择开始时间为1：00
		browser.find_element_by_xpath('//*[@id="recuring_from"]').send_keys(fromtime)
		# browser.find_element_by_xpath('//*[@id="recuring_time_to_btn"]').click()
		# 选择结束时间为2：00
		browser.find_element_by_xpath('//*[@id="recuring_to"]').send_keys(totime)

		# 把打开的计划任务再合上（为避免接下来的操作）
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		# 切换到默认frame
		browser.switch_to.default_content()

		# 切换到左侧frame
		browser.switch_to.frame("lefttree")

		# 点击对象
		browser.find_element_by_xpath(对象).click()

		# 点击计划任务
		browser.find_element_by_xpath(计划任务).click()


# 添加一个计划任务对象
def add_obj_schdule_sel_wxw(browser, name='', desc='', recurring='yes'):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()

	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)

	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	if recurring == 'yes':
		# 点击循环按钮
		browser.find_element_by_xpath('//*[@id="type_0"]').click()
		# 点击下拉框按钮
		browser.find_element_by_xpath('//*[@id="recuring_time_from_btn"]').click()

		# 选择0:00
		browser.find_element_by_xpath('//*[@id="recuring_from_list"]/li[1]').click()

		browser.find_element_by_xpath('//*[@id="recuring_time_to_btn"]').click()

		time.sleep(1)
		# 选择结束时间为2：30
		browser.find_element_by_xpath('//*[@id="recuring_to_list"]/li[48]').click()

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		# 把打开的计划任务再合上（为避免接下来的操作）
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		# 点击对象
		browser.find_element_by_xpath(对象).click()
		# 点击计划任务
		browser.find_element_by_xpath(计划任务).click()


# 添加一条weekly schdule，引用schdule
def add_obj_weekly_schdule_wxw(browser, name='', desc='', monday='yes', schdule1='', tuesday='yes', schdule2='',
							   wednesday='yes', schdule3='', thursday='yes', schdule4='', friday='yes', schdule5='',
							   saturday='yes', schdule6='', sunday='yes', schdule7=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	if monday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_mon"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule1)

	if tuesday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_tues"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule2)

	if wednesday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_wed"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule3)

	if thursday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_thur"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule4)

	if friday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_fri"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule5)

	if saturday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_sat"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule6)

	if sunday=='yes':
		# 找下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="sche_sun"]'))
		# 找下拉框的内容
		s1.select_by_visible_text(schdule7)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 修改一条含有recurring的schedule,添加一条新的recurring
def add_obj_schdule_recurring_wxw(browser, name='', desc='', recurring='yes', fromtime='', totime=''):

	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")

	# 找到要编辑的计划任务
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text
	print(getname)

	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').text
	browser.find_element_by_xpath('//*[@id="namearea'+str(n)+'"]').click()

	# 输入起止时间
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="recuring_from"]').send_keys(fromtime)
	browser.find_element_by_xpath('//*[@id="recuring_to"]').send_keys(totime)

	# 点击新增项目
	browser.find_element_by_xpath('//*[@id="btn_additem"]').click()

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 删除服务对象,参数alert_info=yes时，获取删除失败的警告信息并返回
def del_obj_service_wxw(browser, name='eee', alert_info="no"):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
		# print(getname)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()
	if alert_info == "yes":
		return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


# 修改服务对象
def change_obj_service_wxw(browser, name='obj_serv_1', desc='zhe是ge描shu',
						tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
						udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
						icmp='', item='ping',
						ip='', number='85'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text

	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[7]/a[1]/img').click()
	# 修改描述//*[@id="table"]/tbody/tr[4]/td[7]/a[1]/img
	browser.find_element_by_xpath('//*[@id="comment"]').clear()
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	# 选择协议
	if tcp =='yes':
		browser.find_element_by_xpath('//*[@id="protocol_0"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dest_port_from)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dest_port_to)

	if udp =='yes':
		browser.find_element_by_xpath('//*[@id="protocol_1"]').click()
		# 输入源起始端口
		browser.find_element_by_xpath('//*[@id="src_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="src_port_from"]').send_keys(src_port_from1)
		browser.find_element_by_xpath('//*[@id="src_port_to"]').send_keys(src_port_to1)
		# 输入目的起始端口
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').clear()
		browser.find_element_by_xpath('//*[@id="dst_port_from"]').send_keys(dst_port_from1)
		browser.find_element_by_xpath('//*[@id="dst_port_to"]').send_keys(dst_port_to1)

	if icmp =='yes':
		browser.find_element_by_xpath('//*[@id="protocol_2"]').click()
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="icmp_type"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(item)

	if ip =='yes':
		browser.find_element_by_xpath('//*[@id="protocol_3"]').click()
		browser.find_element_by_xpath('//*[@id="ip"]').clear()
		browser.find_element_by_xpath('//*[@id="ip"]').send_keys(number)
	time.sleep(3)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 删除所有服务对象
def del_all_obj_service_wxw(browser):

	# 定位到默认frame
	# browser.switch_to.default_content()
	into_fun(browser, 自定义)
	# 定位到内容frame
	# browser.switch_to.frame("content")
	time.sleep(0.5)
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()

	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

	# 接受告警
	browser.switch_to_alert().accept()


# 删除所有服务组对象
def del_all_obj_serv_grp_wxw(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, 服务组)
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 接受告警
	browser.switch_to_alert().accept()


# 删除所有计划任务对象
def del_all_schdule_wxw(browser):

	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()

	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

	# 接受告警
	browser.switch_to_alert().accept()


# 删除多条服务对象
def del_more_obj_service_wxw(browser, num=2):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	# 选择要删除的对象//*[@id="button_area"]/div/input[2]
	n = -1
	while n < num-1:
		n += 1
		browser.find_element_by_xpath('//*[@id="check_id_'+str(n)+'"]').click()
	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	time.sleep(2)
	# 接受告警
	browser.switch_to_alert().accept()


# 删除多条地址对象
def del_more_obj_add_wxw(browser, num=2):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击
	# browser.find_element_by_xpath(IPv4地址).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 地址)
	# 选择要删除的对象//*[@id="check_id_0"]
	n = 1
	while n < num:
		browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').click()
		n = n + 1
	# 点击删除所有(选中)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()

	# 接受告警
	browser.switch_to_alert().accept()


# 删除多条地址组对象
def del_more_obj_grp_wxw(browser, num=2):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 地址组)
	# 选择要删除的对象//*[@id="check_id_0"]
	n = 0
	while n < num:
		n += 1
		browser.find_element_by_xpath('//*[@id="check_id_' + str(n-1) + '"]').click()
	# 点击删除所有(选中)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 接受告警
	browser.switch_to_alert().accept()


# 删除多条服务组对象
def del_more_obj_ser_grp_wxw(browser, num=2):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	# 选择要删除的对象
	n = 0
	while n < num:
		n += 1
		browser.find_element_by_xpath('//*[@id="check_id_'+str(n)+'"]').click()

	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 接受告警
	browser.switch_to_alert().accept()


# 删除多条计划任务对象
def del_more_schdule_wxw(browser, num=2):

	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")

	# 选择要删除的对象//*[@id="check_id_0"]
	n = 0
	while n < num:
		n += 1
		browser.find_element_by_xpath('//*[@id="check_id_'+str(n-1)+'"]').click()

	# 点击删除所有
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

	# 接受告警
	browser.switch_to_alert().accept()


# 通过zone名称，找到zone是否存在，如果存在返回组成员字符串，否则返回none
def find_zone_byname(browser, zone_name):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(Zone).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, Zone)
	# 获取目前有多少个zone对象，而且要减去2，因为有两个默认存在的对象
	time.sleep(1)
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 2
	# 根据zone数量,遍历一下，获取要被删除的对象的层数
	for x in range(4, 4+zone_sum):
		if str(zone_name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a/span').text:
			zone_mem = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]/span').text
			# print(zone_mem)
			return zone_mem

	else:
		return None


# 删除所有的zone
def del_zone_all_batch(browser):
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(Zone).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, Zone)
	# 获取目前有多少个zone对象，而且要减去2，因为有两个默认存在的对象
	time.sleep(0.5)
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 2
	# 根据zone数量,遍历一下，获取要被删除的对象的层数
	while zone_sum > 0:
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
		browser.switch_to_alert().accept()
		into_fun(browser, Zone)
		# browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(3)
		zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 2

	return "删除完成"


# 编辑zone
def edit_zone_simple(browser, name, new_desc='', new_mem="no"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# # 点击ipv4
	# browser.find_element_by_xpath(Zone).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, Zone)
	# 获取目前有多少个zone对象，而且要减去2，因为有两个默认存在的对象
	time.sleep(1)
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 2
	# 根据zone数量,遍历一下，获取要被删除的对象的层数
	for x in range(4, 4 + zone_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a/span').text:
			# 点击edit该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[7]/a[1]').click()
			# if EC.alert_is_present:
			# 	alert = browser.switch_to_alert()
			# 	text = alert.text()
			# 	return text
			time.sleep(2)
			# print(str(name) + "edit...")

			browser.find_element_by_xpath('//*[@id="comment"]').clear()
			browser.find_element_by_xpath('//*[@id="comment"]').send_keys(new_desc)
			# 成员的select对象
			s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
			# 选profile下拉框内容
			if new_mem != [" "] and new_mem != "no":

				for n in new_mem:
					s1.select_by_visible_text(n)
					browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
			break


# 删除服务组对象
def del_obj_serv_grp_wxw(browser, name='', alert_info="no"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	# print(getname)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()
	if alert_info == "yes":
		return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


# 勾选自定义服务  通过名字 into_fun(browser, menu) Select
def select_obj_serv_by_name(browser, name=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, 自定义)
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)
	browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').click()


# 取消勾选自定义服务  通过名字 （在勾选之后使用）
def cancel_select_obj_serv_by_name(browser, name=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)
	if browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').is_selected():
		browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').click()
	else:
		print('该服务没有被勾选')


# 判断自定义服务是否被勾选（在勾选或取消勾选之后使用）
def judge_if_select_obj_serv_ornot_by_name(browser, name=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)
	if browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').is_selected():
		return "被勾选"
	else:
		return "未被勾选"


# 点击全选
def click_all_select(browser):
	# into_fun(browser, menu)

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(自定义).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 自定义)
	# 判断是否全选
	if browser.find_element_by_xpath('//*[@id="btn_check_all"]').is_selected():
		print('已全选')
	else:
		# 点击全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()


# 点击取消全选 （在全选之后使用）
def cancel_all_select(browser):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# 判断是否全选
	if browser.find_element_by_xpath('//*[@id="btn_check_all"]').is_selected():
		# 点击取消全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	else:
		print('不是全选状态')


# 添加一个服务组对象，引用多个服务对象(必须传入5个值）
def add_obj_serv_grp_lzy(browser, name='', desc='', serv_obj1='', serv_obj2='', serv_obj3='', serv_obj4='', serv_obj5=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# time.sleep(1)
	# # 点击服务组
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(desc)

	# serv_obj1
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj1)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
	time.sleep(1)

	# serv_obj2
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj2)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

	# serv_obj3
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj3)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

	# serv_obj4
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj4)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

	# serv_obj4
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(serv_obj5)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

	# 点击保存
	browser.find_element_by_xpath('//*[@id="submit_button"]').click()


# 勾选服务组  通过名字 into_fun(browser, menu) Select
def select_obj_serv_group_by_name(browser, name=''):
	# into_fun(browser, menu)

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, 服务组)
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)   //*[@id="namearea1"]  //*[@id="check_id_1"]
	browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').click()


# 判断服务组是否被勾选（在勾选或取消勾选之后使用）
def judge_if_select_obj_serv_group_ornot_by_name(browser, name=''):
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)
	if browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').is_selected():
		return "被勾选"
	else:
		return "未被勾选"


# 点击全选（服务组）
def click_all_select_serv_group(browser):
	# into_fun(browser, menu)

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务组)
	# 判断是否全选
	if browser.find_element_by_xpath('//*[@id="btn_check_all"]').is_selected():
		print('已全选')
	else:
		# 点击全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()


# 点击取消全选 （在全选之后使用）
def cancel_all_select_serv_group(browser):
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# 判断是否全选
	if browser.find_element_by_xpath('//*[@id="btn_check_all"]').is_selected():
		# 点击取消全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	else:
		print('不是全选状态')


# 编辑一个地址组,删除一个对象（左移）
def edit_obj_group_del_obj_lzy(browser, name, obj):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# time.sleep(1)
	# if not browser.find_element_by_xpath(display_IPv4).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(IPv4).click()
	# time.sleep(1)
	# # 点击地址组
	# browser.find_element_by_xpath(IPv4地址组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4地址组)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[3]').text

	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[7]/a[1]/img').click()

	# 选择可用地址
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="s_address"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(obj)
	time.sleep(1)
	# 左移 //*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[2]
	browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()
	# 返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 取消勾选服务组  通过名字 （在勾选之后使用）
def cancel_select_obj_serv_group_by_name(browser, name=''):

	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	# print(getname)
	if browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').is_selected():
		browser.find_element_by_xpath('//*[@id="check_id_' + str(n) + '"]').click()
	else:
		print('该服务没有被勾选')


# 修改服务组 通过名字  增加一个服务对象或者减少一个服务对象
def modify_obj_serv_grp_by_name(browser, name, dec='', add='no', serv_obj1='', reduce='no', serv_obj2=''):
	into_fun(browser, 服务组)

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")

	# //*[@id="namearea0"]  //*[@id="namearea1"]
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
		# print(getname)
	# 点击修改 //*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img  //*[@id="table"]/tbody/tr[3]/td[7]/a[1]/img
	m = n+2
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[7]/a[1]/img').click()
	# 描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(dec)
	# 如果add='yes'
	if add == 'yes':
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(serv_obj1)
		# 点击右移
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
		time.sleep(1)
	if reduce == 'yes':
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="dst_interface"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(serv_obj2)
		# 点击左移
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()
		time.sleep(1)

	# 点击保存 //*[@id="container"]/div/form/div[2]/div[2]/div/input[3]
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 修改地址组 通过名字  增加一个服务对象或者减少一个服务对象
def modify_obj_add_grp_by_name(browser, name, dec='', add='no', add_obj1='', reduce='no', add_obj2=''):
	into_fun(browser, 地址组)

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击对象
	# browser.find_element_by_xpath(对象).click()
	# if not browser.find_element_by_xpath(display_服务).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(服务).click()
	# # 点击自定义
	# browser.find_element_by_xpath(服务组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content") //*[@id="namearea0"]

	# //*[@id="namearea0"]  //*[@id="namearea1"]
	n = 0
	getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="namearea' + str(n) + '"]').text
		# print(getname)
	# 点击修改 //*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img
	m = n+2
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(m) + ']/td[7]/a[1]/img').click()
	# 描述
	browser.find_element_by_xpath('//*[@id="comment"]').send_keys(dec)
	# 如果add='yes'
	if add == 'yes':
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="a_address"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(add_obj1)
		# 点击右移
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
		time.sleep(1)
	if reduce == 'yes':
		# 选profile下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="s_address"]'))
		# 选profile下拉框内容
		s1.select_by_visible_text(add_obj2)
		# 点击左移
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()
		time.sleep(1)

	# 点击保存 //*[@id="container"]/div/form/div[2]/div[2]/div/input[3]
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 获取zone总条目数,返回int型
def get_count_number_zone_lzy(browser):
	into_fun(browser, menu=Zone)
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)


# 设置zone列表界面的每页显示数，15，20，30，150
def change_pagesize_zone_lzy(browser, pagesize="15"):
	into_fun(browser, menu=Zone)
	sleep(2)
	s = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
	s.select_by_visible_text(str(pagesize))
	time.sleep(2)


# zone列表翻页 点击下一页或者前一页
def click_previous_or_next_page_zone_lzy(browser, pre_page="yes/no", next_page="yes/no"):
	into_fun(browser, menu=Zone)
	sleep(2)
	if pre_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
	if next_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
	time.sleep(2)

import math

# zone列表翻页 点击跳转到某页 page跳转到某页 num当前每页显示条目数
def click_into_page_zone_lzy(browser, page="2", num="15"):
	into_fun(browser, menu=Zone)
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	num2 = int(num1)
	# 获取总页数 //*[@id="pagecmd"]/ul/li[1]/select //*[@id="pagecmd"]/ul/li[4]/select
	s1 = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
	s1.select_by_visible_text(str(num))
	page1 = num2/int(num)
	page2 = math.ceil(page1)
	print(page2)
	# 跳转到第二页
	s2 = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[3]/select'))
	s2.select_by_visible_text(str(page)+'/'+str(page2))
	time.sleep(2)




# 命令行添加zone（空）
def cli_add_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("object zone a" + str(x))
		time.sleep(0.2)
		scg.execute("exit")
		time.sleep(0.2)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)

# 命令行删除zone（空）
def cli_delete_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("no object zone a" + str(x))
		time.sleep(0.1)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)