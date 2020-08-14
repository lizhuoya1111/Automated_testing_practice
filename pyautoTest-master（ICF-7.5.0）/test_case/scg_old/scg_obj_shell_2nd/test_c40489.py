import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40489
# 添加每Address对象包含子网20+1个


def test_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.85")

        # 先添加地址对象
        add_obj_address_wxw(browser, name='obj_add_489', desc='zhe是yi个描述1', subnetip='11.11.10.1', subnetmask='32')

        one_obj_add_more_ip_s_wxw(browser, name='obj_add_489', num=9, subnetip='11.11.11.', subnetmask='32')

        one_obj_add_more_ip_s_half_wxw(browser, name='obj_add_489', num=1)

        # 点击增加
        browser.find_element_by_xpath('//*[@id="add_subnet_link"]').click()
        time.sleep(3)

        alert = browser.switch_to_alert()
        # print(alert.text)
        time.sleep(1)

        try:
            assert alert.text == "超出最大限制"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert alert.text == "超出最大限制"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40489.py"])