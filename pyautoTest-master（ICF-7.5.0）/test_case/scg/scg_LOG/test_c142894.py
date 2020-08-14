import pytest
import time
import sys
import math
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from builtins import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142894
# 根据日期时间查询admin日志
# 1.设置为同一天查询日志
# 2.起始日期小于终止日期查询
# 1.可以查询
# 2.可以查询
def test_c142894(browser):
    try:
        # 登录admin
        login_web(browser, url=dev1)
        # 获取系统当前日期
        date1 = get_time_date_lzy(browser)
        print(date1)

        # 设置为同一天查询日志
        query_admin_log_lzy(browser, administrator="", ambiguous_search="", action="", start_date=date1, start_time="",
                            end_date=date1, end_time="")
        # 获取页面信息
        info1 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
        print(info1)

        # 起始时间设置为固定日期
        date2 = '2000-01-01'
        print(date2)

        # 起始日期小于终止日期查询
        query_admin_log_lzy(browser, administrator="", ambiguous_search="", action="", start_date=date2, start_time="",
                            end_date=date1, end_time="")
        # 获取页面信息
        info2 = browser.find_element_by_xpath('//*[@id="timearea0"]').text
        print(info2)

        try:
            assert date1 in info1 and date1 in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert date1 in info1 and date1 in info2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
