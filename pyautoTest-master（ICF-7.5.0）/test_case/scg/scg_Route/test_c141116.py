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

test_id = "141116"
# 添加一条策略路由，指定service（包括any、预定义服务、自定义服务、服务组）
# 匹配了servicep的数据包才能匹配该路由走指定的网关


def test_c141116(browser):

    try:
        # 81 上添加策略路由 服务选择any
        login_web(browser, url=dev1)
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')

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

        # 82 ping 83
        login_web(browser, url=dev2)
        result1 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)
        # print(result1)

        # 81 上添加策略路由 服务选择预定义服务
        login_web(browser, url=dev1)
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='PING',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result2 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)

        # 81 上添加策略路由 服务选择自定义服务
        login_web(browser, url=dev1)
        # 添加自定义服务
        add_obj_service_wxw(browser, name='lzy', desc='zhe是ge描shu',
                            tcp='no', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
                            udp='no', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
                            icmp='yes', item='ping',
                            ip='', number='85')

        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='lzy',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result3 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)

        # 81 上添加策略路由 服务选择服务组
        login_web(browser, url=dev1)
        # 添加服务组
        add_obj_serv_grp_wxw(browser, name='lzy', desc='', serv_obj='C:lzy')

        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='yes', serv_grp='lzy',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result4 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
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

        # 删除服务组
        del_all_obj_serv_grp_wxw(browser)

        # 删除自定义服务
        del_obj_service_wxw(browser, name='lzy')


        try:
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" in result4
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" in result4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])