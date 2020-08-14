from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *


# 判断路由是否存在，若存在返回True,反之返回False
def is_static_route_exist_wxw(browser, destination=''):

    """判断路由是否存在，若存在返回True,反之返回False"""
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击路由
    # browser.find_element_by_xpath(路由).click()
    # # 点击静态路由
    # browser.find_element_by_xpath(静态路由).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 静态路由)
    # 获取目前有多少个路由
    time.sleep(1)
    route_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
    # 根据route数量,遍历一下
    print(str(destination))
    for x in range(2, 2 + route_sum):
        if str(destination) == browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x) + ']/td[4]').text.replace(' ', ''):
            return True
    else:
        return False


