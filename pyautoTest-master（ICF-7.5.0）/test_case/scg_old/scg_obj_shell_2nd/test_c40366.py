import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40366
# 选中多个obj grp,删除,查看log


def test_add_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击对象
        browser.find_element_by_xpath(对象).click()
        # 点击ipv4
        browser.find_element_by_xpath(IPv4).click()
        # 点击地址组
        browser.find_element_by_xpath(IPv4地址组).click()

        for n in range(1, 6):
            add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_366_'+str(n), desc='zhe是yi个描述1', addr_obj='A:any')

        del_more_obj_grp_wxw(browser, num=5)

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到内容frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
        # print(loginfo)
        try:
            assert "配置地址组对象成功，删除内部对象 " in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "配置地址组对象成功，删除内部对象 " in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40366.py"])