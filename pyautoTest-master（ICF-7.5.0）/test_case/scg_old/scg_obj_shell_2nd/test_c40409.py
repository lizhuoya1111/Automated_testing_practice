import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40409
# 添加一个weekly schedule,每天包含相同的schedule,查看log


def test_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击对象
        browser.find_element_by_xpath(对象).click()
        # 点击计划任务
        browser.find_element_by_xpath(计划任务).click()
        # 点击基础计划任务
        browser.find_element_by_xpath('//*[@id="menu"]/div[4]/div/ul/li[5]/ul/li[1]/span/a/span').click()

        add_obj_schdule_wxw(browser, name='schdule_409', desc='描述', recurring='yes', fromtime='01:00', totime='02:00')

        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击计划任务
        browser.find_element_by_xpath(计划任务).click()
        # 点击周计划任务
        browser.find_element_by_xpath(周计划任务).click()

        add_obj_weekly_schdule_wxw(browser, name='week_schd_409', desc='miaoshu',
                                   monday='yes', schdule1='schdule_409',
                                   tuesday='yes', schdule2='schdule_409',
                                   wednesday='yes', schdule3='schdule_409',
                                   thursday='yes', schdule4='schdule_409',
                                   friday='yes', schdule5='schdule_409',
                                   saturday='yes', schdule6='schdule_409',
                                   sunday='yes', schdule7='schdule_409', )

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
        # print(loginfo)

        try:
            assert "配置周程表对象成功，添加内部对象 [week_schd_409]" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "配置周程表对象成功，添加内部对象 [week_schd_409]" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40409.py"])