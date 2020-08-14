import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *

test_id = "26555"


def test_c26555(browser):

    login_web(browser)

    info = add_ipsec_gw(browser, "tt26555", "ipsec_to_test!", "ge0/1", "3.3.3.3", "123456", "3.1.1.0/24", "13.1.1.0/24",
                        ike_id="yes",
                        localidtype="Email Address",
                        localid="test@test.com",
                        remoteidtype="Accept Any Remote ID",
                        remoteid=" "
                        )

    if info == "操作成功":

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

        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+ test_id +".py"])