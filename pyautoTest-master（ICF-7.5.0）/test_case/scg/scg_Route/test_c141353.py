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

test_id = "141353"
# 修改、删除引用了相同link server的网关组
# 其他引用相同linkserver 的网关组不会受影响
def test_c141353(browser):

    try:
        # 81 上添加3个网关分别属于不同多网关组 引用了相同link server
        login_web(browser, url=dev1)
        for x in range(1, 4):
             add_multi_gateway_group_wxw(browser, name='lzy'+str(x), group=str(x)+"(GROUP_"+str(x)+")", modify='no', alias='',
								device=interface_name_2, gateway='12.1.1.'+str(x+1), ping_server='12.1.1.2', ping='yes', arp='no',
								time_switch='7', ub="100000", db="100000")

        # 删除网关3
        del_multi_gateway_group_byname(browser, name='lzy3')



        # 获取日志
        log1 = get_log(browser, 管理日志)
        print(log1)
        # 获取网关状态
        into_fun(browser, 多网关组)
        state1 = browser.find_element_by_xpath('//*[@id="mouseid_101_status"]').text
        print(state1)
        state2 = browser.find_element_by_xpath('//*[@id="mouseid_201_status"]').text
        print(state2)

        # 删除多网关组
        del_multi_gateway_group_all(browser)



        try:
            assert "删除网关对象成功" in log1 and 'up' in state1 and 'up' in state2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "删除网关对象成功" in log1 and 'up' in state1 and 'up' in state2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])