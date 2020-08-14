import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def_static_route import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141330"
# 添加一条静态单网关路由，再添加ip生成一条和该路由目的相同的直连路由
# 可以添加，静态路由优先级高


def test_c141330(browser):

    try:
        # 81 上添加静态路由
        login_web(browser, url=dev1)
        add_static_route_single_wxw(browser, ip='192.168.11.0', mask='24', out_device=interface_name_2, gateway='12.1.1.2',
								enable='yes')
        # 给#2添加IP
        add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='192.168.11.11', mask='24')
        # 查看直连路由
        exist1 = is_static_route_exist_wxw(browser, destination='192.168.11.0/255.255.255.0')

        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]').text
        # print(info1)

        # 删除IP
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="192.168.11.11")
        # 删除静态路由
        del_ipv4_static_route_bydestination(browser, destination='192.168.11.0/255.255.255.0')


        try:
            assert exist1 == True and '192.168.11.0' in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist1 == True and '192.168.11.0' in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])