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

test_id = "144191"
# 加入大小写不一样的相同对象名
# 不可以加入


def test_c144191(browser):
    try:
        login_web(browser, url=dev1)
        # 添加address
        add_obj_address_wxw(browser, name='lzy', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
        # 添加大写address
        add_obj_address_wxw(browser, name='LZY', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
        # 获取提示框信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        # 还原 删除地址
        del_obj_address_wxw(browser, name='lzy')

        try:
            assert "已经存在" in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "已经存在" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False

    if __name__ == '__main__':
        pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])