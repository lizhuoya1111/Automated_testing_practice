import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140987"
# 点击编辑按钮(策略路由)


def test_c140987(browser):

    try:
        login_web(browser, url=dev3)

        add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')
        # 点击返回
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 根据目的地址/掩码选择要编辑的路由
        n = 2
        destination = "12.1.1.0/255.255.255.0"
        getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ', '')
        # print(getdest)
        while getdest != destination:
            n = n + 1
            getdest = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[6]').text.replace(' ',
                                                                                                                    '')
            # print(getdest)
        # 点击编辑
        browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[15]/a[1]/img').click()

        # 获取界面信息，判断是否有编辑单路由
        time.sleep(1)
        get = browser.find_element_by_xpath('//*[@id="for_config_tb_title"]').text
        # print(get)
        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')

        try:
            assert "编辑策略路由" in get
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "编辑策略路由" in get

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev3)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])