
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

test_id = "132293"
# 2.在安全事件列表中选择一个起止时间段（只包含少量安全事件）填写在起始时间栏和终止时间栏中，点击搜索，查看下方列表显示的安全事件
# 3.填写不存在的时间段，点击搜索，并查看列表
# 2.安全事件列表仅显示时间段内的安全事件
# 3.安全事件列表中没有安全事件显示


def test_c132293(browser):
    try:
        login_web(browser, url=dev1)
        # 1. 安全事件高级搜索 输入可查询的起始时间和截止时间
        securityevents_advanced_search_time(browser, StartDateTime = '2019-06-11 13:45:00', EndDateTime = '2019-06-11 13:51:00')
        # 返回高级搜索后第一条事件时间
        info1 = return_time_after_search(browser, StartDateTime = '2019-06-11 13:45:00', EndDateTime = '2019-06-11 13:51:00')
        # 2. 安全事件高级搜索 输入不可查询的起始时间和截止时间
        securityevents_advanced_search_time(browser, StartDateTime='2019-06-12 13:45:00', EndDateTime='2019-06-12 13:51:00')
        # 返回高级搜索后第一条事件时间
        info2 = return_time_after_search(browser, StartDateTime='2019-06-11 13:45:00', EndDateTime='2019-06-11 13:51:00')
        print(info2)


        try:
            assert '2019-06-11' in info1 and '无安全事件' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '2019-06-11' in info1 and '无安全事件' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





