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

test_id = "141138"
# 验证向上添加、向下添加路由功能
# 策略路由正确的添加到指定的位置，验证移动后优先级是否一致


def test_c141138(browser):

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

        # 添加一条多网关策略路由 (不启用)
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='no',
                                   disable='yes', desc='添加多网关策略路由', save='yes', cancel='no')

        # 82上添加到13.1.1.0网段 和34.1.1.0网段的路由
        a82 = Shell_SSH()
        a82.connect(hostip=dev2)
        a82.execute('en')
        a82.execute('con t')
        a82.execute('ip route 13.1.1.0/24 gateway 12.1.1.1')
        a82.execute('ip route 34.1.1.0/24 gateway 12.1.1.1')
        a82.close()
        # 83上添加到12.1.1.0网段的路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('ip route 12.1.1.0/24 gateway 13.1.1.1')
        a83.close()

        # 82 ping 83 不通
        login_web(browser, url=dev2)
        result1 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2, timesleep=6)
        # print(result1)

        # 向上添加路由（可用）
        login_web(browser, url=dev1)
        add_policy_route_by_Index_number_upward_or_downward_lzy(browser, Index_number='1', upward='yes',
                                                                downward='no',
                                                                addmult='yes', m_in_device='全部', m_src_ip='12.1.1.0',
                                                                m_src_mask='24',
                                                                m_dst_ip='34.1.1.0', m_dst_mask='24', m_service='yes',
                                                                m_serv='any',
                                                                m_service_grp='no', m_serv_grp='H323',
                                                                m_gw_group='1(GROUP_1)', m_grp_mem=["主用", "备份1"], m_enable='yes',
                                                                m_desc='maioshu', m_save='yes', m_cancel='no',
                                                                addsingle='no', s_in_device='全部', s_src_ip='',
                                                                s_src_mask='',
                                                                s_dst_ip='', s_dst_mask='', s_service='yes/no',
                                                                s_serv='any',
                                                                s_service_grp='yes/no', s_serv_grp='H323',
                                                                s_Intelligent_protocol='yes/no',
                                                                s_out_device='', s_gateway='', s_enable='yes/no',
                                                                s_desc='maioshu')

        # 82 ping 83 通
        login_web(browser, url=dev2)
        result2 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2, timesleep=3)
        # print(result2)

        # 向下添加路由（不可用）
        login_web(browser, url=dev1)
        add_policy_route_by_Index_number_upward_or_downward_lzy(browser, Index_number='1', upward='no',
                                                                downward='yes',
                                                                addmult='yes', m_in_device='全部', m_src_ip='12.1.1.0',
                                                                m_src_mask='24',
                                                                m_dst_ip='34.1.1.0', m_dst_mask='24', m_service='yes',
                                                                m_serv='any',
                                                                m_service_grp='no', m_serv_grp='H323',
                                                                m_gw_group='1(GROUP_1)', m_grp_mem=["主用", "备份1"],
                                                                m_enable='no',
                                                                m_desc='maioshu', m_save='yes', m_cancel='no',
                                                                addsingle='no', s_in_device='全部', s_src_ip='',
                                                                s_src_mask='',
                                                                s_dst_ip='', s_dst_mask='', s_service='yes/no',
                                                                s_serv='any',
                                                                s_service_grp='yes/no', s_serv_grp='H323',
                                                                s_Intelligent_protocol='yes/no',
                                                                s_out_device='', s_gateway='', s_enable='yes/no',
                                                                s_desc='maioshu')
        # 82 ping 83 通
        login_web(browser, url=dev2)
        result3 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2, timesleep=3)


        # 删除83上路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('no ip route 12.1.1.0/24 gateway 13.1.1.1')
        a83.close()
        # 删除82上路由
        a82 = Shell_SSH()
        a82.connect(hostip=dev2)
        a82.execute('en')
        a82.execute('con t')
        a82.execute('no ip route 13.1.1.0/24 gateway 12.1.1.1')
        a82.execute('no ip route 34.1.1.0/24 gateway 12.1.1.1')
        a82.close()

        # 81 上删除策略路由
        login_web(browser, url=dev1)
        del_all_policy_route_lzy(browser)
        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "Un" in result1 and "ms" in result2 and 'ms' in result3
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "Un" in result1 and "ms" in result2 and 'ms' in result3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])