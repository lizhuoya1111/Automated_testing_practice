import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *
import math


# 进入到安全事件界面 什么也不做
def get_into_securityevents(browser):
    # # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)


# 判断安全事件列表显示是否完整,并返回列表表头
def judge_eventslist_complete(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 列表显示：时间 源设备名 目的设备名 源地址 目的地址 协议 事件级别 事件来源 状态 操作
    info1 = browser.find_element_by_xpath('//*[@id="for_tb_title"]').text.replace('','')
    print(info1)
    return(info1)


# 判断安全事件列表显示是否完整,并返回列表第一条事件
def return_eventslist_first(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 显示第一条事件信息
    info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]').text.replace('','')
    # print(info2)
    return info2


# 事件信息显示顺序 列表按时间排序，最新数据在最上方 判断第一条事件与第二条事件的时间，返回更大的时间（第一条事件时间）
def return_time_bigger(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 显示第一条事件时间
    time1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[1]').text.replace('', '')
    # print(time1)
    # 显示第二条事件时间
    time2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[1]').text.replace('', '')
    # print(time2)
    if time1 > time2:
        return time1


# 安全事件高级搜索（不完整 只搜索时间）
def securityevents_advanced_search_time(browser, StartDateTime, EndDateTime):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()
    # 输入开始时间
    browser.find_element_by_xpath('//*[@id="event_txtStartDateTime"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtStartDateTime"]').send_keys(StartDateTime)
    # 输入结束时间
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="event_txtEndDateTime"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtEndDateTime"]').send_keys(EndDateTime)
    # 点击查询

    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 在securityevents_advanced_search_time安全事件高级搜索后使用 用于返回高级搜索后第一条事件时间
def return_time_after_search(browser, StartDateTime, EndDateTime):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取高级搜索后查询出的事件总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    # 如果搜索到事件，显示第一条事件时间
    if int(num1) > 0:
        time1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[1]').text.replace('', '')
        print(time1)
        if StartDateTime <= time1 and EndDateTime >= time1:
            return time1
    else:
        return '无安全事件'


# 安全事件高级搜索（不完整 只搜索IP）
def securityevents_advanced_search_IP(browser, SourceIP, DestinationIP):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()
    # 输入源IP
    browser.find_element_by_xpath('//*[@id="event_txtSourceIP"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtSourceIP"]').send_keys(SourceIP)
    # 输入目的IP
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="event_txtDestinationIP"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtDestinationIP"]').send_keys(DestinationIP)
    # 点击查询

    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 在securityevents_advanced_search_IP安全事件高级搜索后使用 用于返回高级搜索后第一条事件IP
def return_IP_after_search(browser, SourceIP, DestinationIP):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取高级搜索后查询出的事件总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    # 如果搜索到事件，显示第一条事件源IP和目的IP
    if int(num1) > 0:
        IP1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text
        IP2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text
        if SourceIP in IP1 and DestinationIP in IP2:
            return IP1, IP2
    else:
        return '无安全事件'


# 安全事件高级搜索（不完整 只搜索协议）
def securityevents_advanced_search_Protocol(browser, Protocol):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()
    # 输入协议
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_txtProtocol"]'))
    s1.select_by_visible_text(Protocol)

    # 点击查询
    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 在securityevents_advanced_search_Protocol安全事件高级搜索后使用 用于返回高级搜索后第一条事件协议
def return_Protocol_after_search(browser, Protocol):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取高级搜索后查询出的事件总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    # 如果搜索到事件，显示第一条事件Protocol
    if int(num1) > 0:
        Protocol1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[6]').text
        if Protocol in Protocol1 :
            return Protocol1
    else:
        return '无安全事件'



# 安全事件高级搜索（不完整 只搜索事件来源）
def securityevents_advanced_search_EventSource(browser, EventSource):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()
    # 选择事件来源
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_ddlEventSource"]'))
    s1.select_by_visible_text(EventSource)
    # 点击查询
    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 在securityevents_advanced_search_EventSource安全事件高级搜索后使用 用于返回高级搜索后第一条事件事件来源
def return_EventSource_after_search(browser, EventSource):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取高级搜索后查询出的事件总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    # 如果搜索到事件，显示第一条事件EventSource
    if int(num1) > 0:
        EventSource1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]').text
        if EventSource in EventSource1:
            return EventSource1
    else:
        return '无安全事件'


# 安全事件高级搜索（不完整 只搜索状态）//*[@id="event_handleStatus"]
def securityevents_advanced_search_handleStatus(browser, handleStatus):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()
    # 选择事件来源
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_handleStatus"]'))
    s1.select_by_visible_text(handleStatus)
    # 点击查询
    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 在securityevents_advanced_search_EventSource安全事件高级搜索后使用 用于返回高级搜索后第一条事件事件来源
def return_handleStatus_after_search(browser, handleStatus):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取高级搜索后查询出的事件总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    # 如果搜索到事件，显示第一条事件handleStatus
    if int(num1) > 0:
        handleStatus1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[9]').text
        if handleStatus in handleStatus1:
            return handleStatus1
    else:
        return '无安全事件'


# 安全事件高级搜索（完整）
def securityevents_advanced_search_complete(browser, Sourcedev='', Destinationdev='', SourceIP='', DestinationIP='',
                                            Protocol='全部', StartDateTime='', EndDateTime='',
                                            EventSource='全部', handleStatus='全部'):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击高级搜索，进入高级搜索页
    browser.find_element_by_xpath('//*[@id="search_show_button"]').click()

    # 源设备名，目的设备名
    browser.find_element_by_xpath('//*[@id="event_txtSourceName"]').send_keys(Sourcedev)
    browser.find_element_by_xpath('//*[@id="event_txtDestinationName"]').send_keys(Destinationdev)

    # 源地址，目的地址
    browser.find_element_by_xpath('//*[@id="event_txtSourceIP"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtSourceIP"]').send_keys(SourceIP)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="event_txtDestinationIP"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtDestinationIP"]').send_keys(DestinationIP)

    # 协议
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_txtProtocol"]'))
    s1.select_by_visible_text(Protocol)

    # 开始时间，结束时间
    browser.find_element_by_xpath('//*[@id="event_txtStartDateTime"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtStartDateTime"]').send_keys(StartDateTime)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="event_txtEndDateTime"]').clear()
    browser.find_element_by_xpath('//*[@id="event_txtEndDateTime"]').send_keys(EndDateTime)

    # 事件来源
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_ddlEventSource"]'))
    s1.select_by_visible_text(EventSource)

    # 状态
    s1 = Select(browser.find_element_by_xpath('//*[@id="event_handleStatus"]'))
    s1.select_by_visible_text(handleStatus)

    # 点击查询
    browser.find_element_by_xpath('//*[@id="search_button"]').click()


# 安全事件点击下一页
def click_nextpage_after_getinto_securityevents(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 点击下一页
    browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[2]/a').click()


# 安全事件点击上一页 （注意在有上一页的情况下使用）
def click_previouspage_after_getinto_securityevents(browser):


    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")

    # 点击上一页
    browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[1]/a').click()


# 获取本页最新一条安全事件时间（在进入安全事件页面后 或者翻页后使用）
def get_time_of_Latest_Events_in_Current_page(browser):


    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")

    # 获取最新一条安全事件时间
    time = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[1]').text.strip()
    return time


# 获取安全事件总数 判断总页数是否正确 并返回总页数
def get_allpagenumber_of_securityevents(browser):


    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击工业控制
    # browser.find_element_by_xpath(工业控制).click()
    # # 点击机器学习
    # browser.find_element_by_xpath(安全事件).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 安全事件)
    # 获取安全事件总数
    number11 = browser.find_element_by_xpath('//*[@id="rules_count"]').text.strip()
    number1 = int(number11)
    # 总数除以每页安全事件数得到总页数
    # page11 = number1 / 10
    # page1 = math.ceil(page11)
    # 向上取整
    page1 = math.ceil(number1 / 10)
    return page1
