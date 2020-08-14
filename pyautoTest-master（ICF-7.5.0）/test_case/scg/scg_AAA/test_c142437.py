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

test_id = 142437
# 在各个能输入字符的地方输入&符号，下发后查看Local server是否正常
def test_c142437(browser):
    try:
        login_web(browser, url=dev5)
        # 在各个能输入字符的地方输入&符号，下发后查看Local server是否正常
        info1 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="&", description="abcdef",
                                                      server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                      backup_host_2="10.0.0.3", port="2005", retry="0", timeout="1",
                                                      password="adf123", PAP="yes/no",
                                                      CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info1)
        info2 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="&",
                                                      server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                      backup_host_2="10.0.0.3", port="2005", retry="0", timeout="1",
                                                      password="adf123", PAP="yes/no",
                                                      CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info2)
        info3 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="&", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="1", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info3)

        info4 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="11.1.1.1", backup_host_1="&",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="1", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info4)

        info5 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                  backup_host_2="&", port="2005", retry="0", timeout="1", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info5)
        info6 = return_info_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="&", retry="0", timeout="1",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info6)
        info7 = return_info_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="&", timeout="1",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info7)
        info8 = return_info_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="&",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info8)
        info9 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="1",
                                                       password="&", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info9)


        # 还原
        # 删除所有服务器
        sleep(0.5)
        delete_all_aut_server_lzy(browser)




        try:
            assert "名称输入错误" in info1 and "描述格式输入错误" in info2 and "IP格式输入错误" in info3 and info3 == info4 == info5 and info6 == info7 == info8 and "密码格式输入错误" in info9
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "名称输入错误" in info1 and "描述格式输入错误" in info2 and "IP格式输入错误" in info3 and info3 == info4 == info5 and info6 == info7 == info8 and "密码格式输入错误" in info9
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])