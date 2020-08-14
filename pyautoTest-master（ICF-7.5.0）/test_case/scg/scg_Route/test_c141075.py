import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141075"

# 桥接口添加ip
# 静态路由表和route monitor里会出现相应的直连路由


def test_c141075(browser):

    try:

        login_web(browser, url=dev1)
        # 新建网桥 把81#5 加入网桥
        bridge_add_jyl(browser, bridge_name="br_11")
        bridge_edit_interface_jyl(browser, bridge_interface="br_11", interface=interface_name_5)

        # 给网桥添加IP
        bridge_edit_ip_add_jyl(browser, bridge_interface="br_11", address_mode="manual", ip="192.168.11.1", mask="255.255.255.0")

        # 判断直连路由是否存在（静态路由中判断）
        exist1 = is_static_route_exist_wxw(browser, destination='192.168.11.0/255.255.255.0')
        # print(exist1)
        # 判断直连路由是否存在（路由监控中判断）
        exist2 = is_static_route_exist_wxw(browser, destination='192.168.11.0/255.255.255.0')
        # print(exist2)

        # 还原
        delete_bridge_byname(browser, br_name="br_11")



        try:
            assert exist1 is True and exist2 is True
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist1 is True and exist2 is True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])