"""
2018年10月18日 15:23:36

函数一览：
	add_net_ineterface
		添加物理接口的ip地址

	change_addrmod_physical_inte
		修改物理接口的地址模式

	get_interface_dhcp_status
		获取接口的DHCP的状态

	del_inteface_ipadd
		删除接口的ip地址

"""
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 接口添加IP地址
def add_net_ineterface(browser, ipadd, netmask, interface_name):

	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	#
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	# # 展开接口设置
	# #browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 12):

		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]/a').text

		if inte_name == interface_name:

			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[9]/a').click()

			break

	# 点击物理接口1配置   //*[@id="table"]/tbody/tr[2]/td[9]/a   //*[@id="table"]/tbody/tr[3]/td[9]/a
	# browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+ str(interSeq + 1) +']/td[9]/a').click()

	# 输入IPadd
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ipadd)

	# 输入netmask
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(netmask)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	# 刷新一下网页，解决元素找不到的问题
	browser.refresh()


# 改变物理接口的地址模式
def change_addrmod_physical_inte(browser, interface_name, mod_trpe=''):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	# # 展开接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 用于定位本次编辑的接口序号，方便再次找到该接口
	# interSeq_global = 0
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 12):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]/a').text

		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[9]/a').click()
			# 记住本次接口的序号，用于之后的删除定位
			# global interSeq_global
			# interSeq_global = interSeq
			break
	# 判断要将接口修改为什么地址模式
	# 静态模式
	if mod_trpe == "静态":
		browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
		# 判断是否存在静态ip地址
		if not is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[1]'):
			# 下面有个输入ip地址再删除的过程，因为不能在没有地址情况直接保存静态地址模式
			browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys('111.111.111.111')
			browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
			browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys('255.255.255.255')
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
			print("输入ip地址wait删除的过程done")
			time.sleep(7)
			# 延时7秒，删除刚刚添加的地址
			browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input').click()
			print("删除done")
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		else:
			# 点击保存
			print("有IP，直接保存")
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	elif mod_trpe == "DHCP":
		# 判断存不存在静态ip地址,如果有，删光了 //*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]
		while is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[1]'):
			print("存在ip")
			browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input').click()
			time.sleep(2)
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		time.sleep(7)
		# 点击DHCP地址模式
		browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		time.sleep(6)
		# 判断DHCP是断开状态时，点击一下重新获取
		if browser.find_element_by_xpath('//*[@id="dhcp_status"]').text == "断开":
			browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[2]').click()
	#elif mod_trpe == "PPPoE":


# 添加网桥
def add_br(browser, snat="no", allowping="yes", block_br="no", stp="no", mem_inte="", desc="miaoshu"):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络 '//*[@id="menu"]/div[2]/header/a'
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
	# 获得网桥总数，用于定位网桥
	br_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# 点击添加网桥
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(desc)
	# snat开关
	if snat == "yes":

		if not(browser.find_element_by_xpath('//*[@id="snat"]').is_selected()):

			browser.find_element_by_xpath('//*[@id="snat"]').click()

	if snat == "no":

		if browser.find_element_by_xpath('//*[@id="snat"]').is_selected():

			browser.find_element_by_xpath('//*[@id="snat"]').click()

	# ping开关
	if allowping == "yes":

		if not (browser.find_element_by_xpath('//*[@id="ping"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="ping"]').click()

	if allowping == "no":

		if browser.find_element_by_xpath('//*[@id="ping"]').is_selected():
			browser.find_element_by_xpath('//*[@id="ping"]').click()

	# 桥内通讯开关
	if block_br == "yes":

		if not (browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()

	if block_br == "no":

		if browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected():
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()

	# stp开关
	if stp == "yes":

		if not (browser.find_element_by_xpath('//*[@id="stp"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="stp"]').click()

	if stp == "no":

		if browser.find_element_by_xpath('//*[@id="stp"]').is_selected():
			browser.find_element_by_xpath('//*[@id="stp"]').click()


	# 当传入的参数-桥成员接口的数量大于1时，开始添加br接口操作
	if len(mem_inte) >= 1:

		for x in mem_inte:

			br_se = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))

			br_se.select_by_visible_text(x)

			browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()


	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 删除所有的网桥
def del_br_all(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	# # 展开接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(网桥).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)
	time.sleep(1)
	br_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text

	while int(br_num) > 1:
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[2]').click()
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		br_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text


# 编辑网桥
def edit_br(browser, br_name, ipadd, netmask, snat="no", allowping="yes", block_br="no",
			stp="no", add_mode="static", mem_inte="", desc="miaoshu"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# # 点击网络 '//*[@id="menu"]/div[2]/header/a'
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(网桥).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	#
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 网桥)

	# 获得网桥总数，用于定位网桥
	br_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text

	# 当获取到的网桥个数为1时，说明只有一个br0，所以直接编辑网桥1
	if br_sum == "1":

		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img').click()

	else:

		# 放置获取到br名字
		br_list = []

		# 按传入的参数-网桥名，对界面接口名轮询，得到xpath编号，然后定位到该桥接口的编辑按钮进行点击
		for interSeq in range(2, int(br_sum) + 2):

			inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]').text

			# 去掉网桥名字符串末尾的空格
			inte_name = inte_name.rstrip()

			br_list.append(inte_name)

			print(br_list)

			if inte_name == br_name:

				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[7]/a[1]').click()

				break

		if br_name not in br_list:

			print("没有这个网桥，后期添加弹出错误")

	# 描述
	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(desc)

	# ipadd
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ipadd)

	# mask
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(netmask)

	# snat开关
	if snat == "yes":

		if not(browser.find_element_by_xpath('//*[@id="snat"]').is_selected()):

			browser.find_element_by_xpath('//*[@id="snat"]').click()

	if snat == "no":

		if browser.find_element_by_xpath('//*[@id="snat"]').is_selected():

			browser.find_element_by_xpath('//*[@id="snat"]').click()

	# ping开关
	if allowping == "yes":

		if not (browser.find_element_by_xpath('//*[@id="allow_ping"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="allow_ping"]').click()

	if allowping == "no":

		if browser.find_element_by_xpath('//*[@id="allow_ping"]').is_selected():
			browser.find_element_by_xpath('//*[@id="allow_ping"]').click()

	# 桥内通讯开关
	if block_br == "yes":

		if not (browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()

	if block_br == "no":

		if browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').is_selected():
			browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()

	# stp开关
	if stp == "yes":

		if not (browser.find_element_by_xpath('//*[@id="stp"]').is_selected()):
			browser.find_element_by_xpath('//*[@id="stp"]').click()

	if stp == "no":

		if browser.find_element_by_xpath('//*[@id="stp"]').is_selected():
			browser.find_element_by_xpath('//*[@id="stp"]').click()


	# 当传入的参数-桥成员接口的数量大于1时，开始添加br接口操作
	if len(mem_inte) >= 1:

		for x in mem_inte:

			br_se = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))

			br_se.select_by_visible_text(x)

			browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()


	# 地址模式切换
	if add_mode == "DHCP":

		browser.find_element_by_xpath('//*[@id="address_mode_1"]').click()

		time.sleep(1)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 获取接口的DHCP状态
def get_interface_dhcp_status(browser, interface_name):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	# # 展开接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	# # 点击物理接口   //*[@id="table"]/tbody/tr[2]/td[9]/a/img
	# browser.find_element_by_xpath(物理接口).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 物理接口)
	# 用于定位本次编辑的接口序号，方便再次找到该接口
	# interSeq_global = 0
	# 按传入的参数，对界面接口名轮询，等到xpath编号，然后定位到该接口的编辑按钮进行点击
	for interSeq in range(2, 12):
		inte_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[2]/a').text

		if inte_name == interface_name:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(interSeq) + ']/td[9]/a').click()
			# 记住本次接口的序号，用于之后的删除定位
			# global interSeq_global
			# interSeq_global = interSeq
			break
	# 判断如果是dhcp模式，点击停止，然后提取DHCP状态
	if browser.find_element_by_xpath('//*[@id="address_mode_1"]').is_selected():
		if is_element_exist(browser, '//*[@id="dhcpclient_button_div"]/a[1]'):
			browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
			browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
			time.sleep(7)
			dhcp_info = browser.find_element_by_xpath('//*[@id="dhcp_status"]').text
			return dhcp_info


# 打开或关闭某接口的allow ping 功能
def open_physical_interface_allowping_wxw(browser,interface='ge0/4',allow_ping="open/close"):

	"""打开或关闭某接口的allow ping 功能"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
	#     # 如果不可见，点击加号，展开元素
	#     time.sleep(1)
	#     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
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
	print(allowping)
	if allow_ping == "open":
		if allowping == True:
			print("allow ping已打开")
		else:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
	if allow_ping == "close":
		if allowping == True:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="ping"]').click()
			print("allow ping已关闭")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	# # 把打开的网络合上
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# browser.find_element_by_xpath(接口设置).click()


# 改变物理接口的工作模式
def change_physical_interface_workmode_wxw(browser, interface="",
										   route="yes", ip='', mask='',
										   trans='no'):

	"""改变物理接口的工作模式"""
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(网络).click()
	# # 点击接口设置
	# # browser.find_element_by_xpath(接口设置).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="接口设置"]/../ul').is_displayed():
	#     # 如果不可见，点击加号，展开元素
	#     browser.find_element_by_xpath(接口设置).click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
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

	if route == "yes":
		# 若模式为透明模式，则转换成路由模式
		if not browser.find_element_by_xpath('//*[@id="work_mode_0"]').is_selected():
			# 如果路由没有被选中，点击路由
			browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
			alert = browser.switch_to_alert()
			alert.accept()
		time.sleep(0.5)
		# 点击静态
		browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
		# 输入ip
		browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
		# 保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

	if trans == 'yes':
		# 若模式为路由模式，则转换成透明模式
		if not browser.find_element_by_xpath('//*[@id="work_mode_1"]').is_selected():
			# 判断是否是路由,若有则删除
			browser.implicitly_wait(1)
			# 判断是否存在IP地址
			have = is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[2]')
			print(have)
			while have is True:
				browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input').click()
				time.sleep(0.5)
				have = is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[2]')

		# 点击透明
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 接受告警
		alert = browser.switch_to_alert()
		alert.accept()
		time.sleep(1)
		alert = browser.switch_to_alert()
		alert.accept()


		# 点击保存
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()


# 给物理接口添加一个ip
def add_physical_interface_ip_wxw(browser, interface='ge0/4', ip='', mask='24'):

	"""给物理接口添加一个ip"""
	# # 切换到默认frame
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
	#     # 如果不可见，点击加号，展开元素
	#     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
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
	# 按名字查找
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
	# 添加ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
	browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# print("ip添加完成")


# 给物理接口删除指定ip
def delete_physical_interface_ip_wxw(browser, interface='ge0/4', ip=''):

	"""给物理接口删除指定ip"""
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
	#     # 如果不可见，点击加号，展开元素
	#     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
	#
	# # 点击物理接口
	# browser.find_element_by_xpath(物理接口).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# 定位到内容frame
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

	# 按ip查找
	n = 2
	getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text

	while getip != ip:
		n = n + 1
		getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text

	# 点击删除
	browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[4]/input').click()

	# 保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

