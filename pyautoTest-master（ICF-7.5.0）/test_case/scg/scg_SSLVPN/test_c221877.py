
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

test_id = "221877"

# SSLVPN-本地用户
# 1. 点击某条后面的启用
# 2. 取消启用

def test_c221877(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有本地用户（避免冲突）
        del_all_sslvpn_local_admin_lzy(browser)
        # 增加本地用户2个
        for x in range(1, 3):
            add_sslvpn_local_admin_complete_lzy(browser, name='localadmin'+str(x), password='admin@139', enable='yes',
                                                save='yes', cancel='no')
            sleep(0.5)
        add_sslvpn_local_admin_complete_lzy(browser, name='localadmin3', password='admin@139', enable='no',
                                            save='yes', cancel='no')
        # 获取本地用户个数
        info1 = get_count_sslvpn_local_admin_lzy(browser)
        print(info1)

        # 判断本地用户是否启用 12启用 3不启用
        num1 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='1')
        num2 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='2')
        num3 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='3')
        # 更改本地用户启用状态 12改为不启用 3改为启用
        enable_or_unable_sslvpn_local_admin_lzy(browser, number='1', enable='no')
        enable_or_unable_sslvpn_local_admin_lzy(browser, number='2', enable='no')
        enable_or_unable_sslvpn_local_admin_lzy(browser, number='3', enable='yes')
        # 判断本地用户是否启用 12不启用 3启用
        num11 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='1')
        num22 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='2')
        num33 = judge_enable_or_unable_sslvpn_local_admin_lzy(browser, number='3')
        # 还原
        # 删除所有本地用户
        del_all_sslvpn_local_admin_lzy(browser)


        try:
            assert num1 == num2 ==num33 == True and num3 == num11 == num22 ==False
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert num1 == num2 ==num33 == True and num3 == num11 == num22 ==False



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





