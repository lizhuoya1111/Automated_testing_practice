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

test_id = "141354"
# 修改UI上的网关组参数，验证网关探测参数是否被修改为默认
# 不应该被修改
def test_c141354(browser):

    try:
        # 81 上添加多网关
        login_web(browser, url=dev1)
        add_multi_gateway_group_wxw(browser, name='lzy', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='12.1.1.2', ping_server='12.1.1.2',
                                    ping='yes', arp='no',
                                    time_switch='8', ub="100000", db="100000")

        # 进入修改界面 获取网关探测参数
        into_fun(browser, 多网关组)
        # 点击修改（第一条）
        browser.find_element_by_xpath('//*[@id="route_maintenance_multigw_table"]/tbody/tr[3]/td[9]/a[1]/img').click()
        sleep(5)
        # 获取切换时间信息
        info1 = browser.find_element_by_xpath('//*[@id="switchtime"]').get_attribute('value')
        print(info1)


        # 删除多网关组
        del_multi_gateway_group_all(browser)



        try:
            assert "8" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "8" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])