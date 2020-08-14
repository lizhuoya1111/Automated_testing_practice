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

test_id = "141413"

# snat和静态路由的联合使用：snat配置的出口地址和静态路由指定网关一致，发送数据匹配静态路由
# 对端设备不需要配置回执路由，即可正常通信
#
# snat配置的出口地址和静态路由指定网关一致--这个怎么实现啊
# 本用例按照不一致写  20190919


def test_c141413(browser):

    try:

        login_web(browser, url=dev1)
        # 81 上配SNAT #2
        add_snat(browser, name='lzy', desc="", src_inter_zone="Z:any", des_inter_zone="Z:any", other_match_switch="yes",
			 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="13.1.1.3", srcmask_custom="255.255.255.0",
			 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="12.1.1.2", desmask_custom="255.255.255.0",
			 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
			 other_action_nomap='no',  other_action_maplist='no', save='yes', cancel='no')

        # 83上添加到12网段的路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('ip route 12.1.1.0/24 gateway 13.1.1.1')
        a83.close()
        # 83 ping 82
        login_web(browser, url=dev3)
        result1 = diag_ping(browser, ipadd="12.1.1.2", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_2, timesleep=3)
        # print(result1)


        # 删除83上路由
        a83 = Shell_SSH()
        a83.connect(hostip=dev3)
        a83.execute('en')
        a83.execute('con t')
        a83.execute('no ip route 12.1.1.0/24 gateway 13.1.1.1')
        a83.close()

        # 81 上删除SNAT
        login_web(browser, url=dev1)
        del_snat_byname(browser, name='lzy')


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
        reload(hostip=[dev1, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])