from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from selenium.webdriver.common.keys import Keys
from page_obj.scg.scg_def import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



# 添加admin 权限
def add_admin_profile(browser, profile_name='scg', desc='zhe是yi个描述1', cfg="读写", report="读写"):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	browser.find_element_by_xpath('//*[@id="profilename"]').send_keys(profile_name)
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if cfg == "读写":
		browser.find_element_by_xpath('//*[@id="configsystem_0"]').click()
	elif cfg == "只读":
		browser.find_element_by_xpath('//*[@id="configsystem_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="configsystem_2"]').click()
	if report == "读写":
		browser.find_element_by_xpath('//*[@id="reportsystem_0"]').click()
	elif report == "只读":
		browser.find_element_by_xpath('//*[@id="reportsystem_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="reportsystem_2"]').click()
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(0.5)


# 系统设置
def sys_set_jyl(browser, ssh_port="22/", ssh_timeout="600/", https_port="443/", https_timeout="600/", telent_port="23/",
                telent_timeout="600/", console_timeout="600/", frozen_time="600/", expire_time="600/", retry="3/"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击系统设定
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(1)
	# ssh设置
	# 清除默认输入内容
	if "/" not in ssh_port:
		browser.find_element_by_xpath('//*[@id="sshport"]').clear()
		browser.find_element_by_xpath('//*[@id="sshport"]').send_keys(ssh_port)
	if "/" not in ssh_timeout:
		browser.find_element_by_xpath('//*[@id="sshtimeout"]').clear()
		browser.find_element_by_xpath('//*[@id="sshtimeout"]').send_keys(ssh_timeout)
		# print("5612")
		time.sleep(1)

	# https设置
	# 清除默认输入内容
	if "/" not in https_port:
		browser.find_element_by_xpath('//*[@id="httpsport"]').clear()
		browser.find_element_by_xpath('//*[@id="httpsport"]').send_keys(https_port)
	if "/" not in https_timeout:
		browser.find_element_by_xpath('//*[@id="httpstimeout"]').clear()
		browser.find_element_by_xpath('//*[@id="httpstimeout"]').send_keys(https_timeout)

	# telent设置
	# 清除默认输入内容
	if "/" not in telent_port:
		browser.find_element_by_xpath('//*[@id="telnetport"]').clear()
		browser.find_element_by_xpath('//*[@id="telnetport"]').send_keys(telent_port)
	if "/" not in telent_timeout:
		browser.find_element_by_xpath('//*[@id="telnettimeout"]').clear()
		browser.find_element_by_xpath('//*[@id="telnettimeout"]').send_keys(telent_timeout)

	# console设置
	# 清除默认输入内容
	if "/" not in console_timeout:
		browser.find_element_by_xpath('//*[@id="consoletimeout"]').clear()
		browser.find_element_by_xpath('//*[@id="consoletimeout"]').send_keys(console_timeout)

	# frozen_time设置
	# 清除默认输入内容
	if "/" not in frozen_time:
		browser.find_element_by_xpath('//*[@id="fronzedtime"]').clear()
		browser.find_element_by_xpath('//*[@id="fronzedtime"]').send_keys(frozen_time)

	# expire_time设置
	# 清除默认输入内容
	if "/" not in expire_time:
		browser.find_element_by_xpath('//*[@id="expire_time"]').clear()
		browser.find_element_by_xpath('//*[@id="expire_time"]').send_keys(expire_time)
	# retry设置
	# 清除默认输入内容
	if "/" not in retry:
		browser.find_element_by_xpath('//*[@id="retry"]').clear()
		browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(1)
	try:
		# print("Alert exists")
		alert = browser.switch_to_alert()
		alert.accept()

	except:
		# print("无警告，点击返回")
		pass
		try:
			browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
		except:
			pass
			# print("无点击返回")

	# if EC.alert_is_present:
	# 	print("Alert exists")
	# 	alert = browser.switch_to_alert()
	# 	# print(alert.text)
	# 	alert.accept()
	# 	# print("Alert accepted")
	# else:
	# 	# print("NO alert exists")
	# 	# 点击返回
	# 	browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()

	# time.sleep(2)
	# if https_port != "443":
	# 	# 接受告警
	# 	browser.switch_to_alert().accept()
	# 	time.sleep(2)
	# 	# 点击管理员
	# 	browser.find_element_by_xpath(管理员).click()
	# 	time.sleep(5)
	# 	# 定位到默认frame
	# 	browser.switch_to.default_content()
	# 	# 定位到内容frame
	# 	browser.switch_to.frame("content")
	#
	# 	# 点击系统设定
	# 	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	# 	time.sleep(5)
	# 	# https设置
	# 	# 清除默认输入内容
	# 	browser.find_element_by_xpath('//*[@id="httpsport"]').clear()
	# 	browser.find_element_by_xpath('//*[@id="httpsport"]').send_keys("443")
	# 	time.sleep(2)
	# 	# 点击保存
	# 	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	# 	browser.switch_to_alert().accept()
	# 	time.sleep(2)


# 无返回语句，用于系统设置时弹出告警框的情况，HTTPS端口不是443的情况也改了
def sys_set_lzy(browser, ssh_port="22", ssh_timeout="600", https_port="443", https_timeout="600", telent_port="23",
                telent_timeout="600", console_timeout="600", frozen_time="600", expire_time="600", retry="3"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击系统设定
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(3)
	# ssh设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="sshport"]').clear()
	browser.find_element_by_xpath('//*[@id="sshport"]').send_keys(ssh_port)
	browser.find_element_by_xpath('//*[@id="sshtimeout"]').clear()
	browser.find_element_by_xpath('//*[@id="sshtimeout"]').send_keys(ssh_timeout)
	# print("5612")
	sleep(2)

	# https设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="httpsport"]').clear()
	browser.find_element_by_xpath('//*[@id="httpsport"]').send_keys(https_port)
	browser.find_element_by_xpath('//*[@id="httpstimeout"]').clear()
	browser.find_element_by_xpath('//*[@id="httpstimeout"]').send_keys(https_timeout)

	# telent设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="telnetport"]').clear()
	browser.find_element_by_xpath('//*[@id="telnetport"]').send_keys(telent_port)
	browser.find_element_by_xpath('//*[@id="telnettimeout"]').clear()
	browser.find_element_by_xpath('//*[@id="telnettimeout"]').send_keys(telent_timeout)

	# console设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="consoletimeout"]').clear()
	browser.find_element_by_xpath('//*[@id="consoletimeout"]').send_keys(console_timeout)

	# frozen_time设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').clear()
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').send_keys(frozen_time)

	# expire_time设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="expire_time"]').clear()
	browser.find_element_by_xpath('//*[@id="expire_time"]').send_keys(expire_time)

	# retry设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(3)

	if https_port != "443" and https_port >= '1' and https_port <= '65535':
		# 接受告警
		browser.switch_to_alert().accept()
		time.sleep(2)
		browser.refresh()
		time.sleep(2)
		x = https_port
		login_web(browser, url="10.2.2.81:" + str(x))
		time.sleep(2)
		browser.refresh()
		time.sleep(2)

		# https端口改回443
		# 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("lefttree")
		# # 点击系统
		# browser.find_element_by_xpath(系统).click()
		# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(系统管理).click()
		# # 点击管理员
		# browser.find_element_by_xpath(管理员).click()
		# time.sleep(2)
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 管理员)
		# 点击系统设定
		browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
		time.sleep(5)
		# https设置
		# 清除默认输入内容
		browser.find_element_by_xpath('//*[@id="httpsport"]').clear()
		browser.find_element_by_xpath('//*[@id="httpsport"]').send_keys("443")
		time.sleep(2)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
		browser.switch_to_alert().accept()
		time.sleep(2)


# 添加管理员
def add_admin(browser, admin_name="bob", auth_database="local", temp="log_profile", https="yes", telent="yes",
              ssh="yes", console="yes", password="admin@139", confirm_password="admin@139", status="enable",
              interface=interface_name_1, online_num="32", ip1="0.0.0.0/0", ip2="", ip3="", ip4="", ip5=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(系统).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	#
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击管理员列表
	into_fun(browser, 管理员)
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击添加
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入管理员名称
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(admin_name)

	# 选认证数据库
	s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
	# 选认证数据库下拉框内容
	s1.select_by_visible_text(auth_database)

	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
	# 选profile下拉框内容
	time.sleep(0.5)
	s1.select_by_visible_text(temp)

	if https == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	elif https == "no":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()

	if telent == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_2"]').click()

	if ssh == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_3"]').click()

	if console == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	elif console == "no":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys(password)

	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys(confirm_password)

	# 选择状态下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="status"]'))
	# 选择状态
	s1.select_by_visible_text(status)

	# 选择接口选择下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选择接口
	s1.select_by_visible_text(interface)

	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(online_num)

	# 允许IP长度
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys(ip1)
	browser.find_element_by_xpath('//*[@id="permitip2"]').send_keys(ip2)
	browser.find_element_by_xpath('//*[@id="permitip3"]').send_keys(ip3)
	browser.find_element_by_xpath('//*[@id="permitip4"]').send_keys(ip4)
	browser.find_element_by_xpath('//*[@id="permitip5"]').send_keys(ip5)

	# 允许IPV6_1长度
	#browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_1)
	#browser.find_element_by_xpath('//*[@id="permitipv62"]').send_keys(ipv6_2)
	# 点击保存按钮
	time.sleep(0.5)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(0.5)


# 通过名字删除管理员
def del_admin_byname(browser, name):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/div').click()
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击管理员列表
	into_fun(browser, 管理员)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 获取目前有多少个管理员，而且要减去1，因为有1个默认admin管理的存在
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text) - 1
	# 根据zone数量,遍历一下，获取要被删除的对象的层数
	for x in range(3, 3 + zone_sum):
		if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip():
			# 点击删除该对象
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[11]/a[2]').click()
			print(str(name)+"管理员，删除成功")
			break
			# 这个break是后来加的，出问题请删除


# 获得管理员名字，返回名字列表
def get_admin_name(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(1)
	zone_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# 根据zone数量,遍历一下，获取要被删除的对象的层数
	name_list = []
	for x in range(2, 2 + zone_sum):
		get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
		name_list.append(get_name)
	return name_list


# 添加远程管理员
def add_admin_remote_jyl(browser, admin_name="bob", auth_database="local", temp="log_profile", https="yes",
						 telent="yes", ssh="yes", console="yes", status="enable", interface="ge0/1",
						 online_num="32", ip1="0.0.0.0/0", ip2="3.3.3.0/24"):

	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击添加
	time.sleep(8)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入管理员名称
	time.sleep(8)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(admin_name)
	# 选认证数据库
	s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
	# 选认证数据库下拉框内容
	s1.select_by_visible_text(auth_database)
	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(temp)

	if  https =="yes":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	elif https =="no":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()

	if  telent=="yes":
		browser.find_element_by_xpath('//*[@id="logintype_2"]').click()

	if  ssh=="yes":
		browser.find_element_by_xpath('//*[@id="logintype_3"]').click()

	if  console=="yes":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	elif console == "no":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()

	# 选择状态下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="status"]'))
	# 选择状态
	s1.select_by_visible_text(status)

	# 选择接口选择下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选择接口
	s1.select_by_visible_text(interface)

	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()

	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(online_num)

	# 允许IP长度
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys(ip1)
	browser.find_element_by_xpath('//*[@id="permitip2"]').send_keys(ip2)

	# 允许IPV6_1长度
	#browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_1)
	#browser.find_element_by_xpath('//*[@id="permitipv62"]').send_keys(ipv6_2)

	# 点击保存按钮
	time.sleep(3)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(3)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 从主页获取主机名
def get_sys_info_hostname(browser):
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# browser.find_element_by_xpath(系统状态).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 系统状态)
	time.sleep(1)
	hostname = browser.find_element_by_xpath('//*[@id="home_sysinfo_hostname"]').text
	return hostname


# 从主页uptime
def get_uptime(browser):
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# browser.find_element_by_xpath(系统状态).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 系统状态)
	time.sleep(1)
	uptime = browser.find_element_by_xpath('//*[@id="home_sys_runtime"]').text
	return uptime


# 配置DNS
def set_dns(browser, dns1="114.114.114.114", dns2=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(系统).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	#
	# browser.find_element_by_xpath(DNS).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DNS)
	browser.find_element_by_xpath('//*[@id="dns1"]').clear()
	browser.find_element_by_xpath('//*[@id="dns1"]').send_keys(dns1)
	browser.find_element_by_xpath('//*[@id="dns2"]').clear()
	browser.find_element_by_xpath('//*[@id="dns2"]').send_keys(dns2)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 获取DNS,返回两个DNS的列表
def get_dns(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(系统).click()
	dns_list = []
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	#
	# browser.find_element_by_xpath(DNS).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DNS)
	dns1 = browser.find_element_by_xpath('//*[@id="dns1"]').get_attribute('value')
	dns2 = browser.find_element_by_xpath('//*[@id="dns2"]').get_attribute('value')
	dns_list.append(dns1)
	dns_list.append(dns2)
	return dns_list


# 编辑系统信息-主机名、地点、描述、联系信息、集中管理
def edit_sysinfo(browser, hostname=" ", location=" ", description=" ", contact=" ", cyberview=" "):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(系统信息).click()
	#
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统信息)

	if hostname != " ":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="hostname"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="hostname"]').send_keys(hostname)

	if location != " ":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="location"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="location"]').send_keys(location)

	if description != " ":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="description"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	if contact != " ":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="contact"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="contact"]').send_keys(contact)

	if cyberview != " ":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="agentip"]').clear()
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="agentip"]').send_keys(cyberview)

	browser.find_element_by_xpath('//*[@id="container"]/div/form/div/div[2]/div/input[2]').click()


# 获得系统信息-地点
def get_sys_info_location(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(系统信息).click()
	#
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统信息)
	# time.sleep(2)
	location = browser.find_element_by_xpath('//*[@id="location"]').get_attribute('value')
	browser.refresh()
	# print(location)
	# print("1")
	return location


# 获得系统信息-描述
def get_sys_info_description(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(系统信息).click()
	#
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统信息)
	description = browser.find_element_by_xpath('//*[@id="description"]').get_attribute('value')
	browser.refresh()
	return description


# 获得系统信息-联系信息
def get_sys_info_contact(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(系统信息).click()
	#
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统信息)
	contact = browser.find_element_by_xpath('//*[@id="contact"]').get_attribute('value')
	browser.refresh()
	return contact


# 获得系统信息-CyberView
def get_sys_info_cyberview(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(系统信息).click()
	#
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统信息)
	cyberview = browser.find_element_by_xpath('//*[@id="agentip"]').get_attribute('value')
	browser.refresh()
	return cyberview


# 修改设备语言
def set_language(browser, language_sw="简体中文"):
	# 切换到默认frame
	browser.switch_to.default_content()
	# 切换到左侧frame
	browser.switch_to.frame("topheader")
	while True:
		if not browser.find_element_by_xpath('//*[@id="lang_bar"]/a[1]').is_displayed():
			# 如果不可见，点击加号，展开元素
			browser.find_element_by_xpath('/html/body/nav/ul/li[1]/a/span').click()
		else:
			break

	if language_sw == "简体中文":
		browser.find_element_by_xpath('//*[@id="lang_bar"]/a[2]').click()
	elif language_sw == "繁体中文":
		browser.find_element_by_xpath('//*[@id="lang_bar"]/a[3]').click()
	elif language_sw == "英文":
		browser.find_element_by_xpath('//*[@id="lang_bar"]/a[1]').click()


# 判断设备语言，如果符合，返回Ture
def judge_language(browser, language_sw="简体中文"):

	browser.refresh()
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[1]/span/a').click()
	# browser.switch_to.default_content()
	into_fun(browser, 系统信息)
	# 切换到左侧frame
	browser.switch_to.frame("content")
	hostname_style = browser.find_element_by_xpath('//*[@id="sys_info"]/tbody/tr[1]/td[1]').text
	# print(hostname_style)

	if language_sw == "繁体中文":
		if hostname_style == "主機名稱":
			print("繁体")
			return True
	elif language_sw == "简体中文":
		if hostname_style == "主机名":
			print("简体")
			return True
	elif language_sw == "英文":
		if hostname_style == "Host Name":
			print("英文")
			return True
	else:
		print("F")
		return False


# 设置系统时间
def set_time(browser, date_input="2019-06-08", time_input="00:00:00"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[@id="key_switch_time_zone_link"]').click()
	browser.find_element_by_xpath('//*[@id="date"]').send_keys(date_input)
	browser.find_element_by_xpath('//*[@id="time"]').send_keys(time_input)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 从主页获取系统时间，返回时间字符串
def get_time(browser):
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# browser.find_element_by_xpath(系统状态).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 系统状态)
	time.sleep(2)
	systime = browser.find_element_by_xpath('//*[@id="home_sys_time"]').text
	return systime


# 设置系统时区
def set_timezone(browser, time_zone="(GMT+0800) Asia/Shanghai"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	# 点击时区设置
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	browser.find_element_by_xpath('//*[@id="current"]/a').click()
	browser.find_element_by_xpath('//*[@id="key_switch_time_zone_link"]').click()
	timezone_seclect = Select(browser.find_element_by_xpath('//*[@id="time_zone"]'))
	timezone_seclect.select_by_visible_text(time_zone)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 从主页获取时区，返回时间字符串
def get_timezone(browser):
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# browser.find_element_by_xpath(系统状态).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 系统状态)
	time.sleep(2)
	time_zone = browser.find_element_by_xpath('//*[@id="home_sys_timezone"]').text
	return time_zone


# ping诊断,返回结果字符串
def diag_ping(browser, ipadd="192.168.1.1", packersize="100", count="5", ping_wait_time="2", interface="请选择", timesleep=2):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(诊断工具).click()
	# browser.find_element_by_xpath(网络诊断).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 网络诊断)
	browser.find_element_by_xpath('//*[@id="ping_interface"]').click()
	browser.find_element_by_xpath('//*[@id="ping_name"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_name"]').send_keys(ipadd)

	browser.find_element_by_xpath('//*[@id="ping_packet_size"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_packet_size"]').send_keys(packersize)

	browser.find_element_by_xpath('//*[@id="ping_count"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_count"]').send_keys(count)

	browser.find_element_by_xpath('//*[@id="ping_wait_time"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_wait_time"]').send_keys(ping_wait_time)
	sleep(0.5)

	interface_select = Select(browser.find_element_by_xpath('//*[@id="ping_interface"]'))
	sleep(0.5)
	interface_select.select_by_visible_text(interface)
	sleep(0.5)

	browser.find_element_by_xpath('//*[@id="ping_submit"]').click()
	sleeptime = int(count) * int(ping_wait_time)
	time.sleep(timesleep)
	textarea_txt = browser.find_element_by_xpath('//*[@id="ping_result"]').get_attribute('value')
	return textarea_txt


# 设置NTP服务器,选择默认服务器，直接点保存
def set_ntpservers_default(browser, ntpserver='',):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	browser.find_element_by_xpath('//*[@id="syn_server_0"]').click()
	s1 = Select(browser.find_element_by_xpath('//*[@id="ntp_server"]'))
	# 找下拉框的内容
	s1.select_by_visible_text(ntpserver)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 设置NTP服务器,自定义服务器地址
def set_ntpservers_user(browser, ntpserver1='', ntpserver2=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	browser.find_element_by_xpath('//*[@id="syn_server_1"]').click()
	time.sleep(0.5)
	if ntpserver1 != "":
		browser.find_element_by_xpath('//*[@id="server2"]').clear()
		browser.find_element_by_xpath('//*[@id="server2"]').send_keys(ntpserver1)
	if ntpserver2 != "":
		browser.find_element_by_xpath('//*[@id="server3"]').clear()
		browser.find_element_by_xpath('//*[@id="server3"]').send_keys(ntpserver2)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 设置NTP服务器停用
def set_ntpservers_disable(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	if not browser.find_element_by_xpath('//*[@id="syn_server"]').is_selected():
		browser.find_element_by_xpath('//*[@id="syn_server"]').click()
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 设置NTP服务器的同步间隔
def set_ntpservers_interval(browser, interval="60"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	browser.refresh()
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	browser.find_element_by_xpath('//*[@id="syncinterval"]').clear()
	browser.find_element_by_xpath('//*[@id="syncinterval"]').send_keys(interval)
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()


# 对NTP服务器地址进行可用性的测试，可选默认服务器、自定义服务器1，2，默认是对默认服务器们进行测试，返回结果列表
def itest_ntpservers_availability(browser, servers_option="default/server1/server2", server1="127.0.0.1/un", server2="127.0.0.1/un"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	# 如果选择是默认服务器，那就选中默认服务器，并获取所有的下拉项，逐个进行可用性测试
	resault1 = []
	if servers_option == "default":
		# 选中默认服务器选项
		browser.find_element_by_xpath('//*[@id="syn_server_0"]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="ntp_server"]'))
		options_list = s1.options
		for option1 in options_list:
			# print(option1.text)
			if option1.text != "请选择":
				s1.select_by_visible_text(option1.text)
				browser.find_element_by_xpath('//*[@id="timetr_8"]/td[2]/div/input').click()
				# 获取当前窗口句柄集合（列表类型），开始切换窗口
				handles = browser.window_handles
				# print("wwwww")
				# print(handles)
				for handle in handles:  # 切换窗口（切换到测试窗口）
					if handle != browser.current_window_handle:
						# print('switch to ', handle)
						browser.switch_to_window(handle)
						break
				time.sleep(3)
				test_info = browser.find_element_by_xpath('/html/body').text
				# print(test_info)
				resault1.append(test_info)
				browser.close()  # 关闭当前窗口
				browser.switch_to_window(handles[0])  # 切换回主窗口
				time.sleep(0.2)
				browser.switch_to.default_content()
				browser.switch_to.frame("content")
			else:
				continue
		return resault1
	elif servers_option == 'server1':
		browser.find_element_by_xpath('//*[@id="syn_server_1"]').click()
		if '127.0.0.1/un' not in server1:
			browser.find_element_by_xpath('//*[@id="server2"]').clear()
			browser.find_element_by_xpath('//*[@id="server2"]').send_keys(server1)
			browser.find_element_by_xpath('//*[@id="timetr_10"]/td[2]/div/input').click()
			# 获取当前窗口句柄集合（列表类型），开始切换窗口
			handles = browser.window_handles
			# print("wwwww")
			# print(handles)
			for handle in handles:  # 切换窗口（切换到测试窗口）
				if handle != browser.current_window_handle:
					# print('switch to ', handle)
					browser.switch_to_window(handle)
					break
			time.sleep(3)
			test_info = browser.find_element_by_xpath('/html/body').text
			# print(test_info)
			resault1.append(test_info)
			browser.close()  # 关闭当前窗口
			browser.switch_to_window(handles[0])  # 切换回主窗口
			time.sleep(0.2)
			browser.switch_to.default_content()
			browser.switch_to.frame("content")
		else:
			browser.find_element_by_xpath('//*[@id="timetr_10"]/td[2]/div/input').click()
			# 获取当前窗口句柄集合（列表类型），开始切换窗口
			handles = browser.window_handles
			# print("wwwww")
			# print(handles)
			for handle in handles:  # 切换窗口（切换到测试窗口）
				if handle != browser.current_window_handle:
					# print('switch to ', handle)
					browser.switch_to_window(handle)
					break
			time.sleep(3)
			test_info = browser.find_element_by_xpath('/html/body').text
			# print(test_info)
			resault1.append(test_info)
			browser.close()  # 关闭当前窗口
			browser.switch_to_window(handles[0])  # 切换回主窗口
			time.sleep(0.2)
			browser.switch_to.default_content()
			browser.switch_to.frame("content")

		return	resault1

	elif servers_option == 'server2':
		browser.find_element_by_xpath('//*[@id="syn_server_1"]').click()
		if '127.0.0.1/un' not in server1:
			browser.find_element_by_xpath('//*[@id="server3"]').clear()
			browser.find_element_by_xpath('//*[@id="server3"]').send_keys(server1)
			browser.find_element_by_xpath('//*[@id="timetr_11"]/td[2]/div/input').click()
			# 获取当前窗口句柄集合（列表类型），开始切换窗口
			handles = browser.window_handles
			# print("wwwww")
			# print(handles)
			for handle in handles:  # 切换窗口（切换到测试窗口）
				if handle != browser.current_window_handle:
					# print('switch to ', handle)
					browser.switch_to_window(handle)
					break
			time.sleep(3)
			test_info = browser.find_element_by_xpath('/html/body').text
			# print(test_info)
			resault1.append(test_info)
			browser.close()  # 关闭当前窗口
			browser.switch_to_window(handles[0])  # 切换回主窗口
			time.sleep(0.2)
			browser.switch_to.default_content()
			browser.switch_to.frame("content")
		else:
			browser.find_element_by_xpath('//*[@id="timetr_11"]/td[2]/div/input').click()
			# 获取当前窗口句柄集合（列表类型），开始切换窗口
			handles = browser.window_handles
			# print("wwwww")
			# print(handles)
			for handle in handles:  # 切换窗口（切换到测试窗口）
				if handle != browser.current_window_handle:
					# print('switch to ', handle)
					browser.switch_to_window(handle)
					break
			time.sleep(3)
			test_info = browser.find_element_by_xpath('/html/body').text
			# print(test_info)
			resault1.append(test_info)
			browser.close()  # 关闭当前窗口
			browser.switch_to_window(handles[0])  # 切换回主窗口
			time.sleep(0.2)
			browser.switch_to.default_content()
			browser.switch_to.frame("content")

		return resault1


# 直接点击NTP服务器测试按钮，没有其他任何动作
def itest_ntpservers(browser, servers_option="default/server1/server2"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_配置).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(配置).click()
	# browser.find_element_by_xpath(时间设定).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 时间设定)
	browser.find_element_by_xpath('//*[text()="NTP服务器设置"]').click()
	# 如果选择是默认服务器，那就选中默认服务器，并获取所有的下拉项，逐个进行可用性测试
	resault1 = []
	if servers_option == "default":
		# 选中默认服务器选项
		browser.find_element_by_xpath('//*[@id="timetr_8"]/td[2]/div/input').click()
		# 获取当前窗口句柄集合（列表类型），开始切换窗口
		handles = browser.window_handles
		# print("wwwww")
		# print(handles)
		for handle in handles:  # 切换窗口（切换到测试窗口）
			if handle != browser.current_window_handle:
				# print('switch to ', handle)
				browser.switch_to_window(handle)
				break
		time.sleep(3)
		test_info = browser.find_element_by_xpath('/html/body').text
		# print(test_info)
		resault1.append(test_info)
		browser.close()  # 关闭当前窗口
		browser.switch_to_window(handles[0])  # 切换回主窗口
		time.sleep(0.2)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")

	elif servers_option == 'server1':

		browser.find_element_by_xpath('//*[@id="timetr_10"]/td[2]/div/input').click()
		# 获取当前窗口句柄集合（列表类型），开始切换窗口
		handles = browser.window_handles
		# print("wwwww")
		# print(handles)
		for handle in handles:  # 切换窗口（切换到测试窗口）
			if handle != browser.current_window_handle:
				# print('switch to ', handle)
				browser.switch_to_window(handle)
				break
		time.sleep(3)
		test_info = browser.find_element_by_xpath('/html/body').text
		# print(test_info)
		resault1.append(test_info)
		browser.close()  # 关闭当前窗口
		browser.switch_to_window(handles[0])  # 切换回主窗口
		time.sleep(0.2)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")

	elif servers_option == 'server2':

		browser.find_element_by_xpath('//*[@id="timetr_11"]/td[2]/div/input').click()
		# 获取当前窗口句柄集合（列表类型），开始切换窗口
		handles = browser.window_handles
		# print("wwwww")
		# print(handles)
		for handle in handles:  # 切换窗口（切换到测试窗口）
			if handle != browser.current_window_handle:
				# print('switch to ', handle)
				browser.switch_to_window(handle)
				break
		time.sleep(3)
		test_info = browser.find_element_by_xpath('/html/body').text
		# print(test_info)
		resault1.append(test_info)
		browser.close()  # 关闭当前窗口
		browser.switch_to_window(handles[0])  # 切换回主窗口
		time.sleep(0.2)
		browser.switch_to.default_content()
		browser.switch_to.frame("content")


# 进入管理员列表，查看在线管理员数,返回数量 int
def get_admin_list_look_online_admin(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(1)
	# 点击在线
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[10]/a').click()
	return int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)


# 进入管理员列表，查看冻结管理员
def get_admin_list_look_frozen_admin(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(1)
	# 点击frozen
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[10]/a').click()


# 路由跟踪,返回结果字符串
def trace_route(browser, ipadd="192.168.1.1", packersize="100", count="5", ping_wait_time="2", interface="请选择", timesleep=2):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(诊断工具).click()
	# browser.find_element_by_xpath(网络诊断).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 网络诊断)
	browser.find_element_by_xpath('//*[@id="tr_name"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_name"]').send_keys(ipadd)

	browser.find_element_by_xpath('//*[@id="tr_packet_size"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_packet_size"]').send_keys(packersize)

	browser.find_element_by_xpath('//*[@id="tr_count"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_count"]').send_keys(count)

	browser.find_element_by_xpath('//*[@id="tr_wait_time"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_wait_time"]').send_keys(ping_wait_time)

	interface_select = Select(browser.find_element_by_xpath('//*[@id="tr_interface"]'))
	interface_select.select_by_visible_text(interface)

	browser.find_element_by_xpath('//*[@id="tr_submit"]').click()
	sleeptime = int(count) * int(ping_wait_time)
	time.sleep(timesleep)
	textarea_txt = browser.find_element_by_xpath('//*[@id="tr_result"]').get_attribute('value')
	return textarea_txt


def fail_diag_ping(browser, ipadd="192.168.1.1", packersize="100", count="5", ping_wait_time="2", interface="请选择"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(诊断工具).click()
	# browser.find_element_by_xpath(网络诊断).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 网络诊断)
	browser.find_element_by_xpath('//*[@id="ping_name"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_name"]').send_keys(ipadd)

	browser.find_element_by_xpath('//*[@id="ping_packet_size"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_packet_size"]').send_keys(packersize)

	browser.find_element_by_xpath('//*[@id="ping_count"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_count"]').send_keys(count)

	browser.find_element_by_xpath('//*[@id="ping_wait_time"]').clear()
	browser.find_element_by_xpath('//*[@id="ping_wait_time"]').send_keys(ping_wait_time)

	interface_select = Select(browser.find_element_by_xpath('//*[@id="ping_interface"]'))
	interface_select.select_by_visible_text(interface)

	browser.find_element_by_xpath('//*[@id="ping_submit"]').click()


# 路由跟踪,用于错误的测试用例测试
def fail_test_trace_route(browser, ipadd="192.168.1.1", packersize="100", count="5", ping_wait_time="2", interface="请选择"):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_诊断工具).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(诊断工具).click()
	# browser.find_element_by_xpath(网络诊断).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 网络诊断)
	browser.find_element_by_xpath('//*[@id="tr_name"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_name"]').send_keys(ipadd)

	browser.find_element_by_xpath('//*[@id="tr_packet_size"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_packet_size"]').send_keys(packersize)

	browser.find_element_by_xpath('//*[@id="tr_count"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_count"]').send_keys(count)

	browser.find_element_by_xpath('//*[@id="tr_wait_time"]').clear()
	browser.find_element_by_xpath('//*[@id="tr_wait_time"]').send_keys(ping_wait_time)

	interface_select = Select(browser.find_element_by_xpath('//*[@id="tr_interface"]'))
	interface_select.select_by_visible_text(interface)
	browser.find_element_by_xpath('//*[@id="tr_submit"]').click()


# 重启（系统状态-接口面板-重启）
def reboot_lzy(browser, desc="test!"):
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# browser.find_element_by_xpath(系统).click()
	# browser.find_element_by_xpath(系统状态).click()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("content")
	into_fun(browser, 系统状态)
	browser.find_element_by_xpath('//*[@id="innerbox_line_port"]/div[2]/a').click()
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	browser.switch_to_alert().accept()
	browser.switch_to_alert().send_keys(desc)
	browser.switch_to_alert().accept()
	sleep(65)



# 进入到管理员列表界面，什么也不做
def get_into_adminlist(browser):
	browser.refresh()
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(1)


# 返回告警框信息  （添加admin profile , name输入不规范或描述输入不规范 导致弹出告警框）
def return_alert_when_add_wrong_admin_profile(browser, profile_name='scg', desc='zhe是yi个描述1', cfg="读写", report="读写"):

	into_fun(browser, 管理员)
	# 进入管理员权限
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入
	browser.find_element_by_xpath('//*[@id="profilename"]').send_keys(profile_name)
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
	if cfg == "读写":
		browser.find_element_by_xpath('//*[@id="configsystem_0"]').click()
	elif cfg == "只读":
		browser.find_element_by_xpath('//*[@id="configsystem_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="configsystem_2"]').click()
	if report == "读写":
		browser.find_element_by_xpath('//*[@id="reportsystem_0"]').click()
	elif report == "只读":
		browser.find_element_by_xpath('//*[@id="reportsystem_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="reportsystem_2"]').click()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 弹出警告框 获取内容 接受告警 返回告警框信息
	alert = browser.switch_to_alert().text
	print(alert)
	browser.switch_to_alert().accept()
	return alert


# 返回告警框信息  （添加admin user , 输入不规范 弹出告警框）
def return_alert_when_add_wrong_admin(browser, admin_name="bob", auth_database="local", temp="log_profile", https="yes",
                                      telent="yes",
                                      ssh="yes", console="yes", password="admin@139", confirm_password="admin@139",
                                      status="enable",
                                      interface=interface_name_1, online_num="32", ip1="0.0.0.0/0", ip2="", ip3="",
                                      ip4="", ip5=""):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(系统).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	#
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击添加
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入管理员名称
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(admin_name)

	# 选认证数据库
	s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
	# 选认证数据库下拉框内容
	s1.select_by_visible_text(auth_database)

	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(temp)

	if https == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	elif https == "no":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()

	if telent == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_2"]').click()

	if ssh == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_3"]').click()

	if console == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	elif console == "no":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys(password)

	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys(confirm_password)

	# 选择状态下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="status"]'))
	# 选择状态
	s1.select_by_visible_text(status)

	# 选择接口选择下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选择接口
	s1.select_by_visible_text(interface)

	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(online_num)

	# 允许IP长度
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys(ip1)
	browser.find_element_by_xpath('//*[@id="permitip2"]').send_keys(ip2)
	browser.find_element_by_xpath('//*[@id="permitip3"]').send_keys(ip3)
	browser.find_element_by_xpath('//*[@id="permitip4"]').send_keys(ip4)
	browser.find_element_by_xpath('//*[@id="permitip5"]').send_keys(ip5)

	# 允许IPV6_1长度
	# browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_1)
	# browser.find_element_by_xpath('//*[@id="permitipv62"]').send_keys(ipv6_2)
	# 点击保存按钮
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(1)
	# 弹出警告框 获取内容 接受告警 返回告警框信息
	alert = browser.switch_to_alert().text
	print(alert)
	browser.switch_to_alert().accept()
	return alert


# 用新添加的用户名登录设备后 修改自身登录密码
def modify_password_of_new_adminuser(browser, password="admin@139", confirm_password="admin@139"):
	into_fun(browser, 管理员)
	# 点击编辑修改
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a/img').click()

	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys(password)

	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys(confirm_password)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 登录设备 账号被冻结时使用 并返回“账号冻结”信息
def return_frozon_info_when_login_in(browser, url="10.2.2.81", username="admin", password="admin@139", verificationCode="0613"):
	# 打开 SCG web
	browser.get("https://" + url)
	# 输入帐号
	browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
	# 输入密码
	browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
	# 验证码0613
	browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
		verificationCode)
	# 点击登入
	browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	# 获取冻结信息
	info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	return info


# 仅修改系统设置中的 冻结时间 过期时间 和重试次数
def sys_set_only_frozen_expire_retry(browser, frozen_time="600", expire_time="600", retry="3"):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击系统设定
	browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
	time.sleep(3)

	# frozen_time设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').clear()
	browser.find_element_by_xpath('//*[@id="fronzedtime"]').send_keys(frozen_time)

	# expire_time设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="expire_time"]').clear()
	browser.find_element_by_xpath('//*[@id="expire_time"]').send_keys(expire_time)

	# retry设置
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(3)
	#点击返回
	browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
	time.sleep(2)


# 用新添加的用户名登录设备后 点击修改当前用户
def click_modify_of_new_adminuser(browser):
	into_fun(browser, 管理员)
	# 点击编辑修改
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a/img').click()


# 添加管理员 包括ipv6地址
def add_admin_lzy(browser, admin_name="bob", auth_database="local", temp="log_profile", https="yes", telent="yes",
              ssh="yes", console="yes", password="admin@139", confirm_password="admin@139", status="enable",
              interface=interface_name_1, online_num="32", ip1="0.0.0.0/0", ip2="", ip3="", ip4="", ip5="",
				  ipv6_1='', ipv6_2='', ipv6_3='', ipv6_4='', ipv6_5=''):
	# 切换到默认frame
	# browser.switch_to.default_content()
	#
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	#
	# browser.find_element_by_xpath(系统).click()
	#
	# # 判断菜单是否展开，元素是否可见
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	#
	# browser.find_element_by_xpath(管理员).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	# 点击管理员列表
	into_fun(browser, 管理员)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	# 点击添加
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入管理员名称
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(admin_name)

	# 选认证数据库
	s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
	# 选认证数据库下拉框内容
	s1.select_by_visible_text(auth_database)

	# 选profile下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
	# 选profile下拉框内容
	s1.select_by_visible_text(temp)

	if https == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	elif https == "no":
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_1"]').click()

	if telent == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_2"]').click()

	if ssh == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_3"]').click()

	if console == "yes":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	elif console == "no":
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	else:
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys(password)

	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys(confirm_password)

	# 选择状态下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="status"]'))
	# 选择状态
	s1.select_by_visible_text(status)

	# 选择接口选择下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选择接口
	s1.select_by_visible_text(interface)

	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 填入最大在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(online_num)

	# 允许IP长度
	# 清除默认输入内容
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys(ip1)
	browser.find_element_by_xpath('//*[@id="permitip2"]').send_keys(ip2)
	browser.find_element_by_xpath('//*[@id="permitip3"]').send_keys(ip3)
	browser.find_element_by_xpath('//*[@id="permitip4"]').send_keys(ip4)
	browser.find_element_by_xpath('//*[@id="permitip5"]').send_keys(ip5)

	# 允许IPV6_1长度
	browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_1)
	browser.find_element_by_xpath('//*[@id="permitipv62"]').send_keys(ipv6_2)
	browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_3)
	browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_4)
	browser.find_element_by_xpath('//*[@id="permitipv61"]').send_keys(ipv6_5)

	# 点击保存按钮
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(1)


# 删除权限 通过名字
def del_admin_profile_byname(browser, name):

	into_fun(browser, 管理员)
	# 进入管理员权限页面
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 查找名字
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	# 点击删除
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[6]/a[2]/img').click()


# 解冻用户 通过名字
def unfreeze_admin_user_byname(browser, name):

	into_fun(browser, 管理员)
	# 查找名字
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	# 点击frooze
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[10]/a').click()
	# 点击解冻
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[1]').click()


# 登录设备 密码错误时使用
def login_web_when_password_wrong(browser, url="10.2.2.81", username="admin", password="admin@139", verificationCode="0613"):
	# 打开 SCG web
	browser.get("https://" + url)
	# 输入帐号
	browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
	# 输入密码
	browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
	# 验证码0613
	browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
		verificationCode)
	# 点击登入
	browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 登录设备 使用回车键登录
def login_web_by_Keys_ENTER(browser, url="10.2.2.81", username="admin", password="admin@139", verificationCode="0613"):
	# 打开 SCG web
	browser.get("https://" + url)
	# 输入帐号
	browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
	# 输入密码
	browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
	# 验证码0613
	browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
		verificationCode)
	# 回车登录
	browser.find_element_by_xpath('//*[@id="login-div"]/form/div[5]/input').send_keys(Keys.ENTER)


# 编辑管理员
def edit_admin_jyl(browser, edit_admin_name="bob", auth_data="yes/no", auth_database="local", profile="", temp="log_profile",
                   https="yes/no",
                   telnet="yes/no", ssh="yes", console="yes", password="admin@139", confirm_password="admin@139",
                   status="enable", interface=interface_name_3, ip1="",
                   online_num="32"):
	into_fun(browser, 管理员)
	n = 2
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
	while getname != edit_admin_name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text.strip()
	# 点击编辑
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[11]/a/img').click()
	if auth_data == "yes":
		# 选认证数据库
		s1 = Select(browser.find_element_by_xpath('//*[@id="authdatabase"]'))
		# 选认证数据库下拉框内容
		s1.select_by_visible_text(auth_database)
	if profile == "yes":
		# 选权限
		s1 = Select(browser.find_element_by_xpath('//*[@id="profile"]'))
		# 选权限下拉框内容
		s1.select_by_visible_text(temp)
	if https == "yes":
		enable = browser.find_element_by_xpath('//*[@id="logintype_1"]').is_selected()
		if enable == True:
			print("已启用")
		elif enable == False:
			browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
	elif https == "no":
		enable = browser.find_element_by_xpath('//*[@id="logintype_1"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="logintype_1"]').click()
		elif enable == False:
			print("已禁用")

	if telnet == "yes":
		enable = browser.find_element_by_xpath('//*[@id="logintype_2"]').is_selected()
		if enable == True:
			print("已启用")
		elif enable == False:
			browser.find_element_by_xpath('//*[@id="logintype_2"]').click()
	elif telnet == "no":
		enable = browser.find_element_by_xpath('//*[@id="logintype_2"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="logintype_2"]').click()
		elif enable == False:
			print("已禁用")

	if ssh == "yes":
		enable = browser.find_element_by_xpath('//*[@id="logintype_3"]').is_selected()
		if enable == True:
			print("已启用")
		elif enable == False:
			browser.find_element_by_xpath('//*[@id="logintype_3"]').click()
	elif ssh == "no":
		enable = browser.find_element_by_xpath('//*[@id="logintype_3"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="logintype_3"]').click()
		elif enable == False:
			print("已禁用")

	if console == "yes":
		enable = browser.find_element_by_xpath('//*[@id="logintype_4"]').is_selected()
		if enable == True:
			print("已启用")
		elif enable == False:
			browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
	elif console == "no":
		enable = browser.find_element_by_xpath('//*[@id="logintype_4"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="logintype_4"]').click()
		elif enable == False:
			print("已禁用")
	# 输入密码
	browser.find_element_by_xpath('//*[@id="newpwd"]').send_keys(password)
	# 确认密码
	browser.find_element_by_xpath('//*[@id="cfpwd"]').send_keys(confirm_password)
	# 选认状态
	s1 = Select(browser.find_element_by_xpath('//*[@id="status"]'))
	# 选状态下拉框内容
	s1.select_by_visible_text(status)
	# 选认接口
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选接口下拉框内容
	s1.select_by_visible_text(interface)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 输入在线数
	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys(online_num)
	# 清除默认输入
	browser.find_element_by_xpath('//*[@id="permitip1"]').clear()
	# 输入在线数
	browser.find_element_by_xpath('//*[@id="permitip1"]').send_keys(ip1)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 从主页获取系统时间，返回时间字符串--日期 格式例如：  2019-12-20
def get_time_date_lzy(browser):

	into_fun(browser, 系统状态)
	time.sleep(2)
	systime = browser.find_element_by_xpath('//*[@id="home_sys_time"]').text
	date1 = systime.split(' ', 1)[0]
	return date1


# 从主页获取系统时间，返回时间字符串--时间 格式例如：  15:16:25
def get_time_time_lzy(browser):
	into_fun(browser, 系统状态)
	time.sleep(2)
	systime = browser.find_element_by_xpath('//*[@id="home_sys_time"]').text
	time1 = systime.split(' ', 1)[1]
	return time1


# 导出配置-命令行文件
def export_cli_file(browser, mode="all", encry="no", passwd=""):
	into_fun(browser, 配置文件)
	time.sleep(1)
	browser.find_element_by_xpath('//*[@id="export_mode_0"]').click()
	select_mode = Select(browser.find_element_by_xpath('//*[@id="module"]'))
	select_mode.select_by_visible_text(mode)
	if encry == "no":
		if browser.find_element_by_xpath('//*[@id="encrypt"]').is_selected():
			browser.find_element_by_xpath('//*[@id="encrypt"]').click()
	elif encry == "yes":
		if not browser.find_element_by_xpath('//*[@id="encrypt"]').is_selected():
			browser.find_element_by_xpath('//*[@id="encrypt"]').click()
		browser.find_element_by_xpath('//*[@id="ex_password"]').clear()
		browser.find_element_by_xpath('//*[@id="ex_password"]').send_keys(passwd)
		browser.find_element_by_xpath('//*[@id="ex_retype"]').clear()
		browser.find_element_by_xpath('//*[@id="ex_retype"]').send_keys(passwd)
	browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
	time.sleep(2)


# 打开文件，配置export_cli_file使用
def open_file(file_name, return_type="all"):
	data = ""
	f = open(path_download + '\\'+file_name, encoding='utf-8')
	if return_type == "all":
		data = f.read()
	f.close()
	# print(data)
	return data


# 删除chrome下载目录中的所有文件
def del_chrome_download_file_all():
	if os.path.exists(path_download):
		os.chdir(path_download)
		files = os.listdir(path_download)
		for file in files:
			os.remove(file)
