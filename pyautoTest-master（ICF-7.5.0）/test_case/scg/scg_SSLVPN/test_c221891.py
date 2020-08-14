
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

test_id = "221891"

# 正确配置安全站点，本地用户以及Portal站点
# 在浏览器输入错误的Portal站点地址或端口

def test_c221891(browser):
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

        # 浏览器输入Portal站点-站点非法
        sign_out_jyl(browser)
        info = return_wrong_portal_login_lzy(browser, siteip=dev2, siteport='9091')
        print(info)

        sleep(1)

        info1 = return_wrong_portal_login_lzy(browser, siteip=dev1, siteport='9096')
        print(info1)

        # # 获取信息
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
            assert '无法访问此网站' in info and '无法访问此网站' in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '无法访问此网站' in info and '无法访问此网站' in info1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





