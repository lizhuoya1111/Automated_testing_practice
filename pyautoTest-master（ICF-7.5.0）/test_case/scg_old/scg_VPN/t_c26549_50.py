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

test_id = "26549"

def test_c26549(browser):

    login_web(browser)

    info1 = add_ipsec_gw(browser, "t26549", "ipsec_to_test!", "ge0/5", "3.4.3.49", "123456", "49.1.1.0/24", "23.49.1.0/24")

    if info1 == "操作成功":

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "成功添加远程网关隧道" in loginfo
            rail_pass(178,test_id)
            rail_pass(178,"26550")

        except:
            rail_fail(178, test_id)
            assert "成功添加远程网关隧道" in loginfo

    else:
        rail_fail(178,test_id)

        assert False

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c26549_50.py"])