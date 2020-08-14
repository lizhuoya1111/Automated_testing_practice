import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 添加dnat
def add_dnat(browser, name, desc="", src_inter_zone="Z:any", src_ipadd_switch="预定义", srcaddress_predefine="A:any",
			 srcip_custom="", srcmask_custom="", des_ipadd_switch="预定义", desaddress_predefine="A:any",
			 desip_custom="", desmask_custom="", arp_proxy="no", server='P:any', trans_ip='', trans_port='no',
			 other_action_nomap='no',  other_action_load='no', save="yes", cancel='no'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="NAT"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(NAT).click()
	# browser.find_element_by_xpath(目的NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 目的NAT)
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	select_src_inte = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	select_src_inte.select_by_visible_text(src_inter_zone)
	# 源地址
	if src_ipadd_switch == "预定义":
		select_srcaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
		select_srcaddress_predefine.select_by_visible_text(srcaddress_predefine)
	else:
		browser.find_element_by_xpath('//*[@id="srcaddress_ip"]').send_keys(srcip_custom)
		browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').send_keys(srcmask_custom)
	# 目的地址
	if des_ipadd_switch == "预定义":
		select_desaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
		select_desaddress_predefine.select_by_visible_text(desaddress_predefine)
	else:
		browser.find_element_by_xpath('//*[@id="dstaddress_ip"]').send_keys(desip_custom)
		browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').send_keys(desmask_custom)
	# ARP代理
	if arp_proxy == "yes":
		if not browser.find_element_by_xpath('//*[@id="arp_proxy"]').is_selected():
			browser.find_element_by_xpath('//*[@id="arp_proxy"]').click()
	# 服务
	select_server = Select(browser.find_element_by_xpath('//*[@id="service"]'))
	select_server.select_by_visible_text(server)
	# action
	browser.find_element_by_xpath('//*[@id="trans_singleip_value"]').send_keys(trans_ip)
	if trans_port != "no":
		if not browser.find_element_by_xpath('//*[@id="trans_port_type_2"]').is_selected():
			browser.find_element_by_xpath('//*[@id="trans_port_type_2"]').click()
		browser.find_element_by_xpath('//*[@id="portsingle"]').send_keys(trans_port)
	# others
	if other_action_load != "no" or other_action_nomap == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_20"]/td[2]/div/a').click()
	if other_action_nomap == "yes":
		browser.find_element_by_xpath('//*[@id="action_1"]').click()
	if other_action_load != "no":
		browser.find_element_by_xpath('//*[@id="action_2"]').click()
		select_load = Select(browser.find_element_by_xpath('//*[@id="slb"]'))
		select_load.select_by_visible_text(other_action_load)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()


# 通过名字删除dnat
def del_dnat_byname(browser, name):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/div').click()
	# browser.find_element_by_xpath(目的NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 目的NAT)
	# 获取目前有多少个DNAT
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据dnat数量,遍历一下，获取要被删除的对象的层数
	for x in range(2, 2+dnat_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/span').text:
			# 点击删除该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[12]/a[2]').click()
			# if EC.alert_is_present:
			# 	alert = browser.switch_to_alert()
			# 	text = alert.text()
			# 	return text
			time.sleep(2)
			# print(str(name)+"删除成功")
			break


# 添加snat
def add_snat(browser, name, desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="no",
			 src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
			 des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
			 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
			 other_action_nomap='no',  other_action_maplist='no', save='yes', cancel='no'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_NAT).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(NAT).click()
	# browser.find_element_by_xpath(源NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 点击    SNAT
	# browser.find_element_by_xpath('//*[@id="current"]/a').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(src_inter_zone)
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(des_inter_zone)
	# 其他匹配项目
	if other_match_switch == "yes":
		browser.find_element_by_xpath('//*[@id="hidden_icon"]').click()

		if src_ipadd_switch == "预定义":
			browser.find_element_by_xpath('//*[@id="srcaddress_predefine_rad"]').click()
			select_srcaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
			select_srcaddress_predefine.select_by_visible_text(srcaddress_predefine)
		else:
			browser.find_element_by_xpath('//*[@id="srcaddress_custom"]').click()
			browser.find_element_by_xpath('//*[@id="srcaddress_ip"]').send_keys(srcip_custom)
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').send_keys(srcmask_custom)
			time.sleep(1)
		# 目的地址
		if des_ipadd_switch == "预定义":
			browser.find_element_by_xpath('//*[@id="dstaddress_predefine_rad"]').click()
			select_desaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
			select_desaddress_predefine.select_by_visible_text(desaddress_predefine)
		else:
			browser.find_element_by_xpath('//*[@id="dstaddress_custom"]').click()
			browser.find_element_by_xpath('//*[@id="dstaddress_ip"]').send_keys(desip_custom)
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').send_keys(desmask_custom)
			time.sleep(1)

		select_server = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		select_server.select_by_visible_text(server)
	# 动作
	if trans_local_ip == "yes":
		browser.find_element_by_xpath('//*[@id="trans_type_0"]').click()
	if single_ip != "no":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_0"]').click()
		browser.find_element_by_xpath('//*[@id="trans_singleip_value"]').send_keys(single_ip)
	if ip_range_start != "no" and ip_range_end != "no":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_1"]').click()
		browser.find_element_by_xpath('//*[@id="trans_rangeip_from_value"]').send_keys(ip_range_start)
		browser.find_element_by_xpath('//*[@id="trans_rangeip_to_value"]').send_keys(ip_range_end)
	# 其他动作
	if other_action_nomap != "no" or other_action_maplist != "no":

		# 判断其他匹配项目是否展开,如果不是展开的，点击展开
		if browser.find_element_by_xpath('//*[@id="hidden_icon23"]').is_displayed():
			browser.find_element_by_xpath('//*[@id="conftr_20"]/td[2]/div/a').click()
		if other_action_nomap != "no":
			browser.find_element_by_xpath('//*[@id="action_1"]').click()
		if other_action_maplist != "no":
			browser.find_element_by_xpath('//*[@id="action_2"]').click()
			select_load = Select(browser.find_element_by_xpath('//*[@id="maplist"]'))
			select_load.select_by_visible_text(other_action_maplist)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()


# 删除snat，通过名字
def del_snat_byname(browser, name):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_NAT).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(display_NAT).click()
	# browser.find_element_by_xpath(源NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 获取目前有多少个SNAT
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据snat数量,遍历一下，获取要被删除的对象的层数  //*[@id="table"]/tbody/tr[2]/td[3]
	for x in range(2, 2+dnat_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/span').text:
			# 点击删除该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[2]/img').click()
			# if EC.alert_is_present:
			# 	alert = browser.switch_to_alert()
			# 	text = alert.text()
			# 	return text
			time.sleep(2)
			# print(str(name)+"删除成功")
			break


# 添加maplist
def add_maplist_wxw(browser, name='', desc='', save1='yes/no', cancel='yes/no', oriipfrom='', oriipto='', transipfrom='',
					transipto='', one_to_one_mapping="no", sticky='yes', portfrom='1', portto='65535', save2="yes/no", cance2='yes/no'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="NAT"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(NAT).click()
	# # 点击源NAT
	# browser.find_element_by_xpath(源NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if save1 == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(0.5)
		# 增加映射项
		browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
		# 输入原始IP地址
		browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
		browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
		# 输入转换后ip
		if one_to_one_mapping == "yes":
			browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
			browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
		if one_to_one_mapping != "yes":
			browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
			browser.find_element_by_xpath('//*[@id="transipto"]').send_keys(transipto)
		if sticky == 'yes':
			browser.find_element_by_xpath('//*[@id="sticky"]').click()
		# 输入转换后端口
		time.sleep(0.1)
		browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
		time.sleep(0.1)
		browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
		time.sleep(0.1)
		browser.find_element_by_xpath('//*[@id="portto"]').clear()
		time.sleep(0.1)
		browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)

		# 点击新增项目
		browser.find_element_by_xpath('//*[@id="btn_additem"]').click()
		if save2 == "yes":
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
		if cancel == "yes":
			# 点击取消
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 添加maplist,到新增项目前
def add_maplist_part_wxw(browser, name='', desc='', oriipfrom='', oriipto='', transipfrom='', transipto='',
					one_to_one_mapping="no", sticky='yes', portfrom='1', portto='65535'):

	"""
	添加maplist,到新增项目前
	"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击NAT
	# browser.find_element_by_xpath(NAT).click()
	# # 点击源NAT
	# browser.find_element_by_xpath(源NAT).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

	# 增加映射项
	browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
	# 输入原始IP地址
	browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
	browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
	time.sleep(1)
	# 输入转换后ip
	browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="transipto"]').send_keys(transipto)
	if one_to_one_mapping == "yes":
		browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
	if sticky == 'yes':
		browser.find_element_by_xpath('//*[@id="sticky"]').click()
	# 输入转换后端口
	browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
	browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
	browser.find_element_by_xpath('//*[@id="portto"]').clear()
	browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)


# 添加maplist,只到保存描述前
def add_maplist_desc_wxw(browser, name='', desc=''):

	"""
	添加maplist,只到保存描述前
	"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 点击NAT
	# browser.find_element_by_xpath(NAT).click()
	# # 点击源NAT
	# browser.find_element_by_xpath(源NAT).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)


# 添加一条负载均衡
def add_slb_wxw(browser, name='slb', desc='miaoshu', portfrom='1', portto='2', load_balance_method='轮换/权值',
				monitor_servers="yes/no", monitor_method='Ping', save1='yes/no', ip='1.1.1.1', weight='1', save2='yes/no',
				cancel='yes/no'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="NAT"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(NAT).click()
	# browser.find_element_by_xpath(服务器负载均衡).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务器负载均衡)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	# 端口转换
	browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
	browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)
	if load_balance_method == "轮换":
		browser.find_element_by_xpath('//*[@id="method_0"]').click()
	if load_balance_method == "权值":
		browser.find_element_by_xpath('//*[@id="method_1"]').click()
	if monitor_servers is "yes":
		if (browser.find_element_by_xpath('//*[@id="enable_ip_compression"]').is_selected())is "True":
			pass
		else:
			browser.find_element_by_xpath('//*[@id="monitor"]').click()
	# 选择监控方式
	s1 = Select(browser.find_element_by_xpath('//*[@id="type"]'))
	s1.select_by_visible_text(monitor_method)

	if save1 == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 输入服务器ip
		browser.find_element_by_xpath('//*[@id="server"]').send_keys(ip)
		if load_balance_method == "权值":
			browser.find_element_by_xpath('//*[@id="weight"]').send_keys(weight)
		if save2 == "yes":
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除指定负载均衡
def del_slb_by_name_wxw(browser, name='slb'):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击防火墙
	# browser.find_element_by_xpath(防火墙).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="NAT"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(NAT).click()
	# browser.find_element_by_xpath(服务器负载均衡).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 服务器负载均衡)
	# 点击删除
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.replace(' ', '')
	# print(getname)
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.replace(' ', '')
		# print(getname)
		time.sleep(2)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[2]/img').click()


# 进入snat界面
def get_snat(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_NAT).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(display_NAT).click()
	# browser.find_element_by_xpath(源NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)


# 编辑snat通过名字编辑
def edit_snat_byname(browser, name="", edit_desc="", desc="", edit_src_inter_zone="", src_inter_zone="",
					 edit_des_inter_zone="", des_inter_zone="", other_match_switch="", src_ipadd_switch="",
					srcaddress_predefine="", srcip_custom="", srcmask_custom="", des_ipadd_switch="",
					desaddress_predefine="", desip_custom="", desmask_custom="", server="P:any", trans_local_ip="yes",
					single_ip="", ip_range="", ip_range_start="", ip_range_end="", other_action_nomap="no",
					other_action_maplist="no", save="yes", cancel=""):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(防火墙).click()
	# browser.find_element_by_xpath(NAT).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_NAT).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(display_NAT).click()
	# browser.find_element_by_xpath(源NAT).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 源NAT)
	# 获取目前有多少个SNAT
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据snat数量,遍历一下，获取要被删除的对象的层数  //*[@id="table"]/tbody/tr[2]/td[3]
	for x in range(2, 2+dnat_sum):						# //*[@id="table"]/tbody/tr[2]/td[3]
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/span').text:
			# 点击编辑该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[1]/img').click()
			break
	# 修改snat描述
	time.sleep(2)
	if edit_desc == "yes":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	# 修改源对象接口
	if edit_src_inter_zone == "yes":
		s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
		s1.select_by_visible_text(src_inter_zone)
	# 修改目的对象接口
	if edit_des_inter_zone == "yes":
		s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
		s1.select_by_visible_text(des_inter_zone)
	# 其他匹配项目
	time.sleep(1)
	if other_match_switch == "yes":
		browser.find_element_by_xpath('//*[@id="hidden_icon"]').click()
		# 源地址
		if src_ipadd_switch == "预定义":
			select_srcaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
			select_srcaddress_predefine.select_by_visible_text(srcaddress_predefine)
		else:
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="srcaddress_ip"]').clear()
			browser.find_element_by_xpath('//*[@id="srcaddress_ip"]').send_keys(srcip_custom)
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').send_keys(srcmask_custom)
		# 目的地址
		if des_ipadd_switch == "预定义":
			select_desaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
			select_desaddress_predefine.select_by_visible_text(desaddress_predefine)
		else:
			browser.find_element_by_xpath('//*[@id="dstaddress_ip"]').clear()
			browser.find_element_by_xpath('//*[@id="dstaddress_ip"]').send_keys(desip_custom)
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').send_keys(desmask_custom)

		select_server = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		select_server.select_by_visible_text(server)
	time.sleep(1)
	# 动作
	# 点击转换后地址
	browser.find_element_by_xpath('//*[@id="action_0"]').click()
	if trans_local_ip == "yes":
		browser.find_element_by_xpath('//*[@id="trans_type_0"]').click()
	if single_ip == "yes":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_0"]').click()
		browser.find_element_by_xpath('//*[@id="trans_singleip_value"]').clear()
		browser.find_element_by_xpath('//*[@id="trans_singleip_value"]').send_keys(single_ip)

	if ip_range == "yes":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_1"]').click()
		browser.find_element_by_xpath('//*[@id="trans_rangeip_from_value"]').clear()
		browser.find_element_by_xpath('//*[@id="trans_rangeip_from_value"]').send_keys(ip_range_start)
		browser.find_element_by_xpath('//*[@id="trans_rangeip_to_value"]').clear()
		browser.find_element_by_xpath('//*[@id="trans_rangeip_to_value"]').send_keys(ip_range_end)
	# 其他动作
	time.sleep(1)
	if other_action_nomap != "no" or other_action_maplist != "no":
		browser.find_element_by_xpath('//*[@id="hidden_icon21"]').click()
		if other_action_nomap != "yes":
			browser.find_element_by_xpath('//*[@id="action_1"]').click()
		if other_action_maplist != "yes":
			browser.find_element_by_xpath('//*[@id="action_2"]').click()
			select_load = Select(browser.find_element_by_xpath('//*[@id="maplist"]'))
			select_load.select_by_visible_text(other_action_maplist)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[7]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[8]').click()




# 添加snat
def add_snat_tmp(browser, name, desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="no",
			 src_ipadd_switch="预定义", srcaddress_predefine="A:any", srcip_custom="", srcmask_custom="",
			 des_ipadd_switch="预定义", desaddress_predefine="A:any", desip_custom="", desmask_custom="",
			 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
			 other_action_nomap='no',  other_action_maplist='no', save='yes', cancel='no'):

	browser.switch_to.default_content()
	# 切换到左侧frame
	browser.switch_to.frame("lefttree")
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/header/a').click()
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/span').click()

	# 判断菜单是否展开，元素是否可见
	if not browser.find_element_by_xpath(display_NAT).is_displayed():
		# 如果不可见，点击加号，展开元素
		browser.find_element_by_xpath(display_NAT).click()
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/ul/li[2]/span/a').click()
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# into_fun(browser, 源NAT)
	# 点击    SNAT
	# browser.find_element_by_xpath('//*[@id="current"]/a').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
	s1.select_by_visible_text(src_inter_zone)
	s1 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
	s1.select_by_visible_text(des_inter_zone)
	# 其他匹配项目
	if other_match_switch == "yes":
		browser.find_element_by_xpath('//*[@id="hidden_icon"]').click()

		if src_ipadd_switch == "预定义":
			browser.find_element_by_xpath('//*[@id="srcaddress_predefine_rad"]').click()
			select_srcaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="srcaddress_predefine"]'))
			select_srcaddress_predefine.select_by_visible_text(srcaddress_predefine)
		else:
			browser.find_element_by_xpath('//*[@id="srcaddress_custom"]').click()
			browser.find_element_by_xpath('//*[@id="srcaddress_ip"]').send_keys(srcip_custom)
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="srcaddress_mask"]').send_keys(srcmask_custom)
			time.sleep(1)
		# 目的地址
		if des_ipadd_switch == "预定义":
			browser.find_element_by_xpath('//*[@id="dstaddress_predefine_rad"]').click()
			select_desaddress_predefine = Select(browser.find_element_by_xpath('//*[@id="dstaddress_predefine"]'))
			select_desaddress_predefine.select_by_visible_text(desaddress_predefine)
		else:
			browser.find_element_by_xpath('//*[@id="dstaddress_custom"]').click()
			browser.find_element_by_xpath('//*[@id="dstaddress_ip"]').send_keys(desip_custom)
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').clear()
			browser.find_element_by_xpath('//*[@id="dstaddress_mask"]').send_keys(desmask_custom)
			time.sleep(1)

		select_server = Select(browser.find_element_by_xpath('//*[@id="service"]'))
		select_server.select_by_visible_text(server)
	# 动作
	if trans_local_ip == "yes":
		browser.find_element_by_xpath('//*[@id="trans_type_0"]').click()
	if single_ip != "no":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_0"]').click()
		browser.find_element_by_xpath('//*[@id="trans_singleip_value"]').send_keys(single_ip)
	if ip_range_start != "no" and ip_range_end != "no":
		browser.find_element_by_xpath('//*[@id="trans_ip_type_1"]').click()
		browser.find_element_by_xpath('//*[@id="trans_rangeip_from_value"]').send_keys(ip_range_start)
		browser.find_element_by_xpath('//*[@id="trans_rangeip_to_value"]').send_keys(ip_range_end)
	# 其他动作
	if other_action_nomap != "no" or other_action_maplist != "no":

		# 判断其他匹配项目是否展开,如果不是展开的，点击展开
		if browser.find_element_by_xpath('//*[@id="hidden_icon23"]').is_displayed():
			browser.find_element_by_xpath('//*[@id="conftr_20"]/td[2]/div/a').click()
		if other_action_nomap != "no":
			browser.find_element_by_xpath('//*[@id="action_1"]').click()
		if other_action_maplist != "no":
			browser.find_element_by_xpath('//*[@id="action_2"]').click()
			select_load = Select(browser.find_element_by_xpath('//*[@id="maplist"]'))
			select_load.select_by_visible_text(other_action_maplist)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()


# 通过名字删除snat
def del_snat_byname_tmp(browser, name):
	browser.refresh()
	browser.switch_to.default_content()
	# 切换到左侧frame
	browser.switch_to.frame("lefttree")
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/header/a').click()
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/span').click()

	# 判断菜单是否展开，元素是否可见
	if not browser.find_element_by_xpath(display_NAT).is_displayed():
		# 如果不可见，点击加号，展开元素
		browser.find_element_by_xpath(display_NAT).click()
	browser.find_element_by_xpath('//*[@id="menu"]/div[5]/div/ul/li[3]/ul/li[2]/span/a').click()
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	# into_fun(browser, 源NAT)
	# 获取目前有多少个SNAT
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据snat数量,遍历一下，获取要被删除的对象的层数  //*[@id="table"]/tbody/tr[2]/td[3]
	for x in range(2, 2+dnat_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/span').text:
			# 点击删除该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[13]/a[2]/img').click()
			# if EC.alert_is_present:
			# 	alert = browser.switch_to_alert()
			# 	text = alert.text()
			# 	return text
			time.sleep(2)
			# print(str(name)+"删除成功")
			break


# 通过名字编辑maplist
def edit_maplist_by_name_jyl(browser, name="", desc='', maplist_del="", oriipfrom="", oriipto="", one_to_one_mapping="",
						 transipfrom="", transipto="", sticky="", portfrom="1", portto="65535", new_item="yes", save="yes",
						 cancel="no"):
	into_fun(browser, 源NAT)
	time.sleep(1)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据maplist数量,遍历一下，获取要被删除的对象的层数
	for x in range(2, 2+dnat_sum):
		time.sleep(0.2)
		get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip()
		if get_name == name:
			time.sleep(0.2)
			# 点击编辑该对象				# //*[@id="table"]/tbody/tr[2]/td[3]/a[1]/img
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a[1]/img').click()
			break
	# 是否删除添加的maplist(删除最上面1条)
	if maplist_del == "yes":
		# 点击删除映射列表
		browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody[2]/tr[2]/td[10]/input').click()
	time.sleep(0.5)
	if desc != "":
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	# 增加映射项
	browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
	# 输入原始IP地址
	browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
	browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
	# 输入转换后ip
	if one_to_one_mapping == "yes":
		browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
		browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
	if one_to_one_mapping != "yes":
		browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
		browser.find_element_by_xpath('//*[@id="transipto"]').send_keys(transipto)
	if sticky == 'no':
		browser.find_element_by_xpath('//*[@id="sticky"]').click()
	# 输入转换后端口
	browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
	browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
	browser.find_element_by_xpath('//*[@id="portto"]').clear()
	browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)
	# 点击新增项目
	if new_item == "yes":
		browser.find_element_by_xpath('//*[@id="btn_additem"]').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()


# 删除maplist通过名字
def del_maplist_by_name_jyl(browser, name=""):
	into_fun(browser, 源NAT)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据maplist数量,遍历一下，获取要被删除的对象的层数  //*[@id="table"]/tbody/tr[2]/td[3]/a[1]/img
	for x in range(2, 2+dnat_sum):						# //*[@id="table"]/tbody/tr[2]/td[3]/a[2]/img
		time.sleep(0.1)
		get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip()
		if get_name == name:
			time.sleep(0.1)
			# 点击删除该对象				# //*[@id="table"]/tbody/tr[2]/td[3]/a[2]/img
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a[2]/img').click()
			break


# 编辑maplist只删除映射列表中的映射项(每次只删除最上面的映射项)
def edit_maplist_del_maplist_jyl(browser, name="", maplist_del=""):
	into_fun(browser, 源NAT)
	time.sleep(1)
	# 点击映射列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(1)
	dnat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据maplist数量,遍历一下，获取要被删除的对象的层数
	for x in range(2, 2+dnat_sum):
		time.sleep(0.2)
		get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip()
		if get_name == name:
			time.sleep(0.2)
			# 点击编辑该对象				# //*[@id="table"]/tbody/tr[2]/td[3]/a[1]/img
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a[1]/img').click()
			break
	# 是否删除添加的maplist(删除最上面1条)
	if maplist_del == "yes":
		# 点击删除映射列表
		browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody[2]/tr[2]/td[10]/input').click()