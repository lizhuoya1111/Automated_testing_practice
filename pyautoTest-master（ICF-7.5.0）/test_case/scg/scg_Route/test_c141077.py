# //*[@id="table"]/tbody/tr[8]/td[9]/a[1]/img
# //*[@id="table"]/tbody/tr[8]
# //*[@id="table"]/tbody/tr[2]

import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141077"

# 删除物理接口、桥接口、vlan上接口ip
# 可以从路由表里删除，而且无法使用直连路由通信


def test_c141077(browser):

    try:

        login_web(browser, url=dev1)
        # 查看路由表 12.1.1.0网段直连路由存在
        exist1 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist1)

        # 删除81#2接口IP
        delete_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1')

        # 查看路由表 12.1.1.0网段直连路由删除
        exist2 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist2)

        # 添加子接口 添加IP12.1.1.1
        add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="1", work_mode="route")
        add_vlan_inte_add(browser, interface_name=interface_name_2+'.1', ipadd='12.1.1.1', mask='255.255.255.0')

        # 查看路由表 12.1.1.0网段直连路由存在
        exist3 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist3)

        # 删除子接口
        del_vlan_inte_all(browser)

        # 查看路由表 12.1.1.0网段直连路由删除
        exist4 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist4)

        # 新建网桥 将#5添加到网桥
        bridge_add_jyl(browser, bridge_name="br_11")
        bridge_edit_interface_jyl(browser, bridge_interface="br_11", interface=interface_name_5)
        # 给网桥添加IP 12.1.1.1
        bridge_edit_ip_add_jyl(browser, bridge_interface="br_11", address_mode="manual", ip="12.1.1.1",
                               mask="255.255.255.0")

        # 查看路由表 12.1.1.0网段直连路由存在
        exist5 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist5)
        # 删除网桥
        delete_bridge_byname(browser, br_name="br_11")

        # 查看路由表 12.1.1.0网段直连路由删除
        exist6 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist6)

        # 还原#2的IP
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')





        try:
            assert exist1 is True and exist2 is False and exist3 is True and exist4 is False and exist5 is True and exist6 is False
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist1 is True and exist2 is False and exist3 is True and exist4 is False and exist5 is True and exist6 is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])