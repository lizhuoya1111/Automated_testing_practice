import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37903
# 开启接口ge1/1的Allow Ping功能，
# 1.与此接口相连的PC能否ping通此接口，
# 2.与此接口相连的PC能否ping通其他接口，例如ge0/1, ge0/1没有开启Allow Ping


def test_physical_interface_wxw(browser):

    login_web(browser, url="10.2.2.81")

    open_physical_interface_allowping_wxw(browser, interface='ge0/4', allow_ping="close")
    open_physical_interface_allowping_wxw(browser, interface='ge0/3', allow_ping="close")

    ssh = SSH("10.1.1.202", 'root', 'root', 22)
    ssh.connect()
    result = ssh.execute('ping 20.1.1.1 -c 3')
    print(result)
    ssh.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')
    result2 = ssh.execute('ping 13.1.1.3 -c 3')
    print(result2)
    ssh.execute('route del -net 13.1.1.0/24 gw 20.1.1.1')
    ssh.close()

    open_physical_interface_allowping_wxw(browser, interface='ge0/4', allow_ping="open")
    open_physical_interface_allowping_wxw(browser, interface='ge0/3', allow_ping="open")

    try:
        assert "100% packet loss" not in result
        assert "100% packet loss" in result2
        rail_pass(206, test_id)
    except:
        rail_fail(206, test_id)
        assert "100% packet loss"not in result
        assert "100% packet loss" in result2

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c37903.py"])
