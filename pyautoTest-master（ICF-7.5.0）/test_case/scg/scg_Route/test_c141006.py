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

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141006"

# 编辑策略路由里所有参数：
# 1、编辑修改单网关策略路由的：incoming device、source network、netmask、destination network、
# netmask、service、gateway、outgoing device
# 2、编辑修改多网关策略路由的：incoming device、source network、netmask、
# destination network、netmask、service、gateway、outgoing device
# 操作成功；shell先显示和UI一致；admin log正常


def test_c141006(browser):

    try:
        login_web(browser, url=dev1)
        # 添加1条单网关策略路由
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='30.1.1.0', src_mask='24',
                                        dst_ip='40.1.1.0', dst_mask='24', service='no', serv='any',
                                        service_grp='no', serv_grp='H323',
                                        out_device=interface_name_2, gateway='12.1.1.2', enable='yes', disnable='no',
                                        desc='添加单网关策略路由')
        sleep(1)
        # 修改此单网关策略路由
        edit_policy_route_single_wxw(browser, destination='40.1.1.0/255.255.255.0', in_device=interface_name_2, src_ip='40.1.1.0',
                                     src_mask='24',
                                     dst_ip='30.1.1.0', dst_mask='24', service='no', serv='any',
                                     service_grp='yes', serv_grp='H323',
                                     out_device=interface_name_3, gateway='13.1.1.2', enable='yes',
                                     disnable='no', desc='修改后的单网关策略路由')

        # 获取日志
        log1 = get_log_info(browser, 管理日志)
        print(log1)
        # 删除全部策略路由
        del_all_policy_route_lzy(browser)

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
									device=interface_name_2, gateway='12.1.1.2', ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.2',
                                    ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加一条多网关策略路由
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='30.1.1.0', src_mask='24',
                                   dst_ip='40.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='yes',
                                   disable='no', desc='添加多网关策略路由', save='yes', cancel='no')

        # 修改此多网关策略路由
        edit_policy_route_multi_by_index_number_lzy(browser, index_number='1',
                                                    in_device='全部', src_ip='40.1.1.0', src_mask='24', dst_ip='30.1.1.0', dst_mask='24',
                                                    service='no', serv='any',
                                                    service_grp='yes', serv_grp='H323', gw_group='1(GROUP_1)', grp_mem=["备份1", "主用"],
                                                    enable='yes', desc='修改后的多网关策略路由', save='yes', cancel='no')


        # 获取日志
        log2 = get_log_info(browser, 管理日志)
        print(log2)

        # 删除全部策略路由
        del_all_policy_route_lzy(browser)
        # 删除多网关组
        del_multi_gateway_group_all(browser)



        try:
            assert "修改策略路由对象成功" in log1 and "修改策略路由对象成功" in log2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "修改策略路由对象成功" in log1 and "修改策略路由对象成功" in log2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])