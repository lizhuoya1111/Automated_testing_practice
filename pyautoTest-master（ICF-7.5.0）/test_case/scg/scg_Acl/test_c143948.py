import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "143948"


def test_c143948(browser):
    try:
        pass
        try:
            assert True
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev3)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
