import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144161"
# 添加一个serv obj grp,在ACL中引用,验证serv obj grp中R是否有显示


def test_c144161(browser):

    try:
        login_web(browser, url=dev1)

        add_obj_serv_grp_wxw(browser, name='serv_grp_386', desc='zhe是ge描shu', serv_obj='P:any')

        add_acl_group_wxw(browser, name='acl_group_386')

        add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_386', source_zone_interface=interface_name_4,
                                  source_custom='no', fromip='', fromnetmask='',
                                  source_address_object='yes', s_address_object='A:any',
                                  mac='',
                                  dest_custom='no', toip='', tonetmask='',
                                  dest_address_object='yes', d_address_object='A:any',
                                  dest_zone_interface=interface_name_2,
                                  service='G:serv_grp_386', schdule='-- 无 --',
                                  accept='yes', drop='no',
                                  auth='-- 无 --', icf='no', log='no')

        get_serv_grp_obj_ref_wxw(browser, name='serv_grp_386')
        time.sleep(1)
        # 获取引用
        ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

        del_acl_group_wxw(browser, name='acl_group_386')

        del_obj_serv_grp_wxw(browser, name='serv_grp_386')

        try:
            assert ref == "acl"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ref == "acl"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])