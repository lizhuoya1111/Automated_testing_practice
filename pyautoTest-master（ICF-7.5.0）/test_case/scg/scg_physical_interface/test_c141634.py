import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141634


def test_c141634(browser):

    try:
        login_web(browser, url=dev1)
        switch_physical_interface_snat(browser, interface=interface_name_3, snat="open")
        switch_physical_interface_snat(browser, interface=interface_name_3, snat="close")
        loginfo = get_log_info(browser, 管理日志)

        try:

            assert "snat policy : disable" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "snat policy : disable" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])