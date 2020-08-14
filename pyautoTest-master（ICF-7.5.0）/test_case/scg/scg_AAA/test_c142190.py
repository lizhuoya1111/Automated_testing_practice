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

test_id = 142190
# 配置timeout

def test_c142190(browser):
    try:
        login_web(browser, url=dev5)
        # 新增LDAP服务器
        add_LDAP_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="10.0.0.1", backup_host_1="",
                                backup_host_2="", port="389", LDAP="yes/no", basedn="dc=pip", admin="admin", password="",
                                confirm_password="", timeout="1", save="yes", cancel="yes/no")
        add_LDAP_aut_server_lzy(browser, server_name="lzy1", description="abcdef", server_address="10.0.0.1",
                                backup_host_1="",
                                backup_host_2="", port="389", LDAP="yes/no", basedn="dc=cn", admin="admin1", password="",
                                confirm_password="", timeout="10", save="yes", cancel="yes/no")


        # 获取界面信息
        sleep(0.5)
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody').text
        print(info1)

        log1 = get_log(browser, 管理日志)
        print(log1)

        # 还原
        # 删除所有服务器
        sleep(0.5)
        delete_all_AD_aut_server_lzy(browser)



        try:
            assert "1" in info1 and "10" in info1 and "成功添加 aaa server" in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "1" in info1 and "10" in info1 and "成功添加 aaa server" in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])