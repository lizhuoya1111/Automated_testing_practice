
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

test_id = "141166"

# 添加一条ISP多网关路由，enable和disable该路由条目
# enable时，路由表里状态显示为enable，并且数据匹配这条路由的数据可以从指定网关出去；disable时，该路由失效，路由表里状态显示为disable，通信无法进行


def test_c141166(browser):

    try:

        login_web(browser, url=dev1)
        # 添加ISP
        add_multi_isp_save_wxw(browser, name='lzy')

        # 导入IP
        import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='34.1.1.0.txt')

        # 添加路由 多网关
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_isp_route_lzy(browser, name='lzy', single_gateway='no', device='', gateway='',
					  multi_gateway='yes', gateway_group='1(GROUP_1)', grp_mem=['主用', '备份1'],
					  enable='no', disable='yes')

        # 84上添加到13.1.1.0网段路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()

        # 81 ping 84
        result1 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3, timesleep=5)
        # print(result1)

        # 修改ISP为启用
        edit_isp_enable_or_disable_byname(browser, name='lzy', enable='yes', disable='no')

        # 81 ping 84
        result2 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3, timesleep=3)
        # print(result2)

        # 删除ISP
        del_multi_isp_wxw(browser, name='lzy')
        # 删除多网关组
        del_multi_gateway_group_all(browser)
        # 84上删除到13.1.1.0网段路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("no ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()

        try:
            assert "Un" in result1 and "ms" in result2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "Un" in result1 and "ms" in result2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev4])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])