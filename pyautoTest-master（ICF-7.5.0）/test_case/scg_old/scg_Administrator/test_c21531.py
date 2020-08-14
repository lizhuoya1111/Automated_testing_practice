import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *

test_id = 21531
def test_main(browser):
    login_web(browser)
    # 点击管理员
    browser.find_element_by_xpath(管理员).click()
    # 切换到默认frame
    browser.switch_to.default_content()
    # 切换到内容frame
    browser.switch_to.frame("content")
    # 点击管理员列表
    browser.find_element_by_xpath('//*[@id="tabs"]/li[1]/a/span').click()
    time.sleep(8)
    # 获取页面配置数
    num1 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    i = 1
    while i < int(num1):
        # 点击删除
        browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[11]/a[2]/img').click()
        time.sleep(2)
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        time.sleep(2)
        i += 1
    # 切换到默认frame
    browser.switch_to.default_content()
    # 切换到内容frame
    browser.switch_to.frame("content")
    # 点击管理员权限
    browser.find_element_by_xpath('//*[@id="tabs"]/li[2]/a/span').click()
    time.sleep(8)
    # 获取页面配置数
    num2 = browser.find_element_by_xpath('//*[@id="rules_count"]').text
    i = 3
    while i < int(num2):
        # 点击删除
        browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[6]/a[2]/img').click()
        time.sleep(2)
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        time.sleep(2)
        i += 1
    time.sleep(4)
    for x in range(1, 30):
        add_admin_profile(browser, profile_name='bob'+str(x), desc="bob权限"+str(x), cfg="只读", report="无权限")
    #获取web页面最大profile数目
    web_inrfo = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[33]/td[1]').text
    time.sleep(2)
    get_log(browser, 管理日志)
    # 切换到默认frame
    browser.switch_to.default_content()
    # 切换到内容frame
    browser.switch_to.frame("content")
    loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
    print(loginfo)


    try:
        assert "添加管理员视图成功" in loginfo
        assert web_inrfo == "32"
        rail_pass(178, test_id)

    except:
        rail_fail(178, test_id)
        assert "添加管理员视图失败" in loginfo
        assert web_inrfo == "32"



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c21531.py"])