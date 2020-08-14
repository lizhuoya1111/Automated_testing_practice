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

test_id = "139786"

# 1.添加200个zone对象
# 2.以每页显示15个进行查看，点击上一页和下一页按钮查看
# 3.以每页显示20个进行查看，点击上一页和下一页按钮查看
# 4.以每页显示30个进行查看，点击上一页和下一页按钮查询

def test_c139786(browser):
    try:
        # 添加zone200个
        cli_add_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=201)
        sleep(2)

        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_zone_lzy(browser)
        print(count1)
        # 如果总数小于200，则继续添加
        n = 1
        m = 1
        while count1 < 200:
            cli_add_zone_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=201 + n,
                                   num2=211 + m)
            n = n + 10
            m = m + 10
            count1 = get_count_number_zone_lzy(browser)
            print(count1)

        # 查看翻页等是否正常
        login_web(browser, url=dev1)
        # 获取条目数
        num1 = get_count_number_zone_lzy(browser)
        print(num1)
        # 默认状态每页显示15条
        # 获取zone列表第一条名称
        info1 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info1)
        # 翻页下一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
        # 获取zone列表第一条名称
        info2 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info2)
        # 翻页前一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
        # 获取zone列表第一条名称
        info11 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info11)

        # 设置每页显示条目数-20
        sleep(1)
        change_pagesize_zone_lzy(browser, pagesize="20")
        # 获取设置显示页后zone列表第一条名称
        info3 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info3)
        # 翻页下一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
        # 获取zone列表第一条名称
        info4 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info4)
        # 翻页前一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
        # 获取zone列表第一条名称
        info33 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info33)
        sleep(1)

        # 设置每页显示条目数-30
        sleep(1)
        change_pagesize_zone_lzy(browser, pagesize="30")
        # 获取设置显示页后zone列表第一条名称
        info5 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info5)
        # 翻页下一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[2]/a').click()
        # 获取zone列表第一条名称
        info6 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info6)
        # 翻页下一页
        sleep(1)
        browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[1]/a').click()
        # 获取zone列表第一条名称
        info55 = browser.find_element_by_xpath('//*[@id="namearea2"]').text
        print(info55)


        # 还原
        # 重启设备1
        reload(dev1)
        sleep(1)



        try:
            assert info1 == info11 and info3 == info33 and info5 == info55 and info1 == info3 == info5 and info2 != info4 != info6 and num1 >= 200
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert info1 == info11 and info3 == info33 and info5 == info55 and info1 == info3 == info5 and info2 != info4 != info6 and num1 >= 200

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







