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
from page_obj.scg.scg_def_policy_route import *


test_id = "144062"

# 添加策略路由，添加ACL匹配策略路由的方向
# 可以匹配
# 策略路由这儿还是不会

def test_c144062(browser):
    try:
        # 81上添加策略路由
        login_web(browser, url=dev1)
        add_policy_route_single_wxw(browser, in_device=interface_name_2, src_ip='12.1.1.0', src_mask='255.255.255.0',
                                    dst_ip='34.1.1.0', dst_mask='255.255.255.0', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='no', desc='maioshu')

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_2,
                                  dest_zone_interface=interface_name_3)
        sleep(5)

        # 添加82到83 和34.1.1.0网段    与83到82的路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.execute("ip route 34.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()

        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()

        # 82ping83#3  IP34.1.1.3 并获取ping信息
        login_web(browser, url=dev2)
        sleep(1)
        info1 = diag_ping(browser, ipadd="34.1.1.3", interface=interface_name_2)
        print(info1)

        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_lzy(browser)

        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='34.1.1.0/255.255.255.0')
        # 删82上路由
        shell_82 = Shell_SSH()
        shell_82.connect(hostip=dev2)
        shell_82.execute("en")
        shell_82.execute("conf t")
        shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
        shell_82.execute("no ip route 34.1.1.0/24 gateway 12.1.1.1")
        shell_82.close()
        # 删83上路由
        shell_83 = Shell_SSH()
        shell_83.connect(hostip=dev3)
        shell_83.execute("en")
        shell_83.execute("conf t")
        shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
        shell_83.close()

        try:
            assert "ms" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









