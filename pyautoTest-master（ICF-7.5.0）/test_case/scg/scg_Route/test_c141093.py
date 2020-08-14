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

test_id = "141093"
# 验证list里的编辑按钮，编辑一条多网关静态路由
# 修改后的参数都能立即生效


def test_c1410693(browser):

    try:
        login_web(browser, url=dev2)
        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.1',
                                    ping_server='12.1.1.1', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='24.1.1.4',
                                    ping_server='24.1.1.4', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加一条多网关静态路由
        add_static_route_multi_gateway_wxw(browser, ip='14.1.1.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
										   grp_mem=["主用", "备份1"], enable="yes", save='yes', cancel='no')

        # 83上添加经过81到82的路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('ip route 12.1.1.0/24 gateway 13.1.1.1')
        # print(a83.output())
        a83.close()

        # 82 ping 83 不通
        result1 = diag_ping(browser, ipadd="13.1.1.3", packersize="100", count="5", ping_wait_time="2", interface=interface_name_2,
                            timesleep=7)
        # print(result1)

        # 编辑这条多网关静态路由 IP改为13.1.1.0
        edit_static_route_multi_gateway_wxw(browser, destination='14.1.1.0/255.255.255.0', ip='13.1.1.0', mask='24',
											gateway_grp='1(GROUP_1)', num=2, grp_mem=["主用", "备份1"],
											enable="yes", save='yes', cancel='no')

        # 82 ping 83 通
        result2 = diag_ping(browser, ipadd="13.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)
        # print(result2)

        # 删除路由
        del_ipv4_static_route_bydestination(browser, destination='13.1.1.0/255.255.255.0')

        # 删除多网关组
        del_multi_gateway_group_all(browser)

        # 删除83上路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('no ip route 12.1.1.0/24 gateway 13.1.1.1')
        # print(a83.output())
        a83.close()



        try:
            assert "Unreachable" in result1 and 'ms' in result2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "Unreachable" in result1 and 'ms' in result2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev2, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])