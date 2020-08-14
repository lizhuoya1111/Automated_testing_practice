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

test_id = 142192
# 点击add按钮，配置 name
# 1.大小写字母敏感检测，验证不同大小写字母的条目代表不同的条目
# 2.分别单独输入字母、汉字、数字、- = _和.
# 3.配置一个32个字符的name，（除< > ” ’ & \ ? $ #? 9个之外的所有字符）
# 4.在shell中查看是否与ui配置一致
def test_c142192(browser):
    try:
        login_web(browser, url=dev5)
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="lzy", description="", server_address="30.1.1.2", backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="LZY", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="李卓亚", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="111", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="=", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="、", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")
        # 新增TACACS认证服务器
        add_TACACS_aut_server_lzy(browser, server_name="aaaaaaaaaabbbbbbbbbbccccccccccdd", description="", server_address="30.1.1.2",
                                  backup_host_1="",
                                  backup_host_2="", port="49", timeout="2", share_password="", save="yes",
                                  cancel="yes/no")

        # 获取界面信息
        sleep(0.5)
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody').text
        print(info1)

        log1 = get_log(browser, 管理日志)
        print(log1)


        # 还原
        # 删除所有服务器
        sleep(0.5)
        delete_all_aut_server_lzy(browser)




        try:
            assert "lzy" in info1 and "成功添加 aaa server" in log1 and "LZY" in info1 and "李卓亚" in info1 and "=" in info1 and "、" in info1 and "aaaaaaaaaabbbbbbbbbbccccccccccdd" in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "lzy" in info1 and "成功添加 aaa server" in log1 and "LZY" in info1 and "李卓亚" in info1 and "=" in info1 and "、" in info1 and "aaaaaaaaaabbbbbbbbbbccccccccccdd" in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])