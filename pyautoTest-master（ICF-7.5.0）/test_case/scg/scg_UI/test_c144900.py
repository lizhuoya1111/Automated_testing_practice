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

test_id = 144900


# 点击主页-系统信息-工控协议-详情，可以正常查看看到支持的工控协议，且显示数量与图片显示的数量一致

def test_c144900(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 获取系统状态中的工控协议显示数目
        num1 = get_ICAgreement_number(browser)
        # 获取工控协议详情里图片数量
        num2 = get_ICAgreement_picnumber(browser)


        try:
            assert num1 == num2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert num1 == num2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
