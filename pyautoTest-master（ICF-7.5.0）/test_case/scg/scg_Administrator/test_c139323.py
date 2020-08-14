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

test_id = 139323

# 1.添加10个admin profile
# 2.选择其中的一条，点击delete

def test_c139323(browser):
    try:
        login_web(browser, url=dev1)
        # 添加10个admin profile
        for x in range(1, 11):
            add_admin_profile(browser, profile_name='lzy'+str(x))
        # 选择其中一条删除 根据名字删除
        del_admin_profile_byname(browser, name='lzy2')
        # 查看日志
        log1 = get_log(browser, 管理日志)
        # 还原
        delete_all_admin_profile_jyl(browser)
        try:
            assert "删除" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "删除" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])