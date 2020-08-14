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

test_id = "140569"

# 网桥上创建256个ip地址，PC与此网桥相连并使用网桥的第256个ip地址进行通信，验证能否通信成功
def test_c140569(browser):
    try:

        # 在每个网桥上配置255个ip （配置不完全因为系统ip限制）第256个ip添加可通信ip
        cli_add_bridge_ip_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=2, num11=1,
                              num22=6, num111=1, num222=52, bridge='br_', ip='30.', mask='32')

        # 登录设备
        login_web(browser, url=dev1)

        sleep(0.5)

        # 给网桥br_1添加ip 40.1.1.1
        bridge_ip_add(browser, bridge_interface="br_1", ip="40.1.1.1", mask="255.255.255.0")

        sleep(0.5)

        into_fun(browser, 网桥)
        sleep(0.5)

        # 获取bridge列表br_1的ip 40.1.1.1在其中
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[3]').text
        print(info1)

        sleep(0.5)

        # 删除#2接口ip，变为透明模式，加入网桥br_1
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        physics_interface_change_transparent_interface(browser, interface2=interface_name_2)
        bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)

        sleep(0.5)

        # 登录设备2，将#2接口添加ip 40.1.1.11 24
        login_web(browser, dev2)
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='40.1.1.11', mask='24')

        # 设备2#2ping设备1#2的40.1.1.1 可通
        info3 = diag_ping(browser, ipadd="40.1.1.1", packersize="100", count="5", ping_wait_time="2", interface=interface_name_2, timesleep=5)
        print(info3)

        sleep(0.5)

        # 还原
        reload(hostip=[dev1, dev2])
        sleep(1)

        try:
            assert '40.1.1.1' in info1 and 'ms' in info3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '40.1.1.1' in info1 and 'ms' in info3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







