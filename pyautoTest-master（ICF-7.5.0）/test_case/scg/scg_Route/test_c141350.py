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
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141350"
# 多条路由选择同一个网关组，修改一个路由的网关组的opnion，验证其他路由的多网关情况是否被修改
# 其他路由的网关组不会被修改
def test_c141350(browser):

    try:
        # 81 上添加多网关组
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        # 添加两条路由选择同一网关组
        add_static_route_multi_gateway_wxw(browser, ip='192.168.11.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
                                           grp_mem=['主用', '备份1'], enable="yes",
                                           save='yes', cancel='no')
        add_static_route_multi_gateway_wxw(browser, ip='192.168.12.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
                                           grp_mem=['主用', '备份1'], enable="yes",
                                           save='yes', cancel='no')

        # 修改12网段网关组option
        edit_static_route_multi_gateway_wxw(browser, destination='192.168.12.0/255.255.255.0', ip='192.168.12.0', mask='24',
                                            gateway_grp='1(GROUP_1)', num=2, grp_mem=['备份1', '主用'], enable="yes",
									        save='yes', cancel='no')

        # 获取日志
        log1 = get_log(browser, 管理日志)
        print(log1)

        # 查看11网段网关信息
        gateway1 = return_static_route_gateway_by_destination(browser, destination='192.168.11.0/255.255.255.0')

        # 删除静态路由
        del_ipv4_static_route_bydestination(browser, destination='192.168.11.0/255.255.255.0')
        del_ipv4_static_route_bydestination(browser, destination='192.168.12.0/255.255.255.0')
        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "修改静态路由对象成功" in log1 and '13.1.1.3:alive:active' in gateway1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "修改静态路由对象成功" in log1 and '13.1.1.3:alive:active' in gateway1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])