from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_ifname_OEM import *


# 接口添加ipv6地址
def add_ipv6_add_jyl(browser, physical_interface="", ipv6_add="", ipv6_mask="", add="yes"):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 点击ipv6
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 输入ipv6地址
	browser.find_element_by_xpath('//*[@id="ipv6_addr"]').send_keys(ipv6_add)
	# 输入ipv6掩码
	browser.find_element_by_xpath('//*[@id="ipv6_prefix"]').send_keys(ipv6_mask)
	if add == "yes":
		# 点击增加ipv6地址
		browser.find_element_by_xpath('//*[@id="add_ipaddress_link"]').click()


# 接口删除ipv6地址
def delete_ipv6_add_jyl(browser, physical_interface="", interface_add=""):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 点击ipv6
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	n = 2
	# 获取接口地址
	getname = browser.find_element_by_xpath(' //*[@id="ipaddress"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != interface_add:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(n) + ']/td[3]/input').click()


# 查询所添加的ip地址，返回查询的ip地址
def get_interface_ipvv6_add_all_jyl(browser, physical_interface="", interface_add=""):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 点击ipv6
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	n = 2
	# 获取接口地址
	getname = browser.find_element_by_xpath(' //*[@id="ipaddress"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != interface_add:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	return getname


# 编辑ipv6邻居发现
def edit_neighbor_discovery_jyl(browser, physical_interface="", retransmission_time="", base_reachable_time="",
								duolicate_add_retry_count="", save="", canel=""):
	into_fun(browser, 物理接口)
	n = 2
	# 获取接口名称
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	print(getname)
	while getname != physical_interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	# 点击ipv6
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击展开
	browser.find_element_by_xpath('//*[@id="neigb_toggle_link"]').click()
	# 点击清除默认输入
	browser.find_element_by_xpath('//*[@id="retransinterval"]').clear()
	# 输入重新传输时间
	browser.find_element_by_xpath('//*[@id="retransinterval"]').send_keys(retransmission_time)
	# 点击清除默认输入
	browser.find_element_by_xpath('//*[@id="reachtime"]').clear()
	# 输入基本可达时间
	browser.find_element_by_xpath('//*[@id="reachtime"]').send_keys(base_reachable_time)
	# 点击清除默认输入
	browser.find_element_by_xpath('//*[@id="dadretrycount"]').clear()
	# 输入重复地址检测重试次数
	browser.find_element_by_xpath('//*[@id="dadretrycount"]').send_keys(duolicate_add_retry_count)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[3]').click()
	if canel == "yes":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[4]').click()


# # 获取本地链路地址,返回本地链路地址
# def get_local_link_add(browser, physical_interface=""):
# 	into_fun(browser, 物理接口)
# 	n = 2
# 	# 获取接口名称
# 	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
# 	print(getname)
# 	while getname != physical_interface:
# 		n = n + 1
# 		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
# 		print(getname)
# 	# 点击编辑
# 	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
# 	# 点击ipv6
# 	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
# 	time.sleep(2)
# 	local_link = browser.find_element_by_id('//*[@id="conftr_1"]/td[1]').get_attribute('value')
# 	print(local_link)
# 	return local_link

# 添加ipv6隧道
def add_ipv6_tunnel_lzy(browser, name="", unnumbered="yes/no", interface="", fixed_ip="yes/no", ip="",
						six_to_four_tunnel="yes/no", manual_tunnel="yes/no", destination_ip="",
						MTU="1480", save="yes/no", cancel="yes/no"):
	into_fun(browser, IPv6隧道)
	sleep(0.2)
	# 点击添加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	sleep(0.2)
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
	sleep(0.3)
	# 本地地址设置
	if unnumbered == 'yes':
		browser.find_element_by_xpath('//*[@id="localip_cfg_0"]').click()
		# 选interface下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="localip_inf"]'))
		# 选interface下拉框内容
		s1.select_by_visible_text(interface)
	if fixed_ip == 'yes':
		browser.find_element_by_xpath('//*[@id="localip_cfg_1"]').click()
		# 选interface下拉框
		s2 = Select(browser.find_element_by_xpath('//*[@id="fixip_value"]'))
		# 选interface下拉框内容
		s2.select_by_visible_text(ip)
	sleep(0.2)
	# 远程ip设置
	if six_to_four_tunnel == 'yes':
		browser.find_element_by_xpath('//*[@id="remoteip_cfg_0"]').click()
	if manual_tunnel == 'yes':
		browser.find_element_by_xpath('//*[@id="remoteip_cfg_1"]').click()
		browser.find_element_by_xpath('//*[@id="destip"]').send_keys(destination_ip)
	sleep(0.2)

	# 设置MTU
	browser.find_element_by_xpath('//*[@id="mtu"]').clear()
	browser.find_element_by_xpath('//*[@id="mtu"]').send_keys(MTU)
	sleep(0.2)

	# 保存
	if save == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel == 'yes':
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

# 删除ipv6隧道（按名称）
def delete_ipv6_tunnel_by_name_lzy(browser, name=""):
	into_fun(browser, IPv6隧道)
	sleep(0.2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text
	# print(getname)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[6]/a[2]/img').click()


# 编辑ipv6隧道（按名称） 只进入到编辑界面
def edit_ipv6_tunnel_by_name_lzy(browser, name=""):
	into_fun(browser, IPv6隧道)
	sleep(0.2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text
	# print(getname)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]/a[1]/img').click()







# 删除ipv6隧道（全部）

















