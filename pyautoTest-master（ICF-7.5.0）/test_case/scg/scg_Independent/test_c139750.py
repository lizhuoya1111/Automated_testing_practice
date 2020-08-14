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
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139750"

# 添加1024个zone，检查能否成功;log是否正确、shell下查看是否一致
# 最多可以配置1024个zone；log记录正确，shell和UI的配置一致

def test_c139750(browser):
    try:
        # 添加zone达到1024个（默认有2，再添加1022即可）
        cli_add_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=1023)
        sleep(2)

        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_zone_lzy(browser)
        print(count1)
        # 如果总数小于1024，则继续添加
        n = 1
        m = 1
        while count1 < 1024:
            cli_add_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1023 + n,
                                   num2=1123 + m)
            n = n + 100
            m = m + 100
            count1 = get_count_number_zone_lzy(browser)
            print(count1)

        # 查看翻页等是否正常
        login_web(browser, url=dev1)
        # 获取条目数
        num1 = get_count_number_zone_lzy(browser)
        print(num1)
        # 获取zone列表第一条名称 a1
        info1 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info1)
        # 翻页
        sleep(1)
        click_previous_or_next_page_zone_lzy(browser, pre_page="no", next_page="yes")
        # 获取zone列表第一条名称 a101
        info2 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
        print(info2)
        # 设置每页显示条目数
        sleep(1)
        change_pagesize_zone_lzy(browser, pagesize="20")
        # 获取设置显示页后zone列表最后一条名称 a1013
        info3 = browser.find_element_by_xpath('//*[@id="namearea19"]').text
        print(info3)
        sleep(1)
        change_pagesize_zone_lzy(browser, pagesize="15")
        # 获取设置显示页后zone列表最后一条名称 a1009
        info4 = browser.find_element_by_xpath('//*[@id="namearea14"]').text
        print(info4)
        # 翻页
        click_into_page_zone_lzy(browser, page="2", num="15")
        # 获取翻页后zone列表第一条名称 a1014
        info5 = browser.find_element_by_xpath('//*[@id="namearea0"]').text
        print(info5)


        # 还原
        # 重启设备1
        reload(dev1)
        sleep(1)



        try:
            assert 'a1' in info1 and 'a10' in info2 and 'a10' in info3 and 'a10' in info4 and 'a101' in info5 and num1 >= 1024
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert 'a1' in info1 and 'a10' in info2 and 'a10' in info3 and 'a10' in info4 and 'a101' in info5 and num1 >= 1024

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







