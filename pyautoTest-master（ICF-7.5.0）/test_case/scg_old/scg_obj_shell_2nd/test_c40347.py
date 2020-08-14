import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40347
# 删除以range方式添加的一条addr obj,查看log


def test_add_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        # 先添加再删除
        add_obj_address_range_wxw(browser, name='obj_add_range_347', desc='zhe是yi个描述1',
                                  fromip='12.12.12.1', toip='12.12.12.250')

        del_obj_range_wxw(browser, name='obj_add_range_347')

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()
        get_log(browser, 管理日志)
        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")
        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "配置地址范围对象成功，删除内部对象 [obj_add_range_347]" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "配置地址对象范围成功，删除内部对象 [obj_add_range_347]" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40347.py"])