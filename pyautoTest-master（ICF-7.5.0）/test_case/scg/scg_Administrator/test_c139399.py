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

test_id = 139399

# 1 新建用户密码长度为8~64
# 2 使用该用户登陆
# 可以正常登陆

def test_c139399(browser):
    try:
        login_web(browser, url=dev1)
        # 添加新用户 密码为admin@139
        add_admin(browser, admin_name="lzy", temp='max_profile', password='admin@139', confirm_password='admin@139')
        # 退出当前用户 用新用户登录
        sign_out_jyl(browser)
        login_web(browser, url=dev1, username='lzy', password='admin@139')
        # 获取“系统”
        browser.switch_to.default_content()
        browser.switch_to.frame("lefttree")
        text1 = browser.find_element_by_xpath('//*[@id="menu"]/div[1]/header/a').text
        # 退出新用户 登录admin
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 删除新用户
        del_admin_byname(browser, name='lzy')




        try:
            assert "系统" in text1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "系统" in text1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])