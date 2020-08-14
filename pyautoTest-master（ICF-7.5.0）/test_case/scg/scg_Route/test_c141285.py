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

test_id = "141285"
# 网关group里有多网关，只有一个选backup（backup1，backup2)，其余都选unselect
# 无法配置成功，系统报错


def test_c141285(browser):

    try:
        # 81 上添加策略路由
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.3',
                                    ping_server='13.1.1.3', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2',
                                    ping_server='12.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy3', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_4, gateway='20.1.1.2',
                                    ping_server='20.1.1.2', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加一条多网关策略路由
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["备份1", "不选择", "不选择"], enable='yes',
                                   disable='no', desc='添加多网关策略路由', save='yes', cancel='no')

        # 获取信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)

        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "多网关路由只有一个网关" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "多网关路由只有一个网关" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])