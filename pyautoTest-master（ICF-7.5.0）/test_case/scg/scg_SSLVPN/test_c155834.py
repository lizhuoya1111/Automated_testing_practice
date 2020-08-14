
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "155834"
# 点击界面左侧导航栏中SSLVPN
# 展开二级菜单：安全站点和证书配置
def test_c155834(browser):
    try:
        login_web(browser, url=dev1)
        # 进入安全站点 获取信息
        into_fun(browser, 安全站点)
        info1 = browser.find_element_by_xpath('//*[@id="for_tb_title"]/td[3]').text
        print(info1)
        sleep(0.5)
        # 进入证书配置 获取信息
        into_fun(browser, 证书配置)
        info2 = browser.find_element_by_xpath('//*[@id="container"]/div[3]/p[1]/strong').text
        print(info2)


        try:
            assert "站点名称" in info1 and '证书请求内容' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "站点名称" in info1 and '证书请求内容' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





