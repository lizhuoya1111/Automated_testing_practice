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

test_id = 142433
# 配置Server name输入非法字符串
# 1.输入~ ` !@#$%^&*(){}[];:”,’?\|/+和空格符号的字符串
# 2.输入字符串长度超过 16（中文字符）、32（英文字符）
# 3.输入相同的 name 条目
# 4.中文字符输入非UTF8的格式

def test_c142433(browser):
    try:
        login_web(browser, url=dev5)
        # name输入$ < > \ ' '' | ; , ? & # ￥
        info1 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="$ < > \ ' '' | ; , ? & # ￥", description="abcdef", server_address="10.0.0.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info1)

        # name输入字符串长度超过 16（中文字符）、32（英文字符）
        info2 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd", description="abcdef", server_address="10.0.0.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info2)

        # name输入相同的 name 条目
        # 添加名为lzy的AD认证服务器
        add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="10.0.0.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        # 添加名为lzy的AD认证服务器
        info3 = return_info_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef", server_address="10.0.0.1", backup_host_1="10.0.0.2",
                                  backup_host_2="10.0.0.3", port="2005", retry="0", timeout="2", password="adf123", PAP="yes/no",
                                  CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info3)

        # 还原
        # 删除所有服务器
        sleep(0.5)
        delete_all_aut_server_lzy(browser)




        try:
            assert "名称输入错误，请重新输入" in info1 and "名称输入错误，请重新输入" in info2 and "相同名字的认证服务器 lzy 已经存在" in info3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "名称输入错误，请重新输入" in info1 and "名称输入错误，请重新输入" in info2 and "相同名字的认证服务器 lzy 已经存在" in info3
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])