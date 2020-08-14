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
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139725"

# 添加静态ARP表达到4000，验证系统运行状况

def test_c139725(browser):
    try:
        # 添加静态ARP表达到4000
        cli_add_static_arp_lzy(devname=dev3, username="admin", password="admin@139", port=22, num1=1, num11=21, num2=1, num22=201)
        sleep(2)

        login_web(browser, url=dev3)
        # 获取条目数
        count1 = get_count_number_static_arp_lzy(browser)
        print(count1)
        # 如果总数小于4000，则继续添加
        n = 1
        m = 1
        while count1 < 4000:
            cli_add_static_arp_lzy(devname=dev3, username="admin", password="admin@139", port=22, num1=20+n, num11=23+m, num2=1, num22=201)
            n = n + 3
            m = m + 3
            count1 = get_count_number_static_arp_lzy(browser)
            print(count1)

        # 获取静态ARP列表第一条ip地址 30.1.1.1
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        print(info1)
        # 翻页
        sleep(1)
        click_previous_or_next_page_static_arp_lzy(browser, pre_page="no", next_page="yes")
        # 获取翻页后静态ARP列表第一条ip地址 30.1.1.16
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        print(info2)
        # 设置每页显示条目数
        sleep(1)
        change_pagesize_static_arp_lzy(browser, pagesize="20")
        # 获取设置显示页后静态ARP列表首页最后一条ip地址 30.1.1.20
        info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[21]/td[3]').text
        print(info3)
        sleep(1)
        change_pagesize_static_arp_lzy(browser, pagesize="15")
        # 获取设置显示页后静态ARP列表首页最后一条ip地址 30.1.1.15
        info4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[16]/td[3]').text
        print(info4)
        # 翻页
        click_into_page_static_arp_lzy(browser, page="2", num="15")
        # 获取翻页后静态ARP列表首页第一条ip地址 30.1.1.16
        info5 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        print(info5)


        # 还原
        # 删除admin
        # cli_delete_static_arp_lzy(devname=dev3, username="admin", password="admin@139", port=22, num1='3', num2='5')
        # 重启
        reload(dev3)
        sleep(1)



        try:
            assert '30.1.1.1' in info1 and '30.1.1.16' in info2 and '30.1.1.20' in info3 and '30.1.1.15' in info4 and '30.1.1.16' in info5 and count1 >= 4000
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '30.1.1.1' in info1 and '30.1.1.16' in info2 and '30.1.1.20' in info3 and '30.1.1.15' in info4 and '30.1.1.16' in info5 and count1 >= 4000

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev3)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







