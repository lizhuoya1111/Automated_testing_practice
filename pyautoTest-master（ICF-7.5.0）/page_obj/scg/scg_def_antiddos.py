import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from page_obj.scg.scg_button import *
import pytest
import sys
from page_obj.scg.scg_def import *
from page_obj.common.my_selenium import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *


# antiddos设置
def antiddos_settings_wxw(browser, function_enable='yes', function_disable='no',
                          syn_cookie='yes/no', allways_on='yes/no', intelligent_defense='yes/no',
                          log_enable='yes/no', log_messages='1',
                          other_dos_attack='yes/no',
                          land_attack='yes/no', ping_of_death='yes/no', winnuke='yes/no',
                          replay_attack='yes/no', smurf='yes/no', ip_fragment_attack='yes/no'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS设置
    # browser.find_element_by_xpath(Anti_DDoS设置).click()
    #
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS设置)
    if function_enable == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_0"]').click()
    if function_disable == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_1"]').click()
    if syn_cookie == 'yes':
        if browser.find_element_by_xpath('//*[@id="syncookie"]').is_selected() is True:
            pass
            # print("syn_cookie已打开")
        else:
            browser.find_element_by_xpath('//*[@id="syncookie"]').click()
    else:
        if browser.find_element_by_xpath('//*[@id="syncookie"]').is_selected() is True:
            browser.find_element_by_xpath('//*[@id="syncookie"]').click()
        else:
            pass
            # print("syn_cookie已关闭")
    if allways_on == 'yes':
        browser.find_element_by_xpath('//*[@id="syncookie_mode_0"]').click()
    if intelligent_defense == 'yes':
        browser.find_element_by_xpath('//*[@id="syncookie_mode_1"]').click()
    if log_enable == 'yes':
        browser.find_element_by_xpath('//*[@id="log_0"]').click()
        browser.find_element_by_xpath('//*[@id="time"]').clear()
        browser.find_element_by_xpath('//*[@id="time"]').send_keys(log_messages)
    else:
        browser.find_element_by_xpath('//*[@id="log_1"]').click()
    if other_dos_attack == 'yes':
        try:
            browser.find_element_by_xpath('//*[@id="hidden_icon2"]').click()
        except:
            pass
        if land_attack == 'yes':
            if browser.find_element_by_xpath('//*[@id="land_attack"]').is_selected() is True:
                pass
                # print("land_attack已选中")
            else:
                browser.find_element_by_xpath('//*[@id="land_attack"]').click()
        else:
            if browser.find_element_by_xpath('//*[@id="land_attack"]').is_selected() is True:
                browser.find_element_by_xpath('//*[@id="land_attack"]').click()
            else:
                pass
                # print("land_attack未选中")

        if ping_of_death == 'yes':
            browser.find_element_by_xpath('//*[@id="ping"]').click()
            if ping_of_death == 'yes':
                if browser.find_element_by_xpath('//*[@id="ping"]').is_selected() is True:
                    pass
                    # print("ping_of_death已选中")
                else:
                    browser.find_element_by_xpath('//*[@id="ping"]').click()
            else:
                if browser.find_element_by_xpath('//*[@id="ping"]').is_selected() is True:
                    browser.find_element_by_xpath('//*[@id="ping"]').click()
                else:
                    pass
                    # print("ping_of_death未选中")

        if winnuke == 'yes':
            browser.find_element_by_xpath('//*[@id="winnuke"]').click()
            if winnuke == 'yes':
                if browser.find_element_by_xpath('//*[@id="winnuke"]').is_selected() is True:
                    pass
                    # print("winnuke已选中")
                else:
                    browser.find_element_by_xpath('//*[@id="winnuke"]').click()
            else:
                if browser.find_element_by_xpath('//*[@id="winnuke"]').is_selected() is True:
                    browser.find_element_by_xpath('//*[@id="winnuke"]').click()
                else:
                    pass
                    # print("winnuke未选中")

        if replay_attack == 'yes':
            browser.find_element_by_xpath('//*[@id="replay_attack"]').click()
            if replay_attack == 'yes':
                if browser.find_element_by_xpath('//*[@id="replay_attack"]').is_selected() is True:
                    pass
                    # print("replay_attack已选中")
                else:
                    browser.find_element_by_xpath('//*[@id="replay_attack"]').click()
            else:
                if browser.find_element_by_xpath('//*[@id="replay_attack"]').is_selected() is True:
                    browser.find_element_by_xpath('//*[@id="replay_attack"]').click()
                else:
                    pass
                    # print("replay_attack未选中")

        if smurf == 'yes':
            browser.find_element_by_xpath('//*[@id="smurf"]').click()
            if replay_attack == 'yes':
                if browser.find_element_by_xpath('//*[@id="smurf"]').is_selected() is True:
                    pass
                    # print("smurf已选中")
                else:
                    browser.find_element_by_xpath('//*[@id="smurf"]').click()
            else:
                if browser.find_element_by_xpath('//*[@id="smurf"]').is_selected() is True:
                    browser.find_element_by_xpath('//*[@id="smurf"]').click()
                else:
                    pass
                    # print("smurf未选中")

        if ip_fragment_attack == 'yes':
            browser.find_element_by_xpath('//*[@id="ipfrag"]').click()
            if replay_attack == 'yes':
                if browser.find_element_by_xpath('//*[@id="ipfrag"]').is_selected() is True:
                    pass
                    # print("ip_fragment_attack已选中")
                else:
                    browser.find_element_by_xpath('//*[@id="ipfrag"]').click()
            else:
                if browser.find_element_by_xpath('//*[@id="ipfrag"]').is_selected() is True:
                    browser.find_element_by_xpath('//*[@id="ipfrag"]').click()
                else:
                    pass
                    # print("ip_fragment_attack未选中")
    time.sleep(0.5)
    # 点击保存 //*[@id="container"]/div/form/div[3]/div/input[2]
    try:
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div/input[2]').click()
    except:
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[3]/div/input[2]').click()


# 添加Anti-DDoS配置
def add_antiddos_profile_wxw(browser, name='profile', desc='miaoshu', schdule='请选择',
                             sn_perrule='0', sn_perip='0', sn_sche_perrule='0', sn_sche_perip='0',
                             ss_perrule='0', ss_perip='0', ss_sche_perrule='0', ss_sche_perip='0',
                             ps_perrule='0', ps_perip='0', ps_sche_perrule='0', ps_sche_perip='0',
                             synlow='0', synhigh='0', save='yes', cancel='yes/no'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS用户配置
    # browser.find_element_by_xpath(Anti_DDoS用户配置).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    # 点击增加
    into_fun(browser, Anti_DDoS用户配置)
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 选择schdule//*[@id="schedule"]
    s1 = Select(browser.find_element_by_xpath('//*[@id="schedule"]'))
    s1.select_by_visible_text(schdule)
    # 输入会话数
    browser.find_element_by_xpath('//*[@id="sn_perrule"]').send_keys(sn_perrule)
    browser.find_element_by_xpath('//*[@id="sn_perip"]').send_keys(sn_perip)
    browser.find_element_by_xpath('//*[@id="sn_sche_perrule"]').send_keys(sn_sche_perrule)
    browser.find_element_by_xpath('//*[@id="sn_sche_perip"]').send_keys(sn_sche_perip)
    # 输入会话/秒
    browser.find_element_by_xpath('//*[@id="ss_perrule"]').send_keys(ss_perrule)
    browser.find_element_by_xpath('//*[@id="ss_perip"]').send_keys(ss_perip)
    browser.find_element_by_xpath('//*[@id="ss_sche_perrule"]').send_keys(ss_sche_perrule)
    browser.find_element_by_xpath('//*[@id="ss_sche_perip"]').send_keys(ss_sche_perip)
    # 输入数据包/秒
    browser.find_element_by_xpath('//*[@id="ps_perrule"]').send_keys(ps_perrule)
    browser.find_element_by_xpath('//*[@id="ps_perip"]').send_keys(ps_perip)
    browser.find_element_by_xpath('//*[@id="ps_sche_perrule"]').send_keys(ps_sche_perrule)
    browser.find_element_by_xpath('//*[@id="ps_sche_perip"]').send_keys(ps_sche_perip)
    # 输入高低阈值
    browser.find_element_by_xpath('//*[@id="synlow"]').send_keys(synlow)
    browser.find_element_by_xpath('//*[@id="synhigh"]').send_keys(synhigh)
    # 保存
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="btn_save"]').click()
    # 取消
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="synhigh"]').click()


# 删除指定的Anti-DDoS配置
def del_antiddos_profile_wxw(browser, name='profile'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS用户配置
    # browser.find_element_by_xpath(Anti_DDoS用户配置).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS用户配置)
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.replace(' ', '')
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.replace(' ', '')
    # 点击删除
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[7]/a[2]/img').click()


# 添加Anti-DDoS规则
def add_antiddos_rule_wxw(browser, name='rule', desc='miaoshu', zone='Z:any',
                          s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
                          s_ip='yes/no', saddress_custom='', saddress_mask='',
                          d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
                          d_ip='yes/no', daddress_custom='', daddress_mask='',
                          serv='P:any', profile='', monitor='yes', defense='yes/no',
                          save='yes/no', cancel='yes/no'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS规则列表
    # browser.find_element_by_xpath(Anti_DDoS规则列表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS规则列表)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 选择源网络
    s1 = Select(browser.find_element_by_xpath('//*[@id="zone"]'))
    s1.select_by_visible_text(zone)
    # 选择源地址
    if s_any == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_0"]').click()
    if s_single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').send_keys(saddress_sip)
    if s_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').send_keys(saddress_custom)
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').send_keys(saddress_mask)
    # 选择目的地址
    if d_any == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_0"]').click()
    if d_single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="daddress_sip"]').send_keys(daddress_sip)
    if d_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="daddress_custom1"]').send_keys(daddress_custom)
        browser.find_element_by_xpath('//*[@id="daddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="daddress_custom2"]').send_keys(daddress_mask)

    # 选择服务
    s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
    s1.select_by_visible_text(serv)
    # 选择阈值profile
    s1 = Select(browser.find_element_by_xpath('//*[@id="lmt_profile"]'))
    s1.select_by_visible_text(profile)
    # 选择模式
    if monitor == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_0"]').click()
    if defense == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_1"]').click()
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()


# 删除Anti-DDoS规则
def del_antiddos_rule_wxw(browser, name='rule'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS规则列表
    # browser.find_element_by_xpath(Anti_DDoS规则列表).click()
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS规则列表)
    # 点击删除
    n = 3
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.replace(' ', '')
    # print(getname)
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[2]').text.replace(' ', '')
        # print(getname)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(n)+']/td[12]/a[2]/img').click()


# 编辑指定的Anti-DDoS规则
def edit_antiddos_rule_wxw(browser, name='rule', desc='miaoshu', zone='Z:any',
                           s_any='yes/no', s_single_ip='yes/no', saddress_sip='',
                           s_ip='yes', saddress_custom='192.168.24.0', saddress_mask='24',
                           d_any='yes/no', d_single_ip='yes/no', daddress_sip='',
                           d_ip='yes', daddress_custom='12.12.12.0', daddress_mask='24',
                           serv='P:FTP', profile='profile_606', monitor='yes', defense='yes',
                           save='yes', cancel='yes/no'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # 点击Anti_DDoS规则列表
    # browser.find_element_by_xpath(Anti_DDoS规则列表).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS规则列表)
    # 点击编辑//*[@id="table"]/tbody/tr[3]/td[12]/a[1]/img
    n = 3
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
    # print(getname)
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
        # print(getname)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[12]/a[1]/img').click()
    # 修改描述
    browser.find_element_by_xpath('//*[@id="description"]').clear()
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    # 选择源网络
    s1 = Select(browser.find_element_by_xpath('//*[@id="zone"]'))
    s1.select_by_visible_text(zone)
    # 选择源地址
    if s_any == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_0"]').click()
    if s_single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').send_keys(saddress_sip)
    if s_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').send_keys(saddress_custom)
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').send_keys(saddress_mask)
    # 选择目的地址
    if d_any == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_0"]').click()
    if d_single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="daddress_sip"]').clear()
        browser.find_element_by_xpath('//*[@id="daddress_sip"]').send_keys(daddress_sip)
    if d_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="daddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="daddress_custom1"]').clear()
        browser.find_element_by_xpath('//*[@id="daddress_custom1"]').send_keys(daddress_custom)
        browser.find_element_by_xpath('//*[@id="daddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="daddress_custom2"]').send_keys(daddress_mask)

    # 选择服务
    s1 = Select(browser.find_element_by_xpath('//*[@id="service"]'))
    s1.select_by_visible_text(serv)
    # 选择阈值profile
    s1 = Select(browser.find_element_by_xpath('//*[@id="lmt_profile"]'))
    s1.select_by_visible_text(profile)
    # 选择模式
    if monitor == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_0"]').click()
    if defense == 'yes':
        browser.find_element_by_xpath('//*[@id="mode_1"]').click()
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 添加黑/白名单
def add_black_or_white_list_wxw(browser, name='list', desc='', any='yes',
                           single_ip='yes/no', sip='',
                           ip='yes/no', custom='', mask='',
                           address='yes/no', srange='',
                           white='yes/no', black='yes/no', never='yes',
                           date='yes/no', expire_date='2019-03-06', expire_time='02:00:00',
                           save='yes/no', cancel='yes/no'):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # Anti_DDoS黑_白名单
    # browser.find_element_by_xpath(Anti_DDoS黑_白名单).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS黑_白名单)
    # 点击增加
    browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
    # 输入名称
    browser.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    # 输入描述
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    if any == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_0"]').click()
    if single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').send_keys(sip)
    if ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').send_keys(custom)
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').send_keys(mask)
    if address == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_4"]').click()
        s1 = Select(browser.find_element_by_xpath('//*[@id="srange"]'))
        s1.select_by_visible_text(srange)
    # 选择类型
    if white == 'yes':
        browser.find_element_by_xpath('//*[@id="type_0"]').click()
    if black == 'yes':
        browser.find_element_by_xpath('//*[@id="type_1"]').click()
    # 选择过期的日期
    if never == 'yes':
        browser.find_element_by_xpath('//*[@id="expire_time_0"]').click()
    if date == 'yes':
        browser.find_element_by_xpath('//*[@id="expire_time_1"]').click()
        browser.find_element_by_xpath('//*[@id="date"]').send_keys(expire_date)
        browser.find_element_by_xpath('//*[@id="time"]').send_keys(expire_time)
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[3]').click()
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[4]').click()


# 删除黑/白名单
def del_black_or_white_list_wxw(browser, name='list'):
    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # Anti_DDoS黑_白名单
    # browser.find_element_by_xpath(Anti_DDoS黑_白名单).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS黑_白名单)
    # 点击删除
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
    # print(getname)
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
        # print(getname)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[2]/img').click()


# 编辑黑/白名单
def edit_black_or_white_list_wxw(browser, name='list', desc='', any='yes',
                                 single_ip='yes/no', sip='',
                                 ip='yes/no', custom='', mask='',
                                 address='yes/no', srange='',
                                 white='yes/no', black='yes/no', never='yes',
                                 date='yes/no', expire_date='2019-03-06', expire_time='02:00:00',
                                 save='yes/no', cancel='yes/no'):

    # 切换到默认frame
    # browser.switch_to.default_content()
    # # 切换到左侧frame
    # browser.switch_to.frame("lefttree")
    # # 点击Anti_DDoS
    # browser.find_element_by_xpath(Anti_DDoS).click()
    # # Anti_DDoS黑_白名单
    # browser.find_element_by_xpath(Anti_DDoS黑_白名单).click()
	#
    # # 定位到默认frame
    # browser.switch_to.default_content()
    # # 定位到内容frame
    # browser.switch_to.frame("content")
    into_fun(browser, Anti_DDoS黑_白名单)
    # 点击编辑
    n = 2
    getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
    # print(getname)
    while getname != name:
        n = n + 1
        getname = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.replace(' ', '')
        # print(getname)
    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()
    # 修改描述
    browser.find_element_by_xpath('//*[@id="description"]').clear()
    browser.find_element_by_xpath('//*[@id="description"]').send_keys(desc)
    if any == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_0"]').click()
    if single_ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_1"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_sip"]').send_keys(sip)
    if ip == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_2"]').click()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom1"]').send_keys(custom)
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').clear()
        browser.find_element_by_xpath('//*[@id="saddress_custom2"]').send_keys(mask)
    if address == 'yes':
        browser.find_element_by_xpath('//*[@id="saddress_4"]').click()
        s1 = Select(browser.find_element_by_xpath('//*[@id="srange"]'))
        s1.select_by_visible_text(srange)
    # 选择类型
    if white == 'yes':
        browser.find_element_by_xpath('//*[@id="type_0"]').click()
    if black == 'yes':
        browser.find_element_by_xpath('//*[@id="type_1"]').click()
    # 选择过期的日期
    if never == 'yes':
        browser.find_element_by_xpath('//*[@id="expire_time_0"]').click()
    if date == 'yes':
        browser.find_element_by_xpath('//*[@id="expire_time_1"]').click()
        browser.find_element_by_xpath('//*[@id="date"]').clear()
        browser.find_element_by_xpath('//*[@id="date"]').send_keys(expire_date)
        browser.find_element_by_xpath('//*[@id="time"]').clear()
        browser.find_element_by_xpath('//*[@id="time"]').send_keys(expire_time)
    if save == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
    if cancel == 'yes':
        browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[4]').click()


# 获取anti-ddos用户配置中的索引、Profile名称、ID、会话数、会话速率、包速率以[索引,Profile名称,ID,会话数,会话速率.包速率]返回
def get_into_user_profile_all_jyl(browser):
    into_fun(browser, Anti_DDoS用户配置)
    time.sleep(1.5)
    antiddos_user_profilr_list_all = []
    br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
    for x1 in range(2, br_sum + 2):
        arp_list = []                               # //*[@id="table"]/tbody/tr[2]/td[1]
        get_index = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[1]').text.rstrip()
        get_profile_name = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[2]').text.rstrip()
        get_id = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[3]').text.rstrip()
        get_session_number = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
        get_session_rate = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
        get_packet_rate = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
        arp_list.append(get_index)
        arp_list.append(get_profile_name)
        arp_list.append(get_id)
        arp_list.append(get_session_number)
        arp_list.append(get_session_rate)
        arp_list.append(get_packet_rate)
        antiddos_user_profilr_list_all.append(arp_list)
    # print(arp_list_all)
    return antiddos_user_profilr_list_all


# 获取anti-ddos规则列表中、名称、ID、接口、源地址、目的地址、服务、阈值Profile、模式，[名称,ID,接口,源地址,目的地址,服务,阈值Profile,模式]返回
def get_into_rule_list_all_jyl(browser):
    into_fun(browser, Anti_DDoS规则列表)
    time.sleep(1.5)
    antiddos_rile_list_all = []
    br_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
    for x1 in range(3, br_sum + 3):
        arp_list = []
        get_rule_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[2]').text.rstrip()
        get_id = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[3]').text.rstrip()
        get_interface = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[4]').text.rstrip()
        get_sorce_add = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[5]').text.rstrip()
        get_des_add = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[6]').text.rstrip()
        get_server = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[7]').text.rstrip()
        get_limit_profile = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[8]').text.rstrip()
        get_mode = browser.find_element_by_xpath(
            '//*[@id="table"]/tbody/tr[' + str(x1) + ']/td[9]').text.rstrip()
        arp_list.append(get_rule_name)
        arp_list.append(get_id)
        arp_list.append(get_interface)
        arp_list.append(get_sorce_add)
        arp_list.append(get_des_add)
        arp_list.append(get_server)
        arp_list.append(get_limit_profile)
        arp_list.append(get_mode)
        antiddos_rile_list_all.append(arp_list)
    # print(arp_list_all)
    return antiddos_rile_list_all


# 移动anti-ddos规则列表,通过索引进行操作
def move_ddos_rule_list(browser, fromindex='', toindex=''):
    into_fun(browser, Anti_DDoS规则列表)
    time.sleep(1)
    loop=0
    # 如果fromindex < toindex，向下移动 ///*[@id="table"]/tbody/tr[3]/td[3]
    rule_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(int(fromindex)+2)+']/td[2]').text
    # print("rule_name=", rule_name)
    if int(fromindex) < int(toindex):
        rule_max = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
        # print("rule_max=", rule_max)
        cur_index = fromindex
        # print("cur_index=", cur_index)
        while int(cur_index) != int(toindex):
            # print(cur_index)
            if int(cur_index) == rule_max:
                break
            for x in range(3, 3+rule_max):
                get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text
                if get_name == rule_name:
                    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[11]/a[2]/img').click()
                    # print("down", cur_index, toindex, int(cur_index) != int(toindex))
                    time.sleep(1)
                    try:
                        browser.find_element_by_xpath('//*[@id="link_but"]').click()
                    except:
                        pass
                    for y in range(3, 3 + rule_max):
                        get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[2]').text
                        if get_name == rule_name:
                            cur_index = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[1]').text

    # 如果fromindex > toindex，向上移动
    if int(fromindex) > int(toindex):
        rule_max = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
        # print("rule_name=", rule_name)
        cur_index = fromindex
        # print("cur_index=", cur_index)
        while int(cur_index) != int(toindex):
            if int(cur_index) == 1:
                break
            for x in range(3, 3+rule_max):
                get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[2]').text
                if get_name == rule_name:
                    browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(x)+']/td[11]/a[1]/img').click()
                    # print("up", cur_index, toindex, int(cur_index) != int(toindex))
                    time.sleep(1)
                    try:
                        browser.find_element_by_xpath('//*[@id="link_but"]').click()
                    except:
                        pass
                    for y in range(3, 3 + rule_max):
                        get_name = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[2]').text
                        if get_name == rule_name:
                            cur_index = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(y) + ']/td[1]').text