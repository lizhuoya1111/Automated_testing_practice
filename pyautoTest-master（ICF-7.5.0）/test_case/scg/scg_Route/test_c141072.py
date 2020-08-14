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
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141072"
# 在物理接口、vlan子接口配置ip地址
# 静态路由表和route monitor里会出现直连路由


def test_c141072(browser):

    try:
        login_web(browser, url=dev1)
        # 给81#5 改为路由模式 并添加IP
        transparent_interface_change_physics_interface_lzy(browser, interface5=interface_name_5)
        add_physical_interface_ip_wxw(browser, interface=interface_name_5, ip='192.168.11.1', mask='24')

        # 判断直连路由是否存在（静态路由中判断）
        exist1 = is_static_route_exist_wxw(browser, destination='192.168.11.0/255.255.255.0')
        # print(exist1)
        # 判断直连路由是否存在（路由监控中判断）
        exist2 = is_static_route_exist_wxw(browser, destination='192.168.11.0/255.255.255.0')
        # print(exist2)

        # 删除该物理接口IP
        delete_physical_interface_ip_jyl(browser, interface=interface_name_5, ip="192.168.11.1")

        # 给接口添加子接口
        add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="1", work_mode="route")
        # 给子接口添加IP
        add_vlan_inte_add(browser, interface_name=interface_name_5 + '.1', ipadd='192.168.12.1', mask='24')

        # 判断直连路由是否存在（静态路由中判断）
        exist3 = is_static_route_exist_wxw(browser, destination='192.168.12.0/255.255.255.0')
        # print(exist3)
        # 判断直连路由是否存在（路由监控中判断）
        exist4 = is_static_route_exist_wxw(browser, destination='192.168.12.0/255.255.255.0')
        # print(exist4)

        # 删除子接口
        del_vlan_inte_all(browser)

        # 将物理接口改回透明模式
        physics_interface_change_transparent_interface(browser, interface5=interface_name_5)







        try:
            assert exist1 is True and exist2 is True and exist3 is True and exist4 is True
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist1 is True and exist2 is True and exist3 is True and exist4 is True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])