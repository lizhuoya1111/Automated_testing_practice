import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.common.my_selenium import *


# 添加maplist
def add_maplist_wxw(browser, name='', desc='', oriipfrom='', oriipto='',transipfrom='', transipto='',
                    one_to_one_mapping="no", sticky='yes', portfrom ='1', portto='65535'):

    """
    添加maplist
    """
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # browser.find_element_by_xpath(防火墙).click()
    # browser.find_element_by_xpath(NAT).click()
    #
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath(display_NAT).is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath(display_NAT).click()
    # browser.find_element_by_xpath(源NAT).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 源NAT)
    # 点击映射列表
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    # # 获取目前有多少个SNAT
    # time.sleep(1)
    # maplist_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
    # # 根据snat数量,遍历一下，获取要被删除的对象的层数  //*[@id="table"]/tbody/tr[2]/td[3]
    # for x in range(2, 2 + maplist_sum):  # //*[@id="table"]/tbody/tr[2]/td[2]
    #     if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[2]').text:
    #         # 点击编辑该对象               # //*[@id="table"]/tbody/tr[2]/td[3]/a[1]/img
    #         browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]/a[1]/img').click()
    #         break
    # 增加映射项
    browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
    # 输入原始IP地址
    browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
    browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
    # 输入转换后ip
    if one_to_one_mapping == "yes":
        browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
        browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
    if one_to_one_mapping != "yes":
        browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
        browser.find_element_by_xpath('//*[@id="transipto').send_keys(transipto)
    if sticky == 'yes':
        browser.find_element_by_xpath('//*[@id="sticky"]').click()
    # 输入转换后端口
    browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
    browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
    browser.find_element_by_xpath('//*[@id="portto"]').clear()
    browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)

    # 点击新增项目
    browser.find_element_by_xpath('//*[@id="btn_additem"]').click()
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()


# 添加maplist,到新增项目前
def add_maplist_part_wxw(browser, name='', desc='', oriipfrom='', oriipto='', transipfrom='', transipto='',
                    one_to_one_mapping="no", sticky='yes', portfrom='1', portto='65535'):

    """
    添加maplist,到新增项目前
    """
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # browser.find_element_by_xpath(防火墙).click()
    # browser.find_element_by_xpath(NAT).click()
	#
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath(display_NAT).is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath(display_NAT).click()
    # browser.find_element_by_xpath(源NAT).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 源NAT)
    # 点击映射列表
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()

    # 增加映射项
    browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
    # 输入原始IP地址
    browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
    browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
    time.sleep(1)
    # 输入转换后ip
    browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="transipto"]').send_keys(transipto)
    if one_to_one_mapping == "yes":
        browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
    if sticky == 'yes':
        browser.find_element_by_xpath('//*[@id="sticky"]').click()
    # 输入转换后端口
    browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
    browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
    browser.find_element_by_xpath('//*[@id="portto"]').clear()
    browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)

    # 点击新增项目
    # browser.find_element_by_xpath('//*[@id="btn_additem"]').click()
    # 点击保存
    # browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()


# 添加maplist,只到保存描述前
def add_maplist_desc_wxw(browser, name='', desc=''):

    """
    添加maplist,只到保存描述前
    """
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # browser.find_element_by_xpath(防火墙).click()
    # browser.find_element_by_xpath(NAT).click()
	#
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath(display_NAT).is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath(display_NAT).click()
    # browser.find_element_by_xpath(源NAT).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 源NAT)
    # 点击映射列表
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 点击保存
    # browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 编辑maplist
def edit_maplist(browser, name="", delete_ip="", oriipfrom="", oriipto="", one_to_one_mapping="", transipfrom="", transipto="",
                 sticky="yes", portfrom="1", portto="65535"):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # browser.find_element_by_xpath(防火墙).click()
    # browser.find_element_by_xpath(NAT).click()
	#
    # # 判断菜单是否展开，元素是否可见
    # if not browser.find_element_by_xpath(display_NAT).is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath(NAT).click()
    # browser.find_element_by_xpath(源NAT).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 源NAT)
    # 点击映射列表
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    n = 2                                   # //*[@id="table"]/tbody/tr[2]/td[2]
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
    # print(getname)
    while getname != name:
        n = n + 1
        time.sleep(1)
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
        # print(getname)
    # 点击编辑
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[3]/a[1]/img').click()
    time.sleep(1)
    # 增加映射项
    browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
    time.sleep(1)
    if delete_ip == "yes":
        browser.find_element_by_xpath('//*[@id="ipaddress"]/tbody[2]/tr[2]/td[10]/input').click()
    # 输入原始IP地址
    browser.find_element_by_xpath('//*[@id="oriipfrom"]').send_keys(oriipfrom)
    browser.find_element_by_xpath('//*[@id="oriipto"]').send_keys(oriipto)
    # 输入转换后ip
    if one_to_one_mapping == "yes":
        browser.find_element_by_xpath('//*[@id="one2onemap"]').click()
        browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
    if one_to_one_mapping != "yes":
        browser.find_element_by_xpath('//*[@id="transipfrom"]').send_keys(transipfrom)
        browser.find_element_by_xpath('//*[@id="transipto"]').send_keys(transipto)
    if sticky == 'yes':
        browser.find_element_by_xpath('//*[@id="sticky"]').click()
    # 输入转换后端口
    browser.find_element_by_xpath('//*[@id="portfrom"]').clear()
    browser.find_element_by_xpath('//*[@id="portfrom"]').send_keys(portfrom)
    browser.find_element_by_xpath('//*[@id="portto"]').clear()
    browser.find_element_by_xpath('//*[@id="portto"]').send_keys(portto)
    # 点击新增项目
    browser.find_element_by_xpath('//*[@id="btn_additem"]').click()
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()