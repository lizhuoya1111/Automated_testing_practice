
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_sslvpn import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "221892"

# 正确配置安全站点，本地用户以及Portal站点
# 在登录页输入未启用的用户名和密码，输入错误的用户名，输入错误的密码

def test_c221892(browser):
    try:
        login_web(browser, url=dev1)
        # 清空安全站点
        del_all_sslvpn_safe_site_lzy(browser)
        sleep(0.5)
        # 增加安全站点
        add_sslvpn_safe_site_complete_lzy(browser, sitename='lzy', siteip=dev1, siteport='9090', enable='yes', enable_client_authentication='no',
								infomation_transfer='no', client_real_address='yes/no', certificate_DN='yes/no',
                              real_service_address='47.93.52.230', real_service_port='80', save='yes', cancel='no')
        sleep(0.5)
        # 删除本地用户
        del_all_sslvpn_local_admin_lzy(browser)
        sleep(0.5)
        # 增加本地用户
        add_sslvpn_local_admin_complete_lzy(browser, name='admin', password='admin@139', enable='yes', save='yes',
                                            cancel='no')
        sleep(0.5)

        # 增加Portal站点
        add_sslvpn_portal_site_complete_lzy(browser, enable='yes', sitename='lzy', siteip=dev1, siteport='9091',
                                            addlist='yes', dellist='o', addsite='lzy', delsite='', save='yes',
                                            cancel='no')
        sleep(0.5)

        # 浏览器输入Portal站点
        sign_out_jyl(browser)
        get_portal_lzy(browser, siteip=dev1, siteport='9091')

        sleep(1)

        # 登录界面
        login_portal_login_lzy(browser, username="admin", password="admin1111")

        # 获取信息
        sleep(2)
        alert1 = browser.switch_to_alert().text
        print(alert1)
        # 接受告警
        sleep(2)
        browser.switch_to_alert().accept()

        # 浏览器输入Portal站点
        login_web(browser, dev3)
        get_portal_lzy(browser, siteip=dev1, siteport='9091')

        # 登录界面
        login_portal_login_lzy(browser, username="admin1111", password="admin2222")

        # 获取信息
        sleep(2)
        alert2 = browser.switch_to_alert().text
        print(alert2)
        # 接受告警
        sleep(2)
        browser.switch_to_alert().accept()

        # info1 = browser.find_element_by_xpath('//*[@id="main-message"]/h1/span').text
        # print(info1)

        # 还原
        sleep(0.5)
        login_web(browser, url=dev1)
        sleep(0.5)
        # 删除本地用户
        del_all_sslvpn_local_admin_lzy(browser)
        sleep(0.5)

        # 删除安全站点
        del_all_sslvpn_safe_site_lzy(browser)



        try:
            assert '密码' in alert1 and '密码' in alert2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '密码' in alert1 and '密码' in alert2



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





