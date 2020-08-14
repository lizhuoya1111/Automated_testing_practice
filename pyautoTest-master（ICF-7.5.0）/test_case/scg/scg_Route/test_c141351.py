import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141351"
# 配置网关组是不输入参数
# 无法配置成功，系统报错
def test_c141351(browser):

    try:
        # 81 上添加多网关组
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name=' ', group="1(GROUP_1)", modify='no', alias='',
								device=interface_name_2, gateway='', ping_server='', ping='yes', arp='no',
								time_switch='7', ub="100000", db="100000")

        # 获取告警信息
        alert1 = browser.switch_to_alert().text
        browser.switch_to_alert().accept()


        try:
            assert "名称输入错误，请重新输入" in alert1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "名称输入错误，请重新输入" in alert1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])