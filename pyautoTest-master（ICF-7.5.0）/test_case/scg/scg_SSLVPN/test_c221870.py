
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

test_id = "221870"

# SSLVPN-本地用户
# 新增本地用户
# 其余配置均正确
# 1. 点击保存
# 2. 点击取消

def test_c221870(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有本地用户（避免冲突）
        del_all_sslvpn_local_admin_lzy(browser)
        # 增加本地用户
        add_sslvpn_local_admin_complete_lzy(browser, name='localadmin1', password='admin@139', enable='yes', save='yes', cancel='no')
        sleep(0.5)

        # 获取页面本地用户个数
        info1 = get_count_sslvpn_local_admin_lzy(browser)
        print(info1)

        sleep(0.5)

        # 增加本地用户
        add_sslvpn_local_admin_complete_lzy(browser, name='localadmin2', password='admin@139', enable='no', save='no',
                                            cancel='yes')
        sleep(0.5)

        # 获取页面本地用户个数
        info2 = get_count_sslvpn_local_admin_lzy(browser)
        print(info2)

        # 还原
        # 删除所有本地用户
        del_all_sslvpn_local_admin_lzy(browser)


        try:
            assert info1 == 1 and info2 == 1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert info1 == 1 and info2 == 1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





