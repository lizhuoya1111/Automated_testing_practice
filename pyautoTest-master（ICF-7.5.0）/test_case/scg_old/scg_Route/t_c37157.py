import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *


sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37157
# 点击批量删除按钮
# 操作成功；shell先显示和UI一致；admin log正常


def test_route_wxw(browser):

    try:

        login_web(browser, url="10.2.2.82")

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='12.1.1.1',
                                    enable='yes')
        add_static_route_single_wxw(browser, ip='21.1.1.0', mask='24', out_device='ge0/2', gateway='12.1.1.1',
                                    enable='yes')

        del_static_route_single_wxw(browser, destination1='20.1.1.0/255.255.255.0',
                                    destination2='21.1.1.0/255.255.255.0')

        loginfo = get_log_info_for_batch_dele2_wxw(browser, 管理日志)
        # print(loginfo)

        exist1 = is_static_route_exist_wxw(browser, destination='20.1.1.0/255.255.255.0')
        # print("1exist is True or False:", exist1)

        exist2 = is_static_route_exist_wxw(browser, destination='21.1.1.0/255.255.255.0')
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
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])