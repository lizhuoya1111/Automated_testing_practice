import pytest
import time
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_ui import *

test_id = 144907


# 日志-日志记录-系统日志-清除；
# 查看主页告警统计
# 告警统计也被清除

def test_c144907(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 清除系统日志
        delete_log(browser, 系统日志)
        # 获取主页告警统计数值
        num1 = get_alert_number(browser)


        try:
            assert '0' in num1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert '0' in num1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
