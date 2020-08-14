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


test_id = "144000"

# 添加一条all to all的acl，服务为all，动作为accept，不开启log，打起流量后，在log record处查看traffic日志
# traffic中没有日志记录
# 此时流量日志总数为0


def test_c144000(browser):
    try:

        login_web(browser, url=dev1)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)
        # 添加ACL 全通开log
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
                                  source_address_object='yes', s_address_object='A:any',
                                  dest_address_object='yes', d_address_object='A:any',
                                  dest_zone_interface='Z:any', log='yes')

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

        # 流量日志过滤级别改为all
        edit_log_filter_lzy(browser, index="4", all='yes', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no")
        # 删除日志
        delete_log(browser, log_type=流量日志)

        # 先用82ping83  使本条流量日志源地址=[12.1.1.2]
        login_web(browser, url=dev2)
        sleep(1)
        info1 = diag_ping(browser, ipadd="13.1.1.3", interface=interface_name_2)
        print(info1)

        # 删除所有ACL
        login_web(browser, url=dev1)
        del_all_acl_group_lzy(browser)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL 全通不开log
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
							  source_address_object='yes', s_address_object='A:any',
							  dest_address_object='yes', d_address_object='A:any',
							  dest_zone_interface='Z:any', log='no')


        # 用83ping82
        login_web(browser, url=dev3)
        sleep(1)
        info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
        print(info1)

        # 获取流量日志
        login_web(browser, url=dev1)
        log1 = get_log(browser, 流量日志)
        print(log1)


        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_lzy(browser)
        # 还原流量日志过滤级别error critical alert emerg
        edit_log_filter_lzy(browser, index="4", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes', critical='yes', emerg='yes', alert="yes")
        # 删除日志
        delete_log(browser, log_type=流量日志)
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
            assert "ms" in info1 and "源地址=[13.1.1.3]" not in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in info1 and "源地址=[13.1.1.3]" not in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









