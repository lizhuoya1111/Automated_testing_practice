import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37206
# 对于已导入ip的条目，点击条目后面的add route
# 可以弹出添加网关的界面


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp206', desc='')
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        time.sleep(1)

        # 点击添加isp路由
        browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a').click()
        time.sleep(1)

        # 定位到默认frame
        browser.switch_to.default_content()
        # 定位到内容frame
        browser.switch_to.frame("header")
        gettext = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text
        # print(gettext)
        del_multi_isp_byname(browser, name='isp206')

        try:
            assert "单路由" in gettext
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "单路由" in gettext

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])