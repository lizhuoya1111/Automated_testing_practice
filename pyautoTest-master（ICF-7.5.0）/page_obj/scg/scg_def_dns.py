from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *


# 添加dhs
def add_dns_jyl(browser, master_dns="", standby_dns=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/div').click()
	# # 点击DNS
	# browser.find_element_by_xpath(DNS).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DNS)
	time.sleep(1)
	# 输入主dns
	browser.find_element_by_xpath('//*[@id="dns1"]').send_keys(master_dns)
	# 输入备dns
	browser.find_element_by_xpath('//*[@id="dns2"]').send_keys(standby_dns)
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 进入dns界面
def location_dns_jyl(browser):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/div').click()
	# # 点击DNS
	# browser.find_element_by_xpath(DNS).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DNS)


# 删除dns
def delete_dns_jyl(browser, master_dns="", standby_dns=""):
	# 定位到默认frame
	# browser.switch_to.default_content()
	# browser.switch_to.frame("lefttree")
	# # 点击系统
	# browser.find_element_by_xpath(系统).click()
	# if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/ul').is_displayed():
	# 	# 如果不可见，点击加号，展开元素
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[3]/div').click()
	# # 点击DNS
	# browser.find_element_by_xpath(DNS).click()
	# # 定位到默认frame
	# browser.switch_to.default_content()
	# # 定位到内容frame
	# browser.switch_to.frame("content")
	into_fun(browser, DNS)
	time.sleep(1)
	if master_dns == "delete":
		# 清除
		browser.find_element_by_xpath('//*[@id="dns1"]').clear()
	if standby_dns == "delete":
		# 清除
		browser.find_element_by_xpath('//*[@id="dns2"]').clear()
	# 点击保存
	browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()