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

test_id = 139398

# 1 新建用户密码首字母为$
# 2 使用该用户登陆
# 可以正常登陆
# ps:需修改测试用例为 不能添加且有错误提示 符号$# 为非法

def test_c139398(browser):
    try:
        login_web(browser, url=dev1)
        # 添加新用户 密码为$admin@139
        add_admin(browser, admin_name="lzy", password='$admin@139', confirm_password='$admin@139')
        # 获取告警信息
        alert1 = browser.switch_to_alert().text
        print(alert1)
        # 接受告警
        time.sleep(1)
        browser.switch_to_alert().accept()




        try:
            assert "符号$# 为非法字符" in alert1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "符号$# 为非法字符" in alert1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])