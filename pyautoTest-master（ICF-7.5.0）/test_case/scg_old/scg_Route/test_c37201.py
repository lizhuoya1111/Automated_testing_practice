import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37201
# 点击“import ip”，导入ip config file，点击cancel


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp201', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp201', save='no', cancel='yes')

        # 定位到默认frame
        browser.switch_to.default_content()
        # 定位到内容frame
        browser.switch_to.frame("header")
        gettext = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text
        # print(gettext)

        ip = get_isp_show_ip_wxw(browser, name='isp201')
        # print(ip)

        del_multi_isp_byname(browser, name='isp201')

        try:
            assert ip == "ip is null"
            assert gettext == "Multi-ISP自选列表"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ip == "ip is null"
            assert gettext == "Multi-ISP自选列表"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])