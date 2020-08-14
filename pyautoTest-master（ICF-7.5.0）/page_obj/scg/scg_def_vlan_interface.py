from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 添加子接口
def vlan_add_jyl(browser, physicl_interface="", vlan_id="", work_mode="", snat="", allow_ping="", describe=""):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="port"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(physicl_interface)
	# 输入vlan_id
	browser.find_element_by_xpath('//*[@id="vlanid"]').send_keys(vlan_id)
	if work_mode == "route":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
	else:
		# 点击透明
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
	if snat == "yes":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="snat"]').click()
	if allow_ping == "no":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="allowping"]').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(describe)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 通过子接口名称查询子接口是否存在，如果存在，返回Ture
def find_vlan_interface_byname(browser, interface_name):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("子接口数量：" + str(vlan_num))
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 2 + int(vlan_num)):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]').text.rstrip()
		# print(inte_name)
		if inte_name == interface_name:
			return True


# 设置接口的交换模式
def set_switchmode(hostip1, interface, mode="trunk"):
	shell = Shell_SSH()
	shell.connect(hostip=hostip1)
	shell.execute("en")
	shell.execute("conf t")
	shell.execute("inte gigabitethernet "+interface)
	shell.execute("switchmode "+mode)
	shell.close()


# 查询接口的接口模式，并返回模式字符串
def query_switchmode(hostip1, interface):
	shell = Shell_SSH()
	shell.connect(hostip=hostip1)
	shell.execute("en")
	shell.execute("show interface gigabitethernet "+interface)
	shell_info = shell.output()
	if "TRUNK" in shell_info:
		return "Trunk"
	if "ACCESS" in shell_info:
		return "access"
	shell.close()


# 获得子接口的描述信息
def get_vlan_interface_desc(browser, interface_name):
	desc = "NA"
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("子接口数量："+str(vlan_num))
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 2 + int(vlan_num)):
		inte_name = browser.find_element_by_xpath(
			'//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]').text.rstrip()
		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[8]/a[1]').click()
			desc = browser.find_element_by_xpath('//*[@id="desc"]').get_attribute('value')
			# print(desc)
			break
	return desc


# 删除子接口
def vlan_delete_jyl(browser):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/a[2]/img').click()


# 添加子接口,并选择子接口的工作模式
def add_vlan_inte(browser, physicl_interface="", vlan_id="", work_mode="route/transprent", snat="", allow_ping="yes", describe="", check_workmode="yes"):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 判断物理接口的工作模式，如果是透明模式需要修改为路由
	if get_physical_interface_workmode(browser, interface=physicl_interface) == "透明" and check_workmode == "yes":
		# print(physicl_interface)
		transparent_interface_change_physics_interface_lzy(browser, intefacex=physicl_interface)
	into_fun(browser, 子接口)
	# 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击增加
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="port"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(physicl_interface)
	# 输入vlan_id
	browser.find_element_by_xpath('//*[@id="vlanid"]').send_keys(vlan_id)
	if work_mode == "route":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
	else:
		# 点击透明
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
	if snat == "yes":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="snat"]').click()
	if allow_ping == "no":
		# 点击路由
		browser.find_element_by_xpath('//*[@id="allowping"]').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(describe)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加路由模式下子接口的IP地址
def add_vlan_inte_add(browser, interface_name, ipadd, mask):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("子接口数量："+str(vlan_num))
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 2+int(vlan_num)):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[2]').text.rstrip()
		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[8]/a[1]').click()
			browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ipadd)
			browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
			browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
			break


# 删除路由模式下子接口的IP地址
def del_vlan_inte_add(browser, interface_name, ipadd):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("子接口数量："+str(vlan_num))
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 2+int(vlan_num)):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[2]').text.rstrip()
		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[8]/a[1]').click()
			m = 2
			getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[2]').text

			while getip != ipadd:
				m = m + 1
				getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[2]').text
			# 点击删除
			browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(m) + ']/td[4]/input').click()
			break


# 删除子接口-通过名字
def del_vlan_inte_by_name(browser, interface_name):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("子接口数量："+str(vlan_num))
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 2+int(vlan_num)):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[2]').text.rstrip()
		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(interSeq)+']/td[8]/a[2]').click()
			# print(inte_name+"删除完成")
			break


# 删除全部子接口
def del_vlan_inte_all(browser):
	# browser.refresh()
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 获得子接口数量
	time.sleep(1)
	vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text

	while int(vlan_num) > 0:
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/a[2]').click()
		time.sleep(1)
		vlan_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text


# 子接口从dhcp服务器获取IP地址
def vlan_interface_from_dhcp_obtain_ip_jyl(browser, vlan_interface="", description="", work_mode="dhcp",
                                           dhcp_status1="", dhcp_status2="", dhcp_status3="",
                                           update_default_gateway="", update_system_dns="", snat="", allow_ping=""):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
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
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	time.sleep(2)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(3)
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(3)
	if dhcp_status2 == "stop":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()
	if dhcp_status2 != "stop":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()


# 子接口从dhcp服务器获取IP地址
def vlan_interface_obtain_ip_from_dhcp_jyl(browser, vlan_interface="", description="", work_mode="dhcp"):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	time.sleep(2)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)


# 子接口从dhcp服务器获取IP地址之后，dhcp  ip 状态
def vlan_interface_obtain_ip_dhcp_status_jyl(browser, vlan_interface="", dhcp_status1="", dhcp_status2="", dhcp_status3="", ):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	n = 2
	# 获取接口名称
	time.sleep(5)
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	time.sleep(1)
	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	time.sleep(5)
	if dhcp_status1 == "release_recapture":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()
	if dhcp_status2 == "stop":
		# 点击停止
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(2)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()
	if dhcp_status3 == "refresh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(5)
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[4]').click()


# 子接口从dhcp更新dhcp
def vlan_interface_update_dhcp_jyl(browser, vlan_interface="", description="", update_default_gateway="", update_system_dns="", snat="", allow_ping=""):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
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
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	time.sleep(2)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(5)


# 子接口获取IP地址从dhcp服务器
def vlan_interface_obtain_ip_fromdhcp1_jyl(browser, vlan_interface="", description="", work_mode="dhcp"):
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
	# browser.find_element_by_xpath(子接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	# 输入描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(description)
	# 点击dhcp
	browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
	time.sleep(2)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()
	time.sleep(2)


# 开启/关闭子接口的SNAT
def switch_vlan_interface_snat(browser, vlan_interface='', snat="open/close"):
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(子接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 子接口)
	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()

	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text.rstrip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()

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
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 开启/关闭子接口的allow_ping
def switch_vlan_interface_allow_ping(browser, vlan_interface='', allow_ping="open/close"):
	into_fun(browser, 子接口)

	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()

	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text.rstrip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()

	# 确认allow ping是否打开
	allowping = browser.find_element_by_xpath('//*[@id="snat"]').is_selected()
	# print(allowping)
	if allow_ping == "open":
		if allowping is True:
			print("snat已打开")
		else:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
	if allow_ping == "close":
		if allowping is True:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="snat"]').click()
			print("snat已关闭")
	# 点击保存
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()


# 进入子接口界面，不做任何操作
def get_into_vlan_interface_(browser, vlan_interface=''):
	into_fun(browser, 子接口)

	# 点击编辑
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()

	while getname != vlan_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text.rstrip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()


# 获取vlan子接口总条目数,返回int型
def get_count_number_vlan_lzy(browser):
	into_fun(browser, menu=子接口)
	sleep(2)
	# 获取总条目
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)

# 命令行添加子接口vlan（空）
def cli_add_vlan_lzy(devname=dev1, username="admin", password="admin@139", port=22, interface="", num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("interface vlan "+interface+"."+str(x))
		time.sleep(0.2)
		scg.execute("exit")
		time.sleep(0.2)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)



# 命令行删除子接口vlan（空） 需判断是否删除干净
def cli_delete_vlan_lzy(devname=dev1, username="admin", password="admin@139", port=22, interface="", num1=1, num2=2):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("no interface vlan "+interface+"."+str(x))
		time.sleep(0.5)
	time.sleep(2)
	scg.close()
	output = scg.output()
	print(output)

# 命令行给子接口VLAN添加ip(num1到num2为子接口编号）(添加254个子接口以内适用）
def cli_add_vlan_ip_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2,  num11=1, num22=2, num111=1, num222=2, interface='', ip='40.', mask='32'):
	scg = Shell_SSH()
	scg.connect(hostip=devname, name=username, passwd=password, po=port)
	scg.execute("en")
	scg.execute("con t")
	for x in range(num1, num2):
		scg.execute("interface vlan "+interface+"."+str(x))
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