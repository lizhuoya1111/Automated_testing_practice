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

test_id = 144906


# 反复刷新主页20次
# 不够准确  应获取动态信息看是否正常加载

def test_c144906(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 刷新页面20次
        for x in range(1, 21):
            refresh(browser)
            sleep(1)
            info1 = get_text_systemstate(browser)
            print(x, info1)

        try:
            assert '系统信息' in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert '系统信息' in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
