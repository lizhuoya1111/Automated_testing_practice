import pytest
import time
import sys
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37325
# 验证list里的enable按钮


def test_route_wxw(browser):

    try:

        login_web(browser, url="10.2.2.83")

        add_policy_route_single_wxw(browser, in_device='ge0/3', src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device='ge0/2', gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')
        # 给81加上去84的路由
        a = Shell_SSH()
        a.connect("10.2.2.81")
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给82加上去84的路由
        a = Shell_SSH()
        a.connect("10.2.2.82")
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 12.1.1.1")
        a.execute("exit")

        # 给84加去82的路由
        a = Shell_SSH()
        a.connect("10.2.2.84")
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 12.1.1.0/24 gateway 34.1.1.3")
        # ping82
        a.execute("exit")
        time.sleep(5)
        a.execute("ping 12.1.1.2")
        result1 = a.output()
        # print(result1)
        a.execute("exit")

        enable_policy_route_single_wxw(browser, destination='12.1.1.0/255.255.255.0', enable='no', disnable='yes')

        a = Shell_SSH()
        a.connect("10.2.2.84")
        a.execute("en")
        a.execute("ping 12.1.1.2")
        time.sleep(5)
        result2 = a.output()
        # print(result2)

        # 删路由
        a.execute("conf t")
        a.execute("no ip route 12.1.1.0/24 gateway 34.1.1.3")
        a.execute("exit")

        # 给81删路由
        a = Shell_SSH()
        a.connect("10.2.2.81")
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给82删路由
        a = Shell_SSH()
        a.connect("10.2.2.82")
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 34.1.1.0/24 gateway 12.1.1.1")
        a.execute("exit")

        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')

        try:
            assert "ms" in result1
            assert "Destination Host Unreachable" in result2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1
            assert "Destination Host Unreachable" in result2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])