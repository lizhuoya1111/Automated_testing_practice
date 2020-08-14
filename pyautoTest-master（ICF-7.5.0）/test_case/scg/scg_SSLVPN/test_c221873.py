
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_sslvpn import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "221873"

# SSLVPN-本地用户
# 点击修改本地用户
# 做出修改
# 1. 点击保存
# 2. 点击取消

def test_c221873(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有本地用户（避免冲突）
        del_all_sslvpn_local_admin_lzy(browser)
        # 增加本地用户
        add_sslvpn_local_admin_complete_lzy(browser, name='localadmin1', password='admin@139', enable='yes', save='yes', cancel='no')
        sleep(0.5)

        # 获取页面信息
        info1 = get_list_info_sslvpn_local_admin_lzy(browser)
        print(info1)

        # 编辑--做修改保存
        edit_sslvpn_local_admin_lzy(browser, number='1', password='admin@138', enable='yes', save='yes', cancel='no')

        # 获取页面信息
        info2 = get_list_info_sslvpn_local_admin_lzy(browser)
        print(info2)

        # 编辑--做修改取消
        edit_sslvpn_local_admin_lzy(browser, number='1', password='admin@138', enable='yes',
                                    save='no', cancel='yes')

        # 获取页面信息
        info3 = get_list_info_sslvpn_local_admin_lzy(browser)
        print(info3)

        # 还原
        # 删除所有本地用户

        del_all_sslvpn_local_admin_lzy(browser)


        try:
            assert 'admin@139' in info1 and 'admin@138' in info2 and 'admin@138' in info3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert 'admin@139' in info1 and 'admin@138' in info2 and 'admin@138' in info3



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





