import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141292"
# 输入字符串长度超过 32（中文字符一个占三个字符位）
# 多网关组名称

def test_c141292(browser):
    try:
        login_web(browser, url=dev3)
        alert1 = return_alert_when_add_multi_gateway_group(browser, name='李李李李李李李李李李卓卓卓卓卓卓卓卓卓卓亚亚亚亚亚亚亚亚亚亚', group="1(GROUP_1)", modify='yes/no', alias='',
                                          device=interface_name_1, gateway='192.168.1.2', ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes', arp='no',
                                          time_switch='7', ub="100000", db="100000")
        try:
            assert "名称输入错误" in alert1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "名称输入错误" in alert1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev3)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])