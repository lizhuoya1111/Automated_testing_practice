import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37154
# 点击enable/disable status 按钮


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.83")

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='13.1.1.1',
                                    enable='yes')
        enable_static_route_single_wxw(browser, destination='20.1.1.0/255.255.255.0', enable='no',
                                       disnable='yes')
        get_status1 = get_static_route_status_wxw(browser, destination='20.1.1.0/255.255.255.0')

        loginfo1 = get_log_info(browser, 管理日志)
        # print(loginfo1)

        enable_static_route_single_wxw(browser, destination='20.1.1.0/255.255.255.0', enable='yes',
                                       disnable='no')
        get_status2 = get_static_route_status_wxw(browser, destination='20.1.1.0/255.255.255.0')

        loginfo2 = get_log_info(browser, 管理日志)
        # print(loginfo2)

        del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

        try:
            assert "启用[No]" in loginfo1
            assert get_status1 == "disable"
            assert "启用[Yes]" in loginfo2
            assert get_status2 == "enable"
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "启用[No]" in loginfo1
            assert get_status1 == "disable"
            assert "启用[Yes]" in loginfo2
            assert get_status2 == "enable"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])