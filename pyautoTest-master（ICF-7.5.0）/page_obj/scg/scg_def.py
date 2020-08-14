import time
import os
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_mac import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_multi_gateway_group import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_multi_gateway_group import *
from page_obj.scg.scg_def_monitor import *
from page_obj.scg.scg_def_multi_isp import *


# 登录函数
def login_web(browser, url="10.2.2.81", username="admin", password="admin@139", verificationCode="0613", new="no"):

	"""
	:param browser: pytest的浏览器类
	:param url: 设备管理地址
	:param username: 输入账号
	:param password: 登入密码
	:param verificationCode: 验证码
	:param new: 是否打开新的界面，为加快测试速度而添加
	:return: null
	"""
	# 开始时先清除一下cookie
	# cookies = browser.get_cookies()
	# print(f"main: cookies = {cookies}")
	# browser.delete_all_cookies()

	# print('\n', "1:", time.ctime())
	check_alert(browser)
	# print("2:", time.ctime())
	try:

		# 整体跑时有问题，经常会出现两个标签，用一下办法检测当出现多个标签时，及时关闭无用标签，但是该问题后续再找
		# 或者当前所有标签的句柄
		handles = browser.window_handles
		# print(handles)
		# 当handles的长度大于1时，说明已经出现问题
		if len(handles) > 1:
			# 切到第二个标签，并关闭它
			for newhandle in handles:
				# 筛选新打开的窗口B
				# print(newhandle)
				if newhandle != handles[0]:
					# 切换到新打开的窗口B
					# print(newhandle)
					browser.switch_to_window(newhandle)
					# 关闭当前窗口B
					browser.close()
					# 切换回窗口A
					browser.switch_to_window(handles[0])
		# 这个刷新可以解决如果设备进行了重启，无法获取到界面信息的问题
		browser.refresh()
		# time.sleep(1)
		# browser.refresh()
		# time.sleep(0.5)
		web_title = browser.current_url
		# print("\n@@@@@@@@@@@@@")
		# print(web_title)
		# print("@@@@@@@@@@@@@")
		# 当设备进行了重启，这时URL依旧存在地址信息，但是界面会跳转到登录界面，则进行下一步是不会获取到title
		if url not in web_title:
			new = "yes"
	except:
		pass
	# print("3.5:", time.ctime())
	check_alert(browser)
	# print("3.6:", time.ctime())
	if new == "no":
		# 获取设备模块标题文字，如果没有获取到，则进行重新登入
		try:
			into_fun(browser, 系统状态)
			browser.switch_to.default_content()
			browser.switch_to.frame("header")
			title = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text
			# # print("--登入函数的调试信息--，打印获取到的标题："+str(title))
			# # browser.refresh()
			# browser.switch_to.default_content()
			# browser.switch_to.frame("lefttree")
		except Exception as err1:
			print(err1)
			# print('文件', err1.__traceback__.tb_frame.f_globals['__file__'])
			# print('行号', err1.__traceback__.tb_lineno)
			print("设备可能重启了，重新登入，并清除一次cookies", url)
			cookies = browser.get_cookies()
			# print(f"main: cookies = {cookies}")
			browser.delete_all_cookies()
			# 打开 SCG web
			time.sleep(0.5)
			browser.get("https://" + url)
			# browser.get("https://" + url)
			# 输入帐号
			browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
			# 输入密码
			browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
			# 验证码0613
			browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
				verificationCode)
			# 点击登入
			browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
			# 登入后，定位到左侧frame
			browser.switch_to.frame("lefttree")
	else:
		# 打开 SCG web
		try:
			title1 = "NULL"
			loop_max_login = 0
			while title1 == "NULL" and loop_max_login < 5:
				# print("没有获取到主页信息，准备重新获取", loop_max_login, title1)
				browser.get("https://" + url)
				# 输入帐号
				time.sleep(1)
				browser.find_element_by_xpath("//*[@id='input_username']").send_keys(username)
				# 输入密码
				browser.find_element_by_xpath("//*[@id='input_password']").send_keys(password)
				# 验证码0613
				browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys(
					verificationCode)
				# 点击登入
				browser.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
				browser.switch_to.default_content()
				browser.switch_to.frame("header")
				title1 = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text
				# 登入后，定位到左侧frame
				browser.switch_to.default_content()
				browser.switch_to.frame("lefttree")
				loop_max_login += 1

		except Exception as err1:
			print(err1)
	# print("4:", time.ctime())

# 添加单网关路由
def add_ipRoute(browser, destination_ip, destination_mask, out_device, gateway):

	# browser.switch_to.default_content()
	#
	# browser.switch_to.frame("lefttree")
	# #定位到左侧frame
	#
	# browser.find_element_by_xpath('/html/body/div[1]/div[3]/header/a').click()
	# #点击路由
	#
	# browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/ul/li[1]/span/a').click()
	# #点击静态路由
	#
	# browser.switch_to.default_content()
	# #定位到默认frame
	#
	# browser.switch_to.frame("content")
	# #定位到内容frame
	into_fun(browser, 静态路由)
	browser.find_element_by_xpath('/html/body/div[1]/form/div[2]/div/input[2]').click()
	#点击单网关路由

	browser.find_element_by_xpath('//*[@id="destination_ip"]').send_keys(destination_ip) 
	#输入DesIPadd

	browser.find_element_by_xpath('//*[@id="destination_mask"]').send_keys(destination_mask) 
	#输入netmask

	outInter = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))    
	#定位到出接口的下拉框

	outInter.select_by_visible_text(out_device)
	#选择出接口

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').clear()
	#clear gateway

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
	#input gateway
	
	#点击保存
	browser.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div[2]/div/input[2]').click() 


# 保存配置
def save_sys(browser):
	
	browser.switch_to.default_content()
	# 定位到默认frame
	browser.switch_to.frame("topheader")
	# 登入后，定位到导航frame
	# browser.find_element_by_xpath('/html/body/nav/ul/li[3]/a').click()
	browser.find_element_by_xpath('//*[text()="保存"]').click()
	# 点击”保存“
	browser.switch_to_alert().accept()
	# 接受告警
	time.sleep(3)
	# 接受告警
	browser.switch_to_alert().accept()


# 保存系统配置
def save_sys_inhand(browser):
	
	browser.switch_to.default_content()
	# 定位到默认frame

	browser.switch_to.frame(browser.find_element_by_xpath("/html/frameset/frame"))
	# 登入后，定位到导航frame

	browser.find_element_by_xpath('/html/body/nav/ul/li[2]/a').click() 
	# 点击”保存“

	browser.switch_to_alert().accept()
	# 接受告警

	time.sleep(3)
	
	# 接受告警
	browser.switch_to_alert().accept()


# 设置ssh在线用户数
def set_ssh32user(browser):

	# browser.find_element_by_xpath("/html/body/div[1]/div[1]/header/a").click()
	# #点击”系统“
	#
	# browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul/li[2]/ul/li[1]/span/a").click()
	# #点击”管理员“
	#
	# browser.switch_to.default_content()
	# #定位到默认frame
	#
	# browser.switch_to.frame("content")
	# #定位到内容frame
	into_fun(browser, 管理员)
	browser.find_element_by_xpath("/html/body/div[1]/div[3]/form/div/table/tbody/tr[2]/td[11]/a/img").click()
	# 点击管理员编辑

	browser.find_element_by_xpath('//*[@id="logintype_3"]').click() 
	# 点击SSH

	browser.find_element_by_xpath('//*[@id="newpwd"]').clear()
	# 清除密码

	browser.find_element_by_xpath('//*[@id="onlinenum"]').clear()
	# 清除在线用户数

	browser.find_element_by_xpath('//*[@id="onlinenum"]').send_keys("32")
	# 添加在线用户数

	browser.find_element_by_xpath('/html/body/div[1]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击保存

	time.sleep(5)

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加远程网关（使用sm1和sm3算法）
def add_ipsecRemoteGW_inhand(browser, ipsecRGWname,ipsecRGWinterSeq,ipsecRGWgateway,localid,remoteid,localsubnet,remotesubnet):

	browser.switch_to.default_content()
	# 定位到默认frame

	browser.switch_to.frame("lefttree")
	# 登入后，定位到左侧frame

	browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	# 点击”虚拟专网“

	browser.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[3]/span/a').click()
	# 点击”远程网关“

	browser.switch_to.default_content()
	# 定位到默认frame

	browser.switch_to.frame("content")
	# 定位到内容frame

	browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click() 
	# 点击”增加远程网关“

	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="name"]').send_keys(ipsecRGWname)
	# 输入name

	time.sleep(1)
		
	localif = Select(browser.find_element_by_xpath('//*[@id="localif"]'))   

	localif.select_by_visible_text(ipsecRGWinterSeq)
		
	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(ipsecRGWgateway)
	# 输入remote IP add
		
	time.sleep(1)

	browser.find_element_by_xpath('//*[@id="localid"]').send_keys(localid)
	# input local ID

	# browser.find_element_by_xpath('//*[@id="preshared_key"]').send_keys(preshared_key)
	# input republicKey
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="remoteid"]').send_keys(remoteid)
	# input remote ID

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').clear()
	# clear loacl subnet text

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="localsubnet"]').send_keys(localsubnet) 
	# input local subnet

	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys(remotesubnet)
	# input remote subnet
		
	time.sleep(1)
	
	browser.find_element_by_xpath('/html/body/form/div[1]/div/div[2]/div[1]/table/tbody/tr[16]/td[1]/a').click()
	# 点击”高级“
	
	localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))   
	#Phase 1 encry
	
	localif.select_by_visible_text("sm1")
	
	localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))   
	# Phase 1 auth
	
	localif.select_by_visible_text("sm3")

	localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))   
	# Phase 2 esp_encry
	
	localif.select_by_visible_text("sm1")
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))   
	# Phase 2 esp_auth
	
	localif.select_by_visible_text("sm3")
	
	browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click() 
	# 点击”return“
		
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	# 点击”保存“
		
	time.sleep(1)
		
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	# 点击”return“


# 刷新界面
def refresh(browser):
	browser.refresh()


# 编辑虚拟专网远程网关
def edit_ipsecRemoteGW_inhand(browser, ipsecRGWSeq, encry_1, auth_1, esp_encry_2, esp_auth_2):

	browser.switch_to.default_content()
	# 定位到默认frame

	browser.switch_to.frame("lefttree")
	# 登入后，定位到左侧frame

	browser.find_element_by_xpath("/html/body/div[1]/div[6]/header/a").click()
	# 点击”虚拟专网“

	browser.find_element_by_xpath('/html/body/div[1]/div[6]/div/ul/li[3]/span/a').click()
	# 点击”远程网关“

	browser.switch_to.default_content()
	# 定位到默认frame

	browser.switch_to.frame("content")
	# 定位到内容frame

	browser.find_element_by_xpath(ipsecRGWSeq).click() 
	# 点击要编辑的ipsec

	time.sleep(5)
	
	browser.find_element_by_xpath('//*[@id="conftr_31"]/td[1]/a').click()
	# 点击”高级“       //*[@id="conftr_31"]/td[1]/a
	
	localif = Select(browser.find_element_by_xpath('//*[@id="encry_alg"]'))   
	# Phase 1 encry
	
	localif.select_by_visible_text(encry_1)
	
	localif = Select(browser.find_element_by_xpath('//*[@id="auth_alg"]'))   
	# Phase 1 auth
	
	localif.select_by_visible_text(auth_1)

	localif = Select(browser.find_element_by_xpath('//*[@id="esp_encry_alg"]'))   
	# Phase 2 esp_encry
	
	localif.select_by_visible_text(esp_encry_2)
	
	localif = Select(browser.find_element_by_xpath('//*[@id="esp_auth_alg"]'))   
	# Phase 2 esp_auth
	
	localif.select_by_visible_text(esp_auth_2)
	
	browser.find_element_by_xpath('/html/body/form/div[2]/div/div[2]/div[2]/div/input').click() 
	# 点击”return“
		
	browser.find_element_by_xpath('//*[@id="btn_save"]').click()
	#点击”保存“


# 语言切换
def language_switch(browser, language="China"):
	# 登入后，定位到默认frame
	browser.switch_to.default_content()

	# 登入后，定位到导航frame
	browser.switch_to.frame("topheader")

	# 点击语言						# /html/body/nav/ul/li[1]/a
	browser.find_element_by_xpath('/html/body/nav/ul/li[1]/a/span').click()

	if language == "English":
		# 点击英语
		browser.find_element_by_xpath('// *[ @ id = "lang_bar"] / a[1]').click()

	elif language == "China":
		# 点击中文
		browser.find_element_by_xpath('//*[@id="lang_bar"]/a[2]').click()

	else:
		# 点击繁体中文
		browser.find_element_by_xpath('//*[@id="lang_bar"]/a[3]').click()

	# 定位到默认frame
	browser.switch_to.default_content()


def check_alert(browser):
	browser.implicitly_wait(0.5)
	try:
		# print("Alert exists")

		# alert = browser.switch_to_alert()
		# print(alert.text)
		# alert.accept()
		alert_info = "init"
		while alert_info is not None:
			alert = browser.switch_to_alert()
			alert_info = alert.text
			print(alert_info)
			alert.accept()
	except:
		# print("无警告，点击返回")
		try:
			browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()
		except:
			# print("无点击返回")
			pass


# 重启设备函数，当不填入主机IP时，不进行真正的重启操作，重启后默认等待70S，用于设备启动
def reload(hostip="", user="admin", passwd="admin@139", reloadtime=63, switch="重启", port=22):
	# 重启操作前，先检查一下界面是否有告警出现，如果有，接受一下，保证重启执行正常。
	# check_alert(browser)
	# 已经在登录时进行检查
	try:
		if switch == "重启":
			# 如果是传入的hostip是列表，将先重启再延时70秒
			if type(hostip) is list:
				for x in hostip:
					print(x)
					to_scg = Shell_SSH()
					to_scg.connect(x, user, passwd, po=port)
					to_scg.execute("en")
					time.sleep(2)
					to_scg.execute("reload pytest")
					time.sleep(1)
					to_scg.execute("yes")
					# ssh_info1 = to_scg.output()
					# print(ssh_info1)
					print("正在重启设备:" + x + "等待：" + str(reloadtime) + "秒")
					to_scg.close()
				time.sleep(reloadtime)
			else:
				to_scg = Shell_SSH()
				to_scg.connect(hostip, user, passwd, po=port)
				to_scg.execute("en")
				time.sleep(2)
				to_scg.execute("reload pytest")
				time.sleep(1)
				to_scg.execute("yes")
				time.sleep(0.5)
				to_scg.close()
				# ssh_info1 = to_scg.output()
				# print(ssh_info1)
				print("正在重启设备:" + hostip + "等待：" + str(reloadtime) + "秒")
				time.sleep(reloadtime)

		else:
			print("模拟正在重启设备。。，请传入正确的ip地址参数")
	except:
		print("连接SSH失败，请手动检查")


def location_lefttree(browser):
	"""登入后，定位到左侧frame"""
	browser.switch_to.frame("lefttree")


def location_default_frame(browser):
	"""
	定位到默认frame
	:param ipsec:
	:return:
	"""
	# 定位到默认frame
	browser.switch_to.default_content()

	# 定位到内容frame
	browser.switch_to.frame("content")


# 设置系统信息
def sys_information_modify(browser, Hoetmane="BASFE", Location="location", Description="description",Contact="contact"):
	"""
	系统信息修改
	:param browser:
	:param Hoetmane:
	:param Location:
	:param Description:
	:param Contact:
	:return:
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 清除主机名默认输入内容，并输入主机名
	browser.find_element_by_xpath('//*[@id="hostname"]').clear()
	browser.find_element_by_xpath('//*[@id="hostname"]').send_keys(Hoetmane)

	# 清除地点默认输入内容，并输入地点
	browser.find_element_by_xpath('//*[@id="hostname"]').clear()
	browser.find_element_by_xpath('//*[@id="location"]').send_keys(Location)

	# 清除描述默认输入内容，并输入描述
	browser.find_element_by_xpath('//*[@id="hostname"]').clear()
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(Description)

	# 清除联系信息默认输入内容，并输入联系信息
	browser.find_element_by_xpath('//*[@id="hostname"]').clear()
	browser.find_element_by_xpath('//*[@id="contact"]').send_keys(Contact)


# 给接口添加IP地址
def add_interface_address(browser, ip="192.168.168.23", mask="24"):
	"""
	接口ip,mask的添加
	:param browser:
	:param ip:
	:param mask:
	:return:
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 选择接口的Xpath
	# //*[@id="table"]/tbody/tr[2]/td[9]/a/img	#(ge0/1)
	# //*[@id="table"]/tbody/tr[3]/td[9]/a/img	#(ge0/2)
	# //*[@id="table"]/tbody/tr[4]/td[9]/a/img	#(ge0/3)
	# //*[@id="table"]/tbody/tr[5]/td[9]/a/img	#(ge0/4)
	# //*[@id="table"]/tbody/tr[6]/td[9]/a/img	#(ge0/5)
	# //*[@id="table"]/tbody/tr[7]/td[9]/a/img	#(ge0/6)

	# 点击接口的编辑按钮
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[9]/a/img').click()

	# 填ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)

	# 填掩码
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
	time.sleep(1)

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(1)


# 添加子接口
def vlan_add(browser, VLAN_ID="220", describe="vlan"):
	"""
	子接口添加
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

	# 选择接口下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="port"]'))
	# 选择接口
	s1.select_by_visible_text("ge0/2")

	# 输入VLAN ID
	browser.find_element_by_xpath('//*[@id="vlanid"]').send_keys(VLAN_ID)

	# //*[@id="work_mode_0"]	#(路由模式)
	# //*[@id="work_mode_1"]	#(透明模式）
	# 选择工作模式
	browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()

	# 选择SNAT(若不需要选择，则注释掉这条语句)
	browser.find_element_by_xpath('//*[@id="snat"]').click()

	# 选择允许回应Ping包(默认为允许)
	# browser.find_element_by_xpath('//*[@id="allowping"]').click()

	# 输入describe vlan 内容
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(describe)

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 子接口IP添加IP地址
def valn_ip_add(browser, ip="192.170.12.2", mask="24"):
	"""
	子接口ip添加
	:param browser:
	:param ip:
	:param mask:
	:return:
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击接口的编辑(若选择下面的编辑按钮，只需要改变tr[ ]中的值即可，且第一条的值为2，后面的依次累加1即可)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/a[1]/img').click()

	# //*[@id="work_mode_0"]	#(路由模式)
	# //*[@id="work_mode_1"]	#(透明模式）
	# 选择工作模式
	browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()

	# //*[@id="address_mode_0"]	#(静态)
	# //*[@id="address_mode_1"]	#(DHCP）
	# 选择地址模式
	browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()

	# 填ip
	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)

	# 填掩码
	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)

	# 选择SNAT(若不需要选择，则注释掉这条语句)
	browser.find_element_by_xpath('//*[@id="snat"]').click()

	# 选择允许回应Ping包(默认为允许)
	# browser.find_element_by_xpath('//*[@id="allow_ping"]').click()

	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加网桥
def bridge_add(browser, describe="bridge", add_mem="yes"):
	"""
	网桥添加
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	time.sleep(1)

	# 添加描述
	browser.find_element_by_xpath('//*[@id="des"]').send_keys(describe)
	if add_mem == "yes":
		# 选物理成员接口下拉框(接口必须是透明模式)
		s1 = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))

		# 选物理成员接口下拉框内容
		s1.select_by_visible_text(interface_name_4)

		# //*[@id="conftr_1"]/td[3]/input[1]		#右移
		# //*[@id="conftr_1"]/td[3]/input[2]		#左移
		# 点击右移
		browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()

		# 选择源SNAT(若不需要选择，则注释掉这条语句)(默认为关)
		# browser.find_element_by_xpath('//*[@id="snat"]').click()

		# 选择允许回应Ping包(若不需要选择，则注释掉这条语句)(默认为开)
		# browser.find_element_by_xpath('//*[@id="ping"]').click()

		# 选择阻止网桥通信(若不需要选择，则注释掉这条语句)(默认为关)
		# browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()

		# 选择Spanning Tree(若不需要选择，则注释掉这条语句)(默认为关)
		# browser.find_element_by_xpath('//*[@id="stp"]').click()

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(1)

	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()
	time.sleep(1)


# def bridge_ip_add(browser, describe="bridge", ip="192.171.23.2", mask="24"):
# 	"""
# 	桥ip添加
# 	:param browser:
# 	:param describe:
# 	:param ip:
# 	:param mask:
# 	:return:
# 	"""
# 	# 定位到默认frame
# 	browser.switch_to.default_content()
# 	# 定位到内容frame
# 	browser.switch_to.frame("content")
#
# 	# 添加描述
# 	browser.find_element_by_xpath('//*[@id="desc"]').send_keys(describe)
#
# 	# 选物理成员接口下拉框(接口必须是透明模式)
# 	s1 = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))
# 	# 选物理成员接口下拉框内容
# 	s1.select_by_visible_text(interface_name_4)
#
# 	# //*[@id="conftr_1"]/td[3]/input[1]		#右移
# 	# //*[@id="conftr_1"]/td[3]/input[2]		#左移
# 	# 点击右移
# 	browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
#
# 	# //*[@id="address_mode_0"]	#静态
# 	# //*[@id="address_mode_1"]	#DHCP
# 	# 选择地址模式
# 	browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
#
# 	# 添加ip
# 	browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
#
# 	# 添加mask
# 	browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
#
# 	# 选择源SNAT(若不需要选择，则注释掉这条语句)(默认为关)
# 	# browser.find_element_by_xpath('//*[@id="snat"]').click()
#
# 	# 选择允许回应Ping包(若不需要选择，则注释掉这条语句)(默认为开)
# 	# browser.find_element_by_xpath('//*[@id="allow_ping"]').click()
#
# 	# 选择阻止网桥通信(若不需要选择，则注释掉这条语句)(默认为关)
# 	# browser.find_element_by_xpath('//*[@id="block_intra_traffic"]').click()
#
# 	# 选择Spanning Tree(若不需要选择，则注释掉这条语句)(默认为关)
# 	# browser.find_element_by_xpath('//*[@id="stp"]').click()
#
# 	# 点击保存
# 	browser.find_element_by_xpath(
# 		'//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
# 	time.sleep(1)
#
# 	# 点击返回
# 	browser.find_element_by_xpath('//*[@id="link_but"]').click()
# 	time.sleep(1)


# 添加IP_MAC绑定列表
def IP_MAC_Binding_add(browser, ip="192.175.23.2", mac="00:16:31:f8:5d:7b", hostname="pc"):
	"""
		IP_MAC_Binding列表添加
		:param browser:
		:param ip:
		:param mac:
		:param hostname:
		:return:
		"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击绑定列表
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()

	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[4]').click()

	# 添加ip地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(ip)

	# 选择接口下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="dev"]'))
	# 选择接口
	s1.select_by_visible_text("ge0/1")

	# 添加mac地址
	browser.find_element_by_xpath('//*[@id="mac"]').send_keys(mac)

	browser.find_element_by_xpath('//*[@id="host"]').send_keys(hostname)
	# 添加主机名

	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 点击保存
	time.sleep(3)


# 添加DHCP设定
def DHCP_set_add(browser):
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 选择接口下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
	# 选择接口
	s1.select_by_visible_text("ge0/1")

	# 点击增加
	browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()

	# 点击返回
	browser.find_element_by_xpath('// *[ @ id = "link_but"]').click()

	# 点击取消
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 添加DHCP服务器
def DHCP_Server_add(browser, DNS_Server1, WINS_Server1, DNS_Server2, WINS_Server2, DNS_Server3, WINS_Server3, \
					DNS_Server4, WINS_Server4, domain_name, static_ip, static_mac, gateway="192.170.16.1", \
					mask="255.255.255.0", ip_range1_1="192.173.12.5", ip_range1_2="192.173.12.25", \
					ip_range2_1="192.174.12.5", ip_range2_2="192.174.12.25", ip_range3_1="192.175.12.5", \
					ip_range3_2="192.175.12.25", day="7", hour="0", second="0"):
	"""
	添加DHCP之后，点击添加接口的编辑按钮，选择DHCP服务器
	:param browser:
	:param gateway:
	:param mask:
	:param DNS_Server1:
	:param WINS_Server1:
	:param ip_range1_1:
	:param ip_range1_2:
	:param ip_range2_1:
	:param ip_range2_2:
	:param ip_range3_1:
	:param ip_range3_2:
	:param day:
	:param hour:
	:param second:
	:param DNS_Server2:
	:param WINS_Server2:
	:param DNS_Server3:
	:param WINS_Server3:
	:param DNS_Server4:
	:param WINS_Server4:
	:param domain_name:
	:param static_ip:
	:param static_mac:
	:param static_ip_add:
	:param static_mac_add:
	:return:
	"""
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击添加完成之后的某一接口编辑按钮(若选择下面的编辑按钮，只需要改变tr[ ]中的值即可，且第一条的值为2，后面的依次累加1即可)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[1]/img').click()

	# 点击DHCP Server
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[1]/img').click()

	# 添加网关
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)

	# 添加子网掩码
	browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(mask)

	# 添加DNS服务器1
	browser.find_element_by_xpath('//*[@id="dnsserver1"]').send_keys(DNS_Server1)

	# 添加WINS服务器1
	browser.find_element_by_xpath('//*[@id="winsserver1"]').send_keys(WINS_Server1)

	# 添加IP范围1
	browser.find_element_by_xpath('//*[@id="ipfrom1"]').send_keys(ip_range1_1)
	browser.find_element_by_xpath('//*[@id="ipto1"]').send_keys(ip_range1_2)

	# 添加IP范围2
	browser.find_element_by_xpath('//*[@id="ipfrom2"]').send_keys(ip_range2_1)
	browser.find_element_by_xpath('//*[@id="ipto2"]').send_keys(ip_range2_2)

	# 添加IP范围3
	browser.find_element_by_xpath('//*[@id="ipfrom3"]').send_keys(ip_range3_1)
	browser.find_element_by_xpath('//*[@id="ipto3"]').send_keys(ip_range3_2)

	# 先清除日的默认输入
	# 租约时间,日,时,秒
	browser.find_element_by_xpath('//*[@id="day"]').clear()
	browser.find_element_by_xpath('//*[@id="day"]').send_keys(day)
	browser.find_element_by_xpath('//*[@id="hour"]').send_keys(hour)
	browser.find_element_by_xpath('//*[@id="minute"]').send_keys(second)

	# 点击高级设置
	browser.find_element_by_xpath('//*[@id="is_dhcp_adv"]').click()

	# 添加DNS服务器2
	browser.find_element_by_xpath('//*[@id="dnsserver2"]').send_keys(DNS_Server2)

	# 添加WINS服务器2
	browser.find_element_by_xpath('//*[@id="winsserver2"]"]').send_keys(WINS_Server2)

	# 添加DNS服务器3
	browser.find_element_by_xpath('//*[@id="dnsserver3"]').send_keys(DNS_Server3)

	# 添加WINS服务器3
	browser.find_element_by_xpath('//*[@id="winsserver3"]').send_keys(WINS_Server3)

	# 添加DNS服务器4
	browser.find_element_by_xpath('//*[@id="dnsserver4"]').send_keys(DNS_Server4)

	# 添加WINS服务器4
	browser.find_element_by_xpath('//*[@id="winsserver4"]').send_keys(WINS_Server4)

	# 添加域名
	browser.find_element_by_xpath('//*[@id="domainname"]').send_keys(domain_name)

	# 静态ip与静态mac添加
	browser.find_element_by_xpath('//*[@id="ip0"]').send_keys(static_ip)
	browser.find_element_by_xpath('//*[@id="mac0"]').send_keys(static_mac)
	"""
		#增加/删除多个 静态ip与静态mac
		#//*[@id="add_staticip_link"]	#(增加)
		#//*[@id="del_staticip_link"]	#(删除)
		#browser.find_element_by_xpath('//*[@id="add_staticip_link"]').click()
		#输入静态ip与静态mac
		#browser.find_element_by_xpath('//*[@id="ip1"]').send_keys(static_ip_add)
		#browser.find_element_by_xpath('//*[@id="mac1"]').send_keys(static_mac_add)
		"""


# 添加DHCP中继服务器
def DHCP_Relay_add(browser, DHCP_Relay_Server1, DHCP_Relay_Server2, DHCP_Relay_Server3):
	# 定位到默认frame
	browser.switch_to.default_content()
	# 定位到内容frame
	browser.switch_to.frame("content")

	# 点击添加完成之后的某一接口编辑按钮(若选择下面的编辑按钮，只需要改变tr[ ]中的值即可，且第一条的值为2，后面的依次累加1即可)
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[7]/a[1]/img').click()

	# 点击DHCP Relay
	browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()

	# 添加DHCP中继服务器1
	browser.find_element_by_xpath('//*[@id="relay_server1"]').send_keys(DHCP_Relay_Server1)

	# 添加DHCP中继服务器2
	browser.find_element_by_xpath('//*[@id="relay_server2"]').send_keys(DHCP_Relay_Server2)

	# 添加DHCP中继服务器3
	browser.find_element_by_xpath('//*[@id="relay_server3"]').send_keys(DHCP_Relay_Server3)


# 删除管理员列表所有管理员（不包括默认管理员）
def delete_all_admin_list_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath(display_系统管理).is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到内容frame
	# browser.switch_to.frame("content")
	# 点击管理员列表
	browser.refresh()
	into_fun(browser, 管理员)
	browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
	time.sleep(0.5)
	# 获取页面配置数
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	i = 1
	while i < int(num1):
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[11]/a[2]/img').click()
		time.sleep(0.5)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		i += 1


# 删除所有管理员权限（不包扩默认权限）
def delete_all_admin_profile_jyl(browser):
	# 定位到默认frame
	browser.refresh()
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath(系统管理).click()
	# # 点击物理接口
	# browser.find_element_by_xpath(管理员).click()
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 管理员)
	# 点击管理员权限
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	time.sleep(2)
	# 获取页面配置数
	num2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	i = 3
	while i < int(num2):
		# 点击删除
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[6]/a[2]/img').click()
		time.sleep(1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(1)
		i += 1


# 注销、登出
def sign_out_jyl(browser):
	# 登入后，定位到默认frame
	browser.switch_to.default_content()

	# 登入后，定位到导航frame
	browser.switch_to.frame("topheader")

	# 点击退出
	browser.find_element_by_xpath('//*[text()="退出"]').click()
	# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

# 保存配置 -1
def save_configer(browser):
	# 登入后，定位到默认frame
	browser.switch_to.default_content()
	# 登入后，定位到导航frame
	browser.switch_to.frame("topheader")
	# 点击保存
	browser.find_element_by_xpath('//*[@id="save_sta"]').click()
	time.sleep(2)
	# 接受告警
	browser.switch_to_alert().accept()
	time.sleep(2)
	# 接受告警
	browser.switch_to_alert().accept()


# 登陆错误的登陆函数，用来测试需要错误登陆的测试用例
def login_web_fail(browser, url="10.2.2.81", username="admin", password="admin@139", verificationCode="0613", new="no"):

	"""
	:param browser: pytest的浏览器类
	:param url: 设备管理地址
	:param username: 输入账号
	:param password: 登入密码
	:param verificationCode: 验证码
	:param new: 是否打开新的界面，为加快测试速度而添加
	:return: null
	"""
	try:
		web_title = browser.current_url
		# print("@@@@@@@@@@@@@")
		# print(web_title)
		# print("@@@@@@@@@@@@@")
		if url not in web_title:
			new = "yes"
	except:
		pass

	if new == "no":
		# 获取设备模块标题文字，如果没有获取到，则进行重新登入
		try:
			# browser.switch_to.default_content()
			# browser.switch_to.frame("lefttree")
			# browser.find_element_by_xpath(系统).click()
			# browser.find_element_by_xpath(系统状态).click()
			# time.sleep(1)
			into_fun(browser, 系统状态)
			browser.switch_to.default_content()
			browser.switch_to.frame("header")
			title = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text
			# print("--登入函数的调试信息--，打印获取到的标题："+str(title))
			browser.switch_to.default_content()
			browser.switch_to.frame("lefttree")
		except Exception as err1:
			# print(err1)
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
	else:
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


