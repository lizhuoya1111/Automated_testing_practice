import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg .scg_def_ipv4acl import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141740
# pc1接du的ge0/1，pc2接du的ge0/2,配置一条从接口ge0/1进入，
# ge0/2出去的流量进行允许和拒绝控制的ipv4 acl，
# 检查从对pc1到pc2的数据流是否按照ACL配置进行控制

def test_physical_interface_wxw(browser):
    try:
        login_web(browser, url=dev1)

        del_all_acl_group_noadd_wxw(browser)

        add_acl_group_wxw(browser, name='acl_group933_1')

        add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group933_1', source_zone_interface=interface_name_4,
                                  source_custom='no', fromip='', fromnetmask='',
                                  source_address_object='yes', s_address_object='A:any',
                                  mac='',
                                  dest_custom='no', toip='', tonetmask='',
                                  dest_address_object='yes', d_address_object='A:any',
                                  dest_zone_interface=interface_name_2,
                                  service='P:any', schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 12.1.1.0/24 gw 20.1.1.1')
        result1 = ssh.execute('ping 12.1.1.2 -c 3')
        print(result1)
        ssh.execute('route del -net 12.1.1.0/24 gw 20.1.1.1')
        ssh.close()

        del_all_acl_group_noadd_wxw(browser)

        add_acl_group_wxw(browser, name='acl_group933_2')

        add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group933_2', source_zone_interface=interface_name_4,
                                  source_custom='no', fromip='', fromnetmask='',
                                  source_address_object='yes', s_address_object='A:any',
                                  mac='',
                                  dest_custom='no', toip='', tonetmask='',
                                  dest_address_object='yes', d_address_object='A:any',
                                  dest_zone_interface=interface_name_2,
                                  service='P:any', schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 12.1.1.0/24 gw 20.1.1.1')
        result2 = ssh.execute('ping 12.1.1.2 -c 3')
        print(result2)
        ssh.execute('route del -net 12.1.1.0/24 gw 20.1.1.1')
        ssh.close()

        del_all_acl_group_wxw(browser)

        try:
            assert "100% packet loss" not in result1
            assert "100% packet loss" in result2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "100% packet loss" not in result1
            assert "100% packet loss" in result2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])