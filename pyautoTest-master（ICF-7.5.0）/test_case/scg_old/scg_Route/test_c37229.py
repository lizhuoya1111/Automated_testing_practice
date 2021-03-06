import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37229
# 点击编辑按钮，对除Name里的参数进行修改


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_gateway_group_wxw(browser, name='mgg_229', group="1(GROUP_1)", modify='no', alias='',
                                    device='ge0/3', gateway='24.1.1.7', ping_server='34.1.1.4', ping='yes',
                                    arp='no',
                                    time_switch='7', ub="100000", db="100000")
        edit_multi_gateway_group_wxw(browser, name='mgg_229', group="2(GROUP_2)", modify='no', alias='',
                                     device='ge0/2', gateway='12.1.1.9', ping_server='24.1.1.4', ping='no',
                                     arp='yes',
                                     time_switch='17', ub="500000", db="500000")
        device = get_multi_gateway_group_gateway_wxw(browser, name='mgg_229')
        # print(device)
        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_multi_gateway_group_byname(browser, name='mgg_229')

        try:
            assert "移动网关组网关对象成功" in loginfo
            assert device == "ge0/2"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "移动网关组网关对象成功" in loginfo
            assert device == "ge0/2"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])