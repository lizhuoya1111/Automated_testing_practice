import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "140567"

# 配置8个网桥接口，在所有的网桥上配置256个ip，分别使用接口的第一个和最后一个ip地址进行通信，验证能否通信成功
# 系统总ip数限制为2000 在此配置6个网桥
def test_c140567(browser):
    try:
        # 添加6个网桥br_1到br_6
        cli_add_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=7)

        # 在每个网桥上配置255个ip （配置不完全因为系统ip限制）第256个ip添加可通信ip
        cli_add_bridge_ip_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=7, num11=1,
                              num22=6, num111=1, num222=52, bridge='br_', ip='30.', mask='32')

        # 登录设备
        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_bridge_lzy(browser)
        print(count1)

        sleep(0.5)

        # 给网桥br_1添加ip 40.1.1.1
        bridge_ip_add(browser, bridge_interface="br_1", ip="40.1.1.1", mask="255.255.255.0")
        # 给网桥br_6添加ip 50.1.1.1
        bridge_ip_add(browser, bridge_interface="br_6", ip="50.1.1.1", mask="255.255.255.0")

        sleep(0.5)

        into_fun(browser, 网桥)
        sleep(0.5)

        # 获取bridge列表br_1的ip 40.1.1.1在其中
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[3]').text
        print(info1)
        # 获取bridge列表br_6的ip 50.1.1.1在其中
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[8]/td[3]').text
        print(info2)

        sleep(0.5)

        # 删除#2接口ip，变为透明模式，加入网桥br_1
        # 删除#3接口ip，变为透明模式，加入网桥br_6
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
        physics_interface_change_transparent_interface(browser, interface2=interface_name_2,
                                                       interface3=interface_name_3)
        bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)
        bridge_edit_interface_jyl(browser, bridge_interface="br_6", interface=interface_name_3)

        sleep(0.5)

        # 登录设备2，将#2接口添加ip 40.1.1.11 24
        login_web(browser, dev2)
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='40.1.1.11', mask='24')

        # 设备2#2ping设备1#2的40.1.1.1 可通
        info3 = diag_ping(browser, ipadd="40.1.1.1", packersize="100", count="5", ping_wait_time="2", interface=interface_name_2, timesleep=5)
        print(info3)

        sleep(0.5)

        # 登录设备3，将#2接口添加ip 50.1.1.11 24
        login_web(browser, dev3)
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='50.1.1.11', mask='24')

        # 设备3#2ping设备1#3的50.1.1.1 可通
        info4 = diag_ping(browser, ipadd="50.1.1.1", packersize="100", count="5", ping_wait_time="2",
                          interface=interface_name_2, timesleep=5)
        print(info4)

        # 还原
        # 重启设备1
        reload(hostip=[dev1, dev2, dev3])
        sleep(1)

        try:
            assert '40.1.1.1' in info1 and count1 == 7 and '50.1.1.1' in info2 and 'ms' in info3 and 'ms' in info4
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '40.1.1.1' in info1 and count1 == 7 and '50.1.1.1' in info2 and 'ms' in info3 and 'ms' in info4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







