import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141139"
# 验证move to功能
# 策略路由正确的添加到指定的位置，验证移动后优先级是否一致
# 优先级是否一致怎么验证啊?


def test_c141139(browser):

    try:
        # 81 上添加策略路由
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加4条多网关策略路由
        for x in range(1, 5):
            add_policy_route_multi_wxw(browser, in_device='全部', src_ip=str(x)+'.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='yes',
                                   disable='no', desc='添加多网关策略路由'+str(x), save='yes', cancel='no')
        # 添加一条多网关路由（启用）
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='yes',
                                   disable='no', desc='添加多网关策略路由', save='yes', cancel='no')
        # 移动路由
        move_policy_route_by_Index_number_lzy(browser, Index_number='1', to_number='5')

        # 获取日志
        log1 = get_log(browser, 管理日志)

        # 81 上删除策略路由
        login_web(browser, url=dev1)
        del_all_policy_route_lzy(browser)
        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "移动" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "移动" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])