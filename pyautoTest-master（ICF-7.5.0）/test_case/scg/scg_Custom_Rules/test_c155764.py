import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_sslvpn import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *
from page_obj.scg.scg_def_custom_rules import *


test_id = "155764"

# 1. 协议选择S7，事件处理选择“通过”，其余配置均正确，点击保存。

def test_c155764(browser):
    try:
        login_web(browser, url=dev1)
        # # 清空自定义规则
        # del_all_custom_rules_lzy(browser)

        # 增加自定义规则
        add_custom_rules_complete_lzy(browser, protocol_modubus='no', protocol_s7='yes', protocol='s7',
                                      function='', start_address='',
                                      end_address_or_length='', end_address='',
                                      length='', start_data='', end_data='', action_modbus='',
                                      PduType='Job(1)', FunctionType='OpenS7Communication(240)', action_s7='通过', save='yes', cancel='no')
        sleep(0.5)

        # 获取信息
        sleep(0.5)
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]').text
        print(info1)

        # 还原
        # 删除自定义规则 //*[@id="table"]/tbody/tr[2]/td[7]/a[2]/img
        try_num = 2
        while try_num < 999:
            try:
                browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(try_num+1)+']/td[7]/a[2]/img').click()
                break
            except:
                print('没有多余条目')
                break
        sleep(12)
        delete_sslvpn_safe_site_lzy(browser, number='1')



        try:
            assert '通过' in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '通过' in info1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)

        # 删除自定义规则
        sleep(1)
        login_web(browser, url=dev1)
        delete_sslvpn_safe_site_lzy(browser, number='1')

        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





