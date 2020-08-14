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

test_id = "141069"

# 策略路由克隆多网关路由
# 可正常添加


def test_c141069(browser):

    try:
        login_web(browser, url=dev1)

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes',
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


        # 克隆这条策略路由
        clone_policy_route_by_Index_number_lzy(browser, Index_number='1')
        # 获取日志
        log1 = get_log(browser, 管理日志)
        # print(log1)

        # 删除策略路由
        del_all_policy_route_lzy(browser)
        # 删除网关组
        del_multi_gateway_group_all(browser)





        try:
            assert "我是克隆出来哒" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "我是克隆出来哒" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])