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

test_id = "141422"

# 配置nat规则和策略路由，是数据同时匹配策略路由和nat，修改该nat的参数：服务
# 修改立即生效，并且通信正常
# lzy修改，写的什么，看不懂

def test_c141422(browser):

    try:

        login_web(browser, url=dev1)
        # 81 上配SNAT #3
        add_snat(browser, name='lzy', desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.2", srcmask_custom="255.255.255.0",
			 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.3", desmask_custom="255.255.255.0",
			 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
			 other_action_nomap='no',  other_action_maplist='no', save='yes', cancel='no')
        # 修改SNAT
        edit_snat_byname(browser, name="lzy",  server="P:PING")

        # 82上添加到13.1.1.0网段 和34.1.1.0网段的路由
        a82 = Shell_SSH()
        a82.connect(hostip=dev2)
        a82.execute('en')
        a82.execute('con t')
        a82.execute('ip route 13.1.1.0/24 gateway 12.1.1.1')
        a82.execute('ip route 34.1.1.0/24 gateway 12.1.1.1')
        a82.close()
        # 81 上添加策略路由
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_2, gateway='13.1.1.1',
                                    ping_server='13.1.1.1', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='34.1.1.4',
                                    ping_server='34.1.1.4', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加一条多网关策略路由
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='12.1.1.0', src_mask='24',
                                   dst_ip='34.1.1.0', dst_mask='24', service='yes', serv='any',
                                   service_grp='no', serv_grp='H323',
                                   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1"], enable='yes',
                                   disable='no', desc='添加多网关策略路由', save='yes', cancel='no')
        # 82 ping 83
        login_web(browser, url=dev2)
        result1 = diag_ping(browser, ipadd="34.1.1.3", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2)
        # print(result1)

        # 82上删除到13.1.1.0网段 和34.1.1.0网段的路由
        a82 = Shell_SSH()
        a82.connect(hostip=dev2)
        a82.execute('en')
        a82.execute('con t')
        a82.execute('no ip route 13.1.1.0/24 gateway 12.1.1.1')
        a82.execute('no ip route 34.1.1.0/24 gateway 12.1.1.1')
        a82.close()

        # 81 上删除SNAT
        login_web(browser, url=dev1)
        del_snat_byname(browser, name='lzy')
        # 删除策略路由
        del_all_policy_route_lzy(browser)
        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "ms" in result1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])