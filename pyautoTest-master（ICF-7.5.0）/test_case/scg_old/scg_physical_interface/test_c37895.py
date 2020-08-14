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

test_id = 37895
# 配置某接口为多ip，此接口同时与多个PC进行通信（这些PC与此接口的多ip在相同网段），检查此接口的多ip是否都有效


def test_physical_interface_wxw(browser):

    login_web(browser, url="10.2.2.81")

    for n in range(22, 24):
        add_physical_interface_ip_wxw(browser, interface='ge0/4', ip=str(n)+'.1.1.1', mask='24')

    ssh = SSH("10.1.1.202", 'root', 'root', 22)
    ssh.connect()
    result1 = ssh.execute('ping 20.1.1.1 -c 3')
    print(result1)
    ssh.execute(' ifconfig eth2 22.1.1.2 netmask 255.255.255.0')
    result2 = ssh.execute('ping 22.1.1.1 -c 3')
    print(result2)
    ssh.execute(' ifconfig eth2 23.1.1.2 netmask 255.255.255.0')
    result3 = ssh.execute('ping 23.1.1.1 -c 3')
    print(result3)
    ssh.execute(' ifconfig eth2 20.1.1.2 netmask 255.255.255.0')
    ssh.close()

    for n in range(22, 24):
        delete_physical_interface_ip_wxw(browser, interface='ge0/4', ip=str(n)+'.1.1.1')

    try:
        assert "100% packet loss" not in result1
        assert "100% packet loss" not in result2
        assert "100% packet loss" not in result3
        rail_pass(206, test_id)
    except:
        rail_fail(206, test_id)
        assert "100% packet loss" not in result1
        assert "100% packet loss" not in result2
        assert "100% packet loss" not in result3


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c37895.py"])