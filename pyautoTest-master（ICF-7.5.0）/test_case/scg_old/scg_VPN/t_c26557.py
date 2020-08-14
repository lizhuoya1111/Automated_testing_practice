import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *

test_id = "26557"


def test_c26557(browser):

    login_web(browser)


    info1 = add_ipsec_gw(browser, "tt26557_1", "ipsec_to_test!", "ge0/1", "3.3.3.5", "123456", "3.1.1.0/24", "13.1.1.0/24",
                        ike_id="yes",
                        localidtype="Email Address",
                        localid="test@test.com",
                        remoteidtype="E-mail Address",
                        remoteid="test@test.com"
                        )

    info2 = add_ipsec_gw(browser, "tt26557_2", "ipsec_to_test!", "ge0/1", "3.3.3.5", "123456", "3.1.1.0/24", "13.1.1.0/24",
                        ike_id="yes",
                        localidtype="Domain",
                        localid="test@test.com",
                        remoteidtype="Domain",
                        remoteid="test@test.com"
                        )

    info3 = add_ipsec_gw(browser, "tt26557_3", "ipsec_to_test!", "ge0/1", "3.3.3.5", "123456", "3.1.1.0/24", "13.1.1.0/24",
                        ike_id="yes",
                        localidtype="IP Address",
                        localid="158.158.2.35",
                        remoteidtype="IP Address",
                        remoteid="128.118.22.35"
                        )

    info4 = add_ipsec_gw(browser, "tt26557_4", "ipsec_to_test!", "ge0/1", "3.3.3.5", "123456", "3.1.1.0/24",
                         "13.1.1.0/24",
                         ike_id="yes",
                         localidtype="IP Address",
                         localid="158.158.2.35",
                         remoteidtype="Distinguished Name",
                         remoteid="test1@test.com"
                         )

    if info1 == "操作成功" and info2 == "操作成功" and info3 == "操作成功" and info4 == "操作成功":

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