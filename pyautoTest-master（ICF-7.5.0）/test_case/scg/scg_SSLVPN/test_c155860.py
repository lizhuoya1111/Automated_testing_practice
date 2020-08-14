
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

test_id = "155860"

# 点击某条信息后的编辑，
# 1，不做改动直接保存
# 2，修改之后点击保存
# 1，条目信息不改变
# 2，条目信息相应改变并立即生效

def test_c155860(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有安全站点（避免冲突）
        del_all_sslvpn_safe_site_lzy(browser)
        # 增加安全站点
        add_sslvpn_safe_site_complete_lzy(browser, sitename='lzy', siteip=dev1, siteport='9090', enable='yes',
                                 enable_client_authentication='yes',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                 real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')
        sleep(0.5)

        # 获取页面真实服务端口信息-80
        info1 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[2]/td[7]').text.strip()
        print(info1)

        # 编辑（不做改动直接保存）
        edit_sslvpn_safe_site_lzy(browser, number='1', sitename='lzy', siteip=dev1, siteport='9090', enable='yes',
                                 enable_client_authentication='yes',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                 real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')
        sleep(0.5)

        # 获取页面真实服务端口信息-80
        info11 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[2]/td[7]').text.strip()
        print(info11)

        # 编辑（改动之后保存） 真实服务端口改为90
        edit_sslvpn_safe_site_lzy(browser, number='1', sitename='lzy', siteip=dev1, siteport='9090',
                                  enable='yes',
                                  enable_client_authentication='yes',
                                  infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                  real_service_address='47.93.52.230', real_service_port='90',
                                  save='yes', cancel='no')
        sleep(0.5)

        # 获取页面真实服务端口信息-90
        info2 = browser.find_element_by_xpath('//*[@id="vpn_certadmin_table"]/tbody/tr[2]/td[7]').text.strip()
        print(info2)


        # 还原
        # 删除所有安全站点
        del_all_sslvpn_safe_site_lzy(browser)


        try:
            assert info1 == info11 and info1 != info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert info1 == info11 and info1 != info2



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





