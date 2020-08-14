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

test_id = 139433

# 1.添加admin user
# 2.输入非法ip，例如2.2.2.255/32
# 可以输入，且有提示
def test_c139433(browser):
    try:
        # 登录
        login_web(browser, url=dev1)
        # 添加admin user，输入name含有中文，或者@#￥%这些非法字符
        add_admin(browser, admin_name="lzy", ip1='2.2.2.255/32')
        log1 = get_log(browser, 管理日志)
        # 还原
        delete_all_admin_list_jyl(browser)

        try:
            assert "添加管理员帐户成功" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "添加管理员帐户成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])