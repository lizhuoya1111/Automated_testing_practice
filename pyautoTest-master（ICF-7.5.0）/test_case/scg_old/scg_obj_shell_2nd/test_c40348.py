import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40348
# 在一条addr obj中添加多个host,查看log


def test_add_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        add_obj_address_wxw(browser, name='obj_add_348', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')

        one_obj_add_more_ip_h_wxw(browser, name='obj_add_348', num=3, subnetip='11.11.', subnetmask='24')

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "配置地址对象成功，修改内部对象 [obj_add_348]" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "配置地址对象成功，修改内部对象 [obj_add_348]" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40348.py"])