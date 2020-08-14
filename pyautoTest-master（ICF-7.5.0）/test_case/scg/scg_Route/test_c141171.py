
import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141171"

# ISP list列表里的enable disable功能
# 添加网关后list里添加网关按钮变成enable按钮
# 应该是变成不可点击的吧吧吧


def test_c141171(browser):

    try:

        login_web(browser, url=dev1)
        # 添加ISP
        add_multi_isp_save_wxw(browser, name='lzy')

        # 导入IP
        import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='34.1.1.0.txt')

        # 获取页面信息
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]/a').text.strip()
        # print(info1)


        # 添加路由 单网关
        add_isp_route_lzy(browser, name='lzy', single_gateway='yes', device=interface_name_3, gateway='13.1.1.3',
                          multi_gateway='no', gateway_group='1(GROUP_1)', grp_mem=['主用', '备份1'],
                          enable='yes', disable='no')

        # 获取页面信息
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[11]').text.strip()
        # print(info2)


        # 删除ISP
        del_multi_isp_wxw(browser, name='lzy')




        try:
            assert info1 == info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert info1 == info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])