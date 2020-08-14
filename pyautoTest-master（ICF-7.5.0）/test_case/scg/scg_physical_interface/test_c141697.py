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

test_id = 141697
# 接口ge0/1和ge1/1分别与三层交换机和路由器相连，检查交换机与路由器能否通过ge0/1和ge1/1相通


def test_physical_interface_wxw():
    try:

        # 给82加上去往83的路由
        a = Shell_SSH()
        a.connect(dev2)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 20.1.1.0/24 gateway 12.1.1.1")
        a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")

        # 给83加上去往82的路由
        a = Shell_SSH()
        a.connect(dev3)
        a.execute("en")
        a.execute("conf t")
        a.execute("ip route 20.1.1.0/24 gateway 13.1.1.1")
        a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
        # 用83ping82
        a.execute("exit")
        a.execute("ping 12.1.1.2")
        time.sleep(2)
        result = a.output()
        # 给83删除去往82的路由
        a.execute("conf t")
        a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")

        # 给82删除去往83的路由
        a = Shell_SSH()
        a.connect(dev2)
        a.execute("en")
        a.execute("conf t")
        a.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")

        try:
            assert "Destination Host Unreachable" not in result
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "Destination Host Unreachable" not in result


    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=[dev2, dev3])
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])