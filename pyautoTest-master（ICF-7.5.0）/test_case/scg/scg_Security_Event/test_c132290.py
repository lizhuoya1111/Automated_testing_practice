
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

test_id = "132290"
# 1.选择事件信息-实时安全事件，查看列表显示
# 2.查看事件信息显示顺序
# 1.列表显示：时间，源设备名/目的设备名，源地址/目的地址，协议，事件级别，事件来源，状态，操作，以上信息显示完整.
# 2.列表按时间排序，最新数据在最上方


def test_c132290(browser):
    try:
        login_web(browser, url=dev1)
        # 进入安全事件界面
        get_into_securityevents(browser)
        # 查看列表显示信息显示完整
        info11 = judge_eventslist_complete(browser)
        # 返回列表第一条事件
        info22 = return_eventslist_first(browser)
        # 列表按时间排序，最新数据在最上方
        # 获取第一条事件时间
        time1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[1]').text.replace('', '')
        print(time1)
        time11 = return_time_bigger(browser)

        try:
            assert time1 == time11
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert time1 == time11

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





