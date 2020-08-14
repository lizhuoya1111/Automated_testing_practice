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


test_id = "144040"

# 1.添加多条acl
# 2.产生流量匹配其中的几条acl
# 3.反复上下移动acl，验证流量，检查是否立即生效---.匹配acl的流量正常
# 4.修改其中某个不影响流量的acl rule，检查是否会影响到正常通包的流量---不会影响

def test_c144040(browser):
    try:

        login_web(browser, url=dev1)

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3,
                                  dest_zone_interface='Z:any')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_4,
                                  dest_zone_interface='Z:any')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_5,
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

        # 用83ping82 匹配源接口为interface_name_3的ACL
        login_web(browser, url=dev3)
        sleep(1)
        info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        print(info1)

        # 向下移动源接口为interface_name_3的ACL
        login_web(browser, url=dev1)
        move_ipc4_acl_click(browser, group_name='lzy', acl_id='1', move="down")

        # 向下移动源接口为interface_name_3的ACL
        move_ipc4_acl_click(browser, group_name='lzy', acl_id='2', move="down")

        # 向上移动源接口为interface_name_3的ACL
        move_ipc4_acl_click(browser, group_name='lzy', acl_id='3', move="up")

        # 修改此时的第一条ACL规则（不影响源接口为interface_name_3的ACL）
        edit_acl_rule_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_5,
                          dest_zone_interface='Z:any')

        # 用83ping82
        login_web(browser, url=dev3)
        sleep(1)
        info2 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        print(info2)



        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_wxw(browser)

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
            assert "ms" in info1 and "ms" in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1 and "ms" in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









