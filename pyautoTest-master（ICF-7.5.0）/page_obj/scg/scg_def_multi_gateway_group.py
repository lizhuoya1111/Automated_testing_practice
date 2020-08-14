import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *


# 判断多网关组是否存在，若存在返回True,反之返回False
def is_multi_gateway_group_exist_wxw(browser, name=''):

	"""判断多网关组是否存在，若存在返回True,反之返回False"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	into_fun(browser, 多网关组)
	time.sleep(1)
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:" + group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		# print(x)
		browser.implicitly_wait(1)
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath(
					'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath(
						'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[3]/a').text
					# print(name_info)
					if name_info == name:
						# print("找到该网关组")
						return True
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return False


# 获取多网关组（还不太明白）
def get_multi_gateway_group_dict(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:"+group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		gr_name = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gr)+']/td/a/span').text
		gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gate_stat)+']/td[2]').text
				# print(status)
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				s = x_gr + 1

				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# 写入字典
				dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return dict_group


# 通过名字删除多网关组
def del_multi_gateway_group_byname(browser, name):
	"""
	通过网关名称，删除多网关列表
	:param browser:
	:param name:
	:return: 成功返回OK
	"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:"+group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		# gr_name = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gr)+']/td/a/span').text
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gate_stat)+']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gate_stat)+']/td[3]/a').text
					# print(name_info)
					# print(name)
					# print(name_info == name)
					if name_info == name:
						time.sleep(1)
						browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr['+str(x_gate_stat)+']/td[9]/a[2]').click()
						# //*[@id="route_maintenance_multigw_table"]/tbody/tr[7]/td[9]/a[2]/img
						# print("hahahahahaha1111")
						# print("删除成功")
						# print("hahahahahaha2222")
						return "OK"
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break


# 删除所有的多网关组
def del_multi_gateway_group_all(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 时间不可调整
	time.sleep(0.5)
	gr_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	while True:
		if int(gr_sum) > 0:
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[3]/td[9]/a[2]/img').click()
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			time.sleep(0.5)
			gr_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		else:
			# print("删除完成")
			return "OK"


# 编辑多网关组
def edit_multi_gateway_group_wxw(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
								device='ge0/3', gateway='24.1.1.7', ping_server='34.1.1.4', ping='yes/no', arp='yes/no',
								time_switch='7', ub="100000", db="100000"):

	"""编辑多网关组"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:" + group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath(
					'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath(
						'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[3]/a').text
					# print(name_info)
					if name_info == name:
						# 点击编辑
						browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[9]/a[1]').click()

						# 修改网关组
						# 找下拉框
						s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
						# 找下拉框的内容
						s1.select_by_visible_text(group)

						if modify == "yes":
							# 点击更改
							browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
							# 输入别名
							browser.find_element_by_xpath('//*[@id="alias"]').clear()
							browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
							# 点击保存
							browser.find_element_by_xpath(
								'//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
							# 点击返回
							browser.find_element_by_xpath('//*[@id="link_but"]').click()

						# 选择设备
						s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
						# 找下拉框的内容
						s1.select_by_visible_text(device)
						# 选择网关
						time.sleep(2)
						browser.find_element_by_xpath('//*[@id="gateway"]').clear()
						browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
						# 选择ping服务器
						browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
						browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

						if ping == 'yes':
							browser.find_element_by_xpath('//*[@id="detectmethod_ping"]').click()
							print('探测方式已为ping')
						if arp == 'yes':
							browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
						# 切换时间
						browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
						browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
						# 上传带宽
						browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
						browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
						# 下载带宽
						browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
						browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)
						# 点击保存
						browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()
						return True
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return None


# 获取多网关组的网关
def get_multi_gateway_group_gateway_wxw(browser, name=''):

	"""获取多网关组的网关"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:" + group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath(
					'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath(
						'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[3]/a').text
					# print(name_info)
					if name_info == name:
						# 获取网关组的设备
						device = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[5]').text.replace(' ', '')
						# print(device)
						return device
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return False


# 添加多网关组
def add_multi_gateway_group_wxw(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
								device=' ', gateway=' ', ping_server=' ', ping='yes/no', arp='yes/no',
								time_switch='7', ub="100000", db="100000"):

	""""添加多网关组"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# time.sleep(1)
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	time.sleep(0.5)
	# 点击增加，如果点击“增加”按钮报错，则最多尝试10次，5秒之内完成判断。
	add_button_try_max = 0
	while add_button_try_max < 10:
		try:
			browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
			break
		except:
			add_button_try_max += 1
			time.sleep(0.5)
	# 输入名称
	browser.find_element_by_xpath('//*[@id="gateway_name"]').send_keys(name)
	# 选择网关组
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(group)

	if modify == "yes":
		# 点击更改
		browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
		# 输入别名
		browser.find_element_by_xpath('//*[@id="alias"]').clear()
		browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

	# 选择设备
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(device)
	# 选择网关
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	# 选择ping服务器
	browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

	if ping == 'yes':
		pass
		# print('探测方式已为ping')
	if arp == 'yes':
		browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
	# 切换时间
	browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
	browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
	# 上传带宽
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
	# 下载带宽
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)
	time.sleep(0.5)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(0.5)


# 获取多网关组的状态
def get_multi_gateway_status_gateway_wxw(browser, name=''):

	"""获取多网关组的网关"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 搞一个字典，保存一下网关组和其中网关的数量
	# dict_group = {}
	group_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print("组的总数:" + group_sum)
	# 这个变量用于定位网关组的名字
	x_gr = 2
	# 这个变量用于定位网关的状态
	x_gate_stat = 3
	# 外层循环是网关组循环
	for x in range(0, int(group_sum)):
		browser.implicitly_wait(1)
		# gr_id = gr_name[0]
		# 获取每个网关组中的网关数量
		gate_num = 0
		# 内层循环是一个网关组内网关循环
		for y in range(0, 9):
			try:
				status = browser.find_element_by_xpath(
					'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.rstrip()
				# print(status)
				if status == "up" or status == "down":
					name_info = browser.find_element_by_xpath(
						'//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[3]/a').text
					# print(name_info)
					if name_info == name:
						# 获取网关组的状态
						device = browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[' + str(x_gate_stat) + ']/td[2]').text.replace(' ', '')
						# print(device)
						return device
				gate_num += 1
				x_gate_stat += 1
			except:
				x_gate_stat = x_gate_stat + 1
				x_gr = x_gr + gate_num + 1
				# s = x_gr + 1
				# print("下个循环的XpathID："+str(x_gate_stat))
				# print("下个循环的组的XpathID：" + str(x_gr))
				# print(s)
				# # 写入字典
				# dict_group[gr_id] = gate_num
				# print(dict_group)
				break
	return False


# 添加多网关组(只到保存前)
def add_multi_gateway_group_wxw_before_save_wxw(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
								device=interface_name_3, gateway='24.1.1.7', ping_server='34.1.1.4', ping='yes/no', arp='yes/no',
								time_switch='7', ub="100000", db="100000"):

	""""添加多网关组(只到保存前)"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# time.sleep(2)
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="gateway_name"]').send_keys(name)
	# 选择网关组
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(group)

	if modify == "yes":
		# 点击更改
		browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
		# 输入别名
		browser.find_element_by_xpath('//*[@id="alias"]').clear()
		browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

	# 选择设备
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(device)
	# 选择网关
	time.sleep(2)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	# 选择ping服务器
	browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

	if ping == 'yes':
		pass
		# print('探测方式已为ping')
	if arp == 'yes':
		browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
	# 切换时间
	browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
	browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
	# 上传带宽
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
	# 下载带宽
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)


# 添加多网关组 用于输入不规范导致弹出警告框的情况  并返回告警信息
def return_alert_when_add_multi_gateway_group(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
								device=' ', gateway=' ', ping_server=' ', ping='yes/no', arp='yes/no',
								time_switch='7', ub="100000", db="100000"):

	""""添加多网关组"""
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击路由
	# browser.find_element_by_xpath(路由).click()
	# # 点击多网关组
	# browser.find_element_by_xpath(多网关组).click()
	# time.sleep(1)
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 多网关组)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	time.sleep(0.5)
	# 输入名称
	browser.find_element_by_xpath('//*[@id="gateway_name"]').send_keys(name)
	# 选择网关组
	# 找下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(group)

	if modify == "yes":
		# 点击更改
		browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
		# 输入别名
		browser.find_element_by_xpath('//*[@id="alias"]').clear()
		browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

	# 选择设备
	s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(device)
	# 选择网关
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	# 选择ping服务器
	browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

	if ping == 'yes':
		pass
		# print('探测方式已为ping')
	if arp == 'yes':
		browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
	# 切换时间
	browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
	browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
	# 上传带宽
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
	# 下载带宽
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
	browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(1)

	# 获取告警框信息
	alert = browser.switch_to_alert().text
	print(alert)
	browser.switch_to_alert().accept()
	return alert
