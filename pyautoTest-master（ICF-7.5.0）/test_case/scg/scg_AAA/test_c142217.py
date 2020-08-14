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

test_id = 142217
# 同时修改以上标题，认证成功，认证失败内容，看能否成功，在shell中查看是否与ui配置一致，查看log记录是否正确
# 全局设置
def test_c142217(browser):
    try:
        login_web(browser, url=dev5)
        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="30", retry="1", interval_time="30",
                               phone_interval="1200", idle_time="15", sms_center="111222333", HTTP_port="80",
                               welcome_info="yes", login_title="RADIUS1", login_success="login successfully", login_fail="login failed",
                               language="英语", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")

        log1 = get_log(browser, 管理日志)
        print(log1)

        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="30", retry="1", interval_time="30",
                               phone_interval="1200", idle_time="15", sms_center="111222333", HTTP_port="80",
                               welcome_info="yes", login_title="RADIUS2", login_success="login successfully2",
                               login_fail="login failed2",
                               language="英语", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")

        log11 = get_log(browser, 管理日志)
        print(log11)

        # 还原
        sleep(0.5)
        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="10", retry="3", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center=" ", HTTP_port="80",
                               welcome_info="yes", login_title=" ", login_success=" ",
                               login_fail=" ",
                               language="简体中文", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="10", retry="3", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
                               welcome_info="no", login_title="", login_success="", login_fail="",
                               language="简体中文", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        log2 = get_log(browser, 管理日志)
        print(log2)



        try:
            assert "aaa global setting" in log1 and "http_port=80 is_frozen=1" in log2 and "login_title=RADIUS1 login_success=login successfully login_fail=login failed" in log1 and "login_title=RADIUS2 login_success=login successfully2 login_fail=login failed2" in log11
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "aaa global setting" in log1 and "http_port=80 is_frozen=1" in log2 and "login_title=RADIUS1 login_success=login successfully login_fail=login failed" in log1 and "login_title=RADIUS2 login_success=login successfully2 login_fail=login failed2" in log11
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])