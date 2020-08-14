import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *

import pytest


# 添加ipv4规则，
def add_ipv4_acl(browser, group_num=1):

	# 刷新页面，防止页面元素没有连接成功
	browser.refresh()

	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(防火墙).click()
	#
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 切换到默认frame
	# browser.switch_to.default_content()
	#
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 点击添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul[' + str(group_num) + ']/li[4]/a').click()

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()


# 添加ipv4规则组
def add_ipv4_aclgroup(browser, group_name,):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(防火墙).click()
	#
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 切换到默认frame
	# browser.switch_to.default_content()
	#
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	time.sleep(1)

	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(group_name)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 添加acl组（只有name）
def add_acl_group_wxw(browser,name=''):

	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	#
	# # 点击IPv4访问控制列表
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


#  删除所有防火墙组
def del_all_acl_group_wxw(browser):

	# # 切换到默认frame
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


# 添加ipv4规则组
def add_ipv4_aclgroup_lzy(browser, group_name):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(防火墙).click()
	#
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 切换到默认frame
	# browser.switch_to.default_content()
	#
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 点击添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	time.sleep(1)

	# 输入组名
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(group_name)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 删除所有的规则组
def del_all_acl_group_lzy(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(防火墙).click()
	#
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	#
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)
	# 全选删除
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()
	# 接收告警
	browser.switch_to_alert().accept()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 添加组
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	browser.find_element_by_xpath('//*[@id="name"]').send_keys('default')
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 添加规则
	browser.find_element_by_xpath('//*[@id="storage_new_zone"]/ul/li[4]/a').click()
	# browser.execute_script('window.scrollTo(0,800);')
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 到达IPv4访问列表界面
def get_into_ipv4acl_lzy(browser):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 切换frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, IPv4访问控制列表)


# 删除默认规则
def del_default_acl_group_lzy(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(IPv4访问控制列表).click()
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, IPv4访问控制列表)
	# 全选删除
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	browser.find_element_by_xpath('//*[@id="for_checkall_input"]/a').click()
	# 接收告警
	time.sleep(0.5)
	browser.switch_to_alert().accept()
	time.sleep(0.5)
	try:
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
	except:
		pass


# 添加ACL组，包括源接口目的接口选择新建zone的情况
def add_acl_group_and_choose_new(browser, name='acl_group', enable='yes/no', snew='no', szonename='',
								 szonedesc='', szonemember='', sour='Z:any', dnew='no', dzonename='',
								 dzonedesc='', dzonemember='', dest='Z:any', desc='miaoshu', save='yes',
								 cancel='no'):

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
	# 源接口是否新建
	if snew == 'yes':
		# 选择源接口为新建
		s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
		s1.select_by_visible_text('新建...')
		time.sleep(1)
		# 弹出Create Zone窗口
		# 输入名称
		browser.find_element_by_xpath('//*[@id="name_1"]').send_keys(szonename)
		# 输入描述
		browser.find_element_by_xpath('//*[@id="comment_1"]').send_keys(szonedesc)
		# 成员的select对象
		s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		# 选profile下拉框内容
		if szonemember != [" "]:
			for n in szonemember:
				s1.select_by_visible_text(n)
				browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
		# 点击确定
		time.sleep(1)
		browser.find_element_by_class_name('layui-layer-btn0').click()
		time.sleep(1)
		# 获取信息
		a = browser.find_element_by_class_name('layui-layer-content').text
		print(a)
		# 将新建zone设置为默认接口
		time.sleep(1)
		browser.find_element_by_class_name('layui-layer-btn0').click()
	else:
		# 选择源接口
		s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
		s1.select_by_visible_text(sour)


	# 目的接口是否新建
	if dnew == 'yes':
		# 选择目的接口为新建
		s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
		s1.select_by_visible_text('新建...')
		# 弹出Create Zone窗口
		# 输入名称
		browser.find_element_by_xpath('//*[@id="name_1"]').send_keys(dzonename)
		# 输入描述
		browser.find_element_by_xpath('//*[@id="comment_1"]').send_keys(dzonedesc)
		# 成员的select对象
		s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		# 选profile下拉框内容
		if dzonemember != [" "]:
			for n in dzonemember:
				s1.select_by_visible_text(n)
				browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
		# 点击确定
		time.sleep(1)
		browser.find_element_by_class_name('layui-layer-btn0').click()
		time.sleep(1)
		# 获取信息
		a = browser.find_element_by_class_name('layui-layer-content').text
		print(a)
		# 将新建zone设置为默认接口
		time.sleep(1)
		browser.find_element_by_class_name('layui-layer-btn0').click()
	else:
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