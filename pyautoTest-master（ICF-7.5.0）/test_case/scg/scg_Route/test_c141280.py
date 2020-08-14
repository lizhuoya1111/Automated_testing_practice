import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141280"
# 网关输入不合法IP：255.255.255.255
# 可以添加成功  状态为down
# 策略路由单网关


def test_c141280(browser):
    try:
        login_web(browser, url=dev1)
        # 添加策略路由单网关 网关IP A.2.3.155
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='24',
                                                            dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                                            serv='any', out_device=interface_name_1, gateway='255.255.255.255')
        # 获取此策略路由状态 up/down
        state1 = return_policy_route_state(browser)

        # 还原
        del_policy_route_singele_wxw(browser, destination='192.168.5.0/255.255.255.0')



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