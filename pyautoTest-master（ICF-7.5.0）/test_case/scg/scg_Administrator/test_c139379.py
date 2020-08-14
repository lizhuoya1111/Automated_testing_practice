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

test_id = 139379

# 用超级管理员登录web，查看冻结用户，点击active按钮，对该用户进行解冻
# 可以使用解冻后的用户管理设备
def test_c139379(browser):
    try:
        login_web(browser, url=dev1)
        # 添加管理员lzy
        add_admin(browser, admin_name='lzy', interface="any")
        # 退出admin
        sign_out_jyl(browser)
        # 使用lzy登录 输入错误密码5次
        for x in range(1, 6):
            login_web_when_password_wrong(browser, url=dev1, username="lzy", password="admin"+str(x))
        # 使用admin登录 查看冻结用户 并解冻
        time.sleep(2)
        refresh(browser)
        time.sleep(5)
        login_web(browser, url=dev1, username="admin", password="admin@139")
        unfreeze_admin_user_byname(browser, name='lzy')
        # 退出admin
        sign_out_jyl(browser)
        # 使用lzy登录
        login_web(browser, url=dev1, username='lzy')
        # 日志
        log1 = get_log(browser, 系统日志)
        # 退出lzy 登录admin
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 删除lzy
        delete_all_admin_list_jyl(browser)



        try:
            assert "登录成功" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "登陆成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])