import pytest
import time
import sys
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_interface import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141090"
# static route list功能 1
# 验证批量删除条目、单条删除路由


def test_c141090(browser):

    try:

        # 验证批量删除路由
        login_web(browser, url=dev3)

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='13.1.1.1',
                                    enable='yes')
        add_static_route_single_wxw(browser, ip='21.1.1.0', mask='24', out_device=interface_name_2, gateway='13.1.1.1',
                                    enable='yes')

        login_web(browser, url=dev1)
        change_physical_interface_workmode_wxw(browser, interface=interface_name_5,
                                               route="yes", ip='21.1.1.1', mask='24',
                                               trans='no')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
        result1 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result1)
        ssh.close()

        ssh = SSH("10.1.1.212", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 13.1.1.0/24 gw 21.1.1.1')
        result2 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result2)
        ssh.close()

        login_web(browser, url=dev3)

        # 删除两段路由
        del_static_route_single_wxw(browser, destination1='20.1.1.0/255.255.255.0',
                                    destination2='21.1.1.0/255.255.255.0')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        result1_1 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result1_1)
        ssh.close()

        ssh = SSH("10.1.1.212", 'root', 'root', 22)
        ssh.connect()
        result2_1 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result2_1)
        ssh.execute('route del -net 13.1.1.0/24 gw 21.1.1.1')
        ssh.close()

        # 验证单条删除路由
        login_web(browser, url=dev3)

        add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='13.1.1.1',
                                    enable='yes')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
        result3 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result3)
        ssh.close()

        del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
        result3_1 = ssh.execute('ping 13.1.1.3 -c 3')
        # print(result3_1)
        ssh.execute('route del -net 13.1.1.0/24 gw 21.1.1.1')
        ssh.close()

        login_web(browser, url="10.2.2.81")
        change_physical_interface_workmode_wxw(browser, interface=interface_name_5,
                                               route="no", ip='21.1.1.1', mask='24',
                                               trans='yes')

        try:
            assert "ttl" in result1
            assert "ttl" in result2
            assert "100% packet loss" in result1_1
            assert "100% packet loss" in result2_1
            assert "ttl"in result3
            assert "100% packet loss" in result3_1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ttl" in result1
            assert "ttl" in result2
            assert "100% packet loss" in result1_1
            assert "100% packet loss" in result2_1
            assert "ttl" in result3
            assert "100% packet loss" in result3_1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        # rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev3])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])