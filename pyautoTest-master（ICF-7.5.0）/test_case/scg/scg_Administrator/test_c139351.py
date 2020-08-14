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

test_id = 139351
# 1.添加一个admin profile，conf system是read-only，report system是read-only
# 2.添加admin user，login type是https，引用该profile
# 3.使用该用户登录https，查看和通过web写配置
# 4.使用该用户登录ssh
# 1.只能通过web看配置，不能写入配置，只能查看log和report信息
# 2.不能使用ssh登录设备---如何验证？？？


def test_c139351(browser):
    try:
        # 登录函数
        login_web(browser, url=dev1)
        # 添加权限
        add_admin_profile(browser, profile_name='lzy', desc='zhe是yi个描述1', cfg="只读", report="只读")
        # 添加管理员
        add_admin_lzy(browser, admin_name="lzy", auth_database="local", temp="lzy", https="yes", telent="no",
                      ssh="no", console="no", password="admin@139", confirm_password="admin@139", status="enable",
                      interface=interface_name_1, online_num="32", ip1="", ip2="", ip3="", ip4="", ip5="",
                      ipv6_1='', ipv6_2='', ipv6_3='', ipv6_4='', ipv6_5='')
        # 退出当前账号
        sign_out_jyl(browser)
        # 用新账号登录
        login_web(browser, url=dev1, username="lzy")
        # 修改DNS
        set_dns(browser, dns1="114.114.114.115", dns2="")
        # 获取无权限提示
        info1 = browser.find_element_by_xpath('//*[@id="text_warning"]').text
        # print(info1)
        # 获取日志
        log1 = get_log(browser, 管理日志)
        # print(log1)
        # 获取报表信息
        into_fun(browser, 会话表)
        info2 = browser.find_element_by_xpath('//*[@id="rep_session_table_0"]').text
        # print(info2)

        # # 使用SSH登录设备
        # shell_81 = Shell_SSH()
        # shell_81.connect(hostip=dev1, name="lzy", passwd="admin@139")
        # time.sleep(4)
        # result1 = shell_81.output()
        # shell_81.close()
        # print(result1)

        # 还原
        # 退出当前账号
        sign_out_jyl(browser)
        # 用admin登录
        login_web(browser, url=dev1)
        # 删除管理员和权限
        delete_all_admin_list_jyl(browser)
        delete_all_admin_profile_jyl(browser)

        try:
            assert '您没有权限进行此项操作' in info1 and '系统管理员' in log1 and ':' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '添加管理员帐户成功' in log1 and 'subnet=::1/64' in log1 and ':' in info2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
