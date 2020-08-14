import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40416
# 以host方式添加一条addr obj,查看log


def test_add_obj_wxw(browser):

    try:
        login_web(browser)

        add_obj_address_wxw(browser, name='Big', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')

        add_obj_address_wxw(browser, name='big', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
        time.sleep(2)

        # 定位到默认frame
        browser.switch_to.default_content()
        # 定位到内容frame
        browser.switch_to.frame("content")

        promit = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        # print(promit)

        try:
            assert promit == "big已经存在"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert promit == "big已经存在"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40416.py"])