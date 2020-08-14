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

test_id = "141257"
# 输入不合法IP、掩码：1.1.1.1/255.255.255.256、1.1.1.1/32
# 无法配置成功，系统报错
# PS: 1.1.1.1/32可添加成功 故只验证了1.1.1.1/255.255.255.256

def test_c141257(browser):
    try:
        login_web(browser, url=dev3)
        alert1 = return_alert_after_add_static_route_single(browser, ip='1.1.1.1', mask='255.255.255.256', out_device=interface_name_1, gateway='192.168.1.2')

        try:
            assert "掩码格式输入错误，请重新输入" in alert1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "掩码格式输入错误，请重新输入" in alert1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev3)
        assert False

if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])