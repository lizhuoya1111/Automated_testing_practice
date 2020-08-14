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

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141071"
# 策略路由在每个页面的第一条路由向上添加；页面最后一条路由向下添加
# 可正常添加


def test_c141071(browser):

    try:
        login_web(browser, url=dev1)
        # 添加5条单网关策略路由
        for x in range(1, 6):
            add_policy_route_single_wxw(browser, in_device='全部', src_ip='30.1.1.0', src_mask='24',
                                        dst_ip='40.1.1.0', dst_mask='24', service='no', serv='any',
                                        service_grp='no', serv_grp='H323',
                                        out_device=interface_name_2, gateway='12.1.1.2', enable='yes', disnable='no',
                                        desc='lzy'+str(x))
        sleep(1)
        # 第一条 点击向上add
        add_policy_route_by_Index_number_upward_or_downward_lzy(browser, Index_number='1', upward='yes',
                                                                addsingle='yes', s_in_device='全部', s_src_ip='50.1.1.0',
                                                                s_src_mask='24',
                                                                s_dst_ip='40.1.1.0', s_dst_mask='24', s_service='yes',
                                                                s_serv='any', s_out_device=interface_name_2, s_gateway='12.1.1.2',
                                                                s_enable='yes/no', s_desc='第一条向上添加')

        # 获取日志
        log1 = get_log_info(browser, 管理日志)
        # print(log1)

        # 最后一条点击向下add
        add_policy_route_by_Index_number_upward_or_downward_lzy(browser, Index_number='6', downward='yes',
                                                                addsingle='yes', s_in_device='全部', s_src_ip='60.1.1.0',
                                                                s_src_mask='24',
                                                                s_dst_ip='40.1.1.0', s_dst_mask='24', s_service='yes',
                                                                s_serv='any', s_out_device=interface_name_2,
                                                                s_gateway='12.1.1.2',
                                                                s_enable='yes/no', s_desc='最后一条向下添加')

        # 获取日志
        log2 = get_log_info(browser, 管理日志)
        # print(log2)

        # 删除全部策略路由
        del_all_policy_route_lzy(browser)



        try:
            assert "添加策略路由对象成功" in log1 and "添加策略路由对象成功" in log2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "添加策略路由对象成功" in log1 and "添加策略路由对象成功" in log2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])