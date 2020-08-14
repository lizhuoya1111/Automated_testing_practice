import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144279"
# 加入对象名字超过32个字符,16个汉字


def test_c144279(browser):

    try:

        login_web(browser, url=dev1)
        add_obj_address_wxw(browser, name="$ < > \ ' '' | ; , ? & #", desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
        time.sleep(1)
        alert1 = browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]').text
        browser.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
        try:
            assert "请重新输入" in alert1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "请重新输入" in alert1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])