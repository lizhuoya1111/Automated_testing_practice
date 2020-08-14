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

test_id = 142434
# 配置非法的服务器的ip地址例如：
# 1.输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256
# 2.输入非IP点分格式的字符：例如中文、英文、！@！#！@￥、：“”标点符号
# 3.输入不合法IP、掩码：255.255.255.255、1.1.1.0/32、1.1.1.1/33、1.1.1.1/255.255.255.255
def test_c142434(browser):
    try:
        login_web(browser, url=dev5)
        # 服务器的ip地址输入A.2.3.155、#.$.4.5 、1.1.1.256
        info1 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="A.1.1.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info1)
        info11 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="#.$.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info11)
        info111 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="1.1.1.256", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info111)

        # 服务器的ip地址输入非IP点分格式的字符：例如中文、英文、！@！#！@￥、：“”标点符号
        info2 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="11A1.1.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info2)
        info22 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1李1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info22)
        info222 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11#1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info222)
        info2222 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11,1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info2222)

        # 服务器的ip地址输入不合法IP、掩码：255.255.255.255、1.1.1.0/32、1.1.1.1/33、1.1.1.1/255.255.255.255
        info3 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="255.255.255.258", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2",
                                                       password="adf123", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info3)

        # 还原
        # # 删除所有服务器
        # sleep(0.5)
        # delete_all_aut_server_lzy(browser)




        try:
            assert info1 == info11 == info111 == info2 == info22 == info222 == info2222 == info3 and "IP格式输入错误，请重新输入" in info3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert info1 == info11 == info111 == info2 == info22 == info222 == info2222 == info3 and "IP格式输入错误，请重新输入" in info3
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])