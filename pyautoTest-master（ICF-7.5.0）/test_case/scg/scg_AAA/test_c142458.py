import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_authenticated_user import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *

test_id = 142458
# 配置一个正确的认证服务器，然后修改他的名字，应该无法修改
# 服务器名称无法修改

def test_c142458(browser):
    try:
        login_web(browser, url=dev5)
        # 新增AD服务器
        add_AD_aut_server_lzy(browser, server_name="lzy", description="", server_address="30.1.1.1", backup_host_1="",
                              backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no", LDAP="yes/no", save="yes",
                              cancel="yes/no")

        # 修改服务器名称
        change_AD_aut_server_by_name_lzy(browser, name='lzy', description="", server_address="30.1.1.1",
                                         backup_host_1="",
                                         backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no", LDAP="yes",
                                         save="yes", cancel="yes/no")

        # 获取界面信息 名称为lze而非aaa
        sleep(0.5)
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[2]').text
        print(info1)


        # 还原
        # 删除AD服务器
        sleep(0.5)
        delete_AD_aut_server_by_name_lzy(browser, name='lzy')


        try:
            assert "lzy" in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "lzy" in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])