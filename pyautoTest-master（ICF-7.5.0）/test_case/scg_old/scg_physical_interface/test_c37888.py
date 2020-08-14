import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg .scg_def_ipv4acl import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37888
# 每一个接口都配置为路由模式并配置ip，开启Allow Ping：
# 1.PC1与ge0/1相连，PC2分别与其他所有接口相连，检查PC1与PC2是否相通，例如ping或者ftp；
# 2..PC1与ge0/1相连，PC2和PC3分别与其他不同的两个接口相连，检查PC1、PC2与PC3三者间能否相互通信，变化三个PC所连接的接口，检查是否能相互通信相通


def test_physical_interface_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        change_physical_interface_workmode_wxw(browser, interface='ge0/6',
                                               route="yes", ip='21.1.1.1', mask='24',
                                               trans='no')

        open_physical_interface_allowping_wxw(browser, interface='ge0/2', allow_ping="open")
        open_physical_interface_allowping_wxw(browser, interface='ge0/4', allow_ping="open")
        open_physical_interface_allowping_wxw(browser, interface='ge0/6', allow_ping="open")

        # 给82加路由
        a = Shell_SSH()
        a.connect("10.2.2.82")
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 20.1.1.0/24 gateway 12.1.1.1")
        a.execute("ip route 21.1.1.0/24 gateway 12.1.1.1")

        # 给213加路由
        ssh = SSH("10.1.1.213", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')
        ssh.execute('route add -net 12.1.1.0/24 gw 21.1.1.1')
        ssh.close()

        # 给202加路由,ping213和82
        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
        ssh.execute('route add -net 12.1.1.0/24 gw 20.1.1.1')
        result1 = ssh.execute('ping 12.1.1.2 -c 3')
        time.sleep(3)
        print(result1)
        result2 = ssh.execute('ping 21.1.1.3 -c 3')
        time.sleep(3)
        print(result2)
        ssh.close()

        # 用213ping82，删除路由
        ssh = SSH("10.1.1.213", 'root', 'root', 22)
        ssh.connect()
        result3 = ssh.execute('ping 12.1.1.2 -c 3')
        time.sleep(3)
        print(result3)
        ssh.execute('route del -net 21.1.1.0/24 gw 21.1.1.1')
        ssh.execute('route del -net 12.1.1.0/24 gw 21.1.1.1')
        ssh.close()

        # 给202删除路由：
        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        ssh.execute('route del -net 21.1.1.0/24 gw 20.1.1.1')
        ssh.execute('route del -net 12.1.1.0/24 gw 20.1.1.1')
        ssh.close()

        # 删除82上的路由
        a = Shell_SSH()
        a.connect("10.2.2.82")
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 21.1.1.0/24 gateway 12.1.1.1")
        a.execute("no ip route 20.1.1.0/24 gateway 12.1.1.1")

        change_physical_interface_workmode_wxw(browser, interface='ge0/6',
                                               route="no", ip='', mask='',
                                               trans='yes')

        try:
            assert "ttl" in result1
            assert "ttl" in result2
            assert "ttl" in result3
            rail_pass(206, test_id)
        except:
            rail_fail(206, test_id)
            assert "ttl" in result1
            assert "ttl" in result2
            assert "ttl" in result3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])