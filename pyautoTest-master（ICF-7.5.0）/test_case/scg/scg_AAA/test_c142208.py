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

test_id = 142208
# 配置输入的次数（1－3），例如分别配置（1，2，3）值，看是否能下发
# 全局设置
def test_c142208(browser):
    try:
        login_web(browser, url=dev5)
        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="20", retry="1", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
                               welcome_info="yes", login_title="11111", login_success="", login_fail="",
                               language="英语", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        log1 = get_log(browser, 管理日志)
        print(log1)
        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="20", retry="2", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
                               welcome_info="yes", login_title="11111", login_success="", login_fail="",
                               language="英语", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        log11 = get_log(browser, 管理日志)
        print(log11)
        # 全局设置
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="20", retry="3", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
                               welcome_info="yes", login_title="11111", login_success="", login_fail="",
                               language="英语", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        log111 = get_log(browser, 管理日志)
        print(log111)

        # 还原
        sleep(0.5)
        add_globel_setting_lzy(browser, frozen="yes", frozen_time="10", retry="3", interval_time="10",
                               phone_interval="120", idle_time="60", sms_center="", HTTP_port="80",
                               welcome_info="no", login_title="", login_success="", login_fail="",
                               language="简体中文", keep_current_configuration="yes", update="no",
                               file_name="", save="yes")
        log2 = get_log(browser, 管理日志)
        print(log2)



        try:
            assert "aaa global setting" in log1 and "http_port=80 is_frozen=1" in log2 and "retry=1" in log1 and "retry=2" in log11 and "retry=3" in log111
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "aaa global setting" in log1 and "http_port=80 is_frozen=1" in log2 and "retry=1" in log1 and "retry=2" in log11 and "retry=3" in log111
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev5)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])