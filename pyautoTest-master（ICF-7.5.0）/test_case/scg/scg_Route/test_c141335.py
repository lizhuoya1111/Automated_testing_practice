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

test_id = "141335"
# 修改一条静态单网关路由，使它和系统已存在的一条路由相同
# 修改无法生效


def test_c141335(browser):

    try:
        # 81 上添加2条静态路由
        login_web(browser, url=dev1)
        add_static_route_single_wxw(browser, ip='192.168.11.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
								enable='yes')
        add_static_route_single_wxw(browser, ip='192.168.12.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
                                    enable='yes')
        # 修改12网段静态路由为11网段
        edit_static_route_single_wxw(browser, destination='192.168.12.0/255.255.255.0', ip='192.168.11.0', mask='24',
								 out_device=interface_name_2, gateway='12.1.1.2', enable='yes')
        # 获取信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text


        # 删除路由
        del_ipv4_static_route_bydestination(browser, destination='192.168.11.0/255.255.255.0')
        del_ipv4_static_route_bydestination(browser, destination='192.168.12.0/255.255.255.0')

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