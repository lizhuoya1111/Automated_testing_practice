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

test_id = "140568"

# 在DUT上配置1024个网桥.分别与第一个网桥和第1024个网桥通信，检查数据流速度是否有区别
def test_c140568(browser):
    try:
        # 添加1024个网桥br_1到br_1024
        cli_add_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=1025)

        sleep(0.5)

        # 登录设备
        login_web(browser, url=dev1)

        # 删除#2接口ip，变为透明模式，加入网桥br_1
        # 删除#3接口ip，变为透明模式，加入网桥br_1024
        delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
        delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
        physics_interface_change_transparent_interface(browser, interface2=interface_name_2,
                                                       interface3=interface_name_3)
        sleep(0.5)

        # 给网桥br_1添加ip 40.1.1.1
        # 给网桥br_1024添加ip 50.1.1.1
        # #2加入网桥br_1 #3加入网桥br_1024
        scg = Shell_SSH()
        scg.connect(hostip=dev1)
        scg.execute("en")
        scg.execute("con t")
        scg.execute("interface bridge br_1")
        scg.execute("ip address 40.1.1.1 24")
        scg.execute("bridge-member "+interface_name_2)
        scg.execute("exit")
        scg.execute("interface bridge br_1024")
        scg.execute("ip address 50.1.1.1 24")
        scg.execute("bridge-member " + interface_name_3)
        scg.execute("exit")
        time.sleep(0.5)
        scg.close()
        output = scg.output()
        print(output)


        # 登录设备
        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_bridge_lzy(browser)
        print(count1)

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
            assert count1 == 1025 and 'ms' in info3 and 'ms' in info4
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert count1 == 1025 and  'ms' in info3 and 'ms' in info4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=[dev1, dev2, dev3])
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







