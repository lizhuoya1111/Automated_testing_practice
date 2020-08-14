import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *


# 添加多网关组
def add_multi_gateway_group_wxw(browser, name='', group="1(GROUP_1)", modify='yes/no', alias='',
                                device='ge0/3', gateway='24.1.1.7', ping_server='34.1.1.4', ping='yes/no', arp='yes/no',
                                time_switch='7', ub="100000", db="100000"):

    """"添加多网关组"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击路由
    # browser.find_element_by_xpath(路由).click()
    # # 点击多网关组
    # browser.find_element_by_xpath(多网关组).click()
    # time.sleep(2)
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 多网关组)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="gateway_name"]').send_keys(name)
    # 选择网关组
    # 找下拉框
    s1 = Select(browser.find_element_by_xpath('//*[@id="gateway_group"]'))
    # 找下拉框的内容
    s1.select_by_visible_text(group)

    if modify == "yes":
        # 点击更改
        browser.find_element_by_xpath('//*[@id="sub_tb_area"]/span[2]/a').click()
        # 输入别名
        browser.find_element_by_xpath('//*[@id="alias"]').clear()
        browser.find_element_by_xpath('//*[@id="alias"]').send_keys(alias)
        # 点击保存
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

    # 选择设备
    s1 = Select(browser.find_element_by_xpath('//*[@id="out_device"]'))
    # 找下拉框的内容
    s1.select_by_visible_text(device)
    # 选择网关
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="gateway"]').clear()
    browser.find_element_by_xpath('//*[@id="gateway"]').send_keys(gateway)
    # 选择ping服务器
    browser.find_element_by_xpath('//*[@id="ping_servers"]').clear()
    browser.find_element_by_xpath('//*[@id="ping_servers"]').send_keys(ping_server)

    if ping == 'yes':
        print('探测方式已为ping')
    if arp == 'yes':
        browser.find_element_by_xpath('//*[@id="detectmethod_arp"]').click()
    # 切换时间
    browser.find_element_by_xpath('//*[@id="switchtime"]').clear()
    browser.find_element_by_xpath('//*[@id="switchtime"]').send_keys(time_switch)
    # 上传带宽
    browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').clear()
    browser.find_element_by_xpath('//*[@id="upstreambandwidths"]').send_keys(ub)
    # 下载带宽
    browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').clear()
    browser.find_element_by_xpath('//*[@id="downstreambandwidths"]').send_keys(db)

    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()


# 判断多网关组是否存在，若存在返回True,反之返回False
def is_multi_gateway_group_exist_wxw(browser, name=''):

    """判断isp是否存在，若存在返回True,反之返回False"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击路由
    # browser.find_element_by_xpath(路由).click()
    # # 点击多网关组
    # browser.find_element_by_xpath(多网关组).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 多网关组)
    # 获取目前有多少个多网关组
    # //*[@id="mouseid_101_gatewayname"]
    # // *[ @ id = "mouseid_102_gatewayname"]
    # //*[@id="mouseid_401_gatewayname"]
    # //*[@id="route_maintenance_multigw_table"]/tbody/tr[2]/td/a/span
    # //*[@id="mouseid_401_gatewayname"]
    # //*[@id="route_maintenance_multigw_table"]/tbody/tr[5]/td/a/span
    time.sleep(1)
    gateway_group_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
    # 根据isp数量,遍历一下
    for x in range(2, 2 + gateway_group_sum):
        if str(name) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[3]').text.replace(' ', ''):
            return True
    else:
        return False













