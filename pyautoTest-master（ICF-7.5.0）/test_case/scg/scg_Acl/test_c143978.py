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


test_id = "143978"

# 1.设置一个zone1，该zone内包含ge0/2.1，ge0/1.2，ge0/3.3
# 2.添加一条acl，源接口为zone1，源地址是any，目的也是zone1，目的地址是all，服务是all
# 3.验证接在ge0/2.1，ge0/1.2，ge0/3.3后面pc之间的通信情况，在他们之间进行互ping
# 这几台pc可以互相ping通


def test_c143978(browser):
    try:
        # 81的234接口添加子接口
        login_web(browser, url=dev1)
        delete_physical_interface_ip_wxw(browser, interface_name_2, "12.1.1.1")
        delete_physical_interface_ip_wxw(browser, interface_name_3, "13.1.1.1")
        delete_physical_interface_ip_wxw(browser, interface_name_4, "20.1.1.1")
        add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="1", work_mode="route")
        add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="1", work_mode="route")
        add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="1", work_mode="route")
        sleep(5)
        add_vlan_inte_add(browser, interface_name_2+'.1', "12.1.1.1", '255.255.255.0')
        add_vlan_inte_add(browser, interface_name_3+'.1', "13.1.1.1", '255.255.255.0')
        add_vlan_inte_add(browser, interface_name_4+'.1', "20.1.1.1", '255.255.255.0')
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
        a.execute("exit")
        a.execute("interface gigabitethernet " + interface_name_4)
        a.execute("switchmode access")
        a.execute("exit")

        # 添加zone1  包括三个子接口
        add_obj_zone(browser, "zone1", "lzy", [interface_name_2+".1", interface_name_3+".1", interface_name_4+".1"])
        # 删除默认ACL
        del_default_acl_group_lzy(browser)
        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:zone1',
                                  dest_zone_interface='Z:zone1')
        # 添加路由 82到83 82到10.1.1.202 经过81
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.execute("ip route 20.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()
        # 添加路由 83到82 83到10.1.1.202 经过81
        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.execute("ip route 20.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()
        # 添加路由 10.1.1.202到82和83 经过81
        ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
        ssh2.connect()
        ssh2.execute('route add -net 12.1.1.0/24 gw 20.1.1.1')
        ssh2.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
        ssh2.execute('ifconfig ' + server_pc_2_eth1 + ' 20.1.1.2 netmask 255.255.255.0')
        ssh2.close()

        # 用82ping83和10.1.1.202（地址应该填20.1.1.2）
        login_web(browser, url=dev2)
        sleep(1)
        info1 = diag_ping(browser, ipadd="13.1.1.3", interface=interface_name_2)
        # print("info1", info1)
        sleep(2)
        info2 = diag_ping(browser, ipadd="20.1.1.2", interface=interface_name_2)
        # print("info2", info2)

        # 用83ping82和10.1.1.202（地址应该填20.1.1.2）
        login_web(browser, url=dev3)
        sleep(1)
        info3 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        # print("info3", info3)
        sleep(2)
        info4 = diag_ping(browser, ipadd="20.1.1.2", interface=interface_name_2)
        # print("info4", info4)

        # 用10.1.1.202ping82和83
        ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
        ssh2.connect()
        info5 = ssh2.execute('ping 12.1.1.2 -c 5 -i 0.5')
        # print(info5)
        info6 = ssh2.execute('ping 13.1.1.3 -c 5 -i 0.5')
        # print(info6)
        ssh2.close()

        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_wxw(browser)
        # 删除zone1
        del_obj_zone_byname(browser, 'zone1')

        # 删除子接口
        del_vlan_inte_all(browser)
        # 还原物理接口IP
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')
        add_physical_interface_ip_wxw(browser, interface=interface_name_3, ip='13.1.1.1', mask='255.255.255.0')
        add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='255.255.255.0')

        # 删除路由#
        # 删82上路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.execute("no ip route 20.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()
        # 删83上路由
        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.execute("no ip route 20.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()
        # 删除10.1.1.202上路由
        ssh2 = SSH('10.1.1.202', 'root', 'root', 22)
        ssh2.connect()
        ssh2.execute('route del -net 13.1.1.0/24 gw 20.1.1.1')
        ssh2.execute('route del -net 12.1.1.0/24 gw 20.1.1.1')
        ssh2.close()

        try:
            assert "ms" in info1 and "ms" in info2 and "ms" in info3 and "ms" in info4 and "ms" in info5 and "ms" in info6
            # assert "ms" in info1
            # assert "ms" in info2
            # assert "ms" in info3
            # assert "ms" in info4
            # assert "ms" in info5
            # assert "ms" in info6
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1 and "ms" in info2 and "ms" in info3 and "ms" in info4 and "ms" in info5 and "ms" in info6
            # assert "ms" in info1
            # assert "ms" in info2
            # assert "ms" in info3
            # assert "ms" in info4
            # assert "ms" in info5
            # assert "ms" in info6
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









