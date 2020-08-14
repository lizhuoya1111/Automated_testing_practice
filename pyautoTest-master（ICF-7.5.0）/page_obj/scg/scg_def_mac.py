"""
2018年10月22日 10:32:13

函数一览：
	ip_mac_set
		MAC-绑定列表-设置功能

	add_ipmac_list
		添加ip_mac绑定列表

	del_ipmac_list
		删除ip_mac绑定列表

"""
import math

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def import *


# ip-mac设置
def ip_mac_set(browser, interface_name, s_mac_bing='', unkown_host=''):
	browser.refresh()
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# # 展开接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(绑定列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a').click()
	time.sleep(1)
	# 获得规则数量
	ip_mac_rules_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print(ip_mac_rules_count)
	# 找到对应名字的接口的编辑按钮，并点击进入编辑界面
	for x in range(2, 2+int(ip_mac_rules_count)):
		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip())
		if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip() == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[5]/a').click()

			if s_mac_bing == "yes":
				browser.find_element_by_xpath('//*[@id="src_mac_0"]').click()
			elif s_mac_bing == "no":
				browser.find_element_by_xpath('//*[@id="src_mac_1"]').click()

			if unkown_host == "yes":
				browser.find_element_by_xpath('//*[@id="un_host_0"]').click()
			elif unkown_host == "no":
				browser.find_element_by_xpath('//*[@id="un_host_1"]').click()
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
			break


# 添加ipmac列表
def add_ipmac_list(browser, ipadd, inteface, mac="", host_name='', get_mac_auto="no", get_hostname="no"):
	# 如果在当前页面找到“启用IP-MAC绑定表与静态ARP表同步”，则直接操作，不再重新点击导航栏 //*[@id="current"]/a //*[@id="current"]
	# webinfo = "null"
	#
	# try:
	# 	browser.switch_to.default_content()
	# 	browser.switch_to.frame("content")
	# 	browser.find_element_by_xpath(' //*[@id="current"]/a ').click()
	# 	time.sleep(2)
	# 	webinfo = browser.find_element_by_xpath('//*[@id="note_area"]/div/form/ul/li[1]').text
	# except Exception as err:
	# 	print(err)
	# 	pass
	# print(webinfo)
	# if "启用IP-MAC绑定表与静态ARP表同步" != webinfo:
	# 	into_fun(browser, 绑定列表)
	# else:
	# 	time.sleep(1)
	into_fun(browser, 绑定列表)
	time.sleep(1)
	try_num = 0
	while try_num < 5:
		try:
			browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()
			break
		except:
			time.sleep(1)
			try_num += 1
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ipadd)
	s = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	s.select_by_visible_text(inteface)

	if get_mac_auto == "no":
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	else:
		browser.find_element_by_xpath('//*[@id="mac"]').clear()
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
	if get_hostname == "no":
		browser.find_element_by_xpath('//*[@id="host"]').send_keys(host_name)
	else:
		browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()

	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 删除ipmac列表
def del_ipmac_list(browser, ipadd, inteface, mac):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[3]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[3]/div').click()
	# # 展开接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(绑定列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()
	time.sleep(3)
	ip_mac_list_count = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# 如果ip,mac,接口都匹配点击删除
	for x in range(2, 2+int(ip_mac_list_count)):
		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip())
		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.rstrip())
		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.rstrip())
		if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip() == ipadd:
			if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip() == mac:
				if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[4]').text.rstrip() == inteface:
					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[6]/a[2]').click()
					time.sleep(1)
					break
	# 总是漏删，确认一下是不是删除成功了
	# time.sleep(2)
	# ip_mac_list_count1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# if ip_mac_list_count1 >= ip_mac_list_count:
	# 	for x in range(2, 2 + int(ip_mac_list_count1)):
	# 		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip())
	# 		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.rstrip())
	# 		# print(browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.rstrip())
	# 		if browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.rstrip() == ipadd:
	# 			if browser.find_element_by_xpath(
	# 					'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.rstrip() == mac:
	# 				if browser.find_element_by_xpath(
	# 						'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.rstrip() == inteface:
	# 					browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[6]/a[2]').click()
	# 					break


""


# 通过桥名称获得该桥的MAC地址
def get_br_mac_byname(browser, br_name):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(桥MAC表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 桥MAC表)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) + 1
	for x1 in range(2, br_sum + 2):
		get_brname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		if get_brname == br_name:
			getmac = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[4]').text.rstrip()
			return getmac


# 获得动态ARP表中的IP地址、MAC地址、接口和主机名，以list形式返回[ip, mac, interface, hostname]
def get_dynamic_arp_all(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	arp_list_all = []
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x1 in range(2, br_sum+2):
		arp_list = []
		get_ipadd = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[3]').text.rstrip()
		get_mac = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
		get_inteface = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
		get_hostname = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
		arp_list.append(get_ipadd)
		arp_list.append(get_mac)
		arp_list.append(get_inteface)
		arp_list.append(get_hostname)
		arp_list_all.append(arp_list)
	# print(arp_list_all)
	return arp_list_all


# 获得静态ARP表中的IP地址、MAC地址、接口和主机名，以list形式返回[ip, mac, interface, hostname]
def get_static_arp_all(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	arp_list_all = []
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x1 in range(2, br_sum+2):
		arp_list = []
		get_ipadd = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[3]').text.rstrip()
		get_mac = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
		get_inteface = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
		get_hostname = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
		arp_list.append(get_ipadd)
		arp_list.append(get_mac)
		arp_list.append(get_inteface)
		arp_list.append(get_hostname)
		arp_list_all.append(arp_list)
	# print(arp_list_all)
	return arp_list_all


# 获得绑定列表中的IP地址、MAC地址、接口和主机名，以list形式返回[ip, mac, interface, hostname]
def get_binding_all(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	arp_list_all = []
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x1 in range(2, br_sum+2):
		arp_list = []
		get_ipadd = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		get_mac = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[3]').text.rstrip()
		get_inteface = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
		get_hostname = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
		arp_list.append(get_ipadd)
		arp_list.append(get_mac)
		arp_list.append(get_inteface)
		arp_list.append(get_hostname)
		arp_list_all.append(arp_list)
	# print(arp_list_all)
	return arp_list_all


# 指定序号删除动态ARP列表，每次只能删除一条
# 注意！ 是直接点击列表最后的删除图标，进行删除，如果是勾选checkbox，点击“删除所有”按钮，进行操作，应使用“del_dynamic_arp”函数
def del_dynamic_arp_by_index(browser, index):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:
		index_xpath = int(index) + 1
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(index_xpath)+']/td[7]/a').click()


# 删除 动态 ARP，支持全部删除、自定义序号（1个或者多个）删除，自定义删除时，传入序列号列表，默认是全部删除
def del_dynamic_arp(browser, index_list="all"):
	"""
	:param browser:
	:param index_list:
	:return:
	usage： del_dynamic_arp(browser, index_list=[2, 4])
	"""
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:

		if index_list == "all":
			br_sum1 = br_sum
			while br_sum1 > 1:
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="button_area"]/div/input[5]').click()
				browser.switch_to_alert().accept()
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				br_sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)

		elif type(index_list) is list:
			for x in index_list:
				xx = int(x) - 1
				browser.find_element_by_xpath('//*[@id="check_'+str(xx)+'"]').click()
			browser.find_element_by_xpath('//*[@id="button_area"]/div/input[5]').click()
			browser.switch_to_alert().accept()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 删除 静态 ARP，支持全部删除、自定义序号（1个或者多个）删除，自定义删除时，传入序列号列表，默认是全部删除
def del_static_arp(browser, index_list="all"):
	"""
	:param browser:
	:param index_list:
	:return:
	usage： del_dynamic_arp(browser, index_list=[2, 4])
	"""
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion //*[@id="current"] //*[@id="current"]
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:

		if index_list == "all":
			br_sum1 = br_sum
			while br_sum1 >= 1:
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="button_area"]/div/input[6]').click()
				browser.switch_to_alert().accept()
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				br_sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)

		elif type(index_list) is list:
			for x in index_list:
				xx = int(x) - 1
				browser.find_element_by_xpath('//*[@id="check_'+str(xx)+'"]').click()
			browser.find_element_by_xpath('//*[@id="button_area"]/div/input[6]').click()
			browser.switch_to_alert().accept()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 删除 绑定列表，支持全部删除、自定义序号（1个或者多个）删除，自定义删除时，传入序列号列表，默认是全部删除
def del_bindinglist(browser, index_list="all", pagesize="15/un"):
	"""
	:param browser:
	:param index_list:
	:return:
	usage： del_dynamic_arp(browser, index_list=[2, 4])
	"""
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion //*[@id="current"] //*[@id="current"]
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)

	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(2)
	if 'un' not in pagesize:
		s = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
		s.select_by_visible_text(str(pagesize))
		time.sleep(2)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(br_sum) //*[@id="pagecmd"]/ul/li[2] //*[@id="pagecmd"]/ul
	if br_sum >= 1:
		if index_list == "all":
			br_sum1 = br_sum
			while br_sum1 >= 1:

				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="sub_command_area"]/div[2]/input[2]').click()
				browser.switch_to_alert().accept()
				time.sleep(1)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(1)
				br_sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)


		elif type(index_list) is list:
			for x in index_list:
				xx = int(x) - 1
				browser.find_element_by_xpath('//*[@id="check_'+str(xx)+'"]').click()
			browser.find_element_by_xpath('//*[@id="sub_command_area"]/div[2]/input[2]').click()
			browser.switch_to_alert().accept()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 将 动态 ARP设置为静态ARP,默认是全部设置为静态，或者传入想要转为静态的IP地址
def set_arp_dyn_to_static(browser, ipadd="all"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:

		if ipadd == "all":
			br_sum1 = br_sum
			while br_sum1 > 1:
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# browser.switch_to.default_content()
				# # 定位到左侧frame
				# browser.switch_to.frame("lefttree")
				# # 点击网络
				# browser.find_element_by_xpath(网络).click()
				# if not browser.find_element_by_xpath(display_MAC).is_displayed():
				# 	# 如果不可见，点击加号，展开元素
				# 	browser.find_element_by_xpath(MAC).click()
				# browser.find_element_by_xpath(ARP列表).click()
				# # region Description
				# browser.switch_to.default_content()
				# # endregion
				# # 定位到内容frame
				# browser.switch_to.frame("content")
				into_fun(browser, ARP列表)
				time.sleep(1.5)
				br_sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)

		elif ipadd != "all":
			for x in range(2, br_sum+2):
				ipadd_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip()
				# print(ipadd_info)
				if ipadd_info == ipadd:
					# 目前仅支持第一页的操作
					xx = int(x) - 2
					browser.find_element_by_xpath('//*[@id="check_' + str(xx) + '"]').click()
					browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					break


# 将 动态 ARP绑定到绑定列表,默认是全部都绑定，或者传入想要转为绑定的IP地址
def set_arp_dyn_to_binding(browser, ipadd="all"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:

		if ipadd == "all":
			br_sum1 = br_sum
			while br_sum1 > 1:
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				binding_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
				# browser.switch_to.default_content()
				# # 定位到左侧frame
				# browser.switch_to.frame("lefttree")
				# # 点击网络
				# browser.find_element_by_xpath(网络).click()
				# if not browser.find_element_by_xpath(display_MAC).is_displayed():
				# 	# 如果不可见，点击加号，展开元素
				# 	browser.find_element_by_xpath(MAC).click()
				# browser.find_element_by_xpath(绑定列表).click()
				# browser.switch_to.default_content()
				# # 定位到内容frame
				# browser.switch_to.frame("content")
				into_fun(browser, 绑定列表)
				time.sleep(1.5)
				browser.find_element_by_xpath('//*[@id="tab_area"]/div/ul/li[2]/a').click()
				time.sleep(2)
				br_sum1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
				# print(br_sum1)
				# print(binding_num)
				if br_sum1 == binding_num:
					break

		elif ipadd != "all":
			for x in range(2, br_sum+2):
				ipadd_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip()
				# print(ipadd_info)
				if ipadd_info == ipadd:
					# 目前仅支持第一页的操作
					xx = int(x) - 2
					browser.find_element_by_xpath('//*[@id="check_' + str(xx) + '"]').click()
					browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					break


# 将 静态 ARP绑定到绑定列表,默认是全部都绑定，或者传入想要转为绑定的IP地址
def set_arp_static_to_binding(browser, ipadd="all"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:

		if ipadd == "all":
			br_sum1 = br_sum
			while br_sum1 > 1:
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').click()
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				binding_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
				# browser.switch_to.default_content()
				# # 定位到左侧frame
				# browser.switch_to.frame("lefttree")
				# # 点击网络
				# browser.find_element_by_xpath(网络).click()
				# if not browser.find_element_by_xpath(display_MAC).is_displayed():
				# 	# 如果不可见，点击加号，展开元素
				# 	browser.find_element_by_xpath(MAC).click()
				# browser.find_element_by_xpath(绑定列表).click()
				# browser.switch_to.default_content()
				# # 定位到内容frame
				# browser.switch_to.frame("content")
				into_fun(browser, 绑定列表)
				time.sleep(1.5)
				browser.find_element_by_xpath('//*[@id="tab_area"]/div/ul/li[2]/a').click()
				time.sleep(2)
				br_sum1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
				# print(br_sum1)
				# print(binding_num)
				if br_sum1 == binding_num:
					break

		elif ipadd != "all":
			for x in range(2, br_sum+2):
				ipadd_info = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip()
				# print(ipadd_info)
				if ipadd_info == ipadd:
					# 目前仅支持第一页的操作
					xx = int(x) - 2
					browser.find_element_by_xpath('//*[@id="check_' + str(xx) + '"]').click()
					browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').click()
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					break


# 编辑静态ARP—通过ip地址索引
def edit_static_arp_byipadd(browser, ipadd_index="", ipadd="", interface="", mac="", hostname="", getmac="no",
                            gethostname="no"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	if br_sum >= 1:
		for x1 in range(2, br_sum + 2):
			getipadd = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[3]').text.rstrip()
			# print(getipadd)
			if getipadd == ipadd_index:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[7]/a[1]').click()
				# 进入编辑界面，开始编辑静态ARP
				if ipadd != "":
					browser.find_element_by_xpath('//*[@id="ip"]').clear()
					browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ipadd)
				if interface != "":
					interface_select = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
					interface_select.select_by_visible_text(interface)
					if getmac != "no":
						browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
					if gethostname != "no":
						browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()
				if mac != "":
					browser.find_element_by_xpath('//*[@id="mac"]').clear()
					browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
				if hostname != "":
					browser.find_element_by_xpath('//*[@id="host"]').clear()
					browser.find_element_by_xpath('//*[@id="host"]').send_keys(hostname)

				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 获得IP-MAC设置界面所有接口名，返回接口名的列表
def get_ipmac_set_interfaces(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	time.sleep(1.5)
	interface_list = []
	sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x in range(2, sum1+2):
		getinterface = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
		interface_list.append(getinterface)
	return interface_list


# 根据接口名字，获得源MAC绑定和未定义主机策略的状态，返回是两个状态的列表
def get_info_macbinding_unkownhost_byinterface(browser, interface=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	time.sleep(1.5)
	status_list = []
	sum1 = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x in range(2, sum1+2):
		getinterface = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
		if getinterface == interface:
			get_macbinding_status = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip()
			get_unkownhost_status = browser.find_element_by_xpath(
				'//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.rstrip()
			status_list.append(get_macbinding_status)
			status_list.append(get_unkownhost_status)
			return status_list


# 添加ARP Spoof防御
def add_arp_spoof_jyl(browser, arp_request="", arp_reverse="", gratuitous_update="", update_num=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击ARP Spoof防御
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(1)
	if arp_request == "yes":
		enable = browser.find_element_by_xpath('//*[@id="request_learn"]').is_selected()
		if enable is not True:
			browser.find_element_by_xpath('//*[@id="request_learn"]').click()
	if arp_reverse == "yes":
		enable = browser.find_element_by_xpath('//*[@id="reverse_query"]').is_selected()
		if enable != True:
			browser.find_element_by_xpath('//*[@id="reverse_query"]').click()
	if gratuitous_update == "yes":
		enable = browser.find_element_by_xpath('//*[@id="update"]').is_selected()
		if enable != True:
			# browser.find_element_by_xpath('//*[@id="request_learn"]').click()
			browser.find_element_by_xpath('//*[@id="update"]').click()
		if 	update_num != "":
			browser.find_element_by_xpath('//*[@id="interval"]').clear()
			browser.find_element_by_xpath('//*[@id="interval"]').send_keys(update_num)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 清除ARP Spoof防御界面所有的勾选
def clear_arp_spoof_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击ARP Spoof防御
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	# # 点击ARP Spoof防御
	# browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(0.5)
	enable1 = browser.find_element_by_xpath('//*[@id="request_learn"]').is_selected()
	if enable1 is True:
		browser.find_element_by_xpath('//*[@id="request_learn"]').click()

	enable2 = browser.find_element_by_xpath('//*[@id="reverse_query"]').is_selected()
	if enable2 is True:
		browser.find_element_by_xpath('//*[@id="reverse_query"]').click()

	enable3 = browser.find_element_by_xpath('//*[@id="update"]').is_selected()
	if enable3 is True:
		browser.find_element_by_xpath('//*[@id="update"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 进入ARP Spoof防御界面，不做任何操作
def get_into_arp_spoof_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击ARP Spoof防御
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()


# 添加静态ARP
def add_static_arp_jyl(browser, ip="", interface="", mac_add="manual_mac", mac="", host_name="", host=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击静态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[5]').click()
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 选择自动获取Mac或者手动输入Mac
	# 选择自动获取Mac
	if mac_add == "auto_mac":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
	# 选择手动输入Mac
	elif mac_add == "manual_mac":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	# 选择自动获取主机名或者手动输入主机名
	# 选择自动获取主机名
	if host_name == "auto_host":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()
	# 选择手动输入主机名
	elif host_name == "manual_host":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="host"]').send_keys(host)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加ip-Mac绑定
def add_ip_mac_binding_jyl(browser, ip="", interface="", mac_add="manual_mac", mac="", host_name="", host=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击绑定列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 选择自动获取Mac或者手动输入Mac
	# 选择自动获取Mac
	if mac_add == "auto_mac":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
	# 选择手动输入Mac
	elif mac_add == "manual_mac":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	# 选择自动获取主机名或者手动输入主机名
	# 选择自动获取主机名
	if host_name == "auto_host":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()
	# 选择手动输入主机名
	elif host_name == "manual_host":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="host"]').send_keys(host)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 进入桥Mac界面，不进行任何操作
def get_into_bri_mac_jyl(browser):
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(桥MAC表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 桥MAC表)


# 添加桥Mac表  桥搜索和Mac搜索不打开，默认搜索全部网桥
def add_bri_mac_jyl(browser, bri_serch="", bridge="", mac_serach="", mac=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(桥MAC表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 桥MAC表)
	if bri_serch == "open":
		# 选bridge下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="bridge"]'))
		# 选bridge下拉框内容
		s1.select_by_visible_text(bridge)
	if mac_serach == "open":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	# 点击搜索
	browser.find_element_by_xpath('//*[@id="for_note"]/table/tbody/tr[2]/td[3]/input[2]').click()


# 删除静态ARP
def delete_static_arp_jyl(browser, static_arp_ip=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击静态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
	print(getname)
	while getname != static_arp_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
		print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()


# 编辑静态ARP
def edit_static_arp_jyl(browser, edit_arp_ip="",  ip="", interface="", mac_add="manual_mac", mac="", host_name="",
                        host=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击静态ARP
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
	# print(getname)
	while getname != edit_arp_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 选择自动获取Mac或者手动输入Mac
	# 选择自动获取Mac
	if mac_add == "auto_mac":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
	# 选择手动输入Mac
	elif mac_add == "manual_mac":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="mac"]').clear()
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	# 选择自动获取主机名或者手动输入主机名
	# 选择自动获取主机名
	if host_name == "auto_host":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()
	# 选择手动输入主机名
	elif host_name == "manual_host":
		# 输入主机名
		browser.find_element_by_xpath('//*[@id="host"]').clear()
		browser.find_element_by_xpath('//*[@id="host"]').send_keys(host)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 进入静态ARP界面，不进行任何操作
def get_into_static_arp_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击静态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()


# 进入绑定
def get_into_ip_mac_binding_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击绑定列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()


# 将动态ARP设为静态ARP
def set_dynamic_arp_to_static_arp_jyl(browser, dynamic_arp_ip=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击动态ARP
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
	# print(getname)
	while getname != dynamic_arp_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
		# print(getname)
	# 点击选择
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[1]').click()
	# 点击设为静态
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[3]').click()


# 进入动态ARP界面，不进行任何操作
def get_into_dynamic_arp_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击动态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()


# 删除动态ARP
def delete_dynamic_arp_jyl(browser, dynamic_arp_ip=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击动态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
	# print(getname)
	while getname != dynamic_arp_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
		# print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a/img').click()


# 全选删除所有动态ARP
def delete_all_dynamic_arp_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击动态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击全选
	browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
	# 点击全部删除
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[5]').click()
	# 接受告警
	browser.switch_to_alert().accept()


# 编辑设置绑定列表
def edit_ip_mac_binding_rule_jyl(browser, interface="", source_mac_binding="", policy_for_undefined_host=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 绑定列表)
	# 点击设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(2)
	n = 2
	# 选择接口
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑按钮
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[5]/a/img').click()
	if source_mac_binding == "enable":
		# 点击启用
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="src_mac_0"]').click()
	elif source_mac_binding == "disenable":
		# 点击禁用
		browser.find_element_by_xpath('//*[@id="src_mac_1"]').click()
	if policy_for_undefined_host == "allow":
		# 点击允许
		browser.find_element_by_xpath('//*[@id="un_host_0"]').click()
	elif policy_for_undefined_host == "block":
		# 点击阻止
		browser.find_element_by_xpath('//*[@id="un_host_1"]').click()
	elif policy_for_undefined_host == "alert":
		# 点击警告
		browser.find_element_by_xpath('//*[@id="un_host_2"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除绑定列表
def delete_ip_mac_banding_jyl(browser, ip=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击绑定列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a[2]/img').click()


# 编辑绑定列表
def edit_ip_mac_banding_jyl(browser, banding_ip="", ip="", interface="", mac_add="", mac="", host_name="", host=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击绑定列表
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != banding_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a[1]/img').click()
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 选择自动获取Mac或者手动输入Mac
	# 选择自动获取Mac
	if mac_add == "auto_mac":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/span[2]/a').click()
	# 选择手动输入Mac
	elif mac_add == "manual_mac":
		# 输入MAC
		browser.find_element_by_xpath('//*[@id="mac"]').clear()
		browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)
	# 选择自动获取主机名或者手动输入主机名
	# 选择自动获取主机名
	if host_name == "auto_host":
		# 点击自动获取IP地址
		browser.find_element_by_xpath('//*[@id="conftr_3"]/td[2]/span[2]/a').click()
	# 选择手动输入主机名
	elif host_name == "manual_host":
		# 输入主机名
		browser.find_element_by_xpath('//*[@id="host"]').clear()
		browser.find_element_by_xpath('//*[@id="host"]').send_keys(host)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 进入设置绑定列表界面，不进行任何操作
def get_into_edit_ip_mac_binding_rule_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()


# 启用绑定列表和静态ARP同步
def synchronization_ip_mac_banding_and_static_arp_(browser, banding_static=""):
	# into_fun(browser, menu)
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 绑定列表)
	# 点击绑定列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	if banding_static == "open":
		enable = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if enable is True:
			print("已启用")
		else:
			# 点击启用
			browser.find_element_by_xpath('//*[@id="status"]').click()
			# 接受告警
			browser.switch_to_alert().accept()
			time.sleep(1)
			# 接受告警
			browser.switch_to_alert().accept()
	elif banding_static == "close":
		enable = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if enable is True:
			# 点击启用
			browser.find_element_by_xpath('//*[@id="status"]').click()
			# 接受告警
			browser.switch_to_alert().accept()
			time.sleep(1)
			# 接受告警
			browser.switch_to_alert().accept()
		else:
			print("已关闭")


# 启用静态ARP和绑定列表同步
def synchronization_static_arp_and_ip_mac_banding_(browser, static_arp=""):
	# into_fun(browser, menu)
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(ARP列表).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, ARP列表)
	# 点击静态ARP
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	if static_arp == "open":
		enable = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if enable is True:
			print("已启用")
		else:
			# 点击启用
			browser.find_element_by_xpath('//*[@id="status"]').click()
			# 接受告警
			browser.switch_to_alert().accept()
			time.sleep(1)
			# 接受告警
			browser.switch_to_alert().accept()
	elif static_arp == "close":
		enable = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if enable is True:
			# 点击启用
			browser.find_element_by_xpath('//*[@id="status"]').click()
			# 接受告警
			browser.switch_to_alert().accept()
			time.sleep(1)
			# 接受告警
			browser.switch_to_alert().accept()
		else:
			print("已关闭")


# 通过MAC查询指定的网桥,返回网桥
def get_br_mac_list_byname(browser, br_mac):
	# into_fun(browser, menu)
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(桥MAC表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 桥MAC表)
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(br_mac)
	# 点击搜索
	browser.find_element_by_xpath('//*[@id="for_note"]/table/tbody/tr[2]/td[3]/input[2]').click()
	get_br = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
	return get_br


# 通过MAC查询指定的网桥,返回网桥
def get_br_mac_list_byname_jyl(browser, br_mac):
	into_fun(browser, menu=桥MAC表)
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(桥MAC表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(br_mac)
	# 点击搜索
	browser.find_element_by_xpath('//*[@id="for_note"]/table/tbody/tr[2]/td[3]/input[2]').click()
	get_br = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
	return get_br


# 判断ip-mac绑定设置是否有接口,若存在返回True,反之返回False
def query_ip_mac_binding_set_interface_jyl(browser, des_interface=''):
	into_fun(browser, menu=绑定列表)
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(1)
	route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据数量,遍历一下
	print(str(des_interface))
	for x in range(2, 2 + route_sum):							# //*[@id="table"]/tbody/tr[2]/td[2]
		if str(des_interface) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text.replace(' ', ''):
			return True
	else:
		return False


# 将 绑定列表设为静态arp，支持全部设为静态arp、自定义序号（1个或者多个）设为静态arp，自定义设为静态arp时，传入序列号列表，默认是设为静态arp
def set_bandinglist_to_static_arp(browser, index_list="all"):
	"""
	:param browser:
	:param index_list:
	:return:
	usage： del_dynamic_arp(browser, index_list=[2, 4])
	"""
	into_fun(browser, menu=绑定列表)
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath(display_MAC).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(MAC).click()
	# browser.find_element_by_xpath(绑定列表).click()
	# # region Description
	# browser.switch_to.default_content()
	# # endregion //*[@id="current"] //*[@id="current"]
	# # 定位到内容frame //*[@id="tabs"]/li[2]/a/span
	# browser.switch_to.frame("content") //*[@id="tabs"]/li[2]/a/span
	time.sleep(1.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
	time.sleep(1.5)
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(br_sum)
	if br_sum >= 1:
		if index_list == "all":
			br_sum1 = br_sum
			while br_sum1 >= 1:					# //*[@id="btn_check_all"]
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').click()
				time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				br_sum1 = 0

		elif type(index_list) is list:
			for x in index_list:
				xx = int(x) - 1
				browser.find_element_by_xpath('//*[@id="check_'+str(xx)+'"]').click()
			browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').click()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 获取liunx主机的Mac地址，需要传入主机名字，网卡ip地址（如：host_name="10.1.1.202"，ip_add="20.1.1.2"）返回结果字母是大写
def get_linux_host_mac_jyl(host_name="", user="root", password="root", ip_add=""):
	to_ssh = Shell_SSH()
	to_ssh.connect(host_name, user, password)
	to_ssh.execute("ifconfig | grep "+str(ip_add)+" -C 1 | grep HWaddr")
	result1 = to_ssh.output()
	# print(result1)
	result2 = result1.split('Ethernet')[1]
	# print(result2)
	result3 = result2.split('HWaddr')[1]
	# print(result3)
	result4 = result3.split('[')[0]
	# print(result4)
	result5 = result4.strip()
	to_ssh.close()
	return result5


# 获取设备接口的Mac地址，需要传入设备名，接口（如：dut_name=dev1，interface=dev1）返回结果字母是大写
def get_dut_interface_mac_jyl(dut_name="", interface=""):
	a = Shell_SSH()
	a.connect(hostip=dut_name)
	a.execute("en")
	a.execute("show interface gigabitethernet "+interface)
	result1 = a.output()
	# print(result1)
	result2 = result1.split('HWaddr')[1]
	# print(result2)
	result3 = result2.split('Work-mode')[0]
	# print(result3)
	result4 = result3[1:]
	# print(result4)
	result5 = result4.strip()
	a.close()
	return result5


# 设置绑定列表界面的每页显示数，15，20，30，150
def change_pagesize_ipmac_table_lzy(browser, pagesize="15"):
	into_fun(browser, menu=绑定列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	s = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
	s.select_by_visible_text(str(pagesize))
	time.sleep(2)


# ip_mac绑定列表翻页 点击下一页或者前一页
def click_previous_or_next_page_ipmac_binding_lzy(browser, pre_page="yes/no", next_page="yes/no"):
	into_fun(browser, menu=绑定列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	if pre_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
	if next_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
	time.sleep(2)

import math

# ip_mac绑定列表翻页 点击跳转到某页 page跳转到某页 num当前每页显示条目数
def click_into_page_ipmac_binding_lzy(browser, page="2", num="15"):
	into_fun(browser, menu=绑定列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
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


# 获取ip_mac_binding总条目数,返回int型
def get_count_number_ipmac_binding_lzy(browser):
	into_fun(browser, menu=绑定列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)


# 获取静态ARP总条目数,返回int型
def get_count_number_static_arp_lzy(browser):
	into_fun(browser, menu=ARP列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)

# 静态ARP列表翻页 点击下一页或者前一页
def click_previous_or_next_page_static_arp_lzy(browser, pre_page="yes/no", next_page="yes/no"):
	into_fun(browser, menu=ARP列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	if pre_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
	if next_page == 'yes':
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
	time.sleep(2)


# 设置静态ARP列表界面的每页显示数，15，20，30，150
def change_pagesize_static_arp_lzy(browser, pagesize="15"):
	into_fun(browser, menu=ARP列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	s = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
	s.select_by_visible_text(str(pagesize))
	time.sleep(2)


# 静态ARP绑定列表翻页 点击跳转到某页 page跳转到某页 num当前每页显示条目数
def click_into_page_static_arp_lzy(browser, page="2", num="15"):
	into_fun(browser, menu=ARP列表)
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	num2 = int(num1)
	# 获取总页数
	s1 = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[4]/select'))
	s1.select_by_visible_text(str(num))
	page1 = num2/int(num)
	page2 = math.ceil(page1)
	print(page2)
	# 跳转到第二页
	s2 = Select(browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[3]/select'))
	s2.select_by_visible_text(str(page)+'/'+str(page2))
	time.sleep(2)




# 以下4个函数均是固定P3接口添加静态ARP或者ip_mac_binding，IP为30网段，Mac地址均为aa:aa:aa:aa:aa:aa
# 命令行添加静态ARP 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_add_static_arp_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("arp interface P3 ip 30.1." + str(x) + "." + str(y) + " mac aa:aa:aa:aa:aa:aa")
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行删除静态ARP 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_delete_static_arp_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("no arp interface P3 ip 30.1." + str(x) + "." + str(y))
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行添加IPMac绑定 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_add_ip_mac_binding_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("ip-mac-binding interface P3 ip 30.1." + str(x) + "." + str(y) + " mac aa:aa:aa:aa:aa:aa")
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行删除ipmac绑定 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_delete_ip_mac_binding_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("no ip-mac-binding interface P3 ip 30.1." + str(x) + "." + str(y))
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 以下4个函数是改良后的添加静态ARP或者ip_mac_binding，IP为30网段，Mac地址可选，默认aa:aa:aa:aa:aa:aa，接口可选，默认#6接口
# 命令行添加静态ARP 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_add_static_arp_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2, interface=interface_name_6, mac='aa:aa:aa:aa:aa:aa'):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("arp interface " + interface + " ip 30.1." + str(x) + "." + str(y) + " mac " + mac)
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行删除静态ARP 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_delete_static_arp_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2, interface=interface_name_6):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("no arp interface " + interface + " ip 30.1." + str(x) + "." + str(y))
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行添加IPMac绑定 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_add_ip_mac_binding_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2, interface=interface_name_6, mac='aa:aa:aa:aa:aa:aa'):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("ip-mac-binding interface " + interface + " ip 30.1." + str(x) + "." + str(y) + " mac " + mac)
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


# 命令行删除ipmac绑定 以IP30.1.x.y 为例 num1代表x num2代表y
def cli_delete_ip_mac_binding_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num11=2, num2=1, num22=2, interface=interface_name_6):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num11):
		for y in range(num2, num22):
			scg.execute("no ip-mac-binding interface " + interface + " ip 30.1." + str(x) + "." + str(y))
			time.sleep(0.3)
		time.sleep(0.2)
	time.sleep(5)
	scg.close()
	output = scg.output()
	print(output)


