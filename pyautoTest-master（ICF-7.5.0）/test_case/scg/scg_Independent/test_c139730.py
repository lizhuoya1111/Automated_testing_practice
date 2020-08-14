import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139730"

# 添加IP-MAC Binding的条目4000，验证系统运行状况
# MAC条目可以生效，系统运行正常

def test_c139730(browser):
    try:
        # 添加ip-mac-binding表达到4000条
        cli_add_ip_mac_binding_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1,
                                            num11=21, num2=1, num22=201, interface=interface_name_2,
                                            mac='aa:aa:aa:aa:aa:aa')
        sleep(2)

        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_ipmac_binding_lzy(browser)
        print(count1)
        # 如果总数小于4000，则继续添加
        n = 1
        m = 1
        while count1 < 4000:
            cli_add_ip_mac_binding_complete_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=20 + n,
                                   num11=23 + m, num2=1, num22=201, interface=interface_name_2,
                                            mac='aa:aa:aa:aa:aa:aa')
            n = n + 3
            m = m + 3
            count1 = get_count_number_ipmac_binding_lzy(browser)
            print(count1)

        # 查看翻页等是否正常
        login_web(browser, url=dev1)
        # 获取条目数
        num1 = get_count_number_ipmac_binding_lzy(browser)
        print(num1)
        # 获取ipmacbinding列表第一条ip地址 30.1.1.1
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text
        print(info1)
        # 翻页
        sleep(1)
        click_previous_or_next_page_ipmac_binding_lzy(browser, pre_page="no", next_page="yes")
        # 获取翻页后ipmacbinding列表第一条ip地址 30.1.1.16
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text
        print(info2)
        # 设置每页显示条目数
        sleep(1)
        change_pagesize_ipmac_table_lzy(browser, pagesize="20")
        # 获取设置显示页后ipmacbinding列表首页最后一条ip地址 30.1.1.20
        info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[21]/td[2]').text
        print(info3)
        sleep(1)
        change_pagesize_ipmac_table_lzy(browser, pagesize="15")
        # 获取设置显示页后ipmacbinding列表首页最后一条ip地址 30.1.1.15
        info4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[16]/td[2]').text
        print(info4)
        # 翻页
        click_into_page_ipmac_binding_lzy(browser, page="2", num="15")
        # 获取翻页后ipmacbinding列表首页第一条ip地址 30.1.1.16
        info5 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text
        print(info5)

        # 验证MAC条目是否生效
        # #2接口添加IP 30.1.1.1/24
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='30.1.1.1', mask='255.255.255.0')
        # 开启#2接口的IP—MAC设置，未定义主机策略选择阻止
        edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_2, source_mac_binding="enable",
                                     policy_for_undefined_host="block")
        # 退出设备1 登录设备2 将#2接口添加IP30.1.1.2/24 （Mac不为aa:aa:aa:aa:aa:aa）
        sign_out_jyl(browser)
        login_web(browser, url=dev2)
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='30.1.1.2', mask='255.255.255.0')

        # 用设备2的#2去ping设备1的#2（30.1.1.1）
        sleep(1)
        info10 = diag_ping(browser, ipadd="30.1.1.1", interface=interface_name_2, timesleep=10)
        print(info10)

        # 退出设备2 登录设备1
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 获取安全日志信息 droped在信息中
        log1 = get_log(browser, 安全日志)
        print(log1)


        # 还原
        # 清除安全日志
        delete_log(browser, 安全日志)
        # 重启设备1
        reload(dev1)
        sleep(1)
        # 设备2的#2接口删除ip30.1.1.2
        login_web(browser, url=dev2)
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="30.1.1.2")


        try:
            assert '30.1.1.1' in info1 and '30.1.1.16' in info2 and '30.1.1.20' in info3 and '30.1.1.15' in info4 and '30.1.1.16' in info5 and num1 >= 4000 and 'droped' in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '30.1.1.1' in info1 and '30.1.1.16' in info2 and '30.1.1.20' in info3 and '30.1.1.15' in info4 and '30.1.1.16' in info5 and num1 >= 4000 and 'droped' in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







