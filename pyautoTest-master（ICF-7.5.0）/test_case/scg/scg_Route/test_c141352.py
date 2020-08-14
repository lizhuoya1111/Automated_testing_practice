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

test_id = "141352"
# 网关组探测linkserver 是down掉的，但是单网关路由引用该网关
# 单网关路由不会受影响
def test_c141352(browser):

    try:
        # 81 上添加多网关组
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name='lzy', group="1(GROUP_1)", modify='no', alias='',
								device=interface_name_1, gateway='192.168.1.10', ping_server='192.168.1.11', ping='yes', arp='no',
								time_switch='7', ub="100000", db="100000")

        # 添加单网关路由
        add_static_route_single_wxw(browser, ip='192.168.11.0', mask='24', out_device=interface_name_1, gateway='192.168.1.10',
								enable='yes')

        # 获取日志
        log1 = get_log(browser, 管理日志)
        print(log1)
        # 获取网关状态
        into_fun(browser, 多网关组)
        state1 = browser.find_element_by_xpath('//*[@id="mouseid_101_status"]').text
        print(state1)

        # 删除静态路由
        del_ipv4_static_route_bydestination(browser, destination='192.168.11.0/255.255.255.0')
        # 删除多网关组
        del_multi_gateway_group_all(browser)



        try:
            assert "添加静态路由对象成功" in log1 and 'down' in state1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "添加静态路由对象成功" in log1 and 'down' in state1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])