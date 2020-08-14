import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 打开或关闭某接口的allow ping 功能
def open_physical_interface_allowping_wxw(browser,interface='ge0/4',allow_ping="open/close"):

    """打开或关闭某接口的allow ping 功能"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击网络
    # browser.find_element_by_xpath(网络).click()
    #
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     time.sleep(1)
    #     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
    #
    # # 点击物理接口
    # browser.find_element_by_xpath(物理接口).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 物理接口)
    # 点击编辑
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

    while getname != interface:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
    # 点击编辑
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

    # 确认allow ping是否打开
    allowping = browser.find_element_by_xpath('//*[@id="ping"]').is_selected()
    # print(allowping)
    if allow_ping == "open":
        if allowping == True:
            print("allow ping已打开")
        else:
            browser.find_element_by_xpath('//*[@id="ping"]').click()
    if allow_ping == "close":
        if allowping == True:
            browser.find_element_by_xpath('//*[@id="ping"]').click()
        else:
            browser.find_element_by_xpath('//*[@id="ping"]').click()
            print("allow ping已关闭")
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

    # 把打开的网络合上
    # 切换到默认frame
    browser.switch_to.default_content()
    # 切换到左侧frame
    browser.switch_to.frame("lefttree")
    # 点击网络
    browser.find_element_by_xpath(网络).click()
    # 点击接口设置
    browser.find_element_by_xpath(接口设置).click()



# 改变物理接口的工作模式
def change_physical_interface_workmode_wxw(browser, interface='ge0/6',
                                           route="yes", ip='', mask='',
                                           trans='no'):

    """改变物理接口的工作模式"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击网络
    # browser.find_element_by_xpath(网络).click()
    # # 点击接口设置
    # browser.find_element_by_xpath(接口设置).click()
    #
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
    #
    # # 点击物理接口
    # browser.find_element_by_xpath(物理接口).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 物理接口)
    # 点击编辑
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

    while getname != interface:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
    # 点击编辑
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

    if route == "yes":
        # 若模式为透明模式，则转换成路由模式
        if not browser.find_element_by_xpath('//*[@id="work_mode_0"]').is_selected():
            # 如果路由没有被选中，点击路由
            browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
            alert = browser.switch_to_alert()
            alert.accept()
        time.sleep(1)
        # 点击静态
        browser.find_element_by_xpath('//*[@id="address_mode_0"]').click()
        # 输入ip
        browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
        browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
        browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
        # 保存
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

    if trans == 'yes':
        # 若模式为路由模式，则转换成透明模式
        if not browser.find_element_by_xpath('//*[@id="work_mode_1"]').is_selected():
            # 判断是否有路由,若有则删除

            have = is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[1]')
            while have == True:
                browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[2]/td[4]/input').click()
                have = is_element_exist(browser, '//*[@id="ipaddress"]/tbody/tr[2]/td[1]')

        # 点击透明
        browser.find_element_by_xpath('//*[@id="work_mode_1"]').click()
        # 接受告警
        alert = browser.switch_to_alert()
        alert.accept()
        time.sleep(2)
        alert = browser.switch_to_alert()
        alert.accept()


        # 点击保存
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()



# 给物理接口添加一个ip
def add_physical_interface_ip_wxw(browser, interface='ge0/4', ip='', mask='24'):

    """给物理接口添加一个ip"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击网络
    # browser.find_element_by_xpath(网络).click()
    # # 点击接口设置
    # browser.find_element_by_xpath(接口设置).click()
    #
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
    #
    # # 点击物理接口
    # browser.find_element_by_xpath(物理接口).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 物理接口)
    # 按名字查找
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

    while getname != interface:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
    # 点击编辑
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

    # 添加ip
    browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
    browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
    browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)
    # 保存
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()



# 给物理接口删除指定ip
def delete_physical_interface_ip_wxw(browser, interface='ge0/4', ip=''):

    """给物理接口删除指定ip"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击网络
    # browser.find_element_by_xpath(网络).click()
    # # 点击接口设置
    # browser.find_element_by_xpath(接口设置).click()
    #
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul').is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()
    #
    # # 点击物理接口
    # browser.find_element_by_xpath(物理接口).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 物理接口)
    # 按名字查找
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text

    while getname != interface:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text
    # 点击编辑
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a/img').click()

    # 按ip查找
    n = 2
    getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text

    while getip != ip:
        n = n + 1
        getip = browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[2]').text

    # 点击删除
    browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody/tr[ ' + str(n) + ' ]/td[4]/input').click()

    # 保存
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

