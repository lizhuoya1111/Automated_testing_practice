import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140966"
# 点击批量删除按钮
# 操作成功；shell先显示和UI一致；admin log正常


def test_c140966(browser):

    try:

        login_web(browser, url=dev1)

        add_static_route_single_wxw(browser, ip='124.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
                                    enable='yes')
        add_static_route_single_wxw(browser, ip='121.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
                                    enable='yes')

        del_static_route_single_wxw(browser, destination1='124.1.1.0/255.255.255.0',
                                    destination2='121.1.1.0/255.255.255.0')

        loginfo = get_log(browser, 管理日志)
        # print(loginfo)

        exist1 = is_static_route_exist_wxw(browser, destination='124.1.1.0/255.255.255.0')
        # print("1exist is True or False:", exist1)

        exist2 = is_static_route_exist_wxw(browser, destination='121.1.1.0/255.255.255.0')
        # print("2exist is True or False:", exist2)

        try:
            assert "删除静态路由对象成功" in loginfo
            assert exist1 is False
            assert exist2 is False
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "删除静态路由对象成功" in loginfo
            assert exist1 is False
            assert exist2 is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])