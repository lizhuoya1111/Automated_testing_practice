import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37171
# 点击policy route里的“Add single Gateway”


def test_route_wxw(browser):

    try:

        login_web(browser, url="10.2.2.82")

        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击路由
        browser.find_element_by_xpath(路由).click()
        # 点击策略路由
        browser.find_element_by_xpath(策略路由).click()

        # 定位到默认frame
        browser.switch_to.default_content()
        # 定位到内容frame
        browser.switch_to.frame("content")

        # 增加单网关路由
        browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()

        time.sleep(1)
        gettext = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul/li').text
        # print(gettext)

        try:
            assert "增加新策略路由" in gettext
            rail_pass(178, test_id)
        except:
            rail_fail(178, test_id)
            assert "增加新策略路由" in gettext

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])