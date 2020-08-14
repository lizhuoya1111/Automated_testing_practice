import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139815"
# 添加abc后再添加Abc，检查能否成功
# 无法成功配置，系统报错


def test_c139815(browser):
    try:
        login_web(browser, url=dev1)
        # 添加zone name为abc
        add_obj_zone(browser, "abc", "abc", [interface_name_5, interface_name_6])
        sleep(1)
        # 添加zone name为ABC
        add_obj_zone(browser, "ABC", "abc", [interface_name_5, interface_name_6])
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        # 还原
        del_obj_zone_byname(browser, name='abc')


        try:
            assert '已经存在' in info1
            rail_pass(test_run_id, test_id)
        except Exception as err1:
            print(err1)
            rail_fail(test_run_id, test_id)
            assert '已经存在' in info1
    except Exception as err:
        # 如果上面的步骤有报错，重启设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])