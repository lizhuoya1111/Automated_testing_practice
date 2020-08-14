import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141261"
# 输入GW IP所在网段不在出device上
# 可以添加成功 但状态为down


def test_c141261(browser):
    try:
        login_web(browser, url=dev1)
        add_static_route_single_wxw(browser, ip='192.168.30.0', mask='255.255.255.0', out_device=interface_name_1, gateway='194.1.1.1', enable='yes')
        state1 = return_static_route_state(browser, destination='192.168.30.0/255.255.255.0')
        # 还原
        del_ipv4_static_route_bydestination(browser, destination='192.168.30.0/255.255.255.0')
        try:
            assert "down" in state1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "down" in state1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])