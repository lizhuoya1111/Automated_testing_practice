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

test_id = 37934
# pc1接du的ge0/1，pc2接du的ge0/2,配置一条从接口ge0/2，
# ge0/1出去的流量进行允许和拒绝控制的ipv4 acl，
# 检查从对pc2到pc1的数据流是否按照ACL配置进行控制


def test_physical_interface_wxw(browser):

    login_web(browser, url="10.2.2.81")

    del_all_acl_group_noadd_wxw(browser)

    add_acl_group_wxw(browser, name='acl_group934_1')

    add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group934_1', source_zone_interface='ge0/2',
                     source_custom='no', fromip='', fromnetmask='',
                     source_address_object='yes', s_address_object='A:any',
                     mac='',
                     dest_custom='no', toip='', tonetmask='',
                     dest_address_object='yes', d_address_object='A:any',
                     dest_zone_interface='ge0/4',
                     service='P:any', schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')
    # 给pc加路由
    ssh = SSH("10.1.1.202", 'root', 'root', 22)
    ssh.connect()
    ssh.execute('route add -net 12.1.1.0/24 gw 20.1.1.1')
    ssh.close()

    # 用设备ping pc
    a = Shell_SSH()
    a.connect("10.2.2.82")
    a.execute("en")
    a.execute("ping 20.1.1.2")
    result1 = a.output()

    del_all_acl_group_noadd_wxw(browser)

    add_acl_group_wxw(browser, name='acl_group934_2')

    add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group934_2', source_zone_interface='ge0/2',
                     source_custom='no', fromip='', fromnetmask='',
                     source_address_object='yes', s_address_object='A:any',
                     mac='',
                     dest_custom='no', toip='', tonetmask='',
                     dest_address_object='yes', d_address_object='A:any',
                     dest_zone_interface='ge0/4',
                     service='P:any', schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')

    # 用设备ping pc
    a = Shell_SSH()
    a.connect("10.2.2.82")
    a.execute("en")
    a.execute("ping 20.1.1.2")
    result2 = a.output()

    del_all_acl_group_wxw(browser)

    # 删除pc上的路由
    ssh = SSH("10.1.1.202", 'root', 'root', 22)
    ssh.connect()
    ssh.execute('route del -net 12.1.1.0/24 gw 20.1.1.1')
    ssh.close()



    try:
        assert "Destination Host Unreachable" not in result1
        assert "Destination Host Unreachable" in result2
        rail_pass(206, test_id)
    except:
        rail_fail(206, test_id)
        assert "Destination Host Unreachable"not in result1
        assert "Destination Host Unreachable" in result2

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c37934.py"])