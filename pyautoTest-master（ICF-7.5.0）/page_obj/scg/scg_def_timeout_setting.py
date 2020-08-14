from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_button import *


# 设置SSH超时时间（均输入不规范有告警框弹出）且返回告警框内容
def set_ssh_timeout(browser, ssh_timeout="86400"):
    # 定位到默认frame
    # browser.switch_to.default_content()
    # browser.switch_to.frame("lefttree")
    # # 点击系统
    # browser.find_element_by_xpath(系统).click()
    # if not browser.find_element_by_xpath('//*[@id="menu"]/div[1]/div/ul/li[2]/ul').is_displayed():
    #     # 如果不可见，点击加号，展开元素
    #     browser.find_element_by_xpath(系统管理).click()
    # # 点击物理接口
    # browser.find_element_by_xpath(管理员).click()
    # # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 管理员)
    # 点击系统设定
    browser.find_element_by_xpath('//*[@id="tabs"]/li[3]/a/span').click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="sshtimeout"]').clear()
    browser.find_element_by_xpath('//*[@id="sshtimeout"]').send_keys(ssh_timeout)
    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    time.sleep(2)
    # 获取提示框信息
    alert1 = browser.switch_to_alert().text
    print(alert1)
    browser.switch_to_alert().accept()
    return(alert1)


# 进入到会话表界面，其余什么操作都不做
def get_into_session(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)


# 进入到查询条件设定界面，其余什么操作都不做
def get_into_query_terms(browser):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)
    # 点击查询条件设定
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")


# 新增查询条件
def add_query_terms(browser, name, version='Any', protocol='65535(any)', fromzone='Z:any', sourceaddress='no',
                    sip='', sipmask='', sourcerange='no', sipstart='', sipend='', sourceaddressobject='yes', sipobjaddress='any',
                    tozone='Z:any', destinationaddress='no', dip='', dipmask='', destinationrange='no', dipstart='', dipend='',
                    destinationaddressobject='yes', dipobjaddress='any', service='any', number='1000'):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)
    # 点击查询条件设定
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")

    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 过滤条件设定
    # 名称
    browser.find_element_by_xpath('//*[@id="sessionfilter"]').send_keys(name)
    # 协议版本
    s1 = Select(browser.find_element_by_xpath('//*[@id="version"]'))
    s1.select_by_visible_text(version)
    # 协议号
    s2 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
    s2.select_by_visible_text(protocol)

    # 目的区域/接口
    s5 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
    s5.select_by_visible_text(tozone)
    # 目的地址
    if destinationaddress == 'yes':
        browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
        browser.find_element_by_xpath('//*[@id="dip"]').send_keys(dip)
        browser.find_element_by_xpath('//*[@id="dipmask"]').send_keys(dipmask)
    if destinationrange == 'yes':
        browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
        browser.find_element_by_xpath('//*[@id="dipstart"]').send_keys(dipstart)
        browser.find_element_by_xpath('//*[@id="dipend"]').send_keys(dipend)
    if destinationaddressobject == 'yes':
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="toattribute_2"]').click()
        s6 = Select(browser.find_element_by_xpath('//*[@id="dipobjaddress"]'))
        s6.select_by_visible_text(dipobjaddress)

    # 源区域/接口
    s3 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
    s3.select_by_visible_text(fromzone)
    # 源地址
    if sourceaddress == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
        browser.find_element_by_xpath('//*[@id="sip"]').send_keys(sip)
        browser.find_element_by_xpath('//*[@id="sipmask"]').send_keys(sipmask)
    if sourcerange == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
        browser.find_element_by_xpath('//*[@id="sipstart"]').send_keys(sipstart)
        browser.find_element_by_xpath('//*[@id="sipend"]').send_keys(sipend)
    if sourceaddressobject == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_2"]').click()
        s4 = Select(browser.find_element_by_xpath('//*[@id="sipobjaddress"]'))
        s4.select_by_visible_text(sipobjaddress)


    # 服务
    s7 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
    s7.select_by_visible_text(service)
    # 显示条数
    browser.find_element_by_xpath('//*[@id="lnumber"]').clear()
    browser.find_element_by_xpath('//*[@id="lnumber"]').send_keys(number)


    # 点击保存
    browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()


# 删除查询条件（按名称）
def del_query_terms_by_name(browser, name):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)
    # 点击查询条件设定
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 点击删除
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    # 点击删除
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[2]/img').click()


# 修改查询条件（按名称）
def modify_query_terms_by_name(browser, name, version='Any', protocol='65535(any)',fromzone='Z:any', sourceaddress='no',
                    sip='', sipmask='', sourcerange='no', sipstart='', sipend='', sourceaddressobject='yes', sipobjaddress='any',
                    tozone='Z:any', destinationaddress='no', dip='', dipmask='', destinationrange='no', dipstart='', dipend='',
                    destinationaddressobject='yes', dipobjaddress='any', service='any', number='1000'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)
    # 点击查询条件设定
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    # 点击修改
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    # print(getname)
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.strip()
    # 点击删除
    time.sleep(0.5)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()
    sleep(0.5)
    # 过滤条件设定
    # 名称
    browser.find_element_by_xpath('//*[@id="sessionfilter"]').send_keys(name)
    # 协议版本
    s1 = Select(browser.find_element_by_xpath('//*[@id="version"]'))
    s1.select_by_visible_text(version)
    # 协议号
    s2 = Select(browser.find_element_by_xpath('//*[@id="protocol"]'))
    s2.select_by_visible_text(protocol)

    # 源区域/接口
    s3 = Select(browser.find_element_by_xpath('//*[@id="fromzone"]'))
    s3.select_by_visible_text(fromzone)
    # 源地址
    if sourceaddress == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_0"]').click()
        browser.find_element_by_xpath('//*[@id="sip"]').clear()
        browser.find_element_by_xpath('//*[@id="sip"]').send_keys(sip)
        browser.find_element_by_xpath('//*[@id="sipmask"]').clear()
        browser.find_element_by_xpath('//*[@id="sipmask"]').send_keys(sipmask)
    if sourcerange == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_1"]').click()
        browser.find_element_by_xpath('//*[@id="sipstart"]').clear()
        browser.find_element_by_xpath('//*[@id="sipstart"]').send_keys(sipstart)
        browser.find_element_by_xpath('//*[@id="sipend"]').clear()
        browser.find_element_by_xpath('//*[@id="sipend"]').send_keys(sipend)
    if sourceaddressobject == 'yes':
        browser.find_element_by_xpath('//*[@id="fromattribute_2"]').click()
        s4 = Select(browser.find_element_by_xpath('//*[@id="sipobjaddress"]'))
        s4.select_by_visible_text(sipobjaddress)

    # 目的区域/接口
    s5 = Select(browser.find_element_by_xpath('//*[@id="tozone"]'))
    s5.select_by_visible_text(tozone)
    # 目的地址
    if destinationaddress == 'yes':
        browser.find_element_by_xpath('//*[@id="toattribute_0"]').click()
        browser.find_element_by_xpath('//*[@id="dip"]').clear()
        browser.find_element_by_xpath('//*[@id="dip"]').send_keys(dip)
        browser.find_element_by_xpath('//*[@id="dipmask"]').clear()
        browser.find_element_by_xpath('//*[@id="dipmask"]').send_keys(dipmask)
    if destinationrange == 'yes':
        browser.find_element_by_xpath('//*[@id="toattribute_1"]').click()
        browser.find_element_by_xpath('//*[@id="dipstart"]').clear()
        browser.find_element_by_xpath('//*[@id="dipstart"]').send_keys(dipstart)
        browser.find_element_by_xpath('//*[@id="dipend"]').clear()
        browser.find_element_by_xpath('//*[@id="dipend"]').send_keys(dipend)
    if destinationaddressobject == 'yes':
        browser.find_element_by_xpath('//*[@id="toattribute_2"]').click()
        s6 = Select(browser.find_element_by_xpath('//*[@id="dipobjaddress"]'))
        s6.select_by_visible_text(dipobjaddress)
    # 服务
    s7 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
    s7.select_by_visible_text(service)
    # 显示条数
    browser.find_element_by_xpath('//*[@id="lnumber"]').clear()
    browser.find_element_by_xpath('//*[@id="lnumber"]').send_keys(number)

    # 点击保存
    sleep(1)
    browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()


# 查询会话表（按过滤条件名称）
def query_Sessiontable_by_name(browser, name):
    # # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, 会话表)
    # 选择下拉框
    s1 = Select(browser.find_element_by_xpath('//*[@id="sessionfilter"]'))
    s1.select_by_visible_text(name)
    # 点击查询
    browser.find_element_by_xpath('//*[@id="session_table_form"]/table/tbody/tr/td[3]/input[2]').click()


# 获取某过滤条件下 查询出的会话总数  在查询会话表（按过滤条件名称）之后使用
def catch_number_after_qurey_Sessiontable_by_name(browser):

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")
    # 获取当前过滤条件下的会话数
    a1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    return(a1)


# 删除会话表（按过滤条件名称）
def del_Sessiontable_by_name(browser, name):
    # # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击报表
    # browser.find_element_by_xpath(报表).click()
    # # 点击会话表
    # browser.find_element_by_xpath(会话表).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")

    into_fun(browser, 会话表)
    # 选择下拉框
    s1 = Select(browser.find_element_by_xpath('//*[@id="sessionfilter"]'))
    s1.select_by_visible_text(name)
    # 点击删除
    browser.find_element_by_xpath('//*[@id="session_table_form"]/table/tbody/tr/td[4]/input').click()
    # 弹出警告框后接受告警
    browser.switch_to_alert().accept()



# 获取某过滤条件下 删除会话后 操作成功的弹出框内容 包括删除会话总数  在删除会话表（按过滤条件名称）之后使用
def catch_text_after_del_Sessiontable_by_name(browser):

    a1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
    return(a1)