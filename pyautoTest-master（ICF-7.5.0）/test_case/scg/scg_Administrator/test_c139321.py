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

test_id = 139321

# 2.添加一个admin profile，name为英文字符，description含有中英文字符，config system为write-read，report system为write-read
# 4.点击编辑按钮，修改该profile的config system为read-only

def test_c139321(browser):
    try:
        login_web(browser, url=dev1)
        # 添加admin profile
        add_admin_profile(browser, profile_name='lzy', desc='lizhuoya李卓亚')
        # 修改admin profile
        add_admin_profile(browser, profile_name='lzy', desc='lizhuoya李卓亚', cfg='只读')
        # 查看日志
        log1 = get_log(browser, 管理日志)
        # 还原
        delete_all_admin_profile_jyl(browser)
        try:
            assert "修改管理员视图成功" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "修改管理员视图成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)

        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])