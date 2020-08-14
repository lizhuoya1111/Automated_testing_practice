

import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139335"

# 1.添加10个admin profile，保存
# 2.添加10个admin user，分别引用这10个profile，点击保存
# 3.点击reboot重启设备
# 重启后，这些配置仍然存在
def test_c139335(browser):
    try:
        login_web(browser, url=dev1)
        # 添加10个admin profile
        for x in range(1, 11):
            add_admin_profile(browser, profile_name='lzy'+str(x))
            sleep(1)
        # 添加10个admin user
        for y in range(1, 11):
            add_admin(browser, admin_name="lzy"+str(y), temp="lzy"+str(y))
            sleep(1)
        # 保存配置
        save_configer(browser)
        # 获取adminname
        name1 = get_admin_name(browser)
        print(name1)
        # 点击重启
        reload(hostip=dev1, switch="重启")
        login_web(browser, url=dev1)
        # 获取adminname
        name2 = get_admin_name(browser)
        print(name2)
        # 还原
        # 删除admin
        delete_all_admin_list_jyl(browser)
        sleep(1)
        # 删除profile
        delete_all_admin_profile_jyl(browser)
        # 保存配置
        save_configer(browser)
        sleep(2)

        try:
            assert name1 == name2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert name1 == name2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







