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

test_id = 139392

# 1 使用admin用户新建用户
# 2 该用户登录墙后修改自己的interface
# 不能修改自己的interface，只能更改密码
def test_c139392(browser):
    try:
        login_web(browser, url=dev1)
        # 添加新用户
        add_admin(browser, admin_name="lzy", temp='max_profile')
        # 退出当前用户 用新用户登录
        sign_out_jyl(browser)
        sleep(3)
        login_web(browser, url=dev1, username='lzy')
        sleep(3)
        # 点击编辑修改新用户
        click_modify_of_new_adminuser(browser)
        sleep(5)
        # 获取管理员设置信息
        info1 = browser.find_element_by_class_name('css_config').text
        print(info1)
        # 退出新用户 登录admin用户
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 删除新用户
        del_admin_byname(browser, name='lzy')

        try:
            assert "密码" in info1 and '接口' not in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "密码" in info1 and '接口' not in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])