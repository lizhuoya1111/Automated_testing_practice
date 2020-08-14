import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37211
# 对于已导入ip、添加路由的条目，点击edit
# 已导入ip的条目，不能编辑


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp211', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp211', save='yes', cancel='no')

        add_isp_route_wxw(browser, name='isp211', single_gateway='yes', device='ge0/2', gateway='12.1.1.6',
                          multi_gateway='no', gateway_group='',
                          enable='yes', disable='no')
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        # 获取编辑的title
        title = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[13]/a[1]/img').get_attribute("title")
        # print(title)

        del_multi_isp_byname(browser, name='isp211')

        try:
            assert title != "编辑"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert title != "编辑"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])