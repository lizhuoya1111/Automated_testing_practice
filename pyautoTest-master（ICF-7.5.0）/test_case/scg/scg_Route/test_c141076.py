

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

test_id = "141076"

# 验证直连路由无法删除编辑
# 无法删除和编辑
# 直连路由无法删除编辑 没有删除和编辑按钮


def test_c141076(browser):

    try:

        login_web(browser, url=dev1)
        # 进入静态路由界面
        into_fun(browser, 静态路由)
        # 获取静态路由条目信息 //*[@id="table"]/tbody/tr[9]/td[9]/a[1]/img
        time.sleep(0.5)
        route_sum = browser.find_element_by_xpath('//*[@id="rules_count"]').text

        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(int(route_sum)+1)+']/td[9]/a[1]/img').get_attribute('title')
        # print(info1)
        time.sleep(0.5)
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(int(route_sum)+1)+']/td[9]/a[2]/img').get_attribute('title')
        # print(info2)
        time.sleep(0.5)
        # 获取直连路由条目信息 （不能定位到编辑 删除按钮）
        info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]').text.strip()
        # print(info3)





        try:
            assert '编辑' in info1 and '删除' in info2 and '编辑' not in info3 and '删除' not in info3
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert '编辑' in info1 and '删除' in info2 and '编辑' not in info3 and '删除' not in info3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        # reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])