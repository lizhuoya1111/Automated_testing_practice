import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_obj import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "21613"


def test_c21613(browser):

    login_web(browser)
    add_obj_zone(browser, "zone1", "desc", ["ge0/1"])
    # del_obj_zone_byname(browser,"test")
    add_admin(browser, "test1", temp="max_profile", password="admin@139", confirm_password="admin@139", interface="zone1")
    login_web(browser, username="test1")
    hostname = get_sys_info_hostname(browser)
    print(hostname)

    if str(hostname) == "BSAFE":

        # 进行telnet连接
        to_telnet = TelnetClient()
        telnet_info = to_telnet.login_host("10.2.2.81", "test1", "admin@139")
        print("正在匹配telnet信息..."+telnet_info)

        # 进行SSH连接
        to_ssh = Shell_SSH()
        to_ssh.connect("10.2.2.81","test1")
        ssh_info = to_ssh.output()
        print("正在匹配ssh信息..."+ssh_info)

        try:
            assert hostname in telnet_info and hostname in ssh_info
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert hostname in telnet_info and hostname in ssh_info

    else:
        rail_fail(test_run_id, test_id)
        assert False

    # 删除zone和管理员，恢复配置
    login_web(browser)
    del_admin_byname(browser, "test1")
    browser.refresh()
    del_obj_zone_byname(browser, "zone1")


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])

