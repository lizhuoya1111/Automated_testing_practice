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

test_id = 142454
# 在各个能输入字符的地方输入&符号，下发后查看Local server是否正常

# 范围1-32个字符，不能输入 空格 $ < > \ ' '' | ; , ? & # ￥


def test_c142454(browser):
    try:
        login_web(browser, url=dev5)
        # 名称输入&符号
        info1 = return_alert_add_AD_aut_server_lzy(browser, server_name="&", description="", server_address="30.1.1.1",
                                           backup_host_1="",
                                           backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no", LDAP="yes/no",
                                           save="yes", cancel="yes/no")
        print(info1)
        # 清除输入
        # 服务器地址输入&符号
        info2 = return_alert_add_AD_aut_server_lzy(browser, server_name="lzy", description="", server_address="&",
                                                   backup_host_1="",
                                                   backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no",
                                                   LDAP="yes/no",
                                                   save="yes", cancel="yes/no")
        print(info2)
        # 备用主机输入&符号
        info3 = return_alert_add_AD_aut_server_lzy(browser, server_name="lzy", description="", server_address="30.1.1.1",
                                                   backup_host_1="&",
                                                   backup_host_2="", domain="", NTLM="yes", NTLM2="yes/no",
                                                   LDAP="yes/no",
                                                   save="yes", cancel="yes/no")
        print(info3)

        # 备用主机输入&符号
        info4 = return_alert_add_AD_aut_server_lzy(browser, server_name="lzy",
                                                   description="",
                                                   server_address="30.1.1.1",
                                                   backup_host_1="",
                                                   backup_host_2="&", domain="", NTLM="yes", NTLM2="yes/no",
                                                   LDAP="yes/no",
                                                   save="yes", cancel="yes/no")
        print(info4)
        # 域名输入&符号
        info5 = return_alert_add_AD_aut_server_lzy(browser, server_name="lzy",
                                                   description="",
                                                   server_address="30.1.1.1",
                                                   backup_host_1="",
                                                   backup_host_2="", domain="&", NTLM="yes", NTLM2="yes/no",
                                                   LDAP="yes/no",
                                                   save="yes", cancel="yes/no")
        print(info5)

        # 还原


        try:
            assert "请重新输入" in info1 and info2 == info3 ==info4 and "请重新输入" in info5
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "请重新输入" in info1 and info2 == info3 ==info4 and "请重新输入" in info5
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])