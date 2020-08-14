import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_button import *
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.common.my_selenium import *
from selenium.common.exceptions import NoSuchElementException



# # 删除所有自定义规则（逐条删除）-界面没有数量显示
# def del_all_custom_rules_lzy(browser):
#     # 进入自定义规则界面
#     into_fun(browser, 自定义规则)
#     sleep(0.5)
#     # 获取总数
#     num = browser.find_element_by_xpath('').text.strip()
#     while int(num) > 0:
#         browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(num+1)+']/td[7]/a[2]/img').click()
#         num = browser.find_element_by_xpath('').text.strip()
#
#     try:
#         browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(num + 1) + ')]/td[7]/a[2]/img').click()
#     except NoSuchElementExcept:
#         print('找不到该元素')
#
#     # //*[@id="table"]/tbody/tr[3]/td[7]/a[2]/img
#     # //*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img
#
#
#     try_num = 0
#     while try_num < 5:
#         try:
#             browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()
#             break
#         except:
#             time.sleep(1)
#             try_num += 1





# 新增自定义规则(modbus/s7)  点击保存后再确定返回
def add_custom_rules_complete_lzy(browser, protocol_modubus='yes/no', protocol_s7='yes/no', protocol='', function='', start_address='',
                                  end_address_or_length='end_address/length', end_address='',
                                      length='', start_data='', end_data='', action_modbus='',
                                      PduType='', FunctionType='', action_s7='', save='yes/no', cancel='yes/no'):
    # 进入自定义规则界面
    into_fun(browser, 自定义规则)
    sleep(0.5)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
    # 进入自定义规则添加界面
    # 协议选择-modbus
    if protocol_modubus == 'yes':
        # 选择协议
        s1 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
        s1.select_by_visible_text(protocol)

        # 选择功能
        s1 = Select(browser.find_element_by_xpath('//*[@id="func"]'))
        s1.select_by_visible_text(function)

        # 输入起始地址
        browser.find_element_by_xpath('//*[@id="addr_start"]').clear()
        browser.find_element_by_xpath('//*[@id="addr_start"]').send_keys(start_address)

        # 结束地址和长度任选一项
        if end_address_or_length == 'end_address':
            # 输入结束地址
            browser.find_element_by_xpath('//*[@id="addr_end"]').clear()
            browser.find_element_by_xpath('//*[@id="addr_end"]').send_keys(end_address)
        if end_address_or_length == 'length':
            # 输入长度
            browser.find_element_by_xpath('//*[@id="addr_length"]').clear()
            browser.find_element_by_xpath('//*[@id="addr_length"]').send_keys(length)

        # 输入值域开始值
        browser.find_element_by_xpath('//*[@id="data_start"]').clear()
        browser.find_element_by_xpath('//*[@id="data_start"]').send_keys(start_data)

        # 输入值域结束值
        browser.find_element_by_xpath('//*[@id="data_end"]').clear()
        browser.find_element_by_xpath('//*[@id="data_end"]').send_keys(end_data)

        # 事件处理
        s1 = Select(browser.find_element_by_xpath('//*[@id="conftr_6"]/td[2]/select'))
        s1.select_by_visible_text(action_modbus)

        # 保存或取消
        if save == 'yes':
            browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
        if cancel == 'yes':
            browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    # 协议选择-s7
    if protocol_s7 == 'yes':
        # 选择协议
        s1 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
        s1.select_by_visible_text(protocol)

        # 选择PduType
        s1 = Select(browser.find_element_by_xpath('//*[@id="conftr_a"]/td[2]/span/select'))
        s1.select_by_visible_text(PduType)

        # 选择FunctionType
        s1 = Select(browser.find_element_by_xpath('//*[@id="conftr_b"]/td[2]/span/select'))
        s1.select_by_visible_text(FunctionType)

        # 选择action_s7
        s1 = Select(browser.find_element_by_xpath('//*[@id="conftr_6"]/td[2]/select'))
        s1.select_by_visible_text(action_s7)

        # 保存或取消
        if save == 'yes':
            browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
        if cancel == 'yes':
            browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(8)
    # 点击返回 //*[@id="link_but"]
    browser.find_element_by_xpath('//*[@id="link_but"]').click()



# 根据索引删除自定义规则(modbus/s7)
def delete_sslvpn_safe_site_lzy(browser, number=''):
    # 进入自定义规则界面
    into_fun(browser, 自定义规则)
    sleep(0.5)
    # 根据索引号定位要删除的自定义规则
    n = 2
    num = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        num = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        # if n <= 15:
        #     num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        # else:
        #     print("需要点击下一页")
        #     assert False
    # 删除//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]/td[7]/a[2]/img
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()
    sleep(15)

    # 获取操作成功信息并返回
    info1 = browser.find_element_by_xpath('//*[@id="layui-layer2"]/div[2]').text
    print(info1)
    browser.find_element_by_xpath('//*[@id="layui-layer2"]/div[3]/a').click()
    sleep(0.5)
