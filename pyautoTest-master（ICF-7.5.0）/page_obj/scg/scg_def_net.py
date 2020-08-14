import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *


# 添加路由模式的子接口ip
def add_sub_ip(browser,ip,mask):

    # 点击网络
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/header/a').click()

    # 点击+号
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()

    # 点击子接口
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[2]/span/a/span').click()

    # 定位到默认frame
    browser.switch_to.default_content()

    # 定位到内容frame
    browser.switch_to.frame("content")

    # 点击第一个子接口
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[8]/a[1]/img').click()

    # 输入ip
    browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)

    # 输入掩码
    browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)

    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[3]').click()

    # 点击保存
    browser.find_element_by_xpath('//*[@id="link_but"]').click()


# 添加子接口
def add_sub(browser, inte, vlanid):

    # 点击网络
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/header/a').click()

    # 点击+号
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/div').click()

    # 点击子接口
    browser.find_element_by_xpath('//*[@id="menu"]/div[2]/div/ul/li[1]/ul/li[2]/span/a/span').click()

    # 定位到默认frame
    browser.switch_to.default_content()

    # 定位到内容frame
    browser.switch_to.frame("content")

    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()

    # 找下拉框
    s1 = Select(browser.find_element_by_xpath('//*[@id="port"]'))

    # 找下拉框的内容
    s1.select_by_visible_text(inte)

    # 输入vlan id
    browser.find_element_by_xpath('//*[@id="vlanid"]').send_keys(vlanid)

    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()


# 添加物理接口ip地址
def add_Physical_Interface_ip(browser,ip="11.11.11.1",mask="24"):

    # 点击网络
    browser.find_element_by_xpath(网络).click()

    # 点击接口设置
    browser.find_element_by_xpath(接口设置).click()

    # 点击物理接口
    browser.find_element_by_xpath(物理接口).click()

    time.sleep(5)

    # 定位到默认frame
    browser.switch_to.default_content()

    # 定位到内容frame
    browser.switch_to.frame("content")

    # 点击编辑按钮(第一个接口为ge0/1,路径为tr[2],以此类推)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[9]/a/img').click()

    # 添加ip
    browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys(ip)
    print("3333333333333333333333333333333333")

    # 添加掩码
    browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys(mask)

    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()

    time.sleep(5)


