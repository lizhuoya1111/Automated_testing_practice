from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 开始ospf
def start_ospf_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(路由).click()
	# # 点击OSPF
	# browser.find_element_by_xpath(OSPF).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, OSPF)
	# 点击开始
	browser.find_element_by_xpath('//*[@id="config"]/input').click()
	# 接受告警
	browser.switch_to_alert().accept()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 停止ospf
def stop_ospf_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(路由).click()
	# # 点击OSPF
	# browser.find_element_by_xpath(OSPF).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, OSPF)
	# 点击停止
	browser.find_element_by_xpath('//*[@id="config"]/input').click()
	# 接受告警
	browser.switch_to_alert().accept()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 设置OSPF全局设置（若选择静态或者直连清除默认值）
def ospf_general_jyl(browser, route_id="", manual_ip="", static="", static_num="", connected="", connected_num="",
                     save="", cancel=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(路由).click()
	# # 点击OSPF
	# browser.find_element_by_xpath(OSPF).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, OSPF)
	# 点击全局设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	if route_id == "auto":
		# 点击auto
		browser.find_element_by_xpath('//*[@id="id_type_0"]').click()
	elif route_id == "manual":
		# 点击manual
		browser.find_element_by_xpath('//*[@id="id_type_1"]').click()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="routeId"]').clear()
		# 输入IP
		browser.find_element_by_xpath('//*[@id="routeId"]').send_keys(manual_ip)
	if static == "yes":
		enable = browser.find_element_by_xpath('//*[@id="static"]').is_selected()
		if enable == True:
			print("静态按钮已开启")
		elif enable != True:
			# 点击静态
			browser.find_element_by_xpath('//*[@id="static"]').click()
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="static_metric"]').clear()
			# 输入静态metric
			browser.find_element_by_xpath('//*[@id="static_metric"]').send_keys(static_num)
	elif static == "no":
		enable = browser.find_element_by_xpath('//*[@id="static"]').is_selected()
		if enable == True:
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="static_metric"]').clear()
			# 输入静态metric
			browser.find_element_by_xpath('//*[@id="static_metric"]').send_keys("20")
			# 点击关闭静态
			browser.find_element_by_xpath('//*[@id="static"]').click()
		elif enable != True:
			print("静态按钮已关闭")
	if connected == "yes":
		enable = browser.find_element_by_xpath('//*[@id="connected"]').is_selected()
		if enable == True:
			print("直连按钮已开启")
		elif enable != True:
			# 点击直连
			browser.find_element_by_xpath('//*[@id="connected"]').click()
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="connected_metric"]').clear()
			# 输入直连metric
			browser.find_element_by_xpath('//*[@id="connected_metric"]').send_keys(connected_num)
	elif connected == "no":
		enable = browser.find_element_by_xpath('//*[@id="connected"]').is_selected()
		if enable == True:
			# 清除默认输入
			browser.find_element_by_xpath('//*[@id="connected_metric"]').clear()
			# 输入直连metric
			browser.find_element_by_xpath('//*[@id="connected_metric"]').send_keys("20")
			# 点击关闭静态
			browser.find_element_by_xpath('//*[@id="connected"]').click()
		elif enable != True:
			print("静态按钮已关闭")
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[3]').click()


# 设置OSPF全局设置（若选择静态或者直连不清除默认值）
def ospf_general_no_clear_jyl(browser, route_id="", manual_ip="", static="", connected="",
					 save="", cancel=""):

	into_fun(browser, OSPF)
	# 点击全局设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	if route_id == "auto":
		# 点击auto
		browser.find_element_by_xpath('//*[@id="id_type_0"]').click()
	elif route_id == "manual":
		# 点击manual
		browser.find_element_by_xpath('//*[@id="id_type_1"]').click()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="routeId"]').clear()
		# 输入IP
		browser.find_element_by_xpath('//*[@id="routeId"]').send_keys(manual_ip)
	if static == "yes":
		# 点击静态
		browser.find_element_by_xpath('//*[@id="static"]').click()
	if connected == "yes":
		# 点击直连
		browser.find_element_by_xpath('//*[@id="connected"]').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[3]').click()


# 添加OSPF网络
def add_ospf_network_jyl(browser, network="", mask="", area_id="", save="", cancel=""):
	into_fun(browser, OSPF)
	# 点击网络
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	# 点击增加
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	# 输入网络
	browser.find_element_by_xpath('//*[@id="net_ip"]').send_keys(network)
	# 输入掩码
	browser.find_element_by_xpath('//*[@id="net_mask"]').send_keys(mask)
	# 输入区域ID
	browser.find_element_by_xpath('//*[@id="id"]').send_keys(area_id)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 删除添加的ospf network。支持全部删除，删除一条时，传入所要删除的ip，默认全部删除。
def delete_ospf_network_jyl(browser, ospf_neteork_ip="all"):
	into_fun(browser, OSPF)
	# 点击网络
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	if ospf_neteork_ip == "all":
		# 点击全选
		browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
		# 点击删除所有
		browser.find_element_by_xpath('//*[@id="sub_command_area"]/div[2]/input').click()
		# 接受告警
		browser.switch_to_alert().accept()
	elif ospf_neteork_ip != "all":
		n = 2
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
		while getname != ospf_neteork_ip:
			n = n + 1
			getname = browser.find_element_by_xpath('# //*[@id="table"]/tbody/tr[2]/td[2]').text.rstrip()
			print(getname)
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[5]/a[2]/img').click()
		time.sleep(0.5)


# 编辑时，区域ID和IP的xpath相同，无法编辑，函数目前无法使用
def edit_ospf_network_jyl(browser, ospf_neteork_ip="", network="", mask="", area_id="", save="", cancel=""):
	# 点击网络
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != ospf_neteork_ip:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[5]/a[1]/img').click()
	time.sleep(0.5)
	if network != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="net_ip"]').clear()
		# 输入网络
		browser.find_element_by_xpath('//*[@id="net_ip"]').send_keys(network)
	if mask != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="net_mask"]').clear()
		# 输入掩码
		browser.find_element_by_xpath('//*[@id="net_mask"]').send_keys(mask)
	if area_id != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="id"]').clear()
		# 输入区域ID
		browser.find_element_by_xpath('//*[@id="id"]').send_keys(area_id)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 获取ospf接口界面所有的接口信息，以列表形式返回[接口名称，优先级，hello_interval，hello_death，认证类型]
def get_ospf_interface_name_jyl(browser):
	into_fun(browser, OSPF)
	# 点击接口
	browser.find_element_by_xpath('//*[@id="tabs"]/li[4]/a/span').click()
	time.sleep(1.5)
	ospf_interface_list_all = []
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x1 in range(2, br_sum+2):
		arp_list = []
		get_interface = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		get_priority = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[3]').text.rstrip()
		get_hello_interval = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
		get_dead_interval = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
		get_auth_type = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
		arp_list.append(get_interface)
		arp_list.append(get_priority)
		arp_list.append(get_hello_interval)
		arp_list.append(get_dead_interval)
		arp_list.append(get_auth_type)
		ospf_interface_list_all.append(arp_list)
	# print(arp_list_all)
	return ospf_interface_list_all


# 编辑OSPF接口
def edit_ospf_interface_jyl(browser, ospf_interface="", priority="1", hello_interval="10", dead_interval="40", auth_type="无",
							message_digest_key="", md5_key="", text_key="", save="", cancel=""):
	into_fun(browser, OSPF)
	# 点击接口
	browser.find_element_by_xpath('//*[@id="tabs"]/li[4]/a/span').click()
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != ospf_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a/img').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="priority"]').clear()
	# 输入优先级
	browser.find_element_by_xpath('//*[@id="priority"]').send_keys(priority)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="interval"]').clear()
	# 输入hello interval
	browser.find_element_by_xpath('//*[@id="interval"]').send_keys(hello_interval)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="deadtime"]').clear()
	# 输入dead interval
	browser.find_element_by_xpath('//*[@id="deadtime"]').send_keys(dead_interval)
	# 选认证类型
	s1 = Select(browser.find_element_by_xpath('//*[@id="auth_type"]'))
	# 选认证类型下拉框内容
	s1.select_by_visible_text(auth_type)
	if auth_type == "md5":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="md5-digest-key"]').clear()
		# 输入消息摘要值
		browser.find_element_by_xpath('//*[@id="md5-digest-key"]').send_keys(message_digest_key)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="md5"]').clear()
		# 输入md5
		browser.find_element_by_xpath('//*[@id="md5"]').send_keys(md5_key)
	if auth_type == "简单密码":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="authentication-key"]').clear()
		# 输入text
		browser.find_element_by_xpath('//*[@id="authentication-key"]').send_keys(text_key)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()