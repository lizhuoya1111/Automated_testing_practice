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

test_id = 139353

# 1.使用超级管理员帐号登录，添加一个只读用户
# 2.用该只读用户登录设备，修改自己的口令

def test_c139353(browser):
    try:
        login_web(browser, url=dev1)
        # 添加一个只读权限
        add_admin_profile(browser, profile_name='lzy', cfg='只读', report='只读')
        # 添加用户 权限只读
        add_admin(browser, admin_name='lzy', temp='lzy')
        # 退出当前账号
        sign_out_jyl(browser)
        # 用新账号登陆
        login_web(browser, url=dev1, username='lzy')
        # 添加子接口  显示无权限
        add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id='1', work_mode="route")
        info1 = browser.find_element_by_xpath('//*[@id="text_warning"]').text
        browser.find_element_by_xpath('//*[@id="box"]/div[4]/div/input').click()
        # 修改密码  操作成功
        modify_password_of_new_adminuser(browser, password='A123456@789', confirm_password='A123456@789')
        info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()
        # 退出当前账号 登录admin
        sign_out_jyl(browser)
        login_web(browser, url=dev1)
        # 删除新账号 删除新权限
        del_admin_byname(browser, name='lzy')
        del_admin_profile_byname(browser, name='lzy')


        try:
            assert "没有权限" in info1 and '操作成功' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "没有权限" in info1 and '操作成功' in info2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])