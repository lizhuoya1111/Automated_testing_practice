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

test_id = 139370

# 1.添加一个只读用户，设置语言为简体中文
# 2.用该用户登录设备，查看设备UI
# 设备UI为简体中文
# 添加管理员并没有语言设置这一选项  按照默认语言为简体中文来写脚本

def test_c139370(browser):
    try:
        login_web(browser, url=dev1)
        # 添加一个权限lzy
        add_admin_profile(browser, profile_name='lzy', cfg='只读', report='只读')
        # 添加用户lzy 权限lzy
        add_admin(browser, admin_name='lzy', temp='lzy')
        # 退出当前账号
        sign_out_jyl(browser)
        # 用新账号登陆
        login_web(browser, url=dev1, username='lzy')
        # # 获取“系统”
        # browser.switch_to.default_content()
        # browser.switch_to.frame("lefttree")
        # text1 = browser.find_element_by_xpath('//*[@id="menu"]/div[1]/header/a').text
        into_fun(browser, 系统状态)
        text1 = browser.find_element_by_xpath('//*[@id="box_title_sys_info"]/h4').text

        # 退出当前账号 登录admin
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 删除新账号 删除新权限
        del_admin_byname(browser, name='lzy')
        del_admin_profile_byname(browser, name='lzy')


        try:
            assert "系统信息" in text1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "系统信息" in text1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])