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
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_ipv6 import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "140566"

# 将子接口和网桥接口都添加到极限（du100的1024个），
# 并保证每个接口都有ip地址，然后打开ipsec和ipv6 tunnel的配置界面，
# 检查UI上接口和ip列表是否能加载成功，添加ipsec和ipv6 tunnel是否能成功
# 系统总ip数限制为2000
# 本用例添加100个网桥和100个子接口
def test_c140566(browser):
    try:
        # 添加100个网桥br_1到br_100
        cli_add_bridge_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=101)

        # Dev2的#5 接口添加100个子接口
        cli_add_vlan_lzy(devname=dev2, username="admin", password="admin@139", port=22, interface=interface_name_5,
                         num1=1, num2=101)


        # 在每个网桥上配置1个ip（小于255个网桥可用以下函数给每个网桥添加ip）
        cli_add_bridge_ip_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=101, num11=1,
                              num22=2, num111=1, num222=2, bridge='br_', ip='30.', mask='32')

        sleep(2)

        # 在每个子接口上配置1个ip（小于255个子接口可用以下函数给每个子接口添加ip）
        cli_add_vlan_ip_lzy(devname=dev2, username="admin", password="admin@139", port=22, num1=1, num2=101, num11=1,
                              num22=2, num111=1, num222=2, interface=interface_name_5, ip='40.', mask='32')

        # 登录设备
        login_web(browser, url=dev2)
        # 获取条目数
        count1 = get_count_number_bridge_lzy(browser)
        print(count1)

        sleep(0.5)
        print("1111111111111111111111111111111111111111111")

        # 获取条目数
        count2 = get_count_number_vlan_lzy(browser)
        print(count2)

        # 检查ipv6隧道接口显示是否完全
        into_fun(browser, IPv6隧道)
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
        sleep(0.2)
        info1 = browser.find_element_by_xpath('//*[@id="localip_inf"]').text
        print("ipv6隧道接口显示如下："+info1)
        # 添加ipv6隧道，name为a
        add_ipv6_tunnel_lzy(browser, name="a", unnumbered="yes", interface="br_100", fixed_ip="yes/no", ip="",
                            six_to_four_tunnel="yes", manual_tunnel="yes/no", destination_ip="",
                            MTU="1480", save="yes", cancel="yes/no")

        # 获取日志 添加隧道成功
        log1 = get_log(browser, 管理日志)
        print(log1)

        sleep(1)

        # 检查ipsec隧道接口显示是否完全
        login_web(browser, dev2)
        sleep(0.5)
        into_fun(browser, 远程网关)
        sleep(0.5)
        browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
        sleep(2)
        info2 = browser.find_element_by_xpath('//*[@id="localif"]').text
        sleep(2)
        print("ipsec隧道接口显示如下："+info2)
        sleep(2)



        # 添加ipsec隧道
        if oem_name == "ICF" or oem_name != "SCG":
            add_ipsec_remote_gateway_wxw(browser, name='ipsec_lzy_1',
                                         out_interface=interface_name_2,
                                         remote_gateway='static', gateway='12.1.1.1', auth_method='预共享密钥',
                                         password='123456',
                                         local='local_ip', local_ip='13.1.1.0/255.255.255.0',
                                         local_addr_obj='any',
                                         remote='remote_ip', remote_ip='24.1.1.0/255.255.255.0',
                                         remote_addr_obj='any',
                                         save='yes', cancel='')
        elif oem_name == "SCG":
            add_ipsec_remote_gateway_gm(browser, name='ipsec_lzy_1',
                                        out_interface=interface_name_2,
                                        remote_gateway='static', gateway='12.1.1.1', auth_method='证书',
                                        localid="CN=127.0.0.1", remoteid="CN=127.0.0.2", remote_cert_id_any_switch="no",
                                        local='local_ip', local_ip='30.1.1.0/255.255.255.0',
                                        local_addr_obj='any',
                                        remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
                                        remote_addr_obj='any', ipsec_super_net_switch="no",
                                        advanced='no',
                                        encry_alg_div='3des', auth_alg='sha1',
                                        ike_sa_lifetime='86400',
                                        ah='no', ah_auth_alg='',
                                        esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
                                        ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
                                        tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
                                        save='yes', cancel='no')

        # 获取日志 成功添加远程网关隧道
        log2 = get_log(browser, 管理日志)
        print(log2)

        sleep(0.5)

        # 还原
        # 重启设备1
        reload(hostip=dev2)
        sleep(1)

        try:
            assert 'br_' in info1 and '.' in info1 and count1 == 101 and count2 == 100 and '添加隧道成功' in log1 and '成功添加远程网关隧道' in log2 and 'br_' in info2 and '.' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert 'br_' in info1 and '.' in info1 and count1 == 101 and count2 == 100 and '添加隧道成功' in log1 and '成功添加远程网关隧道' in log2 and 'br_' in info2 and '.' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev2)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







