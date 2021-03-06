import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37158
# 填入destination IPV4/Mask,填入具体的目的地址和掩码
# 操作成功；shell先显示和UI一致；admin log正常


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device='ge0/2', gateway='12.1.1.1',
                                    enable='yes')

        exist = is_static_route_exist_wxw(browser, destination='20.1.1.0/255.255.255.0')
        # print("exist is True or False:", exist)

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_ipv4_static_route_bydestination(browser,destination='20.1.1.0/255.255.255.0')

        try:
            assert "添加静态路由对象成功" in loginfo
            assert exist is True
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "添加静态路由对象成功" in loginfo
            assert exist is True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])