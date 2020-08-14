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


test_id = "144107"

# 添加一条acl，源vlan与目的vlan相同，源IP与目的IP相同
# 可以添加

def test_c144107(browser):
    try:

        login_web(browser, url=dev1)

        # 删除默认ACL
        del_default_acl_group_lzy(browser)

        # 添加ACL
        add_acl_group_complete(browser, name='lzy', enable='yes')
        add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_2,
                                  source_custom='yes', fromip='12.1.1.2', fromnetmask='255.255.255.0',
                                  source_address_object='no',
                                  dest_custom='yes', toip='12.1.1.2', tonetmask='255.255.255.0',
                                  dest_address_object='no', dest_zone_interface=interface_name_2)
        sleep(1)
        # 获取操作成功的信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)



        # 还原
        # 删除ACL
        login_web(browser, url=dev1)
        del_all_acl_group_wxw(browser)



        try:
            assert "操作成功" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "操作成功" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









