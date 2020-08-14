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

test_id = 139386

# 添加一个status为disable的管理员帐号，用该账户登录DUT
# 不能登陆，且有日志
def test_c139386(browser):
    try:
        login_web(browser, url=dev1)
        # 添加admin status为disable
        add_admin(browser, admin_name="lzy", status="disable")
        # 退出当前用户
        sign_out_jyl(browser)
        # 用新用户登录
        login_web_when_password_wrong(browser, url=dev1, username="lzy")
        # 获取用户不能登录的提示信息
        info1 = return_frozon_info_when_login_in(browser, url=dev1, username="lzy")
        print(info1)
        # 还原
        # 用admin登录
        login_web(browser, url=dev1)
        # 删除新用户
        del_admin_byname(browser, name='lzy')




        try:
            assert "此用户不允许登录" in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "此用户不允许登录" in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])