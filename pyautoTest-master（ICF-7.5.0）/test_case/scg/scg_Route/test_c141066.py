# 修改断言内容

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

test_id = "141066"

# 添加成功或者配置失败时候的提示正确
# 显示正确


def test_c141066(browser):

    try:
        login_web(browser, url=dev1)

        # 添加策略路由（配置失败时）
        info1 = return_alert_when_add_policy_route_single_(browser, in_device='全部', src_ip='', src_mask='',
                                                   dst_ip='40.1.1.0', dst_mask='255.0.0.0', service='yes', serv='any',
                                                   service_grp='no', serv_grp='H323',
                                                   out_device=interface_name_2, gateway='12.1.1.2', enable='yes',
                                                   desc='maioshu')
        # print(info1)
        # 添加策略路由（成功时）
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='30.1.1.0', src_mask='24',
                                    dst_ip='40.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_2, gateway='12.1.1.2', enable='yes',
                                    disnable='no', desc='maioshu')
        info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        # print(info2)

        # 删除策略路由
        del_all_policy_route_lzy(browser)




        try:
            assert "IP格式输入错误" in info1 and '操作成功' in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "IP格式输入错误" in info1 and '操作成功' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])