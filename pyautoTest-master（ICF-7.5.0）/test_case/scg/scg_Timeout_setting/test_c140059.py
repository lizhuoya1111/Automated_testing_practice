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
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_timeout_setting import *
test_id = 140059
# 在admin的timeout中设置的ssh等的timeout大于边界值,或小于边界值
# 不能设置

def test_c140059(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 设置SSH超时时间大于边界值
        info1 = set_ssh_timeout(browser, ssh_timeout="86401")
        # 设置SSH超时时间小于边界值
        info2 = set_ssh_timeout(browser, ssh_timeout="59")

        try:
            assert "范围输入错误，请重新输入" in info1 and "范围输入错误，请重新输入" in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "范围输入错误，请重新输入" in info1 and "范围输入错误，请重新输入" in info2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
