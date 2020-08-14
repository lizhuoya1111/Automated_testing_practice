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

test_id = "141410"
# 路由多网关选择vlan子接口
# 通信正常


def test_c141410(browser):

    try:
        # 81上添加多网关组
        login_web(browser, url=dev1)

        # 81 上添加策略路由 in device选择子接口
        # #2删除IP 添加子接口 并添加IP
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="1", work_mode="route", snat="", allow_ping="yes", describe="")
        add_vlan_inte_add(browser, interface_name=interface_name_2+'.1', ipadd='12.1.1.1', mask='255.255.255.0')
        # 转换模式
        shell_81 = Shell_SSH()
        shell_81.connect(hostip=dev1)
        shell_81.execute("en")
        shell_81.execute("conf t")
        shell_81.execute("inte gigabitethernet " + interface_name_2)
        shell_81.execute("switchmode  access")
        shell_81.close()

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

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2+'.1', gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")


        add_policy_route_multi_wxw(browser, in_device=interface_name_2+'.1', src_ip='12.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='yes',
                                   disable='no', desc='添加多网关策略路由', save='yes', cancel='no')

        # 82 ping 83
        login_web(browser, url=dev2)
        result1 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
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

        # 删除多网关组
        login_web(browser, url=dev1)
        del_multi_gateway_group_all(browser)
        # 删除策略路由
        del_all_policy_route_lzy(browser)
        # 删除子接口
        del_vlan_inte_all(browser)

        # #2添加IP
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1', mask='24')




        try:
            assert "ms" in result1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])