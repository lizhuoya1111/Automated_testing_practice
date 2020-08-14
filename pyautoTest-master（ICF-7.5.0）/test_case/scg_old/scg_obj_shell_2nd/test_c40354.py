import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40354
# 添加一个addr obj,在ACL中引用,验证obj中R是否有显示


def test_add_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        add_obj_address_wxw(browser, name='obj_add_354', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')

        time.sleep(2)

        acl_ref_addr_obj_wxw(browser, gname='aclgroup_354', addr_obj='A:obj_add_354')

        get_addr_obj_ref_wxw(browser, name='obj_add_354')

        # 获取引用
        ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

        try:
            assert ref == "acl-group"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ref == "acl-group"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40354.py"])