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


test_id = "144047"

# 1.添加一个地址对象a，然后在一个地址组对象b中引用该地址对象
# 2.再添加一个地址组对象c，引用地址组对象b
# 3.在acl rule中引用地址组对象c，匹配规则产生流量---3.可以匹配
# 4.修改地址组对象c，使其不包含地址组对象b，查看流量是否还能匹配规则---4.不能匹配

def test_c144047(browser):
    try:

        login_web(browser, url=dev1)
        # 添加地址对象a
        add_obj_address_wxw(browser, name='a', subnetip='13.1.1.0', subnetmask='24')

        # 添加地址组对象b中引用该地址对象a
        add_obj_group_use_addr_obj_wxw(browser, name='b', addr_obj='A:a')
        # 添加地址组对象c，引用地址组对象b
        add_obj_group_use_addr_obj_wxw(browser, name='c', addr_obj='G:b')

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL 引用地址组对象c
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
                                  source_address_object='yes', s_address_object='G:c',
                                  dest_zone_interface='Z:any')

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
        info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=5)
        print(info1)


        # 修改地址组对象c 删除b
        login_web(browser, url=dev1)
        edit_obj_group_del_obj_lzy(browser, name='c', obj='G:b')

        # 用83ping82
        login_web(browser, url=dev3)
        sleep(1)
        info2 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=10)
        print(info2)


        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_lzy(browser)

        # 删除c 删除b
        del_obj_grp_wxw(browser, name='c')
        del_obj_grp_wxw(browser, name='b')
        # 删除a
        del_obj_address_wxw(browser, name='a')

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
            assert "ms" in info1 and "Unreachable" in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1 and "Unreachable" in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









