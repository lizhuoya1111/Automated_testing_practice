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
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139198"

# 1.添加128个静态ip地址，检查能否成功；
# 2.添加129个静态ip地址，检查能否成功
# 目前物理接口可添加256个ip
def test_c139198(browser):
    try:
        # 接口添加ip
        scg = Shell_SSH()
        scg.connect(hostip=dev1)
        scg.execute("en")
        scg.execute("con t")
        scg.execute("interface gigabitethernet " + interface_name_6)
        for x in range(1, 201):
            scg.execute("ip address 31.1.1." + str(x) + " 32")
            sleep(0.2)
        time.sleep(1)
        for y in range(1, 57):
            scg.execute("ip address 31.1.2." + str(y) + " 32")
            sleep(0.2)
        time.sleep(1)
        scg.close()
        output = scg.output()
        print(output)


        login_web(browser, url=dev1)
        # 获取物理接口ip
        into_fun(browser, 物理接口)
        sleep(0.5)
        ip1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[7]/td[3]').text
        print(ip1)

        # 还原
        # 删除接口ip
        scg = Shell_SSH()
        scg.connect(hostip=dev1)
        scg.execute("en")
        scg.execute("con t")
        scg.execute("interface gigabitethernet " + interface_name_6)
        for x in range(1, 201):
            scg.execute("no ip address 31.1.1." + str(x))
            sleep(0.2)
        time.sleep(1)
        for y in range(1, 57):
            scg.execute("no ip address 31.1.2." + str(y))
            sleep(0.2)
        time.sleep(1)
        scg.close()
        output = scg.output()
        print(output)


        try:
            assert "31.1.1.2" in ip1 and "31.1.1.200" in ip1 and "31.1.2.2" in ip1 and "31.1.2.56" in ip1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "31.1.1.2" in ip1 and "31.1.1.200" in ip1 and "31.1.2.2" in ip1 and "31.1.2.56" in ip1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







