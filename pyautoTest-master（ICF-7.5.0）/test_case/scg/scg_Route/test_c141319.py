import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141319"
# 单、多网关路由描叙里字符串长度超过256（中文字符1个占三个）
# 输入最大长度为256
# 策略路由



def test_c141319(browser):
    try:
        login_web(browser, url=dev1)
        # 添加策略路由单网关  描叙里输入超过256个字符
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='255.255.255.0',
								dst_ip='192.168.5.0', dst_mask='255.255.255.0', service='yes', serv='any',
								service_grp='no', serv_grp='H323',
								out_device=interface_name_1, gateway='192.168.1.2', enable='yes',
								disnable='no', desc='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
                                                    'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
                                                    'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')

        # 获取日志
        log1 = get_log(browser, 管理日志)

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy', group="1(GROUP_1)", modify='no', alias='',
								device=interface_name_1, gateway='192.168.1.2', ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes', arp='no',
								time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_1, gateway='192.168.1.10',
                                    ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes', arp='no',
                                    time_switch='7', ub="100000", db="100000")

        # 添加策略路由 多网关 描叙里输入超过256个字符
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='255.255.255.0',
							   dst_ip='192.168.5.0', dst_mask='255.255.255.0', service='yes', serv='any',
							   service_grp='no', serv_grp='H323',
							   gw_group='1(GROUP_1)',  grp_mem=["主用", "备份1"], enable='yes',
							   disable='no', desc='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                    'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
                                                    'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'
                                                    'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd', save='yes', cancel='no')

        # 获取日志
        log2 = get_log(browser, 管理日志)

        # 删除策略路由多网关
        del_policy_route_singele_wxw(browser, destination='192.168.5.0/255.255.255.0')

        # 删除多网关组
        del_multi_gateway_group_all(browser)

        # 删除单网关
        del_policy_route_singele_wxw(browser, destination='192.168.5.0/255.255.255.0')


        try:
            assert "dddddddddddddd" not in log1 and "dddddddddddddd" not in log2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "dddddddddddddd" not in log1 and "dddddddddddddd" not in log2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])