import pytest
import time
import sys
from os.path import dirname, abspath

from scg_def_acl import del_default_acl_group_lzy, del_all_acl_group_lzy

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_firewall import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142882
# 能够删除traffic日志信息 先产生traffic日志
def test_c142882(browser):
    try:
        login_web(browser, url=dev3)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL 全通开log
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
                        source_custom='no', fromip='', fromnetmask='',
                        source_address_object='yes', s_address_object='A:any',
                        mac='', dest_zone_interface='Z:any',
                        dest_custom='no', toip='', tonetmask='',
                        dest_address_object='yes', d_address_object='A:any',
                        service='P:any', schdule='-- 无 --',
                        accept='yes', drop='no',
                        auth='-- 无 --', icf='no', log='yes', save='yes', cancel='no')
        # 添加81到84 与84到81的路由
        shell_81 = Shell_SSH()
        shell_81.connect(hostip=dev1)
        shell_81.execute("en")
        shell_81.execute("conf t")
        shell_81.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
        shell_81.close()

        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()

        # 流量日志过滤级别改为all
        edit_log_filter_lzy(browser, index="4", all='yes', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no")

        # 删除日志
        delete_log(browser, log_type=流量日志)

        # 再用81ping84（过ACL 有日志）
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        sleep(1)
        diag_ping(browser, ipadd="34.1.1.4", interface=interface_name_3)

        # 获取日志总数 不为0
        sign_out_jyl(browser)
        login_web(browser, url=dev3)
        num1 = get_log_counts_lzy(browser, log_type=流量日志)
        print(num1)

        # 刪除日志成功
        delete_log(browser, 流量日志)
        log1 = get_log(browser, 管理日志)
        print(log1)

        # 获取日志总数 为0
        num2 = get_log_counts_lzy(browser, log_type=流量日志)
        print(num2)



        # 还原
        # 删除ACL
        del_all_acl_group_lzy(browser)
        # 还原流量日志过滤级别error critical alert emerg
        edit_log_filter_lzy(browser, index="4", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
                            warning='yes/no', error='yes', critical='yes', emerg='yes', alert="yes")
        # 删81上路由
        shell_81 = Shell_SSH()
        shell_81.connect(hostip=dev1)
        shell_81.execute("en")
        shell_81.execute("conf t")
        shell_81.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
        shell_81.close()
        # 删84上路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("no ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()



        try:
            assert num1 != 0 and num2 == 0 and "刪除日志成功" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert num1 != 0 and num2 == 0  and "刪除日志成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev2)
        rail_fail(test_run_id, test_id)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
