
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

test_id = "132297"
# 状态
def test_c132297(browser):
    try:
        login_web(browser, url=dev1)
        # 1. 安全事件高级搜索 输入事件状态已处理
        securityevents_advanced_search_handleStatus(browser, handleStatus='已处理')
        # 返回高级搜索后第一条事件状态
        info1 = return_handleStatus_after_search(browser, handleStatus='已处理')
        print(info1)
        # 安全事件高级搜索 输入事件状态待处理
        securityevents_advanced_search_handleStatus(browser, handleStatus='待处理')
        info2 = return_handleStatus_after_search(browser, handleStatus='待处理')
        print(info2)

        try:
            assert '已处理' in info1 and '待处理' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '已处理' in info1 and '待处理' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





