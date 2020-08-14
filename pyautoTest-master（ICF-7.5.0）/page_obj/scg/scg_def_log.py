from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 获取日志
def get_log(browser, log_type):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# time.sleep(5)
	# if not browser.find_element_by_xpath('//*[text()="日志记录"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志记录).click()
	# browser.find_element_by_xpath(log_type).click()
	# time.sleep(3)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, log_type)
	max1 = 0
	while True:
		if log_type == 管理日志:
			time.sleep(1)
			info_x = browser.find_element_by_xpath('//*[@id="log_record_admin_table"]/tbody/tr[2]/td[1]').text
			if info_x == "1":
				loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
				return loginfo

			elif max1 > 10:
				return "界面加载失败"
			else:
				time.sleep(2)
				max1 += 1
		elif log_type == 系统日志:
			time.sleep(1)
			info_x = browser.find_element_by_xpath('//*[@id="log_record_system_table"]/tbody/tr[2]/td[1]').text
			if info_x == "1":
				loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
				return loginfo

			elif max1 > 10:
				return "界面加载失败"
			else:
				time.sleep(2)
				max1 += 1
		elif log_type == 安全日志:
			time.sleep(1)
			info_x = browser.find_element_by_xpath('//*[@id="log_record_security_table"]/tbody/tr[2]/td[1]').text
			if info_x == "1":
				loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
				return loginfo

			elif max1 > 10:
				return "界面加载失败"
			else:
				time.sleep(2)
				max1 += 1
		elif log_type == 流量日志:
			time.sleep(1)
			info_x = browser.find_element_by_xpath('//*[@id="log_record_traffic_table"]/tbody/tr[2]/td[1]').text
			if info_x == "1":
				loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
				return loginfo

			elif max1 > 10:
				return "界面加载失败"
			else:
				time.sleep(2)
				max1 += 1


# 获取日志，默认每次获取一条，可设置每次获取多条
def get_log_info(browser, log_type, num=1):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath(display_日志记录).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志记录).click()
	# browser.find_element_by_xpath(log_type).click()
	# time.sleep(2)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content") //*[@id="log_record_security_table"]/tbody/tr[2]/td[1]
	into_fun(browser, log_type)
	max1 = 0
	logsum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	while True:
		if log_type == 管理日志:
			info_x = browser.find_element_by_xpath('//*[@id="log_record_admin_table"]/tbody/tr[2]/td[1]').text
		elif log_type == 系统日志:
			info_x = browser.find_element_by_xpath('//*[@id="log_record_system_table"]/tbody/tr[2]/td[1]').text
		elif log_type == 安全日志:
			info_x = browser.find_element_by_xpath('//*[@id="log_record_security_table"]/tbody/tr[2]/td[1]').text
		else:
			info_x = browser.find_element_by_xpath('//*[@id="log_record_traffic_table"]/tbody/tr[2]/td[1]').text
		if info_x == "1":
			if num == 1:
				loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
				# 刷新界面，为了保证不被其他函数错误获取当前日志条目数
				browser.refresh()
				return loginfo
			# 如果num >=1时，获取多条日志
			else:
				if int(logsum) > int(num):
					loginfo = ""
					for j in range(0, num):
						loginfo1 = browser.find_element_by_xpath('//*[@id="namearea'+str(j)+'"]').text
						loginfo = str(loginfo) + "\n" + str(loginfo1)
					return loginfo
				else:
					loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
					return loginfo

		elif max1 > 10:
			browser.refresh()
			return "界面加载失败"

		else:
			time.sleep(1)
			max1 += 1


# 获取批量删除两个条目的日志
def get_log_info_for_batch_dele2_wxw(browser, log_type):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# # 判断日志记录的加号是否存在
	# if not browser.find_element_by_xpath('//*[text()="日志记录"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志记录).click()
	# browser.find_element_by_xpath(log_type).click()
	# time.sleep(3)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, log_type)
	max1 = 0
	while True:
		info_x = browser.find_element_by_xpath('//*[@id="log_record_admin_table"]/tbody/tr[2]/td[1]').text
		if info_x == "1":
			loginfo = browser.find_element_by_xpath('//*[@id="namearea1"]').text
			return loginfo

		elif max1 > 10:
			return "界面加载失败"

		else:
			time.sleep(2)
			max1 += 1


# 开启/关闭  Log Switch-Log 会话表查询过滤
def switch_log(browser, dns="yes/no", icmp="yes/no", packet_without_match="yes/no", invalid="yes/no"):
	browser.refresh()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath(display_日志设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# browser.find_element_by_xpath(日志服务器).click()
	# # time.sleep(3)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	dns_flag = browser.find_element_by_xpath('//*[@id="dns"]').is_selected()
	icmp_flag = browser.find_element_by_xpath('//*[@id="icmp"]').is_selected()
	without_match_flag = browser.find_element_by_xpath('//*[@id="packet_without_match"]').is_selected()
	invalid_flag = browser.find_element_by_xpath('//*[@id="invalid_log_switch"]').is_selected()
	if dns == "yes":
		if dns_flag:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="dns"]').click()
	elif dns == "no":
		if dns_flag:
			browser.find_element_by_xpath('//*[@id="dns"]').click()
		else:
			pass

	if icmp == "yes":
		if icmp_flag:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="icmp"]').click()
	elif icmp == "no":
		if icmp_flag:
			browser.find_element_by_xpath('//*[@id="icmp"]').click()
		else:
			pass

	if packet_without_match == "yes":
		if without_match_flag:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="packet_without_match"]').click()
	elif packet_without_match == "no":
		if without_match_flag:
			browser.find_element_by_xpath('//*[@id="packet_without_match"]').click()
		else:
			pass

	if invalid == "yes":
		if invalid_flag:
			pass
		else:
			browser.find_element_by_xpath('//*[@id="invalid_log_switch"]').click()
	elif invalid == "no":
		if invalid_flag:
			browser.find_element_by_xpath('//*[@id="invalid_log_switch"]').click()
		else:
			pass
	browser.find_element_by_xpath('//*[@id="for_note"]/form/table/tbody/tr[1]/td[1]/input[2]').click()


# 查询会话表查询过滤是否被打开，传入要查询的的表项名称（dns\icmp\packet_without_match\invalid）,返回True\False
def switch_log_get_station(browser, form="dns\icmp\packet_without_match\invalid"):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath(display_日志设置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# browser.find_element_by_xpath(日志服务器).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	if form == "dns":
		if browser.find_element_by_xpath('//*[@id="dns"]').is_selected() is True:
			return True
		else:
			return False

	if form == "icmp":
		if browser.find_element_by_xpath('//*[@id="icmp"]').is_selected() is True:
			return True
		else:
			return False

	if form == "packet_without_match":
		if browser.find_element_by_xpath('//*[@id="packet_without_match"]').is_selected() is True:
			return True
		else:
			return False

	if form == "invalid":
		if browser.find_element_by_xpath('//*[@id="invalid_log_switch"]').is_selected() is True:
			return True
		else:
			return False
	browser.find_element_by_xpath('//*[@id="for_note"]/form/table/tbody/tr[1]/td[1]/input[2]').click()


# 删除日志服务器
def delete_log_server_jyl(browser, log_server=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
	# print(getname)
	while getname != log_server:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
		# print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[9]/a[2]/img').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 增加日志服务器最后点取消
def add_log_server_jyl(browser, status="", server_name="", ip="", port="", format="", protocol="", charset="",
					   save="yes"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
	if status == "enable":
		# 点击启用
		browser.find_element_by_xpath('//*[@id="status"]').click()
	elif status == "disenable":
		# 点击禁用
		browser.find_element_by_xpath('//*[@id="status"]').click()
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="servername"]').send_keys(server_name)
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 输入端口
	browser.find_element_by_xpath('//*[@id="ports"]').send_keys(port)
	# 选格式下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="format"]'))
	# 选格式下拉框内容
	s1.select_by_visible_text(format)
	# 选协议下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
	# 选协议下拉框内容
	s1.select_by_visible_text(protocol)
	# 选字符集下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="charset"]'))
	# 选字符集下拉框内容
	s1.select_by_visible_text(charset)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	elif save == "no":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 编辑日志服务器
def edit_log_server_jyl(browser, log_server="", status="", ip="", port="", format="", protocol="", charset=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	time.sleep(2)
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
	print(getname)
	while getname != log_server:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
		print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()
	if status == "enable":
		# 点击启用
		browser.find_element_by_xpath('//*[@id="status"]').click()
	elif status == "disenable":
		# 点击禁用
		browser.find_element_by_xpath('//*[@id="status"]').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	# 输入IP
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="ports"]').clear()
	# 输入端口
	browser.find_element_by_xpath('//*[@id="ports"]').send_keys(port)
	# 选格式下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="format_tcp"]'))
	# 选格式下拉框内容
	s1.select_by_visible_text(format)
	# 选协议下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
	# 选协议下拉框内容
	s1.select_by_visible_text(protocol)
	# 选字符集下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="charset"]'))
	# 选字符集下拉框内容
	s1.select_by_visible_text(charset)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑admin本地日志服务器
def edit_log_localdb_admin_jyl(browser, admin="500000", admin_num="10"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[2]/td[9]/a[1]/img').click()

	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="maxitem_0"]').clear()
	# 输入最大数
	browser.find_element_by_xpath('//*[@id="maxitem_0"]').send_keys(admin)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="delpolicy_0"]').clear()
	# 输入删除百分比
	browser.find_element_by_xpath('//*[@id="delpolicy_0"]').send_keys(admin_num)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑system本地日志服务器
def edit_log_localdb_system_jyl(browser, system="200000", system_num="10"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[2]/td[9]/a[1]/img').click()

	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="maxitem_1"]').clear()
	# 输入最大数
	browser.find_element_by_xpath('//*[@id="maxitem_1"]').send_keys(system)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="delpolicy_1"]').clear()
	# 输入删除百分比
	browser.find_element_by_xpath('//*[@id="delpolicy_1"]').send_keys(system_num)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑security本地日志服务器
def edit_log_localdb_security(browser,  security="100000", security_num="10"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[2]/td[9]/a[1]/img').click()

	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="maxitem_2"]').clear()
	# 输入最大数
	browser.find_element_by_xpath('//*[@id="maxitem_2"]').send_keys(security)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="delpolicy_2"]').clear()
	# 输入删除百分比
	browser.find_element_by_xpath('//*[@id="delpolicy_2"]').send_keys(security_num)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/table/tbody/tr[4]/td[4]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑traffic本地日志服务器
def edit_log_localdb_traffic_jyl(browser, traffic="800000", traffic_num="50"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志服务器).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志服务器)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[2]/td[9]/a[1]/img').click()

	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="maxitem_3"]').clear()
	# 输入最大数
	browser.find_element_by_xpath('//*[@id="maxitem_3"]').send_keys(traffic)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="delpolicy_3"]').clear()
	# 输入删除百分比
	browser.find_element_by_xpath('//*[@id="delpolicy_3"]').send_keys(traffic_num)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[1]/table/tbody/tr[5]/td[4]/input').click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 编辑日志过滤,参数index是页面的序列号,no_level=关闭levevl
def edit_log_filter(browser, index="", level="all/[debug,info,notice,warning,error,critical,emerg,alert]", no_level="no"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击网络
	# browser.find_element_by_xpath(日志).click()
	# if not browser.find_element_by_xpath('//*[text()="日志设置"]/../ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志设置).click()
	# # 点击日志服务器
	# browser.find_element_by_xpath(日志过滤).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 日志过滤)
	browser.find_element_by_xpath('//*[@id="log_setting_filter_table"]/tbody/tr['+str(int(index)+1)+']/td[6]/a/img').click()
	if level == "全部":
		flag1 = browser.find_element_by_xpath('//*[@id="level_0"]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="level_0"]').click()
			# print("111111")
			time.sleep(2)
	else:
		flag1 = browser.find_element_by_xpath('//*[@id="level_0"]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="level_0"]').click()
		n1 = 0
		for x in level:
			# print("00000000")
			# rr = browser.find_element_by_xpath('//*[text()="Notice"]').text
			# print(rr)
			# print("11111111")
			flag2 = browser.find_element_by_xpath('//*[text()="' + x.capitalize() + '"]/input').is_selected()
			if flag2 is False:
				browser.find_element_by_xpath('//*[text()="' + x.capitalize() + '"]/input').click()
			n1 += 1

	if no_level != "no":
		if no_level == "全部":
			flag1 = browser.find_element_by_xpath('//*[@id="level_0"]').is_selected()
			if flag1 is True:
				browser.find_element_by_xpath('//*[@id="level_0"]').click()
		else:
			flag1 = browser.find_element_by_xpath('//*[@id="level_0"]').is_selected()
			if flag1 is True:
				browser.find_element_by_xpath('//*[@id="level_0"]').click()
			n2 = 0
			for x in no_level:
				flag2 = browser.find_element_by_xpath('//*[text()="' + x.capitalize() + '"]/input').is_selected()
				if flag2 is True:
					browser.find_element_by_xpath('//*[text()="' + x.capitalize() + '"]/input').click()
				n2 += 1

	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 删除日志 清除日志
def delete_log(browser, log_type):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# time.sleep(5)
	# if not browser.find_element_by_xpath(display_日志记录).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志记录).click()
	# browser.find_element_by_xpath(log_type).click()
	# time.sleep(3)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, log_type)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	browser.switch_to_alert().accept()
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 进入到XX日志记录界面
def get_into_logging(browser, log_type):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(日志).click()
	# time.sleep(5)
	# if not browser.find_element_by_xpath(display_日志记录).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(日志记录).click()
	# browser.find_element_by_xpath(log_type).click()
	# time.sleep(3)
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, log_type)


# 添加日志警告服务器
def add_email_alarm_jyl(browser, enable="", email_name="", email_add="", cc_email="",
					cc_email_add="", format="", project="", project_content="", time="", time_num="",
					disk_full="yes", admin_event="", av_vrius_found="", ips="", server_monitor="",
					save="", cancel=""):
	into_fun(browser, 日志告警)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	if enable == "yes":
		browser.find_element_by_xpath('//*[@id="enable"]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(email_name)
	# 输入发送邮件地址
	browser.find_element_by_xpath('//*[@id="email1"]').send_keys(email_add)
	if cc_email == "yes":
		# 输入发送邮件地址
		browser.find_element_by_xpath('//*[@id="email2"]').send_keys(cc_email_add)
	# 选择格式
	s1 = Select(browser.find_element_by_xpath('//*[@id="format"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text(format)
	if project == "yes":
		browser.find_element_by_xpath('//*[@id="items_0"]').click()
		browser.find_element_by_xpath('//*[@id="items_input"]').send_keys(project_content)
	if time == "yes":
		browser.find_element_by_xpath('//*[@id="items_1"]').click()
		browser.find_element_by_xpath('//*[@id="time_input"]').send_keys(time_num)
	if disk_full == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[1]').click()
	if admin_event == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[2]').click()
	if av_vrius_found == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[3]').click()
	if ips == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[4]').click()
	if server_monitor == "yes":
		browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[5]').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[3]').click()


# 删除日志告警服务器
def delete_email_alarm_server_jyl(browser, email_alarm=""):
	into_fun(browser, 日志告警)
	n = 2
	time.sleep(1)
	getname = browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != email_alarm:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()


# 增加FTP服务器-日志服务器
def add_ftp_server_jyl(browser, status="", server_name="", ftp_server_name="", path="", user="",
					   password="", format="", project="", project_content="", time="", time_num="",
					   save="", cancel=""):
	into_fun(browser, 日志服务器)
	# 点击增加FTP服务器
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	if status == "enable":
		browser.find_element_by_xpath('//*[@id="status"]').click()
	elif status == "disable":
		browser.find_element_by_xpath('//*[@id="status"]').click()
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="servername"]').send_keys(server_name)
	# 输入服务器名称
	browser.find_element_by_xpath('//*[@id="ftpserver1"]').send_keys(ftp_server_name)
	# 输入路径
	browser.find_element_by_xpath('//*[@id="path"]').send_keys(path)
	# 输入用户
	browser.find_element_by_xpath('//*[@id="user"]').send_keys(user)
	# 输入密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
	# 选择格式
	s1 = Select(browser.find_element_by_xpath('//*[@id="format"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text(format)
	if project == "yes":
		browser.find_element_by_xpath('//*[@id="items_0"]').click()
		# 输入项目
		browser.find_element_by_xpath('//*[@id="items"]').send_keys(project_content)
	if time == "yes":
		browser.find_element_by_xpath('//*[@id="items_1"]').click()
		# 输入时间
		browser.find_element_by_xpath('//*[@id="time"]').send_keys(time_num)
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除FTP服务器
def delete_ftp_server_jyl(browser, ftp_server="ftp_jia_1"):
	into_fun(browser, 日志服务器)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
	# print(getname)
	while getname != ftp_server:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
		# print(getname)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[9]/a[2]/img').click()


# 获取日志服务器信息，根据名字，返回IP、端口、格式、协议、字符集、状态、属性
def get_logserver_info(browser, server_name="LocalDB"):
	into_fun(browser, 日志服务器)
	n = 2
	getname = browser.find_element_by_xpath(
		'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
	# print(getname)
	while getname != server_name:
		n = n + 1
		getname = browser.find_element_by_xpath(
			'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[1]').text.rstrip()
	server_ip = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	server_port = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[3]').text.rstrip()
	server_style = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[4]').text.rstrip()
	server_protocol = browser.find_element_by_xpath('//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[5]').text.rstrip()
	server_code = browser.find_element_by_xpath(
		'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[6]').text.rstrip()
	server_status = browser.find_element_by_xpath(
		'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[7]').text.rstrip()
	server_property = browser.find_element_by_xpath(
		'//*[@id="log_setting_server_table"]/tbody/tr[' + str(n) + ']/td[8]').text.rstrip()
	return server_ip, server_port, server_style, server_protocol, server_code, server_status, server_property

# print(getname)


# 添加smtp服务器
def add_smtp_alarm_jyl(browser,  smtp_server="", server="", user_name="", password="", save="yes"):
	into_fun(browser, 日志告警)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="smtpserver"]').clear()
	# 输入smtp服务器名称
	browser.find_element_by_xpath('//*[@id="smtpserver"]').send_keys(smtp_server)
	if server == "ip":
		browser.find_element_by_xpath('//*[@id="smtp_ip"]').click()
	elif server == "dns":
		browser.find_element_by_xpath('//*[@id="smtp_dns"]').click()
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="user"]').clear()
	# 输入用户名
	browser.find_element_by_xpath('//*[@id="user"]').send_keys(user_name)
	# 输入密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/div/div[2]/div/input[2]').click()


# 编辑邮件服务器-日志告警
def edit_email_alarm_jyl(browser, email_alert="", enable="", email_name="", email_add="",
					cc_email_add="", format="", project_content="", time_num="",
					disk_full="", admin_event="", av_vrius_found="", ips="", server_monitor="",
					save="", cancel=""):
	into_fun(browser, 日志告警)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
	# print(getname)
	while getname != email_alert:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		# print(getname)
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr[' + str(n) + ']/td[7]/a[1]/img').click()
	if enable == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
	elif enable == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="enable"]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="enable"]').click()
	if email_name != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys(email_name)
	if email_add != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="email1"]').clear()
		# 输入发送邮件地址
		browser.find_element_by_xpath('//*[@id="email1"]').send_keys(email_add)
	if cc_email_add != "":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="email2"]').clear()
		# 输入发送邮件地址
		browser.find_element_by_xpath('//*[@id="email2"]').send_keys(cc_email_add)
	if format != "":
		# 选择格式
		s1 = Select(browser.find_element_by_xpath('//*[@id="format"]'))
		# 选择格式下拉框内容
		s1.select_by_visible_text(format)
	if project_content != "":
		browser.find_element_by_xpath('//*[@id="items_0"]').click()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="items_input"]').clear()
		browser.find_element_by_xpath('//*[@id="items_input"]').send_keys(project_content)
	if time_num != "":
		browser.find_element_by_xpath('//*[@id="items_1"]').click()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="time_input"]').clear()
		browser.find_element_by_xpath('//*[@id="time_input"]').send_keys(time_num)
	if disk_full == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[1]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[1]').click()
	elif disk_full == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[1]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[1]').click()
	if admin_event == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[2]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[2]').click()
	elif admin_event == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[2]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[2]').click()
	if av_vrius_found == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[3]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[3]').click()
	elif av_vrius_found == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[3]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[3]').click()
	if ips == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[4]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[4]').click()
	elif ips == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[4]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[4]').click()
	if server_monitor == "yes":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[5]').is_selected()
		if flag1 is False:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[5]').click()
	elif server_monitor == "no":
		flag1 = browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[5]').is_selected()
		if flag1 is True:
			browser.find_element_by_xpath('//*[@id="conftr_8"]/td[2]/input[5]').click()
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[3]').click()


# 获得日志邮件告警中的名称、发往Email地址、类型、通知频率、启用以list形式返回[name, to_email_add, type, interval, enable]
def get_email_alert_all_jyl(browser):
	into_fun(browser, 日志告警)
	time.sleep(1.5)
	email_alert_list_all = []
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	for x1 in range(2, br_sum+2):
		emali_alert_list = []
		get_name = browser.find_element_by_xpath('//*[@id="log_alert_email_table"]/tbody/tr['+str(x1)+']/td[2]').text.rstrip()
		get_to_email_add = browser.find_element_by_xpath(
			'//*[@id="log_alert_email_table"]/tbody/tr[' + str(x1) + ']/td[3]').text.rstrip()
		get_type = browser.find_element_by_xpath(
			'//*[@id="log_alert_email_table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
		get_interval = browser.find_element_by_xpath(
			'//*[@id="log_alert_email_table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
		get_enable = browser.find_element_by_xpath(
			'//*[@id="log_alert_email_table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
		emali_alert_list.append(get_name)
		emali_alert_list.append(get_to_email_add)
		emali_alert_list.append(get_type)
		emali_alert_list.append(get_interval)
		emali_alert_list.append(get_enable)
		email_alert_list_all.append(emali_alert_list)
	# print(arp_list_all)
	return email_alert_list_all


def different_types_of_queries_log_jyl(browser, log_type, modular="", save_name="", save="yes"):
	into_fun(browser, log_type)
	# 点击高级
	browser.find_element_by_xpath('//*[@id="hid"]').click()
	# 将all移动到左侧
	# 选择格式
	s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text("all")
	sleep(0.5)
	browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
	# 选择模块右移
	# 选择格式
	sleep(0.5)
	s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text(modular)
	sleep(1)
	# 点击右移
	browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()
	# 输入保存名称					# //*[@id="advance"]/table/tbody/tr[5]/td[3]/input[1]
	browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[1]').send_keys(save_name)
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[2]').click()


# 删除不同类型所保存的日志
def delete_different_type_save_log_jyl(browser, log_type, reload=""):
	into_fun(browser, log_type)
	# 点击高级
	browser.find_element_by_xpath('//*[@id="hid"]').click()
	# 选择格式
	s1 = Select(browser.find_element_by_xpath('//*[@id="reloadlist"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text(reload)
	time.sleep(1)
	# 点击高级
	browser.find_element_by_xpath('//*[@id="hid"]').click()
	# 选择格式
	s1 = Select(browser.find_element_by_xpath('//*[@id="reloadlist"]'))
	# 选择格式下拉框内容
	s1.select_by_visible_text(reload)
	# 点击删除
	browser.find_element_by_xpath('//*[@id="delete_reloadlist"]').click()


# 修改日志过滤(只修改级别）,参数index是页面的序列号
def edit_log_filter_lzy(browser, index="", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
						warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no"):

	into_fun(browser, 日志过滤)
	browser.find_element_by_xpath('//*[@id="log_setting_filter_table"]/tbody/tr['+str(int(index)+1)+']/td[6]/a/img').click()
	# 如果原状态为all 则先去掉勾选
	enable0 = browser.find_element_by_xpath('//*[@id="level_0"]').is_selected()
	if enable0 == True:
		browser.find_element_by_xpath('//*[@id="level_0"]').click()

	if all == 'yes':
		browser.find_element_by_xpath('//*[@id="level_0"]').click()
	else:

		if debug == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_1"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_1"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_1"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_1"]').click()
			else:
				pass

		if info == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_2"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_2"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_2"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_2"]').click()
			else:
				pass

		if notice == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_3"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_3"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_3"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_3"]').click()
			else:
				pass

		if warning == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_4"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_4"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_4"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_4"]').click()
			else:
				pass

		if error == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_5"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_5"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_5"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_5"]').click()
			else:
				pass

		if critical == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_6"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_6"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_6"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_6"]').click()
			else:
				pass

		if emerg == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_7"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_7"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_7"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_7"]').click()
			else:
				pass

		if alert == 'yes':
			enable = browser.find_element_by_xpath('//*[@id="level_8"]').is_selected()
			if enable == True:
				pass
			else:
				browser.find_element_by_xpath('//*[@id="level_8"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="level_8"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="level_8"]').click()
			else:
				pass


	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 获取日志总数 返回int型（四种类型）
def get_log_counts_lzy(browser, log_type):
	# 进入日志界面
	into_fun(browser, log_type)
	sleep(0.5)
	# 获取总数
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	return int(num1)


# 查询安全/流量日志
def query_security_or_traffic_log_lzy(browser, log_type="", ambiguous_search="",
									  from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="", to_port="",
									  protocol="", exclude_protocol="", start_date="", start_time="", end_date="", end_time=""):
	# 进入管理日志界面
	into_fun(browser, log_type)
	sleep(0.5)
	# 模糊搜索
	browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)

	# 源IP
	browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(from_ip)
	# 排除的源IP
	browser.find_element_by_xpath('//*[@id="no_src_ip"]').send_keys(exclude_from_ip)
	# 目的IP
	browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(to_ip)
	# 排除的目的IP
	browser.find_element_by_xpath('//*[@id="no_dst_ip"]').send_keys(exclude_to_ip)
	# 源端口
	browser.find_element_by_xpath('//*[@id="src_port"]').send_keys(from_port)
	# 目的端口
	browser.find_element_by_xpath('//*[@id="dst_port"]').send_keys(to_port)
	# 协议
	browser.find_element_by_xpath('//*[@id="proto"]').send_keys(protocol)
	# 排除协议
	browser.find_element_by_xpath('//*[@id="no_proto"]').send_keys(exclude_protocol)

	# 开始时间
	browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
	browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
	# 结束时间
	browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
	browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)
	# 点击查询
	sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[4]/td[5]/input[1]').click()


# 查询安全/流量日志--高级
def advanced_query_security_or_traffic_log_lzy(browser, log_type="", advanced="yes/no", ambiguous_search="",
									  from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="", to_port="",
									  protocol="", exclude_protocol="", start_date="", start_time="", end_date="", end_time=""
								 , level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name=""):
	# 进入管理日志界面
	into_fun(browser, log_type)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 源IP
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(from_ip)
		# 排除的源IP
		browser.find_element_by_xpath('//*[@id="no_src_ip"]').send_keys(exclude_from_ip)
		# 目的IP
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(to_ip)
		# 排除的目的IP
		browser.find_element_by_xpath('//*[@id="no_dst_ip"]').send_keys(exclude_to_ip)
		# 源端口
		browser.find_element_by_xpath('//*[@id="src_port"]').send_keys(from_port)
		# 目的端口
		browser.find_element_by_xpath('//*[@id="dst_port"]').send_keys(to_port)
		# 协议
		browser.find_element_by_xpath('//*[@id="proto"]').send_keys(protocol)
		# 排除协议
		browser.find_element_by_xpath('//*[@id="no_proto"]').send_keys(exclude_protocol)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击右移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 点击查询
		sleep(1)
		browser.find_element_by_xpath(
			'//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[4]/td[5]/input[1]').click()


# 查询安全/流量日志--高级--查询结果另存
def advanced_query_save_security_or_traffic_log_lzy(browser, log_type="", advanced="yes/no", ambiguous_search="",
									  from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="", to_port="",
									  protocol="", exclude_protocol="", start_date="", start_time="", end_date="", end_time=""
								 , level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name="",
								save_as="yes/no", save_as_name=""):
	# 进入管理日志界面
	into_fun(browser, log_type)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 源IP
		browser.find_element_by_xpath('//*[@id="src_ip"]').send_keys(from_ip)
		# 排除的源IP
		browser.find_element_by_xpath('//*[@id="no_src_ip"]').send_keys(exclude_from_ip)
		# 目的IP
		browser.find_element_by_xpath('//*[@id="dst_ip"]').send_keys(to_ip)
		# 排除的目的IP
		browser.find_element_by_xpath('//*[@id="no_dst_ip"]').send_keys(exclude_to_ip)
		# 源端口
		browser.find_element_by_xpath('//*[@id="src_port"]').send_keys(from_port)
		# 目的端口
		browser.find_element_by_xpath('//*[@id="dst_port"]').send_keys(to_port)
		# 协议
		browser.find_element_by_xpath('//*[@id="proto"]').send_keys(protocol)
		# 排除协议
		browser.find_element_by_xpath('//*[@id="no_proto"]').send_keys(exclude_protocol)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击右移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 查询结果另存为
		if save_as == 'yes':
			sleep(0.5)
			# 输入名称
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[1]').send_keys(save_as_name)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[2]').click()


# 查询管理日志  日期及时间格式：2019-12-18  00:00:00
def query_admin_log_lzy(browser, administrator="", ambiguous_search="", action="", start_date="", start_time="", end_date="", end_time=""):
	# 进入管理日志界面
	into_fun(browser, 管理日志)
	sleep(0.5)
	# 填入管理员
	browser.find_element_by_xpath('//*[@id="administrator"]').send_keys(administrator)
	# 模糊搜索
	browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
	# 动作
	browser.find_element_by_xpath('//*[@id="action"]').send_keys(action)
	# 开始时间
	browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
	browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
	# 结束时间
	browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
	browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)
	# 点击查询
	sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()


# 查询管理日志--高级 （除了全选只支持单个模块查询）
def advanced_query_admin_log_lzy(browser, advanced="yes/no", administrator="", ambiguous_search="",
								 action="", start_date="", start_time="", end_date="", end_time=""
								 , level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name=""):
	# 进入管理日志界面
	into_fun(browser, 管理日志)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 填入管理员
		browser.find_element_by_xpath('//*[@id="administrator"]').send_keys(administrator)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 动作
		browser.find_element_by_xpath('//*[@id="action"]').send_keys(action)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击左移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 点击查询
		sleep(1)
		browser.find_element_by_xpath(
			'//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()


# 查询管理日志--高级--查询结果另存（除了全选只支持单个模块查询）
def advanced_query_save_admin_log_lzy(browser, advanced="yes/no", administrator="", ambiguous_search="",
								 action="", start_date="", start_time="", end_date="", end_time=""
								 , level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name="",
								save_as="yes/no", save_as_name=""):
	# 进入管理日志界面
	into_fun(browser, 管理日志)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 填入管理员
		browser.find_element_by_xpath('//*[@id="administrator"]').send_keys(administrator)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 动作
		browser.find_element_by_xpath('//*[@id="action"]').send_keys(action)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击左移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 查询结果另存为
		if save_as == 'yes':
			sleep(0.5)
			# 输入名称
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[4]/td[3]/input[1]').send_keys(save_as_name)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[4]/td[3]/input[2]').click()


# 查询四种日志--高级--查询结果另存后, 刷新或者删除查询条件 前提为该查询条件存在
def advanced_query_save_modify_admin_log_lzy(browser, log_type="", refresh="yes/no", refresh_name="", delete="yes/no"):
	# 进入管理日志界面
	into_fun(browser, log_type)
	sleep(0.5)
	# 点击高级
	browser.find_element_by_xpath('//*[@id="hid"]').click()
	sleep(0.5)
	if refresh == 'yes':
		# 选中查询条件
		s1 = Select(browser.find_element_by_xpath('//*[@id="reloadlist"]'))
		s1.select_by_visible_text(refresh_name)
		sleep(1)
		# 如果要删除该查询条件 则需再次点击高级
		if delete == 'yes':
			# 点击高级
			browser.find_element_by_xpath('//*[@id="hid"]').click()
			sleep(0.5)
			# 点击删除
			browser.find_element_by_xpath('//*[@id="delete_reloadlist"]').click()


# 查询系统日志 日期及时间格式：2019-12-18  00:00:00
def query_system_log_lzy(browser, ambiguous_search="", start_date="", start_time="", end_date="", end_time=""):
	# 进入管理日志界面
	into_fun(browser, 系统日志)
	sleep(0.5)
	# 模糊搜索
	browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
	# 开始时间
	browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
	browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
	# 结束时间
	browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
	browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)
	# 点击查询
	sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()


# 查询系统日志--高级 （除了全选只支持单个模块查询）
def advanced_query_system_log_lzy(browser, advanced="yes/no", ambiguous_search="",
								 start_date="", start_time="", end_date="", end_time=""
								 , level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name=""):
	# 进入管理日志界面
	into_fun(browser, 系统日志)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击左移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 点击查询
		sleep(1)
		browser.find_element_by_xpath(
			'//*[@id="container"]/div[1]/div[1]/div[2]/div/form/table/tbody/tr[2]/td[5]/input[1]').click()


# 查询系统日志--高级--查询结果另存 （除了全选只支持单个模块查询）
def advanced_query_save_system_log_lzy(browser, advanced="yes/no",  ambiguous_search="",
									   start_date="", start_time="", end_date="", end_time="" ,
									   level="change/unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change/unchange", modul_name="",
								save_as="yes/no", save_as_name=""):
	# 进入管理日志界面
	into_fun(browser, 系统日志)
	sleep(0.5)
	if advanced == 'yes':
		# 点击高级
		browser.find_element_by_xpath('//*[@id="hid"]').click()
		sleep(0.5)
		# 模糊搜索
		browser.find_element_by_xpath('//*[@id="included_clause"]').send_keys(ambiguous_search)
		# 开始时间
		browser.find_element_by_xpath('//*[@id="datefrom"]').send_keys(start_date)
		browser.find_element_by_xpath('//*[@id="timefrom"]').send_keys(start_time)
		# 结束时间
		browser.find_element_by_xpath('//*[@id="dateto"]').send_keys(end_date)
		browser.find_element_by_xpath('//*[@id="timeto"]').send_keys(end_time)

		# 级别默认选择所有 若要修改 level填change 取消勾选所有再做其他勾选
		if level == 'change':
			if select_all == 'yes':
				# 验证选择所有是否被勾选 若勾选则先取消
				enable1 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable1 == True:
					pass
				if enable1 == False:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
			else:
				# 先取消全选再勾选其他
				enable2 = browser.find_element_by_xpath('//*[@id="sel_all"]').is_selected()
				if enable2 == True:
					browser.find_element_by_xpath('//*[@id="sel_all"]').click()
				if enable2 == False:
					pass
				sleep(0.5)
				# 勾选emerg
				if emerg == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[1]').click()
				# 勾选alert
				if alert == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[2]').click()
				# 勾选critical
				if critical == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[3]').click()
				# 勾选error
				if error == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[4]').click()
				# 勾选warning
				if warning == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[5]').click()
				# 勾选notice
				if notice == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[6]').click()
				# 勾选info
				if info == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[7]').click()
				# 勾选debug
				if debug == 'yes':
					browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[2]/td[3]/input[8]').click()

		# 模块默认选择all 若要修改 则先将all左移 再选择其他项右移
		if module == 'change':
			# 选择all
			s1 = Select(browser.find_element_by_xpath('//*[@id="Smodules"]'))
			s1.select_by_visible_text('all')
			# 点击左移
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[2]').click()
			sleep(0.5)
			# 选择其他项 点击右移
			s1 = Select(browser.find_element_by_xpath('//*[@id="Amodules"]'))
			s1.select_by_visible_text(modul_name)
			sleep(0.5)
			# 点击右移
			browser.find_element_by_xpath(
				'//*[@id="advance"]/table/tbody/tr[3]/td[3]/table/tbody/tr[2]/td[2]/input[1]').click()

		# 查询结果另存为
		if save_as == 'yes':
			sleep(0.5)
			# 输入名称
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[1]').send_keys(save_as_name)
			# 点击保存
			browser.find_element_by_xpath('//*[@id="advance"]/table/tbody/tr[5]/td[3]/input[2]').click()


# 生成日志，未完成
def generate_log(browser, dev="dev1", log_type="", num="1"):
	if log_type == 系统日志:
		for x in range(0, int(num), 2):
			a = Shell_SSH()
			a.connect(dev)
			a.execute("exit")
			a.close()
			print(x)


# 获取日志过滤的所有信息，每行为一项（[索引，名称，类型，级别，模块]），存在列表中，返回
def get_logfilter_info(browser):
	into_fun(browser, 日志过滤)
	# //*[@id="log_setting_filter_table"]/tbody/tr[2]/td[2]  //*[@id="log_setting_filter_table"]/tbody/tr[3]/td[2]
	# //*[@id="log_setting_filter_table"]/tbody/tr[2]/td[1]
	logfilter_info_list = []
	filter_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	for x in range(2, int(filter_sum)+2):
		filter_index = browser.find_element_by_xpath('//*[@id="log_setting_filter_table"]/tbody/tr['+str(x)+']/td[1]').text.rstrip()
		filter_name = browser.find_element_by_xpath('//*[@id="log_setting_filter_table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
		filter_tpye = browser.find_element_by_xpath(
			'//*[@id="log_setting_filter_table"]/tbody/tr[' + str(x) + ']/td[3]').text.rstrip()
		filter_level = browser.find_element_by_xpath(
			'//*[@id="log_setting_filter_table"]/tbody/tr[' + str(x) + ']/td[4]').text.rstrip()
		filter_mode = browser.find_element_by_xpath(
			'//*[@id="log_setting_filter_table"]/tbody/tr[' + str(x) + ']/td[5]').text.rstrip()
		logfilter_info_list.append([filter_index, filter_name, filter_tpye, filter_level, filter_mode])
	return logfilter_info_list
