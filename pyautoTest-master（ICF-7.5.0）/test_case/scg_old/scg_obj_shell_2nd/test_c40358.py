import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_acl import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40358
# 用selected all选中所有obj,一次性删除


def test_add_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        # 删除所有acl组，以防被引用导致的删除失败
        del_all_acl_group_wxw(browser)

        # 先添加再删除
        for n in range(1, 6):
            add_obj_address_wxw(browser, name='obj_add_358_'+str(n), desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')

        del_all_obj_address_wxw(browser)

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "配置地址对象成功，删除内部对象" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "配置地址对象成功，删除内部对象" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40358.py"])