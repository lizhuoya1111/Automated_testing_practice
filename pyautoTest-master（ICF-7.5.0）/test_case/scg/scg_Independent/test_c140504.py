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

test_id = "140504"

# 配置10个网桥接口，在所有的网桥上配置256个ip，检查能否成功
# 系统总ip数限制为2000
def test_c140504(browser):
    try:
        # 添加10个网桥br_1到br_10
        cli_add_bridge_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=11)

        # 在每个网桥上配置256个ip （配置不完全因为系统ip限制）
        cli_add_bridge_ip_lzy(devname=dev1, username="admin", password="admin@139", port=22, num1=1, num2=11, num11=1,
                              num22=17, num111=1, num222=17, bridge='br_', ip='30.', mask='32')

        # 登录设备
        login_web(browser, url=dev1)
        # 获取条目数
        count1 = get_count_number_bridge_lzy(browser)
        print(count1)

        # 获取bridge列表br_1的ip 30.1.1.1在其中
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[3]').text
        print(info1)

        # 还原
        # 重启设备
        reload(dev1)
        sleep(1)



        try:
            assert '30.1.1.1' in info1 and count1 == 11
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '30.1.1.1' in info1 and count1 == 11

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        #reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







