from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *

def add_user_profile_jyl(browser, user_name="", describe="", mumber_of_repeated_login="1", redirect_url="", vpn_properties="",
					 static="", static_ip="", static_ip_start="", static_ip_end="", primary_dns="no", spare_dns="no",
					 primary_wins="no", spare_wins="", welcome_message="", landing_title="", login_succeeded="",
					 login_failed="", save="yes"):

	into_fun(browser, 用户配置)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(user_name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(describe)
	# 输入账号重复次数
	browser.find_element_by_xpath('//*[@id="max_logins"]').clear()
	browser.find_element_by_xpath('//*[@id="max_logins"]').send_keys(mumber_of_repeated_login)
	if redirect_url != "no":
		# 输入重定向URL
		browser.find_element_by_xpath('//*[@id="redirect_url"]').send_keys(redirect_url)
	# 判断是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="is_vpn"]').is_selected()
	if vpn_properties == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="is_vpn"]').click()
		if static == "ip":
			# 点击IP
			browser.find_element_by_xpath('//*[@id="is_static_0"]').click()
			# 输入静态IP
			browser.find_element_by_xpath('//*[@id="static_ip"]').clear()
			browser.find_element_by_xpath('//*[@id="static_ip"]').send_keys(static_ip)
		elif static == "range":
			# 点击IP_range
			browser.find_element_by_xpath('//*[@id="is_static_1"]').click()
			# 输入IP_range_start
			browser.find_element_by_xpath('//*[@id="ip_from"]').send_keys(static_ip_start)
			# 输入IP_range_end
			browser.find_element_by_xpath('//*[@id="ip_to"]').send_keys(static_ip_end)
		if primary_dns != "no":
			# 输入首要DNS
			browser.find_element_by_xpath('//*[@id="primary_dns"]').send_keys(primary_dns)
		if spare_dns != "no":
			# 输入备用DNS
			browser.find_element_by_xpath('//*[@id="secondary_dns"]').send_keys(spare_dns)
		if primary_wins != "no":
			# 输入首要DNS
			browser.find_element_by_xpath('//*[@id="primary_wins"]').send_keys(primary_wins)
		if spare_wins != "no":
			# 输入备用DNS
			browser.find_element_by_xpath('//*[@id="secondary_wins"]').send_keys(spare_wins)
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="is_vpn"]').click()
	# 判断欢迎信息是否勾选
	enable2 = browser.find_element_by_xpath('//*[@id="is_welcome"]').is_selected()
	if welcome_message == "yes":
		if enable2 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="is_welcome"]').click()
		if landing_title != "no":
			# 输入登陆标题
			browser.find_element_by_xpath('//*[@id="login_titletext"]').send_keys(landing_title)
		if login_succeeded != "no":
			# 输入登陆成功
			browser.find_element_by_xpath('//*[@id="login_success"]').send_keys(login_succeeded)
		if login_failed != "no":
			# 输入登陆失败
			browser.find_element_by_xpath('//*[@id="login_fail"]').send_keys(login_failed)
	else:
		if enable2 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="is_welcome"]').click()
	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	elif save == "no":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除添加的用户权限（默认全部删除）
def delete_user_profile_jyl(browser, user_name="all"):
	into_fun(browser, 用户配置)
	# 获取数目
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(br_sum)
	if user_name == "all":
		while br_sum >= 1:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]/a[2]/img').click()
			time.sleep(0.5)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			br_sum = br_sum-1
	else:
		for x in range(2, br_sum+2):
			getbrname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text.rstrip()
			if getbrname == br_sum:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[4]/a[2]/img').click()


# 认证用户-用户配置通过名称查询
def by_name_select_jyl(browser, user_name=""):
	into_fun(browser, 用户配置)
	# 输入名称
	browser.find_element_by_xpath('//*[@id="queryname"]').send_keys(user_name)
	# 点击搜索
	browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/input[1]').click()


# 每页显示函数
def display_per_page(browser, per_page=""):
	into_fun(browser, 用户配置)
	# 选每页下拉框
	s1 = Select(browser.find_element_by_xpath('//*[@id="totalrules"]/select'))
	# 选每页下拉框内容
	time.sleep(0.5)
	s1.select_by_visible_text(per_page)


# 翻页函数，没次只能翻一页
def turn_page(browser, next_page="", next_page_before=""):
	into_fun(browser, 用户配置)
	# 下一页
	if next_page == "yes":
		browser.find_element_by_xpath('//*[@id="totalrules"]/a').click()
	# 前一页
	if next_page_before == "yes":
		browser.find_element_by_xpath('//*[@id="totalrules"]/a').click()

# 增加本地用户
def add_local_user_jyl(browser, user_name="", describe="", authentication_server="", password="", confpassword="",
					   state="", profile_name="", effective_time="", start_time="", end_time="", phone_number="",
					   acl="yes", l2tp="", pptp="", xauth="yes", save=""):
	into_fun(browser, 本地用户)
	# 点击本地用户
	browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
	# 点击增加
	browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
	# 输入名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(user_name)
	# 输入描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(describe)
	# 选认证服务器
	s1 = Select(browser.find_element_by_xpath('//*[@id="server_name"]'))
	# 选服务器下拉框内容
	time.sleep(0.5)
	s1.select_by_visible_text(authentication_server)
	# 输入密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
	# 确认密码
	browser.find_element_by_xpath('//*[@id="confpassword"]').send_keys(confpassword)
	if state == "enable":
		# 点击启用
		browser.find_element_by_xpath('//*[@id="status_enable"]').click()
	elif state == "disable":
		# 点击禁用
		browser.find_element_by_xpath('//*[@id="status_disable"]').click()
	# 选用户profile
	s1 = Select(browser.find_element_by_xpath('//*[@id="profile_name"]'))
	# 选profile下拉框内容
	time.sleep(0.5)
	s1.select_by_visible_text(profile_name)
	# 总是有效
	if effective_time == "always_effective":
		# 点击
		browser.find_element_by_xpath('//*[@id="always_valid"]').click()
	# 有效时间
	elif effective_time == "eff_time":
		# 点击
		browser.find_element_by_xpath('//*[@id="valid_time_from_to"]').click()
		# 输入起始时间
		browser.find_element_by_xpath('//*[@id="expire_from"]').send_keys(start_time)
		# 确认结束时间
		browser.find_element_by_xpath('//*[@id="expire_to"]').send_keys(end_time)
	elif effective_time == "plan_task":
		# 点击
		browser.find_element_by_xpath('//*[@id="valid_schedule"]').click()
		# 选有效计划任务
		s1 = Select(browser.find_element_by_xpath('//*[@id="expire_schedule"]'))
		# 选有效计划任务下拉框内容
		time.sleep(0.5)
		s1.select_by_visible_text(profile_name)
	# 输入手机号码
	browser.find_element_by_xpath('//*[@id="phone"]').send_keys(phone_number)
	# 判断acl是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="vpnattribute_acl"]').is_selected()
	if acl == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="vpnattribute_acl"]').click()
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="vpnattribute_acl"]').click()
	# 判断L2TP是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="a_l2tp"]').is_selected()
	if l2tp == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_l2tp"]').click()
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_l2tp"]').click()
	# 判断PPTP是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="a_pptp"]').is_selected()
	if pptp == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_pptp"]').click()
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_pptp"]').click()
	# 判断XAUTH是否勾选
	enable1 = browser.find_element_by_xpath('//*[@id="a_xauth"]').is_selected()
	if xauth == "yes":
		if enable1 is not True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_xauth"]').click()
	else:
		if enable1 is True:
			# 点击
			browser.find_element_by_xpath('//*[@id="a_xauth"]').click()

	if save == "yes":
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	elif save == "no":
		# 点击取消
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除本地用户（默认全部删除）
def delete_loacl_user_jyl(browser, user_name="all"):
	into_fun(browser, 本地用户)
	# 获取数目
	br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
	# print(br_sum)
	if user_name == "all":
		while br_sum >= 1:
			browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[6]/a[2]/img').click()
			time.sleep(0.5)
			# 点击返回
			browser.find_element_by_xpath('//*[@id="link_but"]').click()
			br_sum = br_sum-1
	else:
		for x in range(2, br_sum+2):
			getbrname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[3]').text.rstrip()
			if getbrname == br_sum:
				browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[6]/a[2]/img').click()




'''
新增认证服务器(完整）
'''
def add_aut_server_lzy(browser, aut_server="RADIUS服务器/LDAP服务器/AD服务器/TACACS服务器/POP3服务器",):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加RADIUS服务器
	if aut_server == 'RADIUS服务器':
		browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[1]').click()
		# 待补充


	# 增加LDAP服务器
	if aut_server == 'LDAP服务器':
		browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[2]').click()

	# 增加AD服务器
	if aut_server == 'AD服务器':
		browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[3]').click()





	# 增加TACACS服务器
	if aut_server == 'TACACS服务器':
		browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[4]').click()

	# 增加POP3服务器
	if aut_server == 'POP3服务器':
		browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[5]').click()

	# # 选interface下拉框 //*[@id="servers_div"]/ul/li[1] //*[@id="servers_div"]/ul/li[2]
	# s1 = Select(browser.find_element_by_xpath('//*[@id="servers_div"]'))
	# # 选interface下拉框内容
	# s1.select_by_visible_text(aut_server)


'''
新增AD认证服务器,参数无误并点击返回
'''
def add_AD_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", domain="", NTLM="yes/no", NTLM2="yes/no", LDAP="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加AD服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[3]').click()
	sleep(0.5)
	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 域名
	browser.find_element_by_xpath('//*[@id="domain"]').send_keys(domain)

	# 认证方式 //*[@id="auth_method_ntlm2"] //*[@id="auth_method_ldap"]
	if NTLM =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm"]').click()
	if NTLM2 =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm2"]').click()
	if LDAP =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ldap"]').click()

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
新增AD认证服务器,参数不规范，点击保存后弹出警告框,并返回警告框内容
'''
def return_alert_add_AD_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", domain="", NTLM="yes/no", NTLM2="yes/no", LDAP="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加AD服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[3]').click()
	sleep(0.5)
	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 域名
	browser.find_element_by_xpath('//*[@id="domain"]').send_keys(domain)

	# 认证方式 //*[@id="auth_method_ntlm2"] //*[@id="auth_method_ldap"]
	if NTLM =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm"]').click()
	if NTLM2 =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm2"]').click()
	if LDAP =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ldap"]').click()

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 获取警告框内容
	sleep(2)
	alert = browser.switch_to_alert().text
	# print(alert)
	# 接受告警
	sleep(2)
	browser.switch_to_alert().accept()
	return alert


'''
新增AD认证服务器,点击保存，返回提示信息
'''
def return_info_add_AD_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", domain="", NTLM="yes/no", NTLM2="yes/no", LDAP="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加AD服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[3]').click()
	sleep(0.5)
	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 域名
	browser.find_element_by_xpath('//*[@id="domain"]').send_keys(domain)

	# 认证方式 //*[@id="auth_method_ntlm2"] //*[@id="auth_method_ldap"]
	if NTLM =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm"]').click()
	if NTLM2 =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm2"]').click()
	if LDAP =="yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ldap"]').click()

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 获取提示框内容
	sleep(2)
	info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	# print(info)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	return info



'''
删除AD认证服务器，按名称
'''
def delete_AD_aut_server_by_name_lzy(browser, name=''):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[2]/img').click()
	sleep(0.5)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()



'''
按名称进入修改AD认证服务器界面
'''
def get_into_change_AD_aut_server_by_name_lzy(browser, name=''):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[1]/img').click()
	sleep(0.5)
	# 进入服务器设置界面




'''
修改AD认证服务器
'''
def change_AD_aut_server_by_name_lzy(browser, name='', description="", server_address="", backup_host_1="",
						  backup_host_2="", domain="", NTLM="yes/no", NTLM2="yes/no", LDAP="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[1]/img').click()
	sleep(0.5)
	# 进入服务器设置界面
	sleep(0.5)
	# # 服务器名称无法修改
	# browser.find_element_by_xpath('//*[@id="name"]').clear()
	# browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').clear()
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').clear()
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').clear()
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 域名
	browser.find_element_by_xpath('//*[@id="domain"]').clear()
	browser.find_element_by_xpath('//*[@id="domain"]').send_keys(domain)

	# 认证方式 //*[@id="auth_method_ntlm2"] //*[@id="auth_method_ldap"]
	if NTLM == "yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm"]').click()
	if NTLM2 == "yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ntlm2"]').click()
	if LDAP == "yes":
		browser.find_element_by_xpath('//*[@id="auth_method_ldap"]').click()

	# 保存
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
删除全部AD认证服务器
'''
def delete_all_AD_aut_server_lzy(browser):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	# 获取总数量（默认存在一条）
	AD_server_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	while int(AD_server_num) > 1:
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/a[2]/img').click()
		sleep(0.5)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		sleep(0.5)
		AD_server_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text





'''
新增LDAP认证服务器,参数无误并点击返回
'''
def add_LDAP_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="389", LDAP="yes/no", basedn="", admin="", password="",
							confirm_password="", timeout="2", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加LDAP服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[2]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# LDAP
	if LDAP =="yes":
		enable = browser.find_element_by_xpath('//*[@id="ldaps"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="ldaps"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="ldaps"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="ldaps"]').click()
		if enable == False:
			pass

	# 基本DN
	browser.find_element_by_xpath('//*[@id="basedn"]').send_keys(basedn)

	# 管理员账号
	browser.find_element_by_xpath('//*[@id="admin"]').send_keys(admin)

	# 密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

	# 确认密码
	browser.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(confirm_password)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
删除认证服务器，按名称（与删除AD同）
'''
def delete_aut_server_by_name_lzy(browser, name=''):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[8]/a[2]/img').click()
	sleep(0.5)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
删除全部认证服务器（与删除AD同）
'''
def delete_all_aut_server_lzy(browser):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	# 获取总数量（默认存在一条）
	AD_server_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
	while int(AD_server_num) > 1:
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]/a[2]/img').click()
		sleep(0.5)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		sleep(0.5)
		AD_server_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text




'''
新增RADIUS认证服务器,参数无误并点击返回
'''
def add_RADIUS_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="1812", retry="3", timeout="2", password="", PAP="yes/no", CHAP="yes/no",
							charging="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加LDAP服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[1]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 重试
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 共享密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

	# PAP
	if PAP =="yes":
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="method"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="method"]').click()
		if enable == False:
			pass
	# CHAP
		if CHAP == "yes":
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				pass
			if enable == False:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
			if enable == False:
				pass


	# 计费
	if charging == "yes":
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		if enable == False:
			pass

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()



'''
修改RADIUS认证服务器,参数无误并点击返回
'''
def change_RADIUS_aut_server_by_name_lzy(browser, name='', description="", server_address="", backup_host_1="",
						  backup_host_2="", port="1812", retry="3", timeout="2", password="", PAP="yes/no", CHAP="yes/no",
							charging="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	sleep(0.5)
	n = 3
	getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
	while getname != name:
		n = n + 1
		getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
	browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[8]/a[1]/img').click()
	sleep(0.5)
	# 进入服务器设置界面
	sleep(0.5)
	# # 服务器名称无法修改
	# browser.find_element_by_xpath('//*[@id="name"]').clear()
	# browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)
	sleep(0.5)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').clear()
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').clear()
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').clear()
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').clear()
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 重试
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 共享密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

	# PAP
	if PAP =="yes":
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="method"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="method"]').click()
		if enable == False:
			pass
	# CHAP
		if CHAP == "yes":
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				pass
			if enable == False:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
			if enable == False:
				pass


	# 计费
	if charging == "yes":
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		if enable == False:
			pass

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()



'''
新增RADIUS认证服务器,参数不规范，点击保存后弹出警告框,并返回警告框内容
'''
def return_alert_add_RADIUS_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="1812", retry="3", timeout="2", password="", PAP="yes/no", CHAP="yes/no",
							charging="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加RADIUS服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[1]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 重试
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 共享密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

	# PAP
	if PAP == "yes":
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="method"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="method"]').click()
		if enable == False:
			pass
		# CHAP
		if CHAP == "yes":
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				pass
			if enable == False:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
			if enable == False:
				pass

	# 计费
	if charging == "yes":
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		if enable == False:
			pass

	# 保存
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
	# 取消
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()

	# 获取警告框内容
	sleep(2)
	alert = browser.switch_to_alert().text
	# print(alert)
	# 接受告警
	sleep(2)
	browser.switch_to_alert().accept()
	return alert


'''
新增RADIUS认证服务器,点击保存，返回提示信息
'''
def return_info_add_RADIUS_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="1812", retry="3", timeout="2", password="", PAP="yes/no", CHAP="yes/no",
							charging="yes/no", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加RADIUS服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[1]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 重试
	browser.find_element_by_xpath('//*[@id="retry"]').clear()
	browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 共享密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)

	# PAP
	if PAP == "yes":
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="method"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="method"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="method"]').click()
		if enable == False:
			pass
		# CHAP
		if CHAP == "yes":
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				pass
			if enable == False:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		else:
			enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
			if enable == True:
				browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
			if enable == False:
				pass

	# 计费
	if charging == "yes":
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
	else:
		enable = browser.find_element_by_xpath('//*[@id="auth_method_1"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="auth_method_1"]').click()
		if enable == False:
			pass

	# 保存
	if save == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()
	# 取消
	if cancel == "yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[3]').click()

	# 获取提示框内容
	sleep(2)
	info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
	# print(info)
	# 点击返回
	browser.find_element_by_xpath('//*[@id="link_but"]').click()

	return info


'''
新增TACACS认证服务器,参数无误并点击返回
'''
def add_TACACS_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="49", timeout="2", share_password="", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加TACACS服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[4]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 超时
	browser.find_element_by_xpath('//*[@id="timeout"]').clear()
	browser.find_element_by_xpath('//*[@id="timeout"]').send_keys(timeout)

	# 共享密码
	browser.find_element_by_xpath('//*[@id="password"]').send_keys(share_password)

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
新增POP3认证服务器,参数无误并点击返回
'''
def add_POP3_aut_server_lzy(browser, server_name="", description="", server_address="", backup_host_1="",
						  backup_host_2="", port="110", save="yes/no", cancel="yes/no"):
	into_fun(browser, 认证服务器)
	# 点击增加
	browser.find_element_by_xpath('//*[@id="add_btn"]').click()
	sleep(0.5)
	# 增加TACACS服务器
	browser.find_element_by_xpath('//*[@id="servers_div"]/ul/li[5]').click()
	sleep(0.5)

	# 服务器名称
	browser.find_element_by_xpath('//*[@id="name"]').send_keys(server_name)

	# 服务器地址
	browser.find_element_by_xpath('//*[@id="ip"]').send_keys(server_address)

	# 描述
	browser.find_element_by_xpath('//*[@id="description"]').send_keys(description)

	# 备用主机1
	browser.find_element_by_xpath('//*[@id="backup1"]').send_keys(backup_host_1)

	# 备用主机2
	browser.find_element_by_xpath('//*[@id="backup2"]').send_keys(backup_host_2)

	# 端口
	browser.find_element_by_xpath('//*[@id="port"]').clear()
	browser.find_element_by_xpath('//*[@id="port"]').send_keys(port)

	# 保存
	if save =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	# 取消
	if cancel =="yes":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

	# 点击返回
	sleep(1)
	browser.find_element_by_xpath('//*[@id="link_but"]').click()


'''
全局设置
'''
def add_globel_setting_lzy(browser, frozen="yes/no", frozen_time="10", retry="3", interval_time="10",
						  phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
						   welcome_info="yes/no", login_title="", login_success="", login_fail="",
						   language="英语/简体中文/繁体中文", keep_current_configuration="yes/no", update="yes/no",
						   file_name="", save="yes/no"):
	'''

	:param browser:
	:param frozen:
	:param frozen_time:
	:param retry:
	:param interval_time:
	:param phone_interval:
	:param idle_time:
	:param sms_center:
	:param HTTP_port:
	:param welcome_info:
	:param login_title:
	:param login_success:
	:param login_fail:
	:param language:
	:param keep_current_configuration:
	:param update:
	:param file_name:
	:param save:
	:return:
	'''
	into_fun(browser, 认证用户设置)
	# 冻结
	if frozen == "yes":
		enable = browser.find_element_by_xpath('//*[@id="is_frozen"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="is_frozen"]').click()
		# 冻结时间
		browser.find_element_by_xpath('//*[@id="frozen_time"]').clear()
		browser.find_element_by_xpath('//*[@id="frozen_time"]').send_keys(frozen_time)

		# 重试次数
		browser.find_element_by_xpath('//*[@id="retry"]').clear()
		browser.find_element_by_xpath('//*[@id="retry"]').send_keys(retry)

		# 间隔时间
		browser.find_element_by_xpath('//*[@id="interval"]').clear()
		browser.find_element_by_xpath('//*[@id="interval"]').send_keys(interval_time)

		# 电话认证时间
		browser.find_element_by_xpath('//*[@id="phone_interval"]').clear()
		browser.find_element_by_xpath('//*[@id="phone_interval"]').send_keys(phone_interval)

	else:
		enable = browser.find_element_by_xpath('//*[@id="is_frozen"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="is_frozen"]').click()
		if enable == False:
			pass


	# 闲置时间
	browser.find_element_by_xpath('//*[@id="idle_time"]').clear()
	browser.find_element_by_xpath('//*[@id="idle_time"]').send_keys(idle_time)

	# 短信中心
	browser.find_element_by_xpath('//*[@id="sms_center"]').clear()
	browser.find_element_by_xpath('//*[@id="sms_center"]').send_keys(sms_center)

	# HTTP端口（若有更改，点击保存后，需接受告警且等待几秒，再刷新界面，界面回到首页）
	HTTP_port_init = browser.find_element_by_xpath('//*[@id="http_port"]').get_attribute('value')
	# print(HTTP_port_init)
	browser.find_element_by_xpath('//*[@id="http_port"]').clear()
	browser.find_element_by_xpath('//*[@id="http_port"]').send_keys(HTTP_port)


	# 欢迎信息
	if welcome_info == "yes":
		enable = browser.find_element_by_xpath('//*[@id="is_welcome"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="is_welcome"]').click()
		# 登录标题
		browser.find_element_by_xpath('//*[@id="login_titletext"]').clear()
		browser.find_element_by_xpath('//*[@id="login_titletext"]').send_keys(login_title)

		# 登录成功
		browser.find_element_by_xpath('//*[@id="login_success"]').clear()
		browser.find_element_by_xpath('//*[@id="login_success"]').send_keys(login_success)

		# 登陆失败
		browser.find_element_by_xpath('//*[@id="login_fail"]').clear()
		browser.find_element_by_xpath('//*[@id="login_fail"]').send_keys(login_fail)

	else:
		enable = browser.find_element_by_xpath('//*[@id="is_welcome"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="is_welcome"]').click()
		if enable == False:
			pass

	# 客户端设置
	# 语言
	s1 = Select(browser.find_element_by_xpath('//*[@id="conftr_11"]/td[2]/select'))
	s1.select_by_visible_text(language)

	# 背景设置
	# 保留当前设置
	if keep_current_configuration == "yes":
		enable = browser.find_element_by_xpath('//*[@id="modifybg_hide"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="modifybg_hide"]').click()

	else:
		enable = browser.find_element_by_xpath('//*[@id="modifybg_hide"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="modifybg_hide"]').click()
		if enable == False:
			pass

	# 更新
	if update == "yes":
		enable = browser.find_element_by_xpath('//*[@id="modifybg_show"]').is_selected()
		if enable == True:
			pass
		if enable == False:
			browser.find_element_by_xpath('//*[@id="modifybg_show"]').click()
		# 选择文件（以后补全）
		print(file_name)


	else:
		enable = browser.find_element_by_xpath('//*[@id="modifybg_show"]').is_selected()
		if enable == True:
			browser.find_element_by_xpath('//*[@id="modifybg_show"]').click()
		if enable == False:
			pass

	# 若修改HTTP端口
	if HTTP_port_init == HTTP_port:
		if save == "yes":
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
			# 点击返回
			sleep(1)
			browser.find_element_by_xpath('//*[@id="link_but"]').click()

	else:
		if save == "yes":
			# 点击保存
			browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
			# 接受告警
			browser.switch_to_alert().accept()
			# 等待10秒 刷新界面 进入全局设置界面
			sleep(5)
			refresh(browser)
			into_fun(browser, 认证用户设置)
			sleep(1)








