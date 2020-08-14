import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141120"
# 验证策略路由优先级，优先匹配最前面的条目；move后匹配最前面的条目:
# 1.配置两条相同的策略路由，网关不同 （一个网关可以通、一个网关不能通 2.发送流量匹配策略路由的服务；
# 优先匹配最前面的条目；move后匹配最前面的条目：如果网关可以通的策略路由在上面，则数据可以通；移动网关不能通的策略路由在上面；则数据无法通信


def test_c141120(browser):

    try:
        # 81 上添加策略路由 2条 第一条网关通 第二条网关不通 后添加在上
        login_web(browser, url=dev1)
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='yes', desc='maioshu')
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.4', enable='yes',
                                    disnable='yes', desc='maioshu')

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
                            interface=interface_name_2, timesleep=7)
        print(result1)

        # 移动策略路由 使网关通的在上
        login_web(browser, url=dev1)
        move_policy_route_by_Index_number_lzy(browser, Index_number='2', to_number='1')

        # 82 ping 83
        login_web(browser, url=dev2)
        result2 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)


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



        try:
            assert "Unreachable" in result1 and "ms" in result2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "Unreachable" in result1 and "ms" in result2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])