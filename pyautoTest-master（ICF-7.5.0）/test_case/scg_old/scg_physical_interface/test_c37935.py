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

test_id = 37935
# 配置一条all to all drop的acl规则，检查能否从管理口进入DUT进行管理


def test_physical_interface_wxw(browser):

    login_web(browser, url="10.2.2.81")

    del_all_acl_group_noadd_wxw(browser)

    add_acl_group_wxw(browser, name='acl_group935')

    add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group935', source_zone_interface='Z:any',
                              source_custom='no', fromip='', fromnetmask='',
                              source_address_object='yes', s_address_object='A:any',
                              mac='',
                              dest_custom='no', toip='', tonetmask='',
                              dest_address_object='yes', d_address_object='A:any',
                              dest_zone_interface='Z:any',
                              service='P:any', schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')

    login_web(browser, url="10.2.2.81")

    # 定位到默认frame
    browser.switch_to.default_content()
    # 定位到内容frame
    browser.switch_to.frame("content")

    # 获取web界面的元素
    hostname = browser.find_element_by_xpath('//*[@id="home_sysinfo_hostname"]').text
    time.sleep(5)
    print(hostname)

    del_all_acl_group_wxw(browser)


    try:
        assert hostname == "BSAFE"
        rail_pass(206, test_id)
    except:
        rail_fail(206, test_id)
        assert hostname == "BSAFE"


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c37935.py"])