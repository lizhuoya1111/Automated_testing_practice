import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from page_obj.scg.scg_button import *

def ipsec_est(scg):


    #scg.get('https://10.2.2.81')

    scg.get("https://10.2.2.81")

    scg.implicitly_wait(20)

    scg.find_element_by_xpath("//*[@id='input_username']").send_keys("admin")
    # 输入帐号

    scg.find_element_by_xpath("//*[@id='input_password']").send_keys("admin@139")
    # 输入密码

    scg.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[4]/div/div/input").send_keys("0613")
    # 万能验证码0013

    scg.find_element_by_xpath("//*[@id='login-div']/form/div[5]/input").click()
    # 点击登入，验证码让王博先屏蔽掉

    # ipsec.switch_to.frame(ipsec.find_element_by_xpath("/html/frameset/frame"))
    # ipsec.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()

    scg.switch_to.frame("lefttree")
    # 登入后，定位到左侧frame

    scg.find_element_by_xpath(虚拟专网).click()
    # 点击”虚拟专网“

    scg.find_element_by_xpath('//*[@id="menu"]/div[6]/div/ul/li[4]/span/a').click()
    # 点击”远程网关“

    scg.switch_to.default_content()
    # 定位到默认frame

    scg.switch_to.frame("content")
    # 定位到内容frame

    scg.find_element_by_xpath("/html/body/div[1]/div[3]/div/input").click()
    # 点击”增加远程网关“

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="name"]').send_keys("test1")
    # 输入name

    time.sleep(1)

    s1 = Select(scg.find_element_by_xpath('//*[@id="localif"]'))

    s1.select_by_visible_text("ge0/1")

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="gateway"]').send_keys("15.1.1.1")
    # 输入remote IP add

    time.sleep(1)

    # ipsec.find_element_by_xpath('//*[@id="localid"]').send_keys("CN=195.1.61.16")
    # input local ID

    scg.find_element_by_xpath('//*[@id="preshared_key"]').send_keys("123456")
    # input republicKey

    time.sleep(1)

    # ipsec.find_element_by_xpath('//*[@id="remoteid"]').send_keys("CN=195.2.61.16")
    # input remote ID

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="localsubnet"]').clear()
    # clear loacl subnet text

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="localsubnet"]').send_keys("196.1.1.0/24")
    # input local subnet

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="remotesubnet"]').send_keys("178.1.1.0/24")
    # input remote subnet

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="btn_save"]').click()
    # 点击”保存“

    time.sleep(1)

    scg.find_element_by_xpath('//*[@id="link_but"]').click()
    # 点击”retu
    time.sleep(1)
    sum = scg.find_element_by_xpath('//*[@id="rules_count"]').text

    time.sleep(1)

    print(sum)

    return sum





def test_sds(browser):
    assert ipsec_est(browser) == '45'



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_scg1.py"])