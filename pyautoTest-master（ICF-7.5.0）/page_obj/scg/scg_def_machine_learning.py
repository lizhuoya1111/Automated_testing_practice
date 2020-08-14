import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *
from page_obj.common.ssh import *


# tcpreplay重放报文,前提是81的interface4=20.1.1.1,透明inteface5和inteface6的网桥=21.1.1.1
def icf_replay(pcap_type="Oracle", server_ip="10.1.1.211", user="root", passwd="arsenal", hostadd1="121.1.1.120", hostadd2="121.1.1.20"):
	in_interface = "eth2"
	out_interface = "eth3"
	# smac1=in_interface的mac地址，smac2=out_interface的mac地址，dmac1=in_interface直连对端的mac地址，
	# dmac2=out_interface直连对端的mac地址
	smac1 = '00:0C:29:1B:11:A3'
	smac2 = '00:0C:29:1B:11:A4'
	dmac1 = '00:16:31:E5:7B:F9'
	dmac2 = '00:16:31:E5:7B:FA'
	# hostip1=in_interface的ip地址，hostip2=out_interface的ip地址
	hostip1 = hostadd1
	hostip2 = hostadd2
	pcapname = ""
	# 暂时if，后面改为字典
	if pcap_type == "Oracle":
		pcapname = "WhiteList_IEC104"
	else:
		pcapname = pcap_type
	ssh = Shell_SSH()
	ssh.connect(hostip=server_ip, name=user, passwd=passwd)
	ssh.execute('cd /root/DPIforAutotest1')
	ssh.execute('ls')
	# t1 = ssh.output()
	# print(t1)
	ssh.execute('tcpprep -a client -i ' + pcapname + '.pcap -o ' + pcapname + '.cache')
	ssh.execute('tcprewrite --enet-smac='+smac1+','+smac2 + ' --enet-dmac='+dmac1+','+dmac2+' --endpoints='+hostip1+':'+hostip2+' -i '+pcapname+'.pcap -c '+pcapname+'.cache -o '+pcapname+'_1.pcap')
	ssh.execute('tcpreplay -l 1 -c ' + pcapname + '.cache -i '+in_interface+' -I '+out_interface+' ' + pcapname + '_1.pcap -x 100 -M 100')
	# time.sleep(2)
	# t2 = ssh.output()
	# print(t2)
	time.sleep(20)
	ssh.close()


# 进入到机器学习界面 什么也不做
def get_into_machinelearning(browser):
	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)


# 进入到机器学习界面 获取学习时长下拉菜单内容
def get_learntime_menu(browser):
	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)
	# 获取学习时长下拉菜单内容
	c1 = browser.find_element_by_xpath('//*[@id="dur_t"]').text.strip()
	# print(C1)
	return c1


# 设置学习时长为 XX ，执行开始学习（仅仅设置学习时间，其他为默认值，不完整）
def start_learning(browser, learntime):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)
	# 获取学习时长下拉菜单内容
	s1 = Select(browser.find_element_by_xpath('//*[@id="dur_t"]'))
	s1.select_by_visible_text(learntime)
	# 点击开始执行
	browser.find_element_by_xpath('//*[@id="btnid"]').click()


# 执行开始学习（完整版）设置开始时间（暂无），学习时长，自动部署，清除历史记录
def start_learning_complete(browser, learntime='5分钟', aotu_deploy='yes', clear_history='no'):

	# 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)
	# 判断机器学习是否开启
	sleep(2)
	a = browser.find_element_by_xpath('//*[@id="command_area"]/div[1]').text
	# print(a)
	if '剩余学习时间' in a:
		browser.find_element_by_xpath('//*[@id="stops"]').click()
		sleep(2)
		into_fun(browser, 机器学习)
		sleep(1)

	# 输入学习时长
	s1 = Select(browser.find_element_by_xpath('//*[@id="dur_t"]'))
	s1.select_by_visible_text(learntime)
	# 学习结束自动部署
	aotu_deploy1 = browser.find_element_by_xpath('//*[@id="autoset"]').is_selected()
	# print(aotu_deploy1)
	if aotu_deploy == 'yes':
		# 确认学习结束自动部署是否已经被勾选
		if aotu_deploy1 is True:
			print('学习结束自动部署已开启')
		else:
			browser.find_element_by_xpath('//*[@id="autoset"]').click()
	if aotu_deploy == 'no':
		# 确认aotu_deploy是否已经被勾选
		if aotu_deploy1 is True:
			browser.find_element_by_xpath('//*[@id="autoset"]').click()
		else:
			print('学习结束自动部署已关闭')
	# 清除历史记录
	clear_history1 = browser.find_element_by_xpath('//*[@id="clearhis"]').is_selected()
	# print(clear_history1)
	if clear_history == 'yes':
		# 确认清除历史记录是否已经被勾选
		if clear_history1 is True:
			print('清除历史记录已开启')
		else:
			browser.find_element_by_xpath('//*[@id="clearhis"]').click()
	if clear_history == 'no':
		# 确认aotu_deploy是否已经被勾选
		if clear_history1 is True:
			browser.find_element_by_xpath('//*[@id="clearhis"]').click()
		else:
			print('清除历史记录已关闭')
	# 点击开始学习
	sleep(1)
	browser.find_element_by_xpath('//*[@id="btnid"]').click()


# 结束学习（仅仅点击结束学习）
def end_learning(browser):

	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)
	time.sleep(5)
	# 点击结束学习
	browser.find_element_by_xpath('//*[@id="stops"]').click()


# 获取机器学习页面规则总数
def get_rulescount(browser):

	# # 切换到默认frame
	# browser.switch_to.default_content()
	# # 切换到左侧frame
	# browser.switch_to.frame("lefttree")
	# # 点击工业控制
	# browser.find_element_by_xpath(工业控制).click()
	# # 点击机器学习
	# browser.find_element_by_xpath(机器学习).click()
	#
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, 机器学习)
	# 获取规则总数
	num1 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]/span').text
	# print(num1)
	return num1


# 获取机器学习页面条目总数 返回int型
def get_counts_machine_learning(browser):
	into_fun(browser, 机器学习)
	# 获取规则总数
	num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
	# print(num1)
	return int(num1)


# 获取机器学习到的某协议中规则总数 返回int型    ORACLE/PROFINET-IO/Modbus-TCP
def get_rule_counts_machine_learning(browser, protocol_name):
	into_fun(browser, 机器学习)
	n = 2
	x = 0
	protocol = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.strip()
	while protocol != protocol_name:
		n = n + 1
		x = x + 1
		protocol = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.strip()
	# 点击详情
	browser.find_element_by_xpath('//*[@id="' + str(x) + '"]').click()
	sleep(0.5)
	# 获取规则数
	a = browser.find_element_by_xpath('//*[@id="subtr"]/td/div/ul/li[1]').text.strip()
	num1 = a.split('：', 1)
	# print(a)
	# print(num1)
	return int(num1[1])


# 获取机器学习规则详情中第一条和最后一条的的规则名 比较时间 倒序排列 列表中第一条规则时间在最后一条之后（大） 则返回True
def compare_rules_time_machine_learning(browser, protocol_name):
	into_fun(browser, 机器学习)
	n = 2
	x = 0
	protocol = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.strip()
	while protocol != protocol_name:
		n = n + 1
		x = x + 1
		protocol = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.strip()
	# 点击详情
	browser.find_element_by_xpath('//*[@id="' + str(x) + '"]').click()
	sleep(0.5)
	# 获取规则数
	a = browser.find_element_by_xpath('//*[@id="subtr"]/td/div/ul/li[1]').text.strip()
	num1 = a.split('：', 1)
	# print(a)
	# print(num1)
	num2 = int(num1[1])
	print(num2)

	# 获取第一条
	if num2 >= 2:
		time1 = browser.find_element_by_xpath('//*[@id="subtr"]/td/div/table/tbody/tr[2]/td[3]').text.strip()
		print(time1)
		time2 = browser.find_element_by_xpath(
			'//*[@id="subtr"]/td/div/table/tbody/tr[' + str(num2 + 1) + ']/td[3]').text.strip()
		print(time2)
		if time1 >= time2:
			return True
	else:
		print('只有一条规则')
