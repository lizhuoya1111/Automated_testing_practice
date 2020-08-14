
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

test_id = "221866"

# SSLVPN-本地用户
# 新增本地用户，输入非法用户名
# 其余配置均正确
# 点击保存
# 不能成功保存，且有错误提示

def test_c221866(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有本地用户（避免冲突）
        del_all_sslvpn_local_admin_lzy(browser)
        # 增加本地用户
        add_sslvpn_local_admin_lzy(browser, name='$ < > \  | ;  ? & # ￥', password='admin@139', enable='yes', save='yes', cancel='no')

        # 获取告警信息并接受告警
        sleep(1)
        alert1 = browser.switch_to_alert().text
        print(alert1)
        browser.switch_to_alert().accept()
        time.sleep(1)

        # 还原
        # 删除所有本地用户
        del_all_sslvpn_local_admin_lzy(browser)


        try:
            assert '名称输入错误，请重新输入' in alert1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '名称输入错误，请重新输入' in alert1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





