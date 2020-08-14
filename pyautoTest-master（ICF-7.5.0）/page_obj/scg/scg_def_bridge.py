from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *


# 通过名称寻找桥是否存在
def bridge_find_byname(browser, br_name):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) + 1
	for x1 in range(2, br_sum):
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[2]').text.rstrip()
		print(getname)
		# 获取接口名称
		if getname == br_name:
			return True


# 添加网桥
def bridge_add_jyl(browser, bridge_name="", bridge_describe="", snat="no", allow_ping="yes", block_intra_bridge_traffic="", stp="yes/no"):

	# 定位到默认frame
	browser.refresh()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="name"]').clear()
	# 输入网桥名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(bridge_name)
	# 输入网桥描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(bridge_describe)
	# 点击
	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
	# 判断是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
	if snat == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	# 判断是否勾选
	enable2 = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
	if allow_ping=="yes":
		if enable2 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	else:
		if enable2 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	# 判断是否勾选
	enable3 = browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected()
	if block_intra_bridge_traffic=="yes":
		if enable3 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()
	else:
		if enable3 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()
	# 判断是否勾选
	enable4 = browser.find_element_by_xpath('//*[@id="stp"]').is_selected()
	if stp == "yes":
		if enable4 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="stp"]').click()
	else:
		if enable4 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="stp"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加网桥接口成员
def bridge_edit_interface_jyl(browser,  bridge_interface="", interface=""):
	# 定位到默认frame
	browser.refresh()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != bridge_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 点击移动
	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
	# 点击保存
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 编辑网桥添加ip地址
def bridge_edit_ip_add_jyl(browser, bridge_interface="", address_mode="", ip="", mask="", update_default_gateway="", update_system_dns=""):
	# 定位到默认frame
	browser.refresh()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	while getname != bridge_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()

	if address_mode=="manual":
		# 点击
		browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
		# 输入ip
		browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
		# 输入掩码
		browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	else:
		# 点击dhcp
		browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
		if update_default_gateway=="yes":
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
		else:
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
		if update_system_dns=="yes":
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
		else:
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 删除网桥
def delete_bridge_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[2]/img').click()
	time.sleep(2)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑网桥删除接口
def birdge_edit_interface_delete_jyl(browser, interface="", bridge_interface=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到内容frame
	browser.switch_to.frame("content")
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface_dst"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 点击移动
	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[2]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 网桥接口从DHCP服务器获取IP地址
def bridge_interface_from_dhcp_obtain_ip_jyl(browser, bridge="", description="", work_mode="dhcp", dhcp_status1="",
                                             dhcp_status2="", dhcp_status3="", update_default_gateway="",
                                             update_system_dns="", snat="", allow_ping=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
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
	time.sleep(5)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)
	# 获取接口名称
	getname1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
	# print(getname1)
	loopmax = 0
	while getname1 == "0.0.0.0" and loopmax < 5:
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		# 获取接口名称
		getname1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
		print(getname1)
		loopmax += 1
		time.sleep(2)
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(3)
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(1)
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(3)
	if dhcp_status2 == "stop":
		# 点击取消						# //*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if dhcp_status2 != "stop":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		getname2 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
		print(getname2)
		loopmax1 = 0
		while getname2 == "0.0.0.0" and loopmax1 < 5:
			# 点击刷新
			browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
			# 获取接口名称
			getname2 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
			print(getname2)
			loopmax1 += 1
			time.sleep(2)
		time.sleep(2)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 网桥接口从DHCP服务器获取IP地址
def bridge_interface_obtain_ip_from_dhcp_jyl(browser, bridge="", description="", work_mode="dhcp"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(5)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)
	# 获取接口名称
	getname1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
	print(getname1)
	while getname1 == "0.0.0.0":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		# 获取接口名称
		getname1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
		print(getname1)
		time.sleep(2)


# 网桥接口从DHCP服务器获取IP地址之后的状态
def bridge_interface_obtain_ip_dhcp_status_jyl(browser, bridge="", work_mode="dhcp", dhcp_status1="", dhcp_status2="", dhcp_status3="",):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(5)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		getname2 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
		print(getname2)
		while getname2 == "0.0.0.0":
			# 点击刷新
			browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
			# 获取接口名称
			getname2 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text.rstrip()
			print(getname2)
			time.sleep(2)
		time.sleep(2)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()



def bridge_interface_update_dhcp_jyl(browser, bridge="", description="", update_default_gateway="", update_system_dns="", snat="", allow_ping=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
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
	time.sleep(5)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)


# 网桥接口从DHCP获取IP地址
def bridge_interface_obtain_ip_from_dhcp1_jyl(browser, bridge="", description="", work_mode="dhcp"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 添加网桥的IP地址
def bridge_ip_add(browser, bridge_interface="", address_mode="manual", ip="", mask="", update_default_gateway="", update_system_dns=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(1)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	while getname != bridge_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()

	if address_mode == "manual":
		# 点击
		browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
		# 输入ip
		browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
		# 输入掩码
		browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	else:
		# 点击dhcp
		browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
		if update_default_gateway == "yes":
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
		else:
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
			# 点击
			browser.find_element_by_xpath('//*[@id="gw_update"]').click()
		if update_system_dns == "yes":
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
		else:
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
			# 点击
			browser.find_element_by_xpath('//*[@id="dns_update"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 编辑网桥接口
def bri_edit_interface(browser, interface="", bridge_interface=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(1)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != bridge_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 点击移动
	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
	# 点击保存
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 删除网桥,每次只删除第一个（br_0除外）
def delete_bridge(browser):
	browser.refresh()
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[2]/img').click()
	time.sleep(1)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加网桥
def bri_add(browser, bridge_name="", bridge_describe="", snat="", allow_ping="yes", block_intra_bridge_traffic=""):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(1)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="name"]').clear()
	# 输入网桥名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(bridge_name)
	# 输入网桥描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(bridge_describe)
	# 点击
	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
	# 判断是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
	if snat == "yes":
		if enable1 != True:
			# 点击
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	else:
		if enable1 == True:
			# 点击
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	# 判断是否勾选
	enable2 = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
	if allow_ping=="yes":
		if enable2 != True:
			# 点击
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	else:
		if enable2 == True:
			# 点击
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	# 判断是否勾选
	enable3 = browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected()
	if block_intra_bridge_traffic=="yes":
		if enable3 != True:
			# 点击
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()
	else:
		if enable3 == True:
			# 点击
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()
	# 判断是否勾选
	enable4 = browser.find_element_by_xpath('//*[@id="stp"]').is_selected()
	if block_intra_bridge_traffic=="yes":
		if enable4 != True:
			# 点击
			browser.find_element_by_xpath('//*[@id="stp"]').click()
	else:
		if enable4 == True:
			# 点击
			browser.find_element_by_xpath('//*[@id="stp"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 点击编辑，进入编辑网桥界面
def bri_edit_jyl(browser,  bridge=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()


# 点击增加，进入增加网桥界面
def bri_add_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()


# 根据名字删除网桥，默认删除全部
def delete_bridge_byname(browser, br_name="all"):
	browser.refresh()
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	# 点击删除
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(br_sum)
	if br_name == "all":
		while br_sum > 1:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[2]/img').click()
			time.sleep(0.5)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	else:
		for x in range(2, br_sum+2):
			getbrname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
			if getbrname == br_name:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[7]/a[2]/img').click()


# 进入网桥界面，为下一步操作做准备
def get_into_bri_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击网桥
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame 进入网桥界面
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)


# 在网桥列表通过网桥名称，获取网桥mac
def get_bri_mac_byname(browser, br_name):
	# into_fun(browser, menu)
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# browser.find_element_by_xpath(网桥).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) + 1
	for x1 in range(2, br_sum + 2):					# //*[@id="table"]/tbody/tr[2]/td[2]
		get_brname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		if get_brname == br_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[7]/a[1]/img').click()
			getmac = browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/span[2]').text.rstrip()
			return getmac


# 在网桥列表通过网桥名称，获取网桥mac
def get_bri_mac_byname_jyl(browser, br_name):
	into_fun(browser, menu=网桥)
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_接口设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# browser.find_element_by_xpath(网桥).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) + 1
	for x1 in range(2, br_sum + 2):					# //*[@id="table"]/tbody/tr[2]/td[2]
		get_brname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		if get_brname == br_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[7]/a[1]/img').click()
			getmac = browser.find_element_by_xpath('//*[@id="conftr_0"]/td[2]/span[2]').text.rstrip()
			return getmac


# 获取网桥列表接口成员
def get_bri_list_member_inter(browser, bridge=""):
	into_fun(browser, menu=网桥)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != bridge:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# 点击编辑
	time.sleep(2)
	interface = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.rstrip()
	return interface


# 删除指定网桥的指定ip地址
def del_br_addr(browser, br_name, ipadd):
	into_fun(browser, menu=网桥)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) + 1
	for x1 in range(2, br_sum + 2):
		get_brname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[2]').text.rstrip()
		if get_brname == br_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[7]/a[1]/img').click()
			m = 2
			getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[2]').text

			while getip != ipadd:
				m = m + 1
				getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[2]').text
			# 点击删除
			browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[4]/input').click()
			break


# 获取bridge网桥总条目数,返回int型
def get_count_number_bridge_lzy(browser):
	into_fun(browser, menu=网桥)
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)



# 命令行添加网桥bridge（空）
def cli_add_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("interface bridge br_" + str(x))
		time.sleep(0.2)
		scg.execute("exit")
		time.sleep(0.2)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)

# 命令行删除网桥bridge（空）
def cli_delete_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("no interface bridge br_" + str(x))
		time.sleep(0.1)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)

# 命令行添加网桥bridge带接口
def cli_add_bridge_interface_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2, interface=''):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("interface bridge br_" + str(x))
		time.sleep(0.2)
		scg.execute("bridge-member " + interface)
		time.sleep(0.2)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)

# 命令行给网桥bridge添加ip(num1到num2为网桥编号）(添加254个网桥以内适用）
def cli_add_bridge_ip_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2,  num11=1, num22=2, num111=1, num222=2, bridge='br_', ip='30.', mask='32'):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("interface bridge " + bridge + str(x))
		time.sleep(0.2)
		for y in range(num11, num22):
			for z in range(num111, num222):
				scg.execute("ip address " + ip + str(x) + "." + str(y) + "." + str(z) + " " + mask)
				time.sleep(0.2)
		scg.execute("exit")
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)
