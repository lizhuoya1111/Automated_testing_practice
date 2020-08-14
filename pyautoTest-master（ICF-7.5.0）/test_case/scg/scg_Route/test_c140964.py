import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140964"
# 点击编辑按钮(静态路由)


def test_c140965(browser):

    try:
        login_web(browser, url=dev1)

        add_static_route_single_wxw(browser, ip='24.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
                                    enable='yes')
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 根据目的地址/掩码选择要编辑的路由
        n = 2
        destination = "24.1.1.0/255.255.255.0"
        getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ', '')
        while getdest != destination:
            n = n + 1
            getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[4]').text.replace(' ',
                                                                                                                    '')
        # 点击编辑
        browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[9]/a[1]/img').click()

        # 获取界面信息，判断是否有编辑单路由
        get = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]/ul').text
        # print(get)

        del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

        try:
            assert "编辑单路由" in get
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "编辑单路由" in get

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])