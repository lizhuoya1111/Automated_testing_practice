import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.common.ssh import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_bridge import *


test_id = "144054"

# 1.ge0/2和ge0/3纯为透明模式，配在一个桥下br_1
# 2.pca接在ge0/2后，pcb接在ge0/3后面，pca和pcb的ip是同一网段的
# 3.添加一条acl，源接口为br_1,目的接口也是br_1,从pca ping pcb---可以ping通

def test_c144054(browser):
    try:

        login_web(browser, url=dev1)
        # 81 #2#3改为透明模式 （先清除接口IP）
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
        physics_interface_change_transparent_interface(browser, interface2=interface_name_2, interface3=interface_name_3)

        # 俩透明模式接口加入同一网桥
        bridge_add_jyl(browser, bridge_name="br_1")
        bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)
        bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3)

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='br_1',
                                  dest_zone_interface='br_1')

        # 改83#2的IP 使之与82#2的IP 在相同网段
        login_web(browser, url=dev3)
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="13.1.1.3")
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.3', mask='255.255.255.0')

        # 83ping82 并获取ping信息
        sleep(1)
        info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        print(info1)

        # 还原--删除ACL（添加默认ACL）
        login_web(browser, url=dev1)
        del_all_acl_group_wxw(browser)

        # 删除网桥
        delete_bridge_byname(browser, br_name="br_1")
        # 还原81 #2#3为路由模式并还原IP
        transparent_interface_change_physics_interface_lzy(browser, interface2=interface_name_2, interface3=interface_name_3)
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')
        add_physical_interface_ip_wxw(browser, interface=interface_name_3, ip='13.1.1.1', mask='255.255.255.0')

        # 还原83#2的IP
        login_web(browser, url=dev3)
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.3")
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='13.1.1.3', mask='255.255.255.0')



        try:
            assert "ms" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









