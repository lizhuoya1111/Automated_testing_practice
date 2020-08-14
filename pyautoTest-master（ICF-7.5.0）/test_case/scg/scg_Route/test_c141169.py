
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

test_id = "141169"

# 修改指定ISP路由条目里的网关（必须先删除网关在添加。单网关便多网关、多网关变单网关、多网关变多网关）
# 修改可以立即生效，数据包匹配目的ip的会走修改后的网关


def test_c141169(browser):

    try:

        login_web(browser, url=dev1)
        # 添加ISP
        add_multi_isp_save_wxw(browser, name='lzy')

        # 导入IP
        import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='34.1.1.0.txt')

        # 添加路由 单网关
        add_isp_route_lzy(browser, name='lzy', single_gateway='yes', device=interface_name_3, gateway='13.1.1.3',
                          multi_gateway='no', gateway_group='1(GROUP_1)', grp_mem=['主用', '备份1'],
                          enable='yes', disable='no')
        # 84上添加到13.1.1.0网段路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()
        # 81 ping 84
        result1 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3)
        # print(result1)

        # 清除路由
        del_isp_route_byname(browser, name='lzy')

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
					  enable='yes', disable='no')

        # 81 ping 84
        result2 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3)
        # print(result2)

        # 清除路由
        del_isp_route_byname(browser, name='lzy')

        # 添加路由 多网关 通
        add_isp_route_lzy(browser, name='lzy', single_gateway='no', device='', gateway='',
                          multi_gateway='yes', gateway_group='1(GROUP_1)', grp_mem=['备份1', '主用'],
                          enable='yes', disable='no')

        # 81 ping 84
        result3 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3)
        # print(result3)

        # 清除路由
        del_isp_route_byname(browser, name='lzy')

        # 添加路由
        add_isp_route_lzy(browser, name='lzy', single_gateway='yes', device=interface_name_3, gateway='13.1.1.3',
                          multi_gateway='no', gateway_group='1(GROUP_1)', grp_mem=['主用', '备份1'],
                          enable='yes', disable='no')

        # 81 ping 84
        result4 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3)
        # print(result4)


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
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" in result4
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1 and "ms" in result2 and "ms" in result3 and "ms" in result4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev4])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])