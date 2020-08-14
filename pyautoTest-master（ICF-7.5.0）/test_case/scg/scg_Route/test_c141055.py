import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_monitor import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141055"
# 在monitor filter里输入destination、Gateway参数


def test_c141055(browser):

    try:
        login_web(browser, url=dev1)

        monitor_filter_wxw(browser, dest='192.168.1.0', gateway='', route_type='全部', search='yes', reset='no')

        getdest = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[2]/td[2]').text
        # print(getdest)

        getgateway = browser.find_element_by_xpath('//*[@id="route_monitor_table"]/tbody/tr[2]/td[3]').text
        # print(getgateway)

        try:
            assert "192.168.1.0" in getdest
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "192.168.1.0" in getdest

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])