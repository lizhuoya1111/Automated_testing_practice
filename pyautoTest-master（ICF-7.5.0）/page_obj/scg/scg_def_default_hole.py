from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *


# 进入默认漏洞
def get_into_default_hole_jyl(browser, query="no", full_selection_rule="", all_operations="", all_operations_value="",
							  filte="", filter_value="", next_page="", previous_page="", go_to_page="", go_to_page_num=""):

	into_fun(browser, 工业漏洞)
	# 搜索
	if query != "no":
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="keywords"]').clear()
		browser.find_element_by_xpath('//*[@id="keywords"]').send_keys(query)
		browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/div/input').click()
	# 选择启用

	# 全选规则启用
	if full_selection_rule == "enable":
		browser.find_element_by_xpath('//*[@id="check_button"]').click()
		browser.find_element_by_xpath('//*[@id="apply_button"]').click()
	# 全选规则禁用
	elif full_selection_rule == "diaenable":
		browser.find_element_by_xpath('//*[@id="check_button"]').click()
		browser.find_element_by_xpath('//*[@id="unapply_button"]').click()
	# 操作全部（通过、警告、阻断）
	if all_operations == "yes":
		s1 = Select(browser.find_element_by_xpath('//*[@id="balcklist_dllEventAll"]'))
		s1.select_by_visible_text(all_operations_value)
	# 过滤（禁用、启用）
	if filte == "yes":
		s1 = Select(browser.find_element_by_xpath('//*[@id="filter"]'))
		s1.select_by_visible_text(filter_value)
	if next_page == "yes":
		browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[2]/a').click()
	if previous_page == "yes":
		browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[1]/a').click()
	if go_to_page == "yes":
		s1 = Select(browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[3]/select'))
		s1.select_by_visible_text(go_to_page_num)



