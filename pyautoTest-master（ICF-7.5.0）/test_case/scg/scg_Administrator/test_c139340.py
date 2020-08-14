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

test_id = 139340

# 设置ssh timeout为600，port22
# 设置https timeout为600，port443
# 设置telnet timeout为600，port23
# 设置console timeout600

def test_c139340(browser):
    try:
        login_web(browser, url=dev1)
        # 设置
        sys_set_lzy(browser, ssh_port="22", ssh_timeout="600", https_port="443", https_timeout="600", telent_port="23",
                    telent_timeout="600", console_timeout="600")
        # 设置完成等待5m 刷新重新登陆
        sleep(2)
        refresh(browser)
        sleep(2)
        login_web(browser, url=dev1)
        # 查看日志
        log1 = get_log(browser, 管理日志)

        try:
            assert "成功" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "成功" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])