from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 更改报表设置
def reporter_switch(browser, all_reporter="yes/no/un", interface="yes/no", traffic="yes/no", session="yes/no", system="yes/no", action="保存/重置"):
	into_fun(browser, 报表设置)
	if "un" in all_reporter:
		# print("into")
		if browser.find_element_by_xpath('//*[@id="all_status_1"]').is_selected():
			browser.find_element_by_xpath('//*[@id="all_status_0"]').click()
		if interface == "yes":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="interface_status_0"]').click()
			# print("interface-yes")
		elif interface == "no":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="interface_status_1"]').click()
			# print("interface-no")

		if traffic == "yes":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="traffic_status_0"]').click()
			# print("traffic-yes")
		elif traffic == "no":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="traffic_status_1"]').click()
			# print("traffic-no")

		if session == "yes":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="session_status_0"]').click()
			# print("session-yes")
		elif session == "no":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="session_status_1"]').click()
			# print("session-no")

		time.sleep(1)
		if system == "yes":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="system_status_0"]').click()
			# print("system-yes")
		elif system == "no":
			time.sleep(0.5)
			browser.find_element_by_xpath('//*[@id="system_status_1"]').click()
			# print("system-no")
	elif all_reporter == "yes":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="all_status_0"]').click()
		# print("all-yes")
	elif all_reporter == "no":
		time.sleep(0.5)
		browser.find_element_by_xpath('//*[@id="all_status_1"]').click()
	else:
		print("需要打开所有报表功能")

	if action == "保存":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
	elif action == "重置":
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()