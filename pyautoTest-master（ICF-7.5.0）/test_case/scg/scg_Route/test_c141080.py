
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

test_id = "141080"

# 直连路由根据ip地址长度自动排序，目的ip验证包括从0.0.0.0、1.1.1.1；64.0.0.0；128.1.1.1；192.168.1.1；224.224.1.1
# 地址长度大的在路由表前面；修改路由的目的ip能够重新根据新的ip地址排序
#


def test_c141080(browser):

    try:

        login_web(browser, url=dev1)
        # 进入到静态路由界面
        into_fun(browser, 静态路由)
        # 获取直连路由目的地址/掩码
        IP1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.strip()
        IP2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text.strip()
        IP3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[4]').text.strip()
        IP4 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[4]').text.strip()
        IP5 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[4]').text.strip()
        a1 = IP1.split('.')[0] + IP1.split('.')[1] + IP1.split('.')[2]
        a2 = IP2.split('.')[0] + IP2.split('.')[1] + IP2.split('.')[2]
        a3 = IP3.split('.')[0] + IP3.split('.')[1] + IP3.split('.')[2]
        a4 = IP4.split('.')[0] + IP4.split('.')[1] + IP4.split('.')[2]
        a5 = IP5.split('.')[0] + IP5.split('.')[1] + IP5.split('.')[2]
        # print(a1)
        # print(a2)
        # print(a3)
        # print(a4)
        # print(a5)

        # 删除81#2接口IP
        delete_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1')
        # 添加新IP
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='192.168.11.1', mask='255.255.255.0')

        # 进入到静态路由界面
        into_fun(browser, 静态路由)
        # 获取直连路由目的地址/掩码
        IP6 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.strip()
        IP7 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text.strip()
        IP8 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[4]').text.strip()
        IP9 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[4]').text.strip()
        IP10 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[6]/td[4]').text.strip()
        a6 = IP6.split('.')[0] + IP6.split('.')[1] + IP6.split('.')[2]
        a7 = IP7.split('.')[0] + IP7.split('.')[1] + IP7.split('.')[2]
        a8 = IP8.split('.')[0] + IP8.split('.')[1] + IP8.split('.')[2]
        a9 = IP9.split('.')[0] + IP9.split('.')[1] + IP9.split('.')[2]
        a10 = IP10.split('.')[0] + IP10.split('.')[1] + IP10.split('.')[2]
        # print(a6)
        # print(a7)
        # print(a8)
        # print(a9)
        # print(a10)

        # 删除81#2接口IP
        delete_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='192.168.11.1')
        # 还原
        add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')





        try:
            assert int(a1) > int(a2) > int(a3) > int(a4) > int(a5) and int(a6) > int(a7) > int(a8) > int(a9) > int(a10)
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert int(a1) > int(a2) > int(a3) > int(a4) > int(a5) and int(a6) > int(a7) > int(a8) > int(a9) > int(a10)

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])