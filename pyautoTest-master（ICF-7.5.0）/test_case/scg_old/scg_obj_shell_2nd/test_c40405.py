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

test_id = 40405
# 添加一个sch obj,在ACL中引用,验证sch obj中R是否有显示


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

        # 添加一个计划任务对象
        add_obj_schdule_wxw(browser, name='schdule_1', desc='描述', recurring='yes', fromtime='01:00', totime='02:00')
        # 添加一个防火墙组
        add_acl_grp_wxw(browser, name='aclgroup_s1')
        # 添加一条acl规则
        add_acl_rule_wxw(browser, name='aclgroup_s1', schdule_obj='S:schdule_1')
        # 获取计划任务对象的引用
        get_schdule_obj_ref_wxw(browser, name='schdule_1')

        # 切换到默认frame
        browser.switch_to.default_content()

        # 切换到内容frame
        browser.switch_to.frame("content")

        # 获取引用
        ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text
        # print(ref)
        try:
            assert ref == "acl"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ref == "acl"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40405.py"])