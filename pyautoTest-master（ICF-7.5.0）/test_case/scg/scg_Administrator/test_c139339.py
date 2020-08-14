import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
test_id = 139339
# 1.添加一个admin profile aaa，conf system为write-read，report system为read-write
# 2.添加一个admin user，name为32个英文字符，auth database为local，profile 引用aaa，login type选择ssh，https，console，permit ip 使用IPV6地址,interface GE0，inline number是3，status是enable
# 4.点击saveඬ
# 配置成功


def test_c139339(browser):
    try:
        # 登录函数
        login_web(browser, url=dev1)
        # 添加权限
        add_admin_profile(browser, profile_name='lzy', desc='zhe是yi个描述1', cfg="读写", report="读写")
        # 添加管理员
        add_admin_lzy(browser, admin_name="aaaaaaaaaabbbbbbbbbbccccccccccdd", auth_database="local", temp="lzy", https="yes", telent="yes",
                      ssh="yes", console="yes", password="admin@139", confirm_password="admin@139", status="enable",
                      interface=interface_name_1, online_num="32", ip1="", ip2="", ip3="", ip4="", ip5="",
                      ipv6_1='::1/64', ipv6_2='', ipv6_3='', ipv6_4='', ipv6_5='')
        # 获取日志
        log1 = get_log(browser, 管理日志)
        # print(log1)

        # 还原
        delete_all_admin_list_jyl(browser)
        delete_all_admin_profile_jyl(browser)
        try:
            assert '添加管理员帐户成功' in log1 and 'subnet=::1/64' in log1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '添加管理员帐户成功' in log1 and 'subnet=::1/64' in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
