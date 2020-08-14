import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
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


test_id = "143980"

# 1.在子接口中添加ge0/2，vlan id为2，再添加一个子接口，加入接口ge0/3，vlan id为3
# 2.添加一个address对象，名称为address1（包含pca的地址）
# 2.在acl中设置源接口ge0/3.3，source address为any，目的接口为ge0/2.2，源address引用address1，目的address为any，service为any，其他为默认配置
# 4.pca接在ge0/3.3后，pcb接在ge0/2.2后面，从pca ping pcb
# 5.修改acl rule的源address为192.168.7.22(pca的地址)，掩码255.255.255.255，其他不变，从pca ping pcb


def test_c143980(browser):
    try:
        # 81的23接口添加子接口
        login_web(browser, url=dev1)
        delete_physical_interface_ip_wxw(browser, interface_name_2, "12.1.1.1")
        delete_physical_interface_ip_wxw(browser, interface_name_3, "13.1.1.1")
        add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="1", work_mode="route")
        add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="1", work_mode="route")
        sleep(2)
        add_vlan_inte_add(browser, interface_name_2+'.1', "12.1.1.1", '255.255.255.0')
        add_vlan_inte_add(browser, interface_name_3+'.1', "13.1.1.1", '255.255.255.0')
        # 子接口转换模式
        a = Shell_SSH()
        a.connect(dev1)
        a.execute("en")
        a.execute("conf t")
        a.execute("interface gigabitethernet "+interface_name_2)
        a.execute("switchmode access")
        a.execute("exit")
        a.execute("interface gigabitethernet " + interface_name_3)
        a.execute("switchmode access")
        a.close()

        # 添加一个address对象
        add_obj_address_wxw(browser, name='address1', subnetip='13.1.1.0', subnetmask='24')

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3+".1",
                                  source_address_object='yes', s_address_object='A:address1',
                                  dest_zone_interface=interface_name_2+".1")

        # 添加82到83 与83到82的路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()

        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()

        # 用83ping82
        login_web(browser, url=dev3)
        sleep(1)
        info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        # print(info1)

        # 修改ACL
        login_web(browser, url=dev1)
        edit_acl_rule_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3+".1",
                                  source_custom='yes', fromip='13.1.1.2', fromnetmask='255.255.255.255',
                                  dest_zone_interface=interface_name_2+".1")

        # 用83ping82
        login_web(browser, url=dev3)
        sleep(1)
        info2 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        # print(info2)

        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_wxw(browser)

        # 删除address1
        del_obj_address_wxw(browser, name='address1')

        # 删除子接口
        del_vlan_inte_all(browser)
        # 还原物理接口IP
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')
        add_physical_interface_ip_wxw(browser, interface=interface_name_3, ip='13.1.1.1', mask='255.255.255.0')

        # 删82上路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()
        # 删83上路由
        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()

        try:
            # assert "ms" in info1 and "ms" in info2
            assert "ms" in info1
            assert "ms" in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            # assert "ms" in info1 and "ms" in info2
            assert "ms" in info1
            assert "ms" in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









