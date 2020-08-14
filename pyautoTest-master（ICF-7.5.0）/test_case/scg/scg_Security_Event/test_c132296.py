
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

test_id = "132296"
# 事件来源
def test_c132296(browser):
    try:
        login_web(browser, url=dev1)
        # 1. 安全事件高级搜索 输入事件来源机器学习
        securityevents_advanced_search_EventSource(browser, EventSource='机器学习')
        # 返回高级搜索后第一条事件来源
        info1 = return_EventSource_after_search(browser, EventSource='机器学习')
        print(info1)
        # 安全事件高级搜索 输入其事件来源默认漏洞规则
        securityevents_advanced_search_EventSource(browser, EventSource='默认漏洞规则')
        info2 = return_EventSource_after_search(browser, EventSource='默认漏洞规则')
        print(info2)
        # 安全事件高级搜索 输入其事件来源设备地址绑定
        securityevents_advanced_search_EventSource(browser, EventSource='设备地址绑定')
        info3 = return_EventSource_after_search(browser, EventSource='设备地址绑定')
        print(info3)
        # 安全事件高级搜索 输入其事件来源流量告警
        securityevents_advanced_search_EventSource(browser, EventSource='流量告警')
        info4 = return_EventSource_after_search(browser, EventSource='流量告警')
        print(info4)


        try:
            assert '机器学习' in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '机器学习' in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





