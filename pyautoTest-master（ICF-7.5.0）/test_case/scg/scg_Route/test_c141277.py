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

test_id = "141277"
# 输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256、
# 无法配置成功，系统报错
# 策略路由单网关


def test_c141277(browser):
    try:
        login_web(browser, url=dev1)
        # 添加策略路由单网关 源IPA.2.3.155
        alert1 = return_alert_when_add_policy_route_single_(browser, in_device='全部', src_ip='A.2.3.155', src_mask='24',
                                                   dst_ip='192.168.5.0', dst_mask='24', service='yes', serv='any')
        # 添加策略路由单网关 源IP #.$.4.5
        alert2 = return_alert_when_add_policy_route_single_(browser, in_device='全部', src_ip='#.$.4.5', src_mask='24',
                                                            dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                                            serv='any')
        # 添加策略路由单网关 源IP 1.1.1.256
        alert3 = return_alert_when_add_policy_route_single_(browser, in_device='全部', src_ip='1.1.1.256', src_mask='24',
                                                            dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                                            serv='any')

        try:
            assert "IP格式输入错误" in alert1 and "IP格式输入错误" in alert2 and "IP格式输入错误" in alert3
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "IP格式输入错误" in alert1 and "IP格式输入错误" in alert2 and "IP格式输入错误" in alert3
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])