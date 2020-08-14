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

test_id = 139429

# 1.添加admin profile，输入name超过32个英文字符
# 2.点击save
# 不能输入，且有提示
def test_c139429(browser):
    try:
        # 登录
        login_web(browser, url=dev1)
        # 添加admin profile，输入name超过32个英文字符
        alert1 = return_alert_when_add_wrong_admin_profile(browser, profile_name='aaaaaaaaaabbbbbbbbbbccccccccccddddd')

        try:
            assert "name输入错误" in alert1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "name输入错误" in alert1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])