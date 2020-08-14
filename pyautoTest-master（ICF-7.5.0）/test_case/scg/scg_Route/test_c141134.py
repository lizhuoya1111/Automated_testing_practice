import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141134"
# 验证批量删除条目、单条删除(策略)路由


def test_c141134(browser):

    try:
        # 验证删除单条策略路由
        login_web(browser, url=dev3)

        add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')
        # 给81加上去84的路由
        a = Shell_SSH()
        a.connect(dev1)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给82加上去84的路由
        a = Shell_SSH()
        a.connect(dev2)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 12.1.1.1")
        a.execute("exit")

        # 给84加去82的路由
        a = Shell_SSH()
        a.connect(dev4)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 12.1.1.0/24 gateway 34.1.1.3")
        # ping82
        a.execute("exit")
        a.execute("ping 12.1.1.2")
        time.sleep(6)
        result1 = a.output()
        # print(result1)
        a.execute("exit")

        # 删除策略路由
        del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')

        a = Shell_SSH()
        a.connect(dev4)
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
        a.connect(dev1)
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给82删路由
        a = Shell_SSH()
        a.connect(dev2)
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 34.1.1.0/24 gateway 12.1.1.1")
        a.execute("exit")

        # 验证批量删除策略路由
        login_web(browser, url=dev3)

        add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')
        add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
                                    dst_ip='21.1.1.0', dst_mask='24', service='no', serv='any',
                                    service_grp='no', serv_grp='H323',
                                    out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
                                    desc='maioshu')
        # 把81的6口变为路由模式，并加ip
        login_web(browser, url=dev1)

        change_physical_interface_workmode_wxw(browser, interface=interface_name_6,
                                               route="yes", ip='21.1.1.1', mask='24', trans='no')
        # 给pc4配路由
        num = Shell_SSH()
        num.connect('10.1.1.213', 'root', 'root')
        num.execute('route add -net 34.1.1.0/24 gw 21.1.1.1')
        num.execute('exit')

        # 给81加上去84的路由
        a = Shell_SSH()
        a.connect(dev1)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给82加上去84的路由
        a = Shell_SSH()
        a.connect(dev2)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 34.1.1.0/24 gateway 12.1.1.1")
        a.execute("exit")

        # 给84加去82/pc4的路由
        a = Shell_SSH()
        a.connect(dev4)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 12.1.1.0/24 gateway 34.1.1.3")
        a.execute("ip route 21.1.1.0/24 gateway 34.1.1.3")
        # ping82
        a.execute("exit")
        a.execute("ping 12.1.1.2")
        time.sleep(6)
        result3 = a.output()
        # ping pc4
        # print(result3)
        a.execute("ping 21.1.1.3")
        time.sleep(6)
        result4 = a.output()
        # print(result4)
        a.execute("exit")

        # 批量删除两个策略路由
        login_web(browser, url=dev3)
        del_enable_policy_route_single_wxw(browser, destination1='12.1.1.0/255.255.255.0',
                                           destination2='21.1.1.0/255.255.255.0')
        time.sleep(1)
        # 再次登84ping，ping完删除路由
        a = Shell_SSH()
        a.connect(dev4)
        a.execute("en")
        # ping82
        a.execute("ping 12.1.1.2")
        time.sleep(6)
        result5 = a.output()
        # print(result5)
        # ping pc4
        a.execute("ping 21.1.1.3")
        time.sleep(6)
        result6 = a.output()
        # print(result6)
        a.execute("conf t")
        a.execute("no ip route 12.1.1.0/24 gateway 34.1.1.3")
        a.execute("no ip route 21.1.1.0/24 gateway 34.1.1.3")
        a.execute("exit")
        a.execute("exit")

        # 给81删路由
        a = Shell_SSH()
        a.connect(dev1)
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 34.1.1.0/24 gateway 13.1.1.3")
        a.execute("exit")

        # 给pc4删路由
        num = Shell_SSH()
        num.connect('10.1.1.213', 'root', 'root')
        num.execute('route del -net 34.1.1.0/24 gw 21.1.1.1')
        num.execute('exit')

        # 把81的6口变回透明模式
        login_web(browser, url=dev1)

        change_physical_interface_workmode_wxw(browser, interface=interface_name_6,
                                               route="no", ip='21.1.1.1', mask='24', trans='yes')
        time.sleep(2)

        try:
            assert "ms" in result1
            assert "Destination Host Unreachable" in result2
            assert "ms" in result3
            assert "ms" in result4
            assert "Destination Host Unreachable" in result5
            assert "Destination Host Unreachable" in result6
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1
            assert "Destination Host Unreachable" in result2
            assert "ms" in result3
            assert "ms" in result4
            assert "Destination Host Unreachable" in result5
            assert "Destination Host Unreachable" in result6

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev2, dev3, dev4])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])