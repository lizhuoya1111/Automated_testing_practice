from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def import *


# 进入到系统状态界面，其余什么操作都不做
def get_into_systemstate(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击系统
    # browser.find_element_by_xpath(系统).click()
    # # 点击系统状态
    # browser.find_element_by_xpath(系统状态).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 系统状态)


# 获取系统状态中的工控协议显示数目  ICAgreement==Industrial Control Agreement工控协议
def get_ICAgreement_number(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击系统
    # browser.find_element_by_xpath(系统).click()
    # # 点击系统状态
    # browser.find_element_by_xpath(系统状态).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 系统状态)
    # 获取系统状态中的工控协议显示数目
    a = browser.find_element_by_xpath('//*[@id="sys_info"]/tbody/tr[5]/td[4]/span[1]').text.strip()
    return int(a)


# 进入到系统状态界面，点击工控协议详情 获取工控协议图片数 (方法不准确 已知图片宽度为50 且 协议图片先打印出来）
def get_ICAgreement_picnumber(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击系统
    # browser.find_element_by_xpath(系统).click()
    # # 点击系统状态
    # browser.find_element_by_xpath(系统状态).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 系统状态)
    # 点击工控协议详情
    browser.find_element_by_xpath('//*[@id="icdetail"]').click()
    # 进入到工控协议图片界面 获取页面中图片个数
    n = 1
    for a in browser.find_elements_by_tag_name('img'):
        print(a.size)
        b = a.size.get('height')
        print(n, b)
        if b != 50:
            break
        n = n + 1
    return n-1


# 在refresh后使用  获取系统状态页content中“系统信息”文本，看刷新之后界面是否可以正常加载
def get_text_systemstate(browser):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    a = browser.find_element_by_xpath('//*[@id="box_title_sys_info"]/h4').text
    return a


# 获取主页告警统计数值
def get_alert_number(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击系统
    # browser.find_element_by_xpath(系统).click()
    # # 点击系统状态
    # browser.find_element_by_xpath(系统状态).click()
    into_fun(browser, 系统状态)

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到头frame
    browser.switch_to.frame("topheader")

    # 获取告警统计数值
    a = browser.find_element_by_xpath('//*[@id="gaojing"]').text
    return a
