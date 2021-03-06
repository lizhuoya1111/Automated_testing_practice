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

test_id = "140990"
# 点击向上move、向下move、move to按钮
# 操作成功；shell先显示和UI一致；admin log正常


def test_c140990(browser):

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
        # 移动某条策略路由到第几位
        move_policy_route_by_Index_number_lzy(browser, Index_number='5', to_number='1')
        # 获取日志
        log1 = get_log_info(browser, 管理日志)
        # print(log1)
        # 删除全部策略路由
        del_all_policy_route_lzy(browser)



        try:
            assert "移动策略路由对象成功" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "移动策略路由对象成功" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])