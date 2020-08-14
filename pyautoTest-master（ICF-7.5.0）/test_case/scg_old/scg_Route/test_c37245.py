import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_monitor import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37245
# 在monitor filter里输入destination、Gateway参数


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        monitor_filter_wxw(browser, dest='0.0.0.0', gateway='10.2.2.1', type='全部', search='yes', reset='no')

        getdest = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[2]/td[2]').text
        # print(getdest)

        getgateway = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[2]/td[3]').text
        # print(getgateway)

        try:
            assert "0.0.0.0" in getdest
            assert "10.2.2.1" in getgateway
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "0.0.0.0" in getdest
            assert "10.2.2.81" in getgateway

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])