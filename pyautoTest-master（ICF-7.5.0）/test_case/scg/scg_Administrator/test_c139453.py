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

test_id = 139453

# 1 新建用户aaa，密码为aaa
# 2 成功登陆后，在UI中将密码改为&*
# 用户能使用新密码登陆
def test_c139453(browser):
    try:
        # 登录
        login_web(browser, url=dev1)
        # 添加admin user 用户名为lzy 密码为admin@139.com
        add_admin(browser, admin_name='lzy',  password='admin@138', confirm_password='admin@138')
        # 退出admin 用lzy登录
        sign_out_jyl(browser)
        login_web(browser, url=dev1, username='lzy', password='admin@138')
        # 修改密码
        modify_password_of_new_adminuser(browser, password="&*", confirm_password="&*")
        # 退出lzy 用新密码登录lzy
        sign_out_jyl(browser)
        login_web(browser, url=dev1, username='lzy', password='&*')
        # 获取日志
        log1 = get_log(browser, 系统日志)
        # 退出lzy 登录admin 删除lzy
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        delete_all_admin_list_jyl(browser)

        try:
            assert "管理员登录成功" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "管理员登录成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])