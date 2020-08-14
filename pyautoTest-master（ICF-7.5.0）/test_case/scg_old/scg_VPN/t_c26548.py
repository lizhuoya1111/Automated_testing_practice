import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_interface import *
from page_obj.common.rail import *

test_id = "26548"


def test_c26548(browser):

    login_web(browser)

    add_net_ineterface(browser, "5.5.5.5", "24", "ge0/5")

    add_br(browser)

    browser.refresh()

    edit_br(browser, "br_3", "176.1.1.1", "24", stp="yes")

    info1 = add_ipsec_gw(browser, "tt2", "ipsec_to_test!", "ge0/5", "3.4.3.3", "123456", "31.1.1.0/24", "23.1.1.0/24")

    info2 = add_ipsec_gw(browser, "tt3","www", "br_3", "56.2.2.1","123456","95.5.2.0/24","65.65.2.0/24")

    if info1 == "操作成功" and info2 == "操作成功":

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "成功添加远程网关隧道" in loginfo
            rail_pass(178,test_id)

        except:
            rail_fail(178, test_id)
            assert "成功添加远程网关隧道" in loginfo

    else:
        rail_fail(178,test_id)

        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])