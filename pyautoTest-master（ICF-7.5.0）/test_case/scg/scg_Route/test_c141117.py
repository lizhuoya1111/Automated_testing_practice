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

test_id = "141117"
# 添加一条策略路由，指定GW、out device（空接口、auto、桥接口、子接口、物理接口）
# 匹配该策略路由的数据包走指定的网关


def test_c141117(browser):

    try:
        # 81 上添加策略路由 out device选择物理接口
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

        # 81 上添加策略路由 out device选择子接口
        login_web(browser, url=dev1)
        # #3删除IP 添加子接口 并添加IP
        delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
        add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="1", work_mode="route", snat="", allow_ping="yes", describe="")
        add_vlan_inte_add(browser, interface_name=interface_name_3+'.1', ipadd='13.1.1.1', mask='255.255.255.0')
        # 转换模式
        shell_81 = Shell_SSH()
        shell_81.connect(hostip=dev1)
        shell_81.execute("en")
        shell_81.execute("conf t")
        shell_81.execute("inte gigabitethernet " + interface_name_3)
        shell_81.execute("switchmode  access")
        shell_81.close()

        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24',service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3+'.1', gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result2 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)
        # print("test1")
        # time.sleep(80)
        # 81 上添加策略路由 out device选择网桥
        login_web(browser, url=dev1)
        # 删除策略路由
        del_all_policy_route_lzy(browser)
        # 删除子接口 #3改为透明模式 添加到网桥br_11 添加IP
        del_vlan_inte_all(browser)
        physics_interface_change_transparent_interface(browser, interface1="", interface2="", interface3=interface_name_3,
                                                       interface4="",
                                                       interface5="", interface6="")
        bridge_add_jyl(browser, bridge_name="br_11", bridge_describe="", snat="no", allow_ping="yes", block_intra_bridge_traffic="")
        bridge_edit_interface_jyl(browser, bridge_interface="br_11", interface=interface_name_3)
        bridge_ip_add(browser, bridge_interface="br_11", address_mode="manual", ip="13.1.1.1", mask="255.255.255.0", update_default_gateway="",
                      update_system_dns="")

        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device='br_11', gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result3 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2, timesleep=10)


        # 81 上添加策略路由 out device选择空
        login_web(browser, url=dev1)

        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device='空', gateway='0.0.0.0', enable='yes',
                                    disnable='no', desc='maioshu')
        # 82 ping 83
        login_web(browser, url=dev2)
        result4 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="8", ping_wait_time="2",
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

        # 删除网桥
        delete_bridge_byname(browser, br_name="br_11")

        # #3改为路由模式 并添加IP
        transparent_interface_change_physics_interface_lzy(browser, interface1="", interface2="", interface3=interface_name_3,
                                                           interface4="", interface5="", interface6="")
        add_physical_interface_ip_wxw(browser, interface=interface_name_3, ip='13.1.1.1', mask='24')




        try:
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" not in result4
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" not in result4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])