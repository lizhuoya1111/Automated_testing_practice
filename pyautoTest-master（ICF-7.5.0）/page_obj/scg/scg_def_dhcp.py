"""
函数一览：

"""
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *


# 添加DHCP服务器
def dhcp_server_add_jyl(browser, interface="",dhcp_type="dhcp_server", dhcp_gw="192.165.12.1", dhcp_sm="255.255.255.0",
						dns_server1="",wins_server1="", ip_range1_1="", ip_range1_2="", ip_range2_1="", ip_range2_2="",
						ip_range3_1="", ip_range3_2="", lease_time_day="7", lease_time_hours="", lease_time_second="",
                        senior="no", dns_server2="", wins_server2="", dns_server3="", wins_server3="", dns_server4="",
						wins_server4="", domain_name="", static_ip_add1="", static_mac_add1="", static_ip="",
						static_ip_add_num="", static_ip_add2="", static_mac_add2="", static_ip_add3="",
						static_mac_add3="", dhcp_rely_server1="", dhcp_rely_server2="", dhcp_rely_server3=""):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	# 选interface下拉框
	time.sleep(1)
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选interface下拉框内容
	time.sleep(1)
	s1.select_by_visible_text(interface)
	time.sleep(1)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	if dhcp_type == "dhcp_server":
		time.sleep(2)
		# 点击dhcp_server
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 输入dhcp网关
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(dhcp_gw)
		# 输入dhcp子网掩码
		browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
		# 输入dhcp DNS服务器1
		browser.find_element_by_xpath('//*[@id="dnsserver1"]').send_keys(dns_server1)
		# 输入dhcp WINS服务器1
		browser.find_element_by_xpath('//*[@id="winsserver1"]').send_keys(wins_server1)
		# 输入dhcp ip地址范围1
		browser.find_element_by_xpath('//*[@id="ipfrom1"]').send_keys(ip_range1_1)
		browser.find_element_by_xpath('//*[@id="ipto1"]').send_keys(ip_range1_2)
		# 输入dhcp ip地址范围2
		browser.find_element_by_xpath('//*[@id="ipfrom2"]').send_keys(ip_range2_1)
		browser.find_element_by_xpath('//*[@id="ipto2"]').send_keys(ip_range2_2)
		# 输入dhcp ip地址范围3
		browser.find_element_by_xpath('//*[@id="ipfrom3"]').send_keys(ip_range3_1)
		browser.find_element_by_xpath('//*[@id="ipto3"]').send_keys(ip_range3_2)

		# 输入dhcp 租约时间
		browser.find_element_by_xpath('//*[@id="day"]').clear()
		browser.find_element_by_xpath('//*[@id="day"]').send_keys(lease_time_day)
		browser.find_element_by_xpath('//*[@id="hour"]').send_keys(lease_time_hours)
		browser.find_element_by_xpath('//*[@id="minute"]').send_keys(lease_time_second)
		if senior == "yes":
			# 点击高级
			browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()
			# 输入dhcp DNS服务器2
			browser.find_element_by_xpath('//*[@id="dnsserver2"]').send_keys(dns_server2)
			# 输入dhcp WINS服务器2
			browser.find_element_by_xpath('//*[@id="winsserver2"]').send_keys(wins_server2)
			# 输入dhcp DNS服务器3
			browser.find_element_by_xpath('//*[@id="dnsserver3"]').send_keys(dns_server3)
			# 输入dhcp WINS服务器3
			browser.find_element_by_xpath('//*[@id="winsserver3"]').send_keys(wins_server3)
			# 输入dhcp DNS服务器4
			browser.find_element_by_xpath('//*[@id="dnsserver4"]').send_keys(dns_server4)
			# 输入dhcp WINS服务器4
			browser.find_element_by_xpath('//*[@id="winsserver4"]').send_keys(wins_server4)
			# 输入dhcp 域名
			browser.find_element_by_xpath('//*[@id="domainname"]').send_keys(domain_name)
			# 输入静态ip地址
			browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add1)
			# 输入静态mac地址
			browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add1)

			if static_ip == "add":
				if static_ip_add_num == "1":
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add2)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add2)
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				elif static_ip_add_num == "2":
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add2)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add2)
					# 点击增加
					browser.find_element_by_xpath('//*[@id="add_staticip_link"]').click()
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add3)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add3)
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					time.sleep(0.5)
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				else:
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			elif static_ip == "delete":
				# 点击删除
				browser.find_element_by_xpath('//*[@id="del_staticip_link"]').click()
				# 点击保存
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
				# 点击返回
				time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			else:
				# 点击保存
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
				# 点击返回
				time.sleep(0.5)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()

		else:
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			# 点击启用
			browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			# 点击返回,延时不可修改
			time.sleep(2)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()

	elif dhcp_type == "dhcp_rely":
		# 点击dhcp_rely
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 输入dhcp_rely服务器1
		browser.find_element_by_xpath('//*[@id="relay_server1"]').send_keys(dhcp_rely_server1)
		# 输入dhcp_rely服务器2
		browser.find_element_by_xpath('//*[@id="relay_server2"]').send_keys(dhcp_rely_server2)
		# 输入dhcp_rely服务器3
		browser.find_element_by_xpath('//*[@id="relay_server3"]').send_keys(dhcp_rely_server3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击启用
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
	else:
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击启用
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="link_but"]').click()


# DHCP服务器编辑或者删除
def dhcp_server_edit_or_delete_jyl(browser, fuction="", dhcp_type="", dhcp_gw="", dhcp_sm="", dns_server1="",wins_server1="",ip_range1_1="", ip_range1_2="", ip_range2_1="",ip_range2_2="",
                    ip_range3_1="", ip_range3_2="",lease_time_day="", lease_time_hours="", lease_time_second="",senior="",dns_server2="",wins_server2="" ,dns_server3="",wins_server3="",
                    dns_server4="", wins_server4="", domain_name="", static_ip_add1="",static_mac_add1="",static_ip_add2="",static_mac_add2="",static_ip_add3="",static_mac_add3="",
                    dhcp_rely_server1="", dhcp_rely_server2="", dhcp_rely_server3=""):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	time.sleep(2)
	if fuction == "edit":
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img').click()
		if dhcp_type == "server":
			# 点击dhcp_server
			browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
			if dhcp_gw == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="gateway"]').clear()
				# 输入dhcp网关
				browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(dhcp_gw)
			if dhcp_sm == "":
				print(1)

			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="netmask"]').clear()
				# 输入dhcp子网掩码
				browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
			if dns_server1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="netmask"]').clear()
				# 输入dhcp子网掩码
				browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
			if wins_server1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="winsserver1"]').clear()
				# 输入dhcp DNS服务器1
				browser.find_element_by_xpath('//*[@id="winsserver1"]').send_keys(dns_server1)
			if ip_range1_1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom1"]').clear()
				# 输入dhcp ip地址范围1_1
				browser.find_element_by_xpath('//*[@id="ipfrom1"]').send_keys(ip_range1_1)
			if ip_range1_2 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto1"]').clear()
				# 输入dhcp ip地址范围1_2
				browser.find_element_by_xpath('//*[@id="ipto1"]').send_keys(ip_range1_2)
			if ip_range2_1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom2"]').clear()
				# 输入dhcp ip地址范围2_1
				browser.find_element_by_xpath('//*[@id="ipfrom2"]').send_keys(ip_range2_1)
			if ip_range2_2 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto2"]').clear()
				# 输入dhcp ip地址范围2_2
				browser.find_element_by_xpath('//*[@id="ipto2"]').send_keys(ip_range2_2)
			if ip_range3_1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom3"]').clear()
				# 输入dhcp ip地址范围3_1
				browser.find_element_by_xpath('//*[@id="ipfrom3"]').send_keys(ip_range3_1)
			if ip_range3_2 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto3"]').clear()
				# 输入dhcp ip地址范围2_2
				browser.find_element_by_xpath('//*[@id="ipto3"]').send_keys(ip_range3_2)
			if lease_time_day == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="day"]').clear()
				# 输入租约时间天
				browser.find_element_by_xpath('//*[@id="day"]').send_keys(lease_time_day)
			if lease_time_hours == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="hour"]').clear()
				# 输入租约时间时
				browser.find_element_by_xpath('//*[@id="hour"]').send_keys(lease_time_hours)
			if lease_time_second == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="minute"]').clear()
				# 输入租约时间秒
				browser.find_element_by_xpath('//*[@id="minute"]').send_keys(lease_time_second)
			if senior == "":
				print(1)
			else:
				# 点击高级
				browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()
				if dns_server2 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver2"]').clear()
					# 输入dhcp DNS服务器2
					browser.find_element_by_xpath('//*[@id="dnsserver2"]').send_keys(dns_server2)
				if wins_server2 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver2"]').clear()
					# 输入dhcp WINS服务器2
					browser.find_element_by_xpath('//*[@id="winsserver2"]').send_keys(wins_server2)
				if dns_server3 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver3"]').clear()
					# 输入dhcp DNS服务器3
					browser.find_element_by_xpath('//*[@id="dnsserver3"]').send_keys(dns_server3)
				if wins_server3 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver3"]').clear()
					# 输入dhcp WINS服务器3
					browser.find_element_by_xpath('//*[@id="winsserver3"]').send_keys(wins_server3)
				if dns_server4 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver4"]').clear()
					# 输入dhcp DNS服务器4
					browser.find_element_by_xpath('//*[@id="dnsserver4"]').send_keys(dns_server4)
				if wins_server4 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver4"]').clear()
					# 输入dhcp WINS服务器4
					browser.find_element_by_xpath('//*[@id="winsserver4"]').send_keys(wins_server4)
				if domain_name == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="domainname"]').clear()
					# 输入dhcp 域名
					browser.find_element_by_xpath('//*[@id="domainname"]').send_keys(domain_name)

				if static_ip_add1 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip0"]').clear()
					# 输入静态ip地址1
					browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add1)
				if static_mac_add1 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac0"]').clear()
					# 输入静态mac地址1
					browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add1)
				if static_ip_add2 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip1"]').clear()
					# 输入静态ip地址2
					browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add2)
				if static_mac_add2 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac1"]').clear()
					# 输入静态mac地址2
					browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add2)
				if static_ip_add3 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip2"]').clear()
					# 输入静态ip地址3
					browser.find_element_by_xpath('//*[@id="ip2"]').send_keys(static_ip_add3)
				if static_mac_add3 == "":
					print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac2"]').clear()
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac2"]').send_keys(static_mac_add3)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		elif dhcp_type == "rely":
			# 点击dhcp_rely
			browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
			if dhcp_rely_server1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server1"]').clear()
				# 输入dhcp_rely服务器1
				browser.find_element_by_xpath('//*[@id="relay_server1"]').send_keys(dhcp_rely_server1)
			if dhcp_rely_server2 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server2"]').clear()
				# 输入dhcp_rely服务器2
				browser.find_element_by_xpath('//*[@id="relay_server2"]').send_keys(dhcp_rely_server2)
			if dhcp_rely_server3 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server3"]').clear()
				# 输入dhcp_rely服务器3
				browser.find_element_by_xpath('//*[@id="relay_server3"]').send_keys(dhcp_rely_server3)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
		else:
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
	else:
		# 获取页面配置数
		num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		i = 0
		while i < int(num):
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				time.sleep(1)
				# 点击关闭启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				# 点击返回
				time.sleep(2)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击删除
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
				time.sleep(2)
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(2)
				i += 1
			else:
				# 点击删除
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
				time.sleep(2)
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(2)
				i += 1


# 添加DHCP服务器或者DHCP中继服务器
def add_dhcp_server_or_realy_jyl(browser, interface=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()


# DHCP服务器添加
def dhcp_server_add(browser, interface="ge0/5",
                    dhcp_type="dhcp_server", dhcp_gw="192.165.12.1", dhcp_sm="255.255.255.0",
                    dns_server1="", wins_server1="", ip_range1_1="", ip_range1_2="",
                    ip_range2_1="", ip_range2_2="", ip_range3_1="", ip_range3_2="",
                    lease_time_day="7", lease_time_hours="", lease_time_second="",
                    senior="no", dns_server2="", wins_server2="", dns_server3="", wins_server3="", dns_server4="",
                    wins_server4="", domain_name="", static_ip_add1="", static_mac_add1="",
                    static_ip="", static_ip_add_num="", static_ip_add2="", static_mac_add2="", static_ip_add3="",
                    static_mac_add3="", dhcp_rely_server1="", dhcp_rely_server2="", dhcp_rely_server3=""):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	time.sleep(1)
	# 选interface下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选interface下拉框内容
	s1.select_by_visible_text(interface)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	if dhcp_type == "dhcp_server":
		# 点击dhcp_server
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 输入dhcp网关
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(dhcp_gw)
		# 输入dhcp子网掩码
		browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
		# 输入dhcp DNS服务器1
		browser.find_element_by_xpath('//*[@id="dnsserver1"]').send_keys(dns_server1)
		# 输入dhcp WINS服务器1
		browser.find_element_by_xpath('//*[@id="winsserver1"]').send_keys(wins_server1)
		# 输入dhcp ip地址范围1
		browser.find_element_by_xpath('//*[@id="ipfrom1"]').send_keys(ip_range1_1)
		browser.find_element_by_xpath('//*[@id="ipto1"]').send_keys(ip_range1_2)
		# 输入dhcp ip地址范围2
		browser.find_element_by_xpath('//*[@id="ipfrom2"]').send_keys(ip_range2_1)
		browser.find_element_by_xpath('//*[@id="ipto2"]').send_keys(ip_range2_2)
		# 输入dhcp ip地址范围3
		browser.find_element_by_xpath('//*[@id="ipfrom3"]').send_keys(ip_range3_1)
		browser.find_element_by_xpath('//*[@id="ipto3"]').send_keys(ip_range3_2)

		# 输入dhcp 租约时间
		browser.find_element_by_xpath('//*[@id="day"]').clear()
		browser.find_element_by_xpath('//*[@id="day"]').send_keys(lease_time_day)
		browser.find_element_by_xpath('//*[@id="hour"]').send_keys(lease_time_hours)
		browser.find_element_by_xpath('//*[@id="minute"]').send_keys(lease_time_second)
		if senior == "yes":
			# 点击高级
			browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()
			# 输入dhcp DNS服务器2
			browser.find_element_by_xpath('//*[@id="dnsserver2"]').send_keys(dns_server2)
			# 输入dhcp WINS服务器2
			browser.find_element_by_xpath('//*[@id="winsserver2"]').send_keys(wins_server2)
			# 输入dhcp DNS服务器3
			browser.find_element_by_xpath('//*[@id="dnsserver3"]').send_keys(dns_server3)
			# 输入dhcp WINS服务器3
			browser.find_element_by_xpath('//*[@id="winsserver3"]').send_keys(wins_server3)
			# 输入dhcp DNS服务器4
			browser.find_element_by_xpath('//*[@id="dnsserver4"]').send_keys(dns_server4)
			# 输入dhcp WINS服务器4
			browser.find_element_by_xpath('//*[@id="winsserver4"]').send_keys(wins_server4)
			# 输入dhcp 域名
			browser.find_element_by_xpath('//*[@id="domainname"]').send_keys(domain_name)
			# 输入静态ip地址
			browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add1)
			# 输入静态mac地址
			browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add1)

			if static_ip == "add":
				if static_ip_add_num == "1":
					# 点击增加
					browser.find_element_by_xpath('//*[@id="add_staticip_link"]').click()
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add2)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add2)
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				elif static_ip_add_num == "2":
					# 点击增加
					browser.find_element_by_xpath('//*[@id="add_staticip_link"]').click()
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add2)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add2)
					# 点击增加
					browser.find_element_by_xpath('//*[@id="add_staticip_link"]').click()
					# 输入静态ip地址
					browser.find_element_by_xpath('//*[@id="ip2"]').send_keys(static_ip_add3)
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac2"]').send_keys(static_mac_add3)
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				else:
					# 点击保存
					browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
					# 点击返回
					browser.find_element_by_xpath('//*[@id="link_but"]').click()
					# 点击启用
					browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			elif static_ip == "delete":
				# 点击删除
				browser.find_element_by_xpath('//*[@id="del_staticip_link"]').click()
				# 点击保存
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			else:
				# 点击保存
				browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()

		else:
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			# 点击启用
			browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
			# 点击返回
			time.sleep(1)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()

	elif dhcp_type == "dhcp_rely":
		# 点击dhcp_rely
		browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
		# 输入dhcp_rely服务器1
		browser.find_element_by_xpath('//*[@id="relay_server1"]').send_keys(dhcp_rely_server1)
		# 输入dhcp_rely服务器2
		browser.find_element_by_xpath('//*[@id="relay_server2"]').send_keys(dhcp_rely_server2)
		# 输入dhcp_rely服务器3
		browser.find_element_by_xpath('//*[@id="relay_server3"]').send_keys(dhcp_rely_server3)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击启用
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
	else:
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击启用
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()


# DHCP服务器编辑或者删除
def dhcp_server_edit_or_delete(browser, fuction="",
                               dhcp_type="", dhcp_gw="", dhcp_sm="", dns_server1="", wins_server1="", ip_range1_1="",
                               ip_range1_2="", ip_range2_1="", ip_range2_2="", ip_range3_1="", ip_range3_2="",
                               lease_time_day="", lease_time_hours="", lease_time_second="", senior="", dns_server2="",
                               wins_server2="", dns_server3="", wins_server3="", dns_server4="", wins_server4="",
                               domain_name="", static_ip_add1="", static_mac_add1="", static_ip_add2="",
                               static_mac_add2="", static_ip_add3="", static_mac_add3="", dhcp_rely_server1="",
                               dhcp_rely_server2="", dhcp_rely_server3=""):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	time.sleep(2)
	if fuction == "edit":
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img').click()
		if dhcp_type == "server":
			# 点击dhcp_server
			browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
			if dhcp_gw == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="gateway"]').clear()
				# 输入dhcp网关
				browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(dhcp_gw)
			if dhcp_sm == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="netmask"]').clear()
				# 输入dhcp子网掩码
				browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
			if dns_server1 == "":
				print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="netmask"]').clear()
				# 输入dhcp子网掩码
				browser.find_element_by_xpath('//*[@id="netmask"]').send_keys(dhcp_sm)
			if wins_server1 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="winsserver1"]').clear()
				# 输入dhcp DNS服务器1
				browser.find_element_by_xpath('//*[@id="winsserver1"]').send_keys(dns_server1)
			if ip_range1_1 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom1"]').clear()
				# 输入dhcp ip地址范围1_1
				browser.find_element_by_xpath('//*[@id="ipfrom1"]').send_keys(ip_range1_1)
			if ip_range1_2 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto1"]').clear()
				# 输入dhcp ip地址范围1_2
				browser.find_element_by_xpath('//*[@id="ipto1"]').send_keys(ip_range1_2)
			if ip_range2_1 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom2"]').clear()
				# 输入dhcp ip地址范围2_1
				browser.find_element_by_xpath('//*[@id="ipfrom2"]').send_keys(ip_range2_1)
			if ip_range2_2 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto2"]').clear()
				# 输入dhcp ip地址范围2_2
				browser.find_element_by_xpath('//*[@id="ipto2"]').send_keys(ip_range2_2)
			if ip_range3_1 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipfrom3"]').clear()
				# 输入dhcp ip地址范围3_1
				browser.find_element_by_xpath('//*[@id="ipfrom3"]').send_keys(ip_range3_1)
			if ip_range3_2 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="ipto3"]').clear()
				# 输入dhcp ip地址范围2_2
				browser.find_element_by_xpath('//*[@id="ipto3"]').send_keys(ip_range3_2)
			if lease_time_day == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="day"]').clear()
				# 输入租约时间天
				browser.find_element_by_xpath('//*[@id="day"]').send_keys(lease_time_day)
			if lease_time_hours == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="hour"]').clear()
				# 输入租约时间时
				browser.find_element_by_xpath('//*[@id="hour"]').send_keys(lease_time_hours)
			if lease_time_second == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="minute"]').clear()
				# 输入租约时间秒
				browser.find_element_by_xpath('//*[@id="minute"]').send_keys(lease_time_second)
			if senior == "":
				pass
				# print(1)
			else:
				# 点击高级
				browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()
				if dns_server2 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver2"]').clear()
					# 输入dhcp DNS服务器2
					browser.find_element_by_xpath('//*[@id="dnsserver2"]').send_keys(dns_server2)
				if wins_server2 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver2"]').clear()
					# 输入dhcp WINS服务器2
					browser.find_element_by_xpath('//*[@id="winsserver2"]').send_keys(wins_server2)
				if dns_server3 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver3"]').clear()
					# 输入dhcp DNS服务器3
					browser.find_element_by_xpath('//*[@id="dnsserver3"]').send_keys(dns_server3)
				if wins_server3 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver3"]').clear()
					# 输入dhcp WINS服务器3
					browser.find_element_by_xpath('//*[@id="winsserver3"]').send_keys(wins_server3)
				if dns_server4 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="dnsserver4"]').clear()
					# 输入dhcp DNS服务器4
					browser.find_element_by_xpath('//*[@id="dnsserver4"]').send_keys(dns_server4)
				if wins_server4 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="winsserver4"]').clear()
					# 输入dhcp WINS服务器4
					browser.find_element_by_xpath('//*[@id="winsserver4"]').send_keys(wins_server4)
				if domain_name == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="domainname"]').clear()
					# 输入dhcp 域名
					browser.find_element_by_xpath('//*[@id="domainname"]').send_keys(domain_name)

				if static_ip_add1 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip0"]').clear()
					# 输入静态ip地址1
					browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip_add1)
				if static_mac_add1 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac0"]').clear()
					# 输入静态mac地址1
					browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac_add1)
				if static_ip_add2 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip1"]').clear()
					# 输入静态ip地址2
					browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add2)
				if static_mac_add2 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac1"]').clear()
					# 输入静态mac地址2
					browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add2)
				if static_ip_add3 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="ip2"]').clear()
					# 输入静态ip地址3
					browser.find_element_by_xpath('//*[@id="ip2"]').send_keys(static_ip_add3)
				if static_mac_add3 == "":
					pass
					# print(1)
				else:
					# 清除默认输入
					browser.find_element_by_xpath('//*[@id="mac2"]').clear()
					# 输入静态mac地址
					browser.find_element_by_xpath('//*[@id="mac2"]').send_keys(static_mac_add3)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				pass
				# print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		elif dhcp_type == "rely":
			# 点击dhcp_rely
			browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
			if dhcp_rely_server1 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server1"]').clear()
				# 输入dhcp_rely服务器1
				browser.find_element_by_xpath('//*[@id="relay_server1"]').send_keys(dhcp_rely_server1)
			if dhcp_rely_server2 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server2"]').clear()
				# 输入dhcp_rely服务器2
				browser.find_element_by_xpath('//*[@id="relay_server2"]').send_keys(dhcp_rely_server2)
			if dhcp_rely_server3 == "":
				pass
				# print(1)
			else:
				# 清除默认输入
				browser.find_element_by_xpath('//*[@id="relay_server3"]').clear()
				# 输入dhcp_rely服务器3
				browser.find_element_by_xpath('//*[@id="relay_server3"]').send_keys(dhcp_rely_server3)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				pass
				# print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
		else:
			browser.find_element_by_xpath('//*[@id="work_mode_2"]').click()
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				pass
				# print(1)
			else:
				# 点击启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
	else:
		# 获取页面配置数
		num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
		i = 0
		while i < int(num):
			enable = browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').is_selected()
			if enable is True:
				time.sleep(1)
				# 点击关闭启用
				browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
				# 点击返回
				time.sleep(1)
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				# 点击删除
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
				time.sleep(2)
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(2)
				i += 1
			else:
				# 点击删除
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img').click()
				time.sleep(2)
				# 点击返回
				browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(2)
				i += 1


# 进入DHCP租用列表
def dhcp_renting_list_jyl(browser):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp租用列表
	# browser.find_element_by_xpath(DHCP租用列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP租用列表)


# 物理接口从dhcp_server获取IP之后，从新获取、释放、刷新IP地址
def dhcp_client_obtain_ip_dhcp_static(browser, interface="", dhcp_static=""):
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
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
	# print(getname)
	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/a').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()
	if dhcp_static == "release":
		# 点击释放
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(1)
	if dhcp_static == "renew":
		# 点击重新获取
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[2]').click()
		time.sleep(1)
	if dhcp_static == "refesh":
		# 点击刷新
		browser.find_element_by_xpath('//*[@id="dhcpclient_con_div"]/a').click()
		time.sleep(1)
	if dhcp_static == "new_obtain":
		# 重新获取新的IP
		browser.find_element_by_xpath('//*[@id="dhcpclient_button_div"]/a[1]').click()
		time.sleep(1)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 进入dhcp server高级界面
def get_into_dhcp_server(browser, interface=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	time.sleep(0.5)
	getname.lstrip()
	# print(getname)
	# print(interface)
	while getname != interface:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
	time.sleep(1)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")
	browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()


# 进入dhcp 租约界面高级界面
def get_into_dhcp_lease(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP租用列表).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP租用列表)


# 进入dhcp设定界面，不任何操作
def get_into_dhcp_set(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(网络).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[text()="DHCP"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(DHCP).click()
	# # 点击dhcp设定
	# browser.find_element_by_xpath(DHCP设定).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DHCP设定)
