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


# 删除所有SSLVPN安全站点
def del_all_sslvpn_safe_site_lzy(browser):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 点击全选
    browser.find_element_by_xpath('//*[@id="checkall"]').click()
    sleep(0.5)
    # 删除所有
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
    # 获取告警信息 并接受告警
    sleep(1)
    alert1 = browser.switch_to_alert().text
    print(alert1)
    browser.switch_to_alert().accept()
    time.sleep(1)


# 获取SSLVPN安全站点总数
def get_count_sslvpn_safe_site_lzy(browser):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 获取总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    sleep(0.5)
    return int(num1)


# 获取安全站点列表信息
def get_list_info_sslvpn_safe_site_lzy(browser):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 获取安全站点列表信息
    info1 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[2]').text
    print(info1)
    sleep(0.5)
    return info1


# 获取安全站点列表条目数（前提添加条数已知） 返回int型
def get_list_num_sslvpn_safe_site_lzy(browser, number):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 获取安全站点列表条目数
    n =1
    for x in range(2, 2 + int(number)):
        num2 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(x)+']/td[2]').text.strip()
        print(num2)
        n = n+1
    sleep(0.5)
    a = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
    return int(a)


# 新增SSLVPN安全站点  点击保存截止  证书体web界面已经删除
def add_sslvpn_safe_site_lzy(browser, sitename='', siteip='', siteport='', enable='yes/no',
                             enable_client_authentication='yes/no',
                             infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                              real_service_address='', real_service_port='', save='yes/no',
                             cancel='yes/no'):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 点击增加 //*[@id="button_area"]/div/input[1]
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
    # 进入创建安全站点界面
    # 输入站点名称
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(sitename)

    # 输入站点地址 站点地址改为下拉框式
    time.sleep(1)
    s1 = Select(browser.find_element_by_xpath('//*[@id="site_ip"]'))
    s1.select_by_visible_text(siteip)

    # 输入站点端口
    browser.find_element_by_xpath('//*[@id="site_port"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port"]').send_keys(siteport)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    # 启用客户端认证
    if enable_client_authentication == 'yes':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
    if enable_client_authentication == 'no':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
        else:
            pass

    # 信息传递
    if infomation_transfer == 'yes':
        # 客户端真实地址
        if client_real_address == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
        if client_real_address == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
            else:
                pass
        # 证书DN
        if certificate_DN == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
        if certificate_DN == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
            else:
                pass
        # # 证书体
        # if certificate_body =='yes':
        #     enable3 = browser.find_element_by_xpath('//*[@id="cert_subject"]').is_selected()
        #     if enable3 == True:
        #         pass
        #     else:
        #         browser.find_element_by_xpath('//*[@id="cert_subject"]').click()
        # if certificate_body =='no':
        #     enable3 = browser.find_element_by_xpath('//*[@id="cert_subject"]').is_selected()
        #     if enable3 == True:
        #         browser.find_element_by_xpath('//*[@id="cert_subject"]').click()
        #     else:
        #         pass

    # 真实服务地址
    browser.find_element_by_xpath('//*[@id="site_ip1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_ip1"]').send_keys(real_service_address)

    # 真实服务端口
    browser.find_element_by_xpath('//*[@id="site_port1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port1"]').send_keys(real_service_port)

    sleep(1)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(1)


# 新增：完整的SSLVPN站点 包括点击后再确认返回

# 新增SSLVPN安全站点  点击保存后再确定返回
def add_sslvpn_safe_site_complete_lzy(browser, sitename='', siteip='', siteport='', enable='yes/no',
                                      enable_client_authentication='yes/no',
                                      infomation_transfer='yes/no', client_real_address='yes/no',
                                      certificate_DN='yes/no',
                                      real_service_address='', real_service_port='', save='yes/no', cancel='yes/no'):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 点击增加 //*[@id="button_area"]/div/input[1]
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
    # 进入创建安全站点界面
    # 输入站点名称
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(sitename)

    # 输入站点地址 站点地址改为下拉框式
    time.sleep(1)
    s1 = Select(browser.find_element_by_xpath('//*[@id="site_ip"]'))
    s1.select_by_visible_text(siteip)

    # 输入站点端口
    browser.find_element_by_xpath('//*[@id="site_port"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port"]').send_keys(siteport)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    # 启用客户端认证
    if enable_client_authentication == 'yes':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
    if enable_client_authentication == 'no':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
        else:
            pass

    # 信息传递
    if infomation_transfer == 'yes':
        # 客户端真实地址
        if client_real_address == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
        if client_real_address == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
            else:
                pass
        # 证书DN
        if certificate_DN == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
        if certificate_DN == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
            else:
                pass

    # 真实服务地址
    browser.find_element_by_xpath('//*[@id="site_ip1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_ip1"]').send_keys(real_service_address)

    # 真实服务端口
    browser.find_element_by_xpath('//*[@id="site_port1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port1"]').send_keys(real_service_port)

    sleep(1)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(1)

    # 获取操作成功信息并返回
    info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    # print(info1)
    browser.find_element_by_xpath('//*[@id="link_but"]').click()
    sleep(0.5)


# 根据索引号 勾选或者取消勾选安全站点 -重新进入界面 勾选自动消失 取消勾选功能暂不用
def select_or_unselect_sslvpn_safe_site_lzy(browser, number='', select='yes/no'):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 根据索引号选择要编辑的安全站点
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 勾选

    # 先判断该条是否被勾选
    enable = browser.find_element_by_xpath(
        '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').is_selected()
    # print(enable)
    if select == "yes":
        if enable == True:
            pass
            # print("状态已经是selected")
        else:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
            # print('已勾选')
    if select == 'no':
        if enable == True:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
            # print('已取消勾选')
        else:
            pass
            # print("状态已经是unselected")


# 根据索引号判断该条安全站点是否被勾选，返回TRUE或者FALSE 该函数连接在勾选函数之后使用
def judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number=''):
    sleep(0.5)
    # 根据索引号选择要编辑的安全站点
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 判断该条是否被勾选
    enable = browser.find_element_by_xpath(
        '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').is_selected()
    # print(enable)
    return enable


# 全选或者取消全选安全站点
def select_or_unselect_all_sslvpn_safe_site_lzy(browser, select='yes/no'):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)

    # 勾选
    if select == 'yes':
        # 先判断该条是否被勾选
        enable = browser.find_element_by_xpath('//*[@id="checkall"]').is_selected()
        print(enable)
        if select == "yes":
            if enable == True:
                pass
                # print("状态已经是selected")
            else:
                browser.find_element_by_xpath('//*[@id="checkall"]').click()
                # print('已勾选')
        if select == 'no':
            if enable == True:
                browser.find_element_by_xpath('//*[@id="checkall"]').click()
                # print('已取消勾选')
            else:
                pass
                # print("状态已经是unselected")


# 判断安全站点是否被全部勾选，返回TRUE或者FALSE 该函数连接在勾选函数之后使用
def judge_select_or_unselect_all_sslvpn_safe_site_lzy(browser):
    sleep(0.5)
    # 判断该条是否被勾选
    enable = browser.find_element_by_xpath('//*[@id="checkall"]').is_selected()
    # print(enable)
    return enable


# 根据索引号 删除安全站点 获取操作成功信息并返回
def delete_sslvpn_safe_site_lzy(browser, number=''):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 根据索引号选择要编辑的安全站点
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 删除
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[9]/a[2]/img').click()
    sleep(12)

    # 获取操作成功信息并返回
    info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    print(info1)
    browser.find_element_by_xpath('//*[@id="link_but"]').click()
    sleep(0.5)


# 根据索引号 编辑安全站点
def edit_sslvpn_safe_site_lzy(browser, number='', sitename='', siteip='', siteport='', enable='yes/no',
                              enable_client_authentication='yes/no',
                              infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                              real_service_address='', real_service_port='', save='yes/no', cancel='yes/no'):
    # 进入安全站点界面
    into_fun(browser, 安全站点)
    sleep(0.5)
    # 根据索引号选择要编辑的安全站点
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False

    # 编辑 //*[@id="vpn_certadmin_table"]/tbody/tr[3]/td[9]/a[1]/img
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()
    sleep(0.5)

    # 进入编辑页面
    # 输入站点名称
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(sitename)

    # 输入站点地址 站点地址改为下拉框式
    time.sleep(1)
    s1 = Select(browser.find_element_by_xpath('//*[@id="site_ip"]'))
    s1.select_by_visible_text(siteip)

    # 输入站点端口
    browser.find_element_by_xpath('//*[@id="site_port"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port"]').send_keys(siteport)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    # 启用客户端认证
    if enable_client_authentication == 'yes':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
    if enable_client_authentication == 'no':
        enable2 = browser.find_element_by_xpath('//*[@id="client_auth"]').is_selected()
        if enable2 == True:
            browser.find_element_by_xpath('//*[@id="client_auth"]').click()
        else:
            pass

    # 信息传递
    if infomation_transfer == 'yes':
        # 客户端真实地址
        if client_real_address == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
        if client_real_address == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="info_trans"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="info_trans"]').click()
            else:
                pass
        # 证书DN
        if certificate_DN == 'yes':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                pass
            else:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
        if certificate_DN == 'no':
            enable3 = browser.find_element_by_xpath('//*[@id="clientdn"]').is_selected()
            if enable3 == True:
                browser.find_element_by_xpath('//*[@id="clientdn"]').click()
            else:
                pass

    # 真实服务地址
    browser.find_element_by_xpath('//*[@id="site_ip1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_ip1"]').send_keys(real_service_address)

    # 真实服务端口
    browser.find_element_by_xpath('//*[@id="site_port1"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port1"]').send_keys(real_service_port)

    sleep(1)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
        sleep(0.5)
        # 获取操作成功信息并返回
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        sleep(0.5)
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()

    sleep(0.5)


# 新增本地用户 点击保存截止
def add_sslvpn_local_admin_lzy(browser, name='', password='', enable='yes/no', save='yes/no', cancel='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
    # 进入创建本地用户界面
    # 输入本地用户
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(name)

    # 输入密码
    browser.find_element_by_xpath('//*[@id="passwd"]').clear()
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
             pass

    sleep(0.5)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(1)


# 新增本地用户  点击保存后再确定返回
def add_sslvpn_local_admin_complete_lzy(browser, name='', password='', enable='yes/no', save='yes/no', cancel='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
    # 进入创建本地用户界面
    # 输入本地用户
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(name)

    # 输入密码
    browser.find_element_by_xpath('//*[@id="passwd"]').clear()
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
             pass

    sleep(0.5)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
        sleep(0.5)
        # 获取操作成功信息并返回
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        sleep(0.5)
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(0.5)


# 删除所有本地用户
def del_all_sslvpn_local_admin_lzy(browser):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 点击全选 //*[@id="checkall"]
    browser.find_element_by_xpath('//*[@id="checkall"]').click()
    sleep(0.5)
    # 删除所有
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
    # 获取告警信息 并接受告警
    sleep(1)
    alert1 = browser.switch_to_alert().text
    print(alert1)
    browser.switch_to_alert().accept()
    time.sleep(1)


# 获取本地用户总数 返回int型
def get_count_sslvpn_local_admin_lzy(browser):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 获取总数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    print(num1)
    sleep(0.5)
    return int(num1)


# 获取本地用户列表信息
def get_list_info_sslvpn_local_admin_lzy(browser):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 获取安全站点列表信息
    info1 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[2]').text
    print(info1)
    sleep(0.5)
    return info1


# 获取本地用户列表条目数（前提添加条数已知） 返回int型
def get_list_num_sslvpn_local_admin_lzy(browser, number):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 获取本地用户列表条目数
    n =1
    for x in range(2, 2 + int(number)):
        num2 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(x)+']/td[2]').text.strip()
        print(num2)
        n = n+1
    sleep(0.5)
    a = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(n)+']/td[2]').text.strip()
    return int(a)


# 根据索引号 勾选或者取消勾选本地用户-单个
def select_or_unselect_sslvpn_local_admin_lzy(browser, number='', select='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 勾选
    # 先判断该条是否被勾选
    enable = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').is_selected()
    if select == "yes":
        if enable == True:
            pass
            # print("状态已经是selected")
        else:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
            # print('已勾选')
    if select == 'no':
        if enable == True:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
            # print('已取消勾选')
        else:
            pass
            # print("状态已经是unselected")


# 根据索引号判断该条本地用户是否被勾选，返回TRUE或者FALSE 该函数连接在勾选函数之后使用
def judge_select_or_unselect_sslvpn_local_admin_lzy(browser, number=''):

    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 判断该条是否被勾选
    enable = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').is_selected()
    # print(enable)
    return enable


# 全选或者取消全选本地用户
def select_or_unselect_all_sslvpn_local_admin_lzy(browser, select='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)

    # 勾选
    if select == 'yes':
        # 先判断该条是否被勾选
        enable = browser.find_element_by_xpath('//*[@id="checkall"]').is_selected()
        print(enable)
        if select == "yes":
            if enable == True:
                pass
                # print("状态已经是selected")
            else:
                browser.find_element_by_xpath('//*[@id="checkall"]').click()
                # print('已勾选')
        if select == 'no':
            if enable == True:
                browser.find_element_by_xpath('//*[@id="checkall"]').click()
                # print('已取消勾选')
            else:
                pass
                # print("状态已经是unselected")


# 判断本地用户是否被全部勾选，返回TRUE或者FALSE 该函数连接在勾选函数之后使用
def judge_select_or_unselect_all_sslvpn_local_admin_lzy(browser):

    sleep(0.5)
    # 判断该条是否被勾选
    enable = browser.find_element_by_xpath('//*[@id="checkall"]').is_selected()
    # print(enable)
    return enable


# 根据索引号 删除本地用户 获取操作成功信息并返回
def delete_sslvpn_local_admin_lzy(browser, number=''):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 删除
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(n)+']/td[6]/a[2]/img').click()
    sleep(0.5)

    # 获取操作成功信息并返回
    info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    print(info1)
    browser.find_element_by_xpath('//*[@id="link_but"]').click()
    sleep(0.5)


# 根据索引号 编辑本地用户
def edit_sslvpn_local_admin_lzy(browser, number='', password='', enable='yes/no', save='yes/no', cancel='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的安全站点
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False

    # 编辑 //*[@id="vpn_certadmin_table"]/tbody/tr[2]/td[6]/a[1]/img
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr['+str(n)+']/td[6]/a[1]/img').click()
    sleep(0.5)

    # 进入创建本地用户界面
    # 输入本地用户-不允许编辑
    # 输入密码
    browser.find_element_by_xpath('//*[@id="passwd"]').clear()
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    sleep(0.5)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
        sleep(0.5)
        # 获取操作成功信息并返回
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        sleep(0.5)
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()

    sleep(0.5)


# 根据索引号 勾选本地用户-多个（2个）
def select_some_sslvpn_local_admin_lzy(browser, number1='', number2=''):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number1:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False

    # 勾选
    # 先判断该条是否被勾选
    enable = browser.find_element_by_xpath(
        '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').is_selected()
    # print(enable)

    if enable == True:
        pass
        # print("状态已经是selected")
    else:
        browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
        # print('已勾选')

    if enable == True:
        browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[1]/input').click()
        # print('已取消勾选')
    else:
        pass
        # print("状态已经是unselected")

    m = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(m) + ']/td[2]').text.strip()
    while num != number2:
        m = m + 1
        if m <= 15:
            num = browser.find_element_by_xpath(
                '//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(m) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False

    if enable == True:
        pass
        # print("状态已经是selected")
    else:
        browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(m) + ']/td[1]/input').click()
        # print('已勾选')

    if enable == True:
        browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(m) + ']/td[1]/input').click()
        # print('已取消勾选')
    else:
        pass
        # print("状态已经是unselected")


# 新增Portal站点
def add_sslvpn_portal_site_complete_lzy(browser, enable='yes/no', sitename='', siteip='', siteport='',
                                        addlist='yes/no', dellist='yes/no', addsite='', delsite='', save='yes/no',
                                        cancel='yes/no'):
    # 进入安全站点界面
    into_fun(browser, Portal站点)
    sleep(0.5)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    # 输入站点名称
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(sitename)

    # 输入站点地址 站点地址改为下拉框式
    time.sleep(1)
    s1 = Select(browser.find_element_by_xpath('//*[@id="site_ip"]'))
    s1.select_by_visible_text(siteip)

    # 输入站点端口
    browser.find_element_by_xpath('//*[@id="site_port"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port"]').send_keys(siteport)

    # 增加安全站点
    if addlist == 'yes':
        # 选择站点资源（单个）
        sleep(0.5)
        s1 = Select(browser.find_element_by_xpath('//*[@id="safe_site_list"]'))
        s1.select_by_visible_text(addsite)
        # 右移
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="conftr_4"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

    # 删除安全站点
    if dellist == 'yes':
        # 选择站点资源（单个）
        sleep(0.5)
        s1 = Select(browser.find_element_by_xpath('//*[@id="safe_site_list_selected"]'))
        s1.select_by_visible_text(delsite)
        # 右移
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="conftr_4"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()

    sleep(1)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div/div[2]/div/input[1]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div/div[2]/div/input[2]').click()

    sleep(1)

    # 获取操作成功信息并返回
    info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    print(info)
    browser.find_element_by_xpath('//*[@id="link_but"]').click()
    sleep(0.5)


# 浏览器输入Portal站点
def get_portal_login_lzy(browser, siteip='', siteport='', username="admin", password="admin"):
    sleep(0.5)
    # 打开 SCG web
    browser.get("https://" + str(siteip) + ":" + str(siteport))
    sleep(0.5)
    # 登录
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="sub_btn"]').click()
    sleep(1)


# 新增Portal站点-点击保存截止
def add_sslvpn_portal_site_lzy(browser, enable='yes/no', sitename='', siteip='', siteport='',
                                        addlist='yes/no', dellist='yes/no', addsite='', delsite='', save='yes/no',
                                        cancel='yes/no'):
    # 进入安全站点界面
    into_fun(browser, Portal站点)
    sleep(0.5)

    # 启用 首先判断是否已经勾选启用
    if enable == 'yes':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            pass
        else:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    if enable == 'no':
        enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="site_enable"]').click()
        else:
            pass

    # 输入站点名称
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys(sitename)

    # 输入站点地址 站点地址改为下拉框式
    time.sleep(1)
    s1 = Select(browser.find_element_by_xpath('//*[@id="site_ip"]'))
    s1.select_by_visible_text(siteip)

    # 输入站点端口
    browser.find_element_by_xpath('//*[@id="site_port"]').clear()
    browser.find_element_by_xpath('//*[@id="site_port"]').send_keys(siteport)

    # 增加安全站点
    if addlist == 'yes':
        # 选择站点资源（单个）
        sleep(0.5)
        s1 = Select(browser.find_element_by_xpath('//*[@id="safe_site_list"]'))
        s1.select_by_visible_text(addsite)
        # 右移
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="conftr_4"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()

    # 删除安全站点
    if dellist == 'yes':
        # 选择站点资源（单个）
        sleep(0.5)
        s1 = Select(browser.find_element_by_xpath('//*[@id="safe_site_list_selected"]'))
        s1.select_by_visible_text(delsite)
        # 右移
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="conftr_4"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()

    sleep(1)

    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div/div[2]/div/input[1]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div/div[2]/div/input[2]').click()

    sleep(1)



# 删除所有本地用户，再新增admin用户 用于还原时的删除 目前密码有限制 该函数暂时不用
def del_all_add_default_sslvpn_local_admin_lzy(browser):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 点击全选 //*[@id="checkall"]
    browser.find_element_by_xpath('//*[@id="checkall"]').click()
    sleep(0.5)
    # 删除所有
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
    # 获取告警信息 并接受告警
    sleep(1)
    alert1 = browser.switch_to_alert().text
    print(alert1)
    browser.switch_to_alert().accept()
    time.sleep(1)
    # 增加默认本地用户 admin/admin启用
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
    # 输入本地用户
    browser.find_element_by_xpath('//*[@id="site_name"]').clear()
    browser.find_element_by_xpath('//*[@id="site_name"]').send_keys('admin')

    # 输入密码
    browser.find_element_by_xpath('//*[@id="passwd"]').clear()
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys('admin')

    # 启用 首先判断是否已经勾选启用
    enable1 = browser.find_element_by_xpath('//*[@id="site_enable"]').is_selected()
    if enable1 == True:
        pass
    else:
        browser.find_element_by_xpath('//*[@id="site_enable"]').click()
    sleep(0.5)

    # 保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    sleep(0.5)
    # 获取操作成功信息并返回
    info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    print(info)
    browser.find_element_by_xpath('//*[@id="link_but"]').click()
    sleep(0.5)


# 根据索引号判断该条本地用户是否被启用，返回TRUE或者FALSE
def judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number=''):
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 判断该条是否启用 //*[@id="vpn_certadmin_table"]/tbody/tr[2]/td[5]/input
    enable = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[5]/input').is_selected()
    # print(enable)
    return enable


# 根据索引号 启用或者不启用本地用户-单个
def enable_or_unable_sslvpn_local_admin_lzy(browser, number='', enable='yes/no'):
    # 进入本地用户界面
    into_fun(browser, sslvpn本地用户)
    sleep(0.5)
    # 根据索引号选择要编辑的本地用户
    n = 2
    num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while num != number:
        n = n + 1
        if n <= 15:
            num = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
        else:
            print("需要点击下一页")
            assert False
    # 先判断该条是否启用
    enable1 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[5]/input').is_selected()
    if enable == "yes":
        if enable1 == True:
            pass
            # print("状态已经是selected")
        else:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[5]/input').click()
            # print('已勾选')
    if enable == 'no':
        if enable1 == True:
            browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[' + str(n) + ']/td[5]/input').click()
            # print('已取消勾选')
        else:
            pass
            # print("状态已经是unselected")


# 浏览器输入Portal站点-非法
def return_wrong_portal_login_lzy(browser, siteip='', siteport=''):
    sleep(0.5)
    # 打开 SCG web
    browser.get("https://" + str(siteip) + ":" + str(siteport))
    sleep(0.5)
    # 获取页面信息
    info = browser.find_element_by_xpath('//*[@id="main-message"]/h1/span').text
    # print(info)
    return info

# 浏览器输入Portal站点-截止 不带登录
def get_portal_lzy(browser, siteip='', siteport=''):
    sleep(0.5)
    # 打开 SCG web
    browser.get("https://" + str(siteip) + ":" + str(siteport))
    sleep(0.5)
    # # 获取页面信息
    # info = browser.find_element_by_xpath('//*[@id="main-message"]/h1').text
    # print(info)
    # browser.find_element_by_xpath('//*[@id="details-button"]').click()
    # browser.find_element_by_xpath('//*[@id="proceed-link"]').click()


# 浏览器输入Portal站点后的用户登录
def login_portal_login_lzy(browser, username="admin", password="admin"):
    sleep(0.5)
    # 登录
    browser.find_element_by_xpath('//*[@id="name"]').clear()
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="passwd"]').clear()
    browser.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="sub_btn"]').click()
    sleep(1)


# 浏览器输入安全站点
def get_into_safe_site__lzy(browser, siteip='', siteport=''):
    sleep(0.5)
    # 打开 SCG web
    browser.get("https://" + str(siteip) + ":" + str(siteport))
    sleep(0.5)