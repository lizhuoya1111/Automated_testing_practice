import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37184
# 填入destination IPV4/Mask,填入具体的目的地址和掩码


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.83")

        add_policy_route_single_wxw(browser, in_device='ge0/3', src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device='ge0/2', gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        exist = is_policy_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist)

        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')

        try:
            assert "添加策略路由对象成功" in loginfo
            assert exist is True
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "添加策略路由对象成功" in loginfo
            assert exist is True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])