import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_policy_route import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37178
# 点击单个条目里删除按钮


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.83")

        add_policy_route_single_wxw(browser, in_device='ge0/3', src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device='ge0/2', gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')

        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')

        exist = is_policy_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print("exist is True or False:", exist)

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        try:
            assert "删除策略路由" in loginfo
            assert exist is False
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "删除策略路由" in loginfo
            assert exist is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])