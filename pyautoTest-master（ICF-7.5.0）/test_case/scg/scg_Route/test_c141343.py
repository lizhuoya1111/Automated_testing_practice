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
from page_obj.scg.scg_def_static_route import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141343"
# 先后配置两条相同的静态多网关路由，第一条disable，再添加第二条。然后enbale第一条
# 路由disable也无法添加相同的静态路由


def test_c141343(browser):

    try:
        # 81 上添加2条相同静态路由 第一条不启用
        login_web(browser, url=dev1)
        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_static_route_multi_gateway_wxw(browser, ip='192.168.11.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
                                           grp_mem=['主用', '备份1'], enable="no",
                                           save='yes', cancel='no')
        add_static_route_multi_gateway_wxw(browser, ip='192.168.11.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
                                           grp_mem=['主用', '备份1'], enable="yes",
                                           save='yes', cancel='no')
        # 获取信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text

        # 删除路由
        del_ipv4_static_route_bydestination(browser, destination='192.168.11.0/255.255.255.0')
        # 删除多网关组
        del_multi_gateway_group_all(browser)

        try:
            assert "静态路由已存在" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "静态路由已存在" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])