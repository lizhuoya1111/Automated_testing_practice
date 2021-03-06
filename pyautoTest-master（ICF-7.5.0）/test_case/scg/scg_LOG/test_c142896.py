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
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142896
# 根据功能模块查询admin日志
def test_c142896(browser):
    try:
        # 登录admin
        login_web(browser, url=dev1)
        # 清除流量日志以产生admin日志
        delete_log(browser, 流量日志)
        # 根据功能模块查询日志--log
        advanced_query_admin_log_lzy(browser, advanced="yes", administrator="", ambiguous_search="",
								 action="", start_date="", start_time="", end_date="", end_time=""
								 , level="unchange", select_all="yes/no", emerg="yes/no", alert="yes/no",
								 critical="yes/no",error="yes/no", warning="yes/no", notice="yes/no", info="yes/no",
								 debug="yes/no", module="change", modul_name="log")

        # 获取页面信息
        info1 = browser.find_element_by_xpath('//*[@id="modulesarea0"]').text
        print(info1)


        try:
            assert 'log' in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert 'log' in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
