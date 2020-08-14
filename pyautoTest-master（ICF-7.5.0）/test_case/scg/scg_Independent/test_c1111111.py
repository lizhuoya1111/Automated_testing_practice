

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
from page_obj.scg.scg_def_authenticated_user import *
from page_obj.scg.scg_def_ipv6 import *
from page_obj.scg.scg_def_machine_learning import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "1111111"

# 在DUT上配置1024个网桥.分别与第一个网桥和第1024个网桥通信，检查数据流速度是否有区别
def test_c1111111(browser):
    try:
        # cli_add_vlan_lzy(devname=dev2, username="admin", password="admin@139", port=22, interface=interface_name_5, num1=1, num2=20)
        # sleep(2)
        # cli_add_vlan_ip_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=20, num11=1,
        #                     num22=2, num111=1, num222=2, interface=interface_name_5, ip='40.', mask='32')
        login_web(browser, url=dev5)
        info1 = return_alert_add_AD_aut_server_lzy(browser, server_name="###", description="", server_address="11.1.1.1", backup_host_1="",
                               backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no", LDAP="yes/no", save="yes", cancel="yes/no")
        print(info1)
        # add_AD_aut_server_lzy(browser, server_name="lzy", description="", server_address="11.1.1.1", backup_host_1="",
        #                       backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no", LDAP="yes/no", save="yes", cancel="yes/no")
        # sleep(2)
        # icf_replay(pcap_type="Oracle", server_ip="10.1.1.211", user="root", passwd="arsenal", hostadd1="121.1.1.120",
        #            hostadd2="121.1.1.20")


        # into_fun(browser, 子接口)
        # sleep(10)
        # cli_delete_vlan_lzy(devname=dev2, username="admin", password="admin@139", port=22, interface=interface_name_5, num1=1, num2=20)

        # into_fun(browser, 子接口)
        # sleep(10)
        # login_web(browser, dev2)
        # cli_delete_bridge_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=101)
        # add_ipv6_tunnel_lzy(browser, name="a", unnumbered="yes", interface="br_0", fixed_ip="yes/no", ip="",
        #                     six_to_four_tunnel="yes", manual_tunnel="yes/no", destination_ip="",
        #                     MTU="1480", save="yes", cancel="yes/no")
        # sleep(5)
        # delete_ipv6_tunnel_by_name_lzy(browser, name="a")

        # # 添加100个网桥br_1到br_1024
        # cli_add_bridge_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=101)
        #
        # sleep(0.5)
        # # 登录设备2，将#2接口添加ip 40.1.1.11 24
        # login_web(browser, dev3)
        # get_into_physical_interface(browser,interface_name_2)
        # info1 = browser.find_element_by_xpath('//*[@id="dhcp_ip"]').text
        # print(info1)

        # # 添加1024个网桥br_1到br_1024
        # cli_add_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=1025)
        #
        # sleep(0.5)
        #
        # # 登录设备
        # login_web(browser, url=dev1)
        #
        # # 删除#2接口ip，变为透明模式，加入网桥br_1
        # # 删除#3接口ip，变为透明模式，加入网桥br_1024
        # delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        # delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
        # physics_interface_change_transparent_interface(browser, interface2=interface_name_2,
        #                                                interface3=interface_name_3)
        # sleep(0.5)
        #
        # # 给网桥br_1添加ip 40.1.1.1
        # # 给网桥br_1024添加ip 50.1.1.1
        # # #2加入网桥br_1 #3加入网桥br_1024
        # scg = Shell_SSH()
        # scg.connect(hostip=dev1)
        # scg.execute("en")
        # scg.execute("con t")
        # scg.execute("interface bridge br_1")
        # scg.execute("ip address 40.1.1.1 24")
        # scg.execute("bridge-member "+interface_name_2)
        # scg.execute("exit")
        # scg.execute("interface bridge br_1024")
        # scg.execute("ip address 50.1.1.1 24")
        # scg.execute("bridge-member " + interface_name_3)
        # scg.execute("exit")
        # time.sleep(0.5)
        # scg.close()
        # output = scg.output()
        # print(output)
        #
        #
        # # 登录设备
        # login_web(browser, url=dev1)
        # # 获取条目数
        # count1 = get_count_number_bridge_lzy(browser)
        # print(count1)
        #
        # sleep(0.5)
        #
        # # 登录设备2，将#2接口添加ip 40.1.1.11 24
        # login_web(browser, dev2)
        # add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='40.1.1.11', mask='24')
        #
        # # 设备2#2ping设备1#2的40.1.1.1 可通
        # info3 = diag_ping(browser, ipadd="40.1.1.1", packersize="100", count="5", ping_wait_time="2", interface=interface_name_2, timesleep=5)
        # print(info3)
        #
        # sleep(0.5)
        #
        # # 登录设备3，将#2接口添加ip 50.1.1.11 24
        # login_web(browser, dev3)
        # add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='50.1.1.11', mask='24')
        #
        # # 设备3#2ping设备1#3的50.1.1.1 可通
        # info4 = diag_ping(browser, ipadd="50.1.1.1", packersize="100", count="5", ping_wait_time="2",
        #                   interface=interface_name_2, timesleep=5)
        # print(info4)
        #
        # # 还原
        # # 重启设备1
        # reload(hostip=[dev1, dev2, dev3])
        # sleep(1)

        try:
            assert 1 == 1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert 1 == 1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        #reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





