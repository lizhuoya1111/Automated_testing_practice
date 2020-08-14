
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
from page_obj.scg.scg_def_security_event import *

test_id = "132300"

# 1.查看下方翻页栏，总页数是否正确
# 2.依次点击，尾页，首页，下一页，上一页
# 1.总页数正确
# 2.页面跳转正确

def test_c132300(browser):
    try:
        login_web(browser, url=dev1)
        # 进入安全事件界面
        get_into_securityevents(browser)
        # 获取本页最新一条安全事件时间
        time1 = get_time_of_Latest_Events_in_Current_page(browser)
        print(time1)
        # 点击下一页 跳转到第2页
        click_nextpage_after_getinto_securityevents(browser)
        # 获取本页最新一条安全事件时间
        time2 = get_time_of_Latest_Events_in_Current_page(browser)
        print(time2)
        # 点击上一页 跳转到第1页
        click_previouspage_after_getinto_securityevents(browser)
        # 获取本页最新一条安全事件时间
        time3 = get_time_of_Latest_Events_in_Current_page(browser)
        print(time3)


        try:
            assert time1 > time2 and time1 <= time3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert time1 > time2 and time1 <= time3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





