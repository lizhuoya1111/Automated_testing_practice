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

    a4 = Shell_SSH()
    a4.connect("10.2.2.84")
    a4.execute("en")
    a4.execute("ping 12.1.1.2")
    result2 = a4.output()
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_123.py"])