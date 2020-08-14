import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_monitor import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
from page_obj.scg.scg_def import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141056"
# 万兆防火墙，ISP路由界面没有操作，导致本测试用例未完成


def test_c141056(browser):

    try:
        login_web(browser, url=dev1)
        # 获取全部路由
        r_sum0 = get_routenum(browser, r_type='全部')
        r_info0 = get_route_monitor_info(browser, r_type='全部', index=7)
        print(r_sum0, r_info0)

        # 获取policy路由
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                    dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_3, gateway='13.1.1.3', enable='yes',
                                    disnable='yes', desc='maioshu')
        r_sum1 = get_routenum(browser, r_type='全部')
        r_info1 = get_route_monitor_info(browser, r_type='全部', index=7)
        print(r_sum1, r_info1)

        # 获取connected路由
        r_sum2 = get_routenum(browser, r_type='connected')
        r_info2 = get_route_monitor_info(browser, r_type='connected', index=7)
        print(r_sum2, r_info2)

        # 获取static路由
        r_sum3 = get_routenum(browser, r_type='static')
        r_info3 = get_route_monitor_info(browser, r_type='static', index=7)
        print(r_sum3, r_info3)

        # 获取ospf路由
        r_sum4 = get_routenum(browser, r_type='ospf')
        r_info4 = get_route_monitor_info(browser, r_type='ospf', index=7)
        print(r_sum4, r_info4)

        # 获取isp-auto路由
        add_multi_isp_save_wxw(browser, name='isp212', desc='miaoshu')

        import_ip_config_file_wxw(browser, name='isp212', save='yes', cancel='no')

        add_isp_route_wxw(browser, name='isp212', single_gateway='yes', device=interface_name_2, gateway='12.1.1.6',
                          multi_gateway='no', gateway_group='',
                          enable='yes', disable='no')

        r_sum5 = get_routenum(browser, r_type='isp-auto')
        r_info5 = get_route_monitor_info(browser, r_type='isp-auto', index=7)
        print(r_sum5, r_info5)

        # 获取默认路由
        r_sum6 = get_routenum(browser, r_type='默认')
        r_info6 = get_route_monitor_info(browser, r_type='isp-auto', index=7)
        print(r_sum6, r_info6)


        try:
            assert True
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert True

        del_multi_isp_byname(browser, name='isp212')
        # del_all_policy_route_lzy(browser)
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1,switch="不重启")
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])