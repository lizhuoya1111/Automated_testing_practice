import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140971"
# 选择enable或者不选
# 操作成功；shell先显示和UI一致；admin log正常


def test_c140971(browser):

    try:

        login_web(browser, url=dev2)

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.1',
                                    enable='yes')

        status1 = is_static_route_enable_wxw(browser, destination='20.1.1.0/255.255.255.0')
        # print(status1)
        loginfo1 = get_log_info(browser, 管理日志)
        # print(loginfo1)

        add_static_route_single_wxw(browser, ip='21.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.1',
                                    enable='no')
        status2 = is_static_route_enable_wxw(browser, destination='21.1.1.0/255.255.255.0')
        # print(status2)
        loginfo2 = get_log_info(browser, 管理日志)
        # print(loginfo2)

        del_static_route_single_wxw(browser, destination1='20.1.1.0/255.255.255.0',
                                    destination2='21.1.1.0/255.255.255.0')

        try:
            assert "启用[Yes]" in loginfo1
            assert "启用[No]" in loginfo2
            assert status1 is True
            assert status2 is False
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "启用[Yes]" in loginfo1
            assert "启用[No]" in loginfo2
            assert status1 is True
            assert status2 is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev2)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])