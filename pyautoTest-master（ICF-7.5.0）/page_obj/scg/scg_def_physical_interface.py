from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


# 透明接口改变为物理接口
def transparent_interface_change_physics_interface_jyl(browser, interface1="", interface2="", interface3="", interface4="",
													   interface5="", interface6="", intefacex=""):
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	if interface1 == interface_name_1 or intefacex == interface_name_1:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface2 == interface_name_2 or intefacex == interface_name_2:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface3 == interface_name_3 or intefacex == interface_name_3:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface4 == interface_name_4 or intefacex == interface_name_4:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface5 == interface_name_5 or intefacex == interface_name_5:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface6 == interface_name_6 or intefacex == interface_name_6:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 物理接口改变为透明接口
def physics_interface_change_transparent_interface(browser, interface1="", interface2="", interface3="", interface4="",
												   interface5="", interface6="",  intefacex=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	if interface1 == interface_name_1 or intefacex == interface_name_1:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[9]/a/img').click()
		# 点击透明
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface2 == interface_name_2 or intefacex == interface_name_2:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[9]/a/img').click()
		# 点击透明
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(1)
	if interface3 == interface_name_3 or intefacex == interface_name_3:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[9]/a/img').click()
		# 点击透明
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(1)
	if interface4 == interface_name_4 or intefacex == interface_name_4:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[9]/a/img').click()
		# 点击透明
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(1)
	if interface5 == interface_name_5 or intefacex == interface_name_5:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[9]/a/img').click()
		# 点击透明
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		# 接受告警
		time.sleep(1)
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		time.sleep(1)
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(1)
	if interface6 == interface_name_6 or intefacex == interface_name_6:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[9]/a/img').click()
		time.sleep(1)
		# 点击透明
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 物理接口从DHCP服务器获取IP地址
def physics_interface_from_dhcp_obtain_ip_jyl(browser, physical_interface="", alias="", description="", work_mode="dhcp",
											  dhcp_status1="", dhcp_status2="", dhcp_status3="",
											  update_default_gateway="", update_system_dns="", snat="", allow_ping=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 输入别名
	browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(1)
	if update_default_gateway == "open":
		enable = browser.find_element_by_xpath('//*[@id="gw_update"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
	if update_default_gateway == "close":
		enable = browser.find_element_by_xpath('//*[@id="gw_update"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
	if update_system_dns == "open":
		enable = browser.find_element_by_xpath('//*[@id="dns_update"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	if update_system_dns == "close":
		enable = browser.find_element_by_xpath('//*[@id="dns_update"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	if snat == "open":
		enable = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if snat == "close":
		enable = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if allow_ping == "open":
		enable = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
		if enable == True:
			time.sleep(1)
		else:
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	if allow_ping == "close":
		enable = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(1)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(2)
	if dhcp_status2 == "stop":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if dhcp_status2 != "stop":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)


# 物理接口使用PPPOE（ADSL）的地址模式,输入用户名和密码进行连接
def physics_interface_pppoe_set(browser, physical_interface, pppoe_uesr="", pppoe_passwd="", dns_renew="yes/no", idle_time="0"):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# # 删掉静态地址，暂时不用这快代码
	# while is_element_exist(browser, element='//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input'):
	# 	browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input').click()
	browser.find_element_by_xpath('//*[@id="address_mode_2"]').click()
	browser.find_element_by_xpath('//*[@id="pppoe_user_name"]').clear()
	browser.find_element_by_xpath('//*[@id="pppoe_user_name"]').send_keys(pppoe_uesr)
	browser.find_element_by_xpath('//*[@id="pppoe_password"]').clear()
	browser.find_element_by_xpath('//*[@id="pppoe_password"]').send_keys(pppoe_passwd)
	if dns_renew == "yes":
		if not browser.find_element_by_xpath('//*[@id="pppoe_updns"]').is_selected():
			browser.find_element_by_xpath('//*[@id="pppoe_updns"]').click()
	elif dns_renew == "no":
		if browser.find_element_by_xpath('//*[@id="pppoe_updns"]').is_selected():
			browser.find_element_by_xpath('//*[@id="pppoe_updns"]').click()

	browser.find_element_by_xpath('//*[@id="pppoe_inactivitytime"]').clear()
	browser.find_element_by_xpath('//*[@id="pppoe_inactivitytime"]').send_keys(idle_time)

	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 对已经开启PPPoE的端口，进行刷新和断开的操作
def physics_interface_pppoe_action(browser, physical_interface, action="断开/刷新"):
	browser.refresh()
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	if action == "断开":
		browser.find_element_by_xpath('//*[@id="pppoe_button_div"]/a').click()
	elif action == "刷新":
		browser.find_element_by_xpath('//*[@id="ajax_pppoe_refreshlink"]').click()


# 获取指定物理接口的PPPoE状态、IP地址、子网掩码、网关,返回去字符串列表 [pppoe_stat, pppoe_ipaddr, pppoe_netmask, pppoe_gateway]
def get_physics_interface_pppoe_station(browser, physical_interface):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	pppoe_stat = browser.find_element_by_xpath('//*[@id="pppoe_status_span"]').text
	pppoe_ipaddr = browser.find_element_by_xpath('//*[@id="pppoe_ipaddr"]').text
	pppoe_netmask = browser.find_element_by_xpath('//*[@id="pppoe_netmask"]').text
	pppoe_gateway = browser.find_element_by_xpath('//*[@id="pppoe_gateway"]').text
	return [pppoe_stat, pppoe_ipaddr, pppoe_netmask, pppoe_gateway]


# 物理接口从DHCP获IP地址
def physical_interface_obtain_ip_from_dhcp_jyl(browser, physical_interface="", alias="", description="", work_mode="dhcp"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 输入别名
	browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(1)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(1)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)


# 物理接口从dhcp服务器获取IP地址之后，dhcp的状态
def physical_interface_obtain_ip_dhcp_status_jyl(browser, physical_interface="", work_mode="dhcp", dhcp_status1="", dhcp_status2="", dhcp_status3="",):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(2)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)


# 物理接口更新状态从dhcp
def physical_interface_update_dhcp_jyl(browser, physical_interface="", alias="", description="", update_default_gateway="", update_system_dns="", snat="", allow_ping=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 输入别名
	browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(1)
	if update_default_gateway == "open":
		enable = browser.find_element_by_xpath('//*[@id="gw_update"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
	if update_default_gateway == "close":
		enable = browser.find_element_by_xpath('//*[@id="gw_update"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
	if update_system_dns == "open":
		enable = browser.find_element_by_xpath('//*[@id="dns_update"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	if update_system_dns == "close":
		enable = browser.find_element_by_xpath('//*[@id="dns_update"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	if snat == "open":
		enable = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
		if enable != True:
			time.sleep(1)
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if snat == "close":
		enable = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if allow_ping == "open":
		enable = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
		if enable == True:
			time.sleep(1)
		else:
			# 点击更新默认网关(开启)
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	if allow_ping == "close":
		enable = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
		if enable == True:
			time.sleep(1)
			# 点击更新默认网关（关闭）
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(1)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)


# 给物理接口添加一个ip-wxw,并返回添加的结果信息,不适用于出现alert的情况，如非法输入
def add_physical_interface_ip_wxw(browser, interface='', ip='', mask=''):

	"""给物理接口添加一个ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 按名字查找
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 添加ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 获得操作结束的信息，并返回
	return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


# 给物理接口添加一个静态ip-jyl,并返回添加的结果信息，不适用于出现alert的情况，如非法输入
def add_physical_interface_static_ip_jyl(browser, interface='', ip='', mask=''):
	"""给物理接口添加一个ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# browser.refresh()
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	time.sleep(1)
	# 点击静态
	browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()

	# 添加ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 获得操作结束的信息，并返回
	return browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


# 给物理接口添加一个静态非法的ip,并返回添加的结果信息（alert），适用于出现alert的情况，如非法输入
def add_physical_interface_static_ip_jyl_alert(browser, interface='', ip='', mask=''):
	"""给物理接口添加一个ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	time.sleep(2)
	# 点击静态
	browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()

	# 添加ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 保存 switch_to_alert()
	alert = browser.switch_to_alert()
	alert_info = alert.text
	time.sleep(0.5)
	alert.accept()
	return alert_info


# 给物理接口添加一个非法的描述,并返回添加的结果信息（alert），适用于出现alert的情况，如非法输入
def add_physical_interface_description_alert(browser, interface='', des=''):
	"""给物理接口添加一个ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 添加描述
	browser.find_element_by_xpath('//*[@id="des"]').clear()
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(des)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 保存 switch_to_alert()
	time.sleep(2)
	alert = browser.switch_to_alert()
	alert_info = alert.text
	time.sleep(0.5)
	alert.accept()
	return alert_info


# 给物理接口添加一个描述
def add_physical_interface_description(browser, interface='', des=''):
	"""给物理接口添加一个ip"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 添加描述
	browser.find_element_by_xpath('//*[@id="des"]').clear()
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(des)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 物理接口从dhcp服务器更新IP地址
def physical_intertface_obtain_ip_address_from_dhcp1_jyl(browser, physical_interface="", alias="", description="",
														 work_mode="dhcp"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 输入别名
	browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(1)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(1)


# 打开或关闭物理接口的allow ping
def open_physical_interface_allowping_wxw(browser, interface='ge0/4', allow_ping="open/close"):

	"""打开或关闭某接口的allow ping 功能"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 确认allow ping是否打开
	allowping = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
	# print(allowping)
	if allow_ping == "open":
		if allowping == True:
			pass
			# print("allow ping已打开")
		else:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	if allow_ping == "close":
		if allowping == True:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
			# print("allow ping已关闭")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	# 把打开的网络合上

# 打开或关闭某接口的allow ping 功能
# 切换到默认frame
# 	browser.switch_to.default_content()
# 	# 切换到左侧frame
# 	browser.switch_to.frame("lefttree")
# 	# 点击网络
# 	browser.find_element_by_xpath(网络).click()
# 	# 点击接口设置
# 	browser.find_element_by_xpath(接口设置).click()


# 开启/关闭接口SNAT
def switch_physical_interface_snat(browser, interface='', snat="open/close"):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 确认allow ping是否打开
	allowping = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
	# print(allowping)
	if snat == "open":
		if allowping is True:
			print("snat已打开")
		else:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if snat == "close":
		if allowping is True:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
			print("snat已关闭")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	# 把打开的网络合上

# 打开或关闭某接口的allow ping 功能
# 切换到默认frame
# 	browser.switch_to.default_content()
# 	# 切换到左侧frame
# 	browser.switch_to.frame("lefttree")
# 	# 点击网络
# 	browser.find_element_by_xpath(网络).click()
# 	# 点击接口设置
# 	browser.find_element_by_xpath(接口设置).click()


# 删除物理接口IP地址
def delete_physical_interface_ip_jyl(browser, interface="", ip=""):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 点击编辑 //*[@id="ipaddress"]/tbody/tr[2]/td[2] //*[@id="table"]/tbody/tr[2]/td[2]/a
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[9]/a/img').click()
	time.sleep(0.5)
	# 点击编辑
	m = 2
	getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr['+str(m)+']/td[2]').text

	while getip != ip:
		m = m + 1
		getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr['+str(m)+']/td[2]').text
	# 点击删除
	browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr['+str(m)+']/td[4]/input').click()


# 启用/停用 物理接口 ,传入参数为disable或者enable
def physical_interface_switch(browser, interface="", status="enable", interface_id=""):
	browser.refresh()
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# print(interface)
	into_fun(browser, 物理接口)
	if interface == interface_name_1:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/input').is_selected()
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")

	elif interface == interface_name_2:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/input').is_selected()
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")

	elif interface == interface_name_3:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[8]/input').is_selected()
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")

	elif interface == interface_name_4:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[8]/input').is_selected()
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")

	elif interface == interface_name_5:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)

		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[8]/input').is_selected()
			# print(status_now)
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
				print("22222")

		else:
			print("传入参数错误")

	elif interface == interface_name_6:
		# 如果输入的状态是启动，则点击启动
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[8]/input').is_selected()

			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")

	else:
		# 结合id参数，对接口进行选择，id就是接口序号
		interface_id = int(interface_id) + 1
		if status == "enable":
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interface_id)+']/td[8]/input').is_selected()
			if status_now is not True:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interface_id)+']/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		# 如果输入的状态是不启动，则取消点击启动
		elif status == "disable":
			time.sleep(0.5)
			status_now = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interface_id)+']/td[8]/input').is_selected()
			if status_now is not False:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interface_id)+']/td[8]/input').click()
				time.sleep(0.5)
				browser.switch_to_alert().accept()
				time.sleep(0.5)
		else:
			print("传入参数错误")


# 检查物理接口是否全部启用,默认是全部检查，或者输入某一端口名进行查询，返回值为Ture/Fail,暂未实现某一端口的查询
def check_physical_interface_enble(browser, interface="all"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# print(interface)
	inteface_sum = 0
	if interface == "all":
		inteface_enbale_checkbox = browser.find_elements_by_id('net_interface')
		print(inteface_enbale_checkbox)
		for x in inteface_enbale_checkbox:
			inteface_sum += 1
			if x.is_selected() is False:
				print(inteface_sum)
				return False

		else:
			print(inteface_sum)
			return True


# 获得接口的链接状态，输入参数为界面的接口序列索引号,返回接口的状态
def get_physical_interface_link_station(browser, interface_id=""):
	browser.refresh()
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)

	# 结合id参数，对接口进行选择，id就是接口序号
	interface_id = int(interface_id) + 1
	time.sleep(1)
	link_sata = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interface_id)+']/td[6]/span ').text
	return link_sata


# 获得设备的物理接口总数,返回整型
def get_physical_interface_sum(browser):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	return len(browser.find_elements_by_id('net_interface'))


# 获得设备的物理接口描述信息,并返回
def get_physical_interface_des(browser, interface=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 添加描述
	des_info = browser.find_element_by_xpath('//*[@id="des"]').get_attribute("value")
	return des_info


# 获得设备的工作模式,并返回
def get_physical_interface_workmode(browser, interface=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	return browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]/span').text


# 清除设备的物理接口描述信息,并返回
def clear_physical_interface_des(browser, interface=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

	# 添加描述
	browser.find_element_by_xpath('//*[@id="des"]').clear()
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(" ")
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 进入物理接口，不进行任何操作
def get_into_physical_interface(browser, interface=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")


# 物理接口透明模式转换为路由模式（接口用interface_name_X表示）
def transparent_interface_change_physics_interface_lzy(browser, interface1="", interface2="", interface3="",
                                                       interface4="", interface5="", interface6="", intefacex=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	if interface1 == interface_name_1 or intefacex == interface_name_1:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface2 == interface_name_2 or intefacex == interface_name_2:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface3 == interface_name_3 or intefacex == interface_name_3:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface4 == interface_name_4 or intefacex == interface_name_4:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface5 == interface_name_5 or intefacex == interface_name_5:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if interface6 == interface_name_6 or intefacex == interface_name_6:
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[9]/a/img').click()
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(1)
		# 定位到默认frame
		browser.switch_to.default_content()
		# 定位到内容frame
		browser.switch_to.frame("content")
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 编辑接口的模式和速率
def edit_interface_senior_jyl(browser, interface="", negotiation="", anto_mtu="", speed="", duplex="", force_mtu="",
						  save="yes"):
	into_fun(browser, menu=物理接口)
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	n = 2
	time.sleep(0.5)
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	time.sleep(1)
	# 点击高级
	browser.find_element_by_xpath('//*[@id="adv_toggle"]').click()
	time.sleep(1)
	if negotiation == "自动":
		# 点击自动
		browser.find_element_by_xpath('//*[@id="negotiation_0"]').click()
		# 清除默认输入并且输入mtu
		browser.find_element_by_xpath('//*[@id="mtu"]').clear()
		browser.find_element_by_xpath('//*[@id="mtu"]').send_keys(anto_mtu)
	elif negotiation == "强制":
		# 点击强制
		browser.find_element_by_xpath('//*[@id="negotiation_1"]').click()
		if speed == "10":
			browser.find_element_by_xpath('//*[@id="speed_0"]').click()
		elif speed == "100":
			browser.find_element_by_xpath('//*[@id="speed_1"]').click()
		elif speed == "1000":
			browser.find_element_by_xpath('//*[@id="speed_2"]').click()
		if duplex == "全双工":
			browser.find_element_by_xpath('//*[@id="duplex_0"]').click()
		elif duplex == "半双工":
			browser.find_element_by_xpath('//*[@id="duplex_1"]').click()
		# 清除默认输入并且输入mtu
		browser.find_element_by_xpath('//*[@id="mtu"]').clear()
		browser.find_element_by_xpath('//*[@id="mtu"]').send_keys(force_mtu)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	elif save == "no":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()