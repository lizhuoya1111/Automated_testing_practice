
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

test_id = "132295"
# 2.填写存在的协议名称，点击搜索，查看下方安全事件列表
# 3.填写不存在的协议名称，点击搜索，并查看列表
# 2.安全事件列表显示包含该协议的所有安全事件
# 3.安全事件列表中没有安全事件显示 注：协议搜索为模糊搜索，可以是完整的协议名称，也可以是部分
def test_c132295(browser):
    try:
        login_web(browser, url=dev1)
        # 1. 安全事件高级搜索 输入可查询的协议
        securityevents_advanced_search_Protocol(browser, Protocol='FTP')
        # 返回高级搜索后第一条事件协议
        info1 = return_Protocol_after_search(browser, Protocol='FTP')
        print(info1)
        # 2. 安全事件高级搜索 输入不可查询的协议
        securityevents_advanced_search_Protocol(browser, Protocol='S7')
        # 返回高级搜索后第一条事件协议
        info2 = return_Protocol_after_search(browser, Protocol='S7')
        print(info2)

        try:
            assert 'FTP' in info1 and '无安全事件' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert 'FTP' in info1 and '无安全事件' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





