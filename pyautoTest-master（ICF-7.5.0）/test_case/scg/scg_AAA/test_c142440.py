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

test_id = 142440
# 配置Radius的secret密码长度是大于64，查看是否能下发
def test_c142440(browser):
    try:
        login_web(browser, url=dev5)
        # aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggg

        info1 = return_alert_add_RADIUS_aut_server_lzy(browser, server_name="lzy", description="abcdef",
                                                       server_address="11.1.1.1", backup_host_1="10.0.0.2",
                                                       backup_host_2="10.0.0.3", port="1812", retry="2", timeout="1",
                                                       password="aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggg", PAP="yes/no",
                                                       CHAP="yes", charging="yes/no", save="yes", cancel="yes/no")
        print(info1)


        # 还原
        # 删除所有服务器
        sleep(0.5)
        delete_all_aut_server_lzy(browser)




        try:
            assert "密码格式输入错误，请重新输入" in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "密码格式输入错误，请重新输入" in info1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])