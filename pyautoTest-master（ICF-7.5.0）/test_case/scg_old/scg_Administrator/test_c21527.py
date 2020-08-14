import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *

test_id = "21527"


def test_c21527(browser):

    login_web(browser)
    add_admin_profile(browser,profile_name="test1")
    get_log(browser, 管理日志)
    browser.switch_to.default_content()
    # 切换到左侧frame
    browser.switch_to.frame("content")
    loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
    print(loginfo)

    try:
        assert "管理员视图成功" in loginfo
        rail_pass(178, test_id)

    except:
        rail_fail(178, test_id)
        assert "管理员视图成功" in loginfo
        print("????")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c21527.py"])