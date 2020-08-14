
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

test_id = "132294"
# 1.选择事件信息-安全事件-点击高级搜索
# 2.在安全事件列表中选择一个存在的源IP和一个存在的目的IP，填写在源IP栏和目的IP栏中(支持模糊搜索)，点击搜索，查看下方列表显示的安全事件
# 3.填写不存在的源ip和目的ip，点击搜索，并查看列表
# 2.安全事件列表显示包含所填写的源IP和目的IP的所有安全事件
# 3.安全事件列表中没有安全事件显示 注：IP搜索为模糊搜索，可以是完整的ip，也可以是部分数值
# PS：源IP必须为30.1.1.2  目的IP必须为40.1.1.2
def test_c132294(browser):
    try:
        login_web(browser, url=dev1)
        # 1. 安全事件高级搜索 输入可查询的源IP和目的IP
        securityevents_advanced_search_IP(browser, SourceIP='30.1.1.2', DestinationIP='40.1.1.2')
        # 返回高级搜索后第一条事件源IP和目的IP
        info1 = return_IP_after_search(browser, SourceIP='30.1.1.2', DestinationIP='40.1.1.2')
        print(info1)
        # 2. 安全事件高级搜索 输入不可查询的源IP和目的IP
        securityevents_advanced_search_IP(browser, SourceIP='10.1.1.2', DestinationIP='10.1.1.3')
        # 返回高级搜索后第一条事件源IP和目的IP
        info2 = return_IP_after_search(browser, SourceIP='10.1.1.2', DestinationIP='10.1.1.3')
        print(info2)

        try:
            assert '30.1.1.2', '40.1.1.2' in info1 and '无安全事件' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '30.1.1.2', '40.1.1.2' in info1 and '无安全事件' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





