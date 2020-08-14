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
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141074"

# 验证dhcp client 获取地址
# 静态路由表和route monitor里会出现相应的直连路由


def test_c141074(browser):

    try:
        # 82 #2 设定DHCP服务器 并开启
        login_web(browser, url=dev2)
        dhcp_server_add_jyl(browser, interface=interface_name_2, dhcp_type="dhcp_server", dhcp_gw="12.1.1.1",
                            dhcp_sm="255.255.255.0", ip_range1_1="12.1.1.3", ip_range1_2="12.1.1.10")

        # 81 #2 删除原有IP
        login_web(browser, url=dev1)
        delete_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1')

        # 81 #2 通过DHCP方式获取IP
        physics_interface_from_dhcp_obtain_ip_jyl(browser, physical_interface=interface_name_2, alias="", description="", work_mode="dhcp",
                                                  update_default_gateway="open", update_system_dns="close", snat="close", allow_ping="open")

        # 判断直连路由是否存在（静态路由中判断）
        exist1 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist1)
        # 判断直连路由是否存在（路由监控中判断）
        exist2 = is_static_route_exist_wxw(browser, destination='12.1.1.0/255.255.255.0')
        # print(exist2)

        # 还原
        # 81 #2 静态方式添加IP
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')

        # 82 #2 DHCP先禁用再删除
        login_web(browser, url=dev2)
        dhcp_server_edit_or_delete_jyl(browser, fuction="delete")


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
        reload(hostip=[dev1, dev2])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])