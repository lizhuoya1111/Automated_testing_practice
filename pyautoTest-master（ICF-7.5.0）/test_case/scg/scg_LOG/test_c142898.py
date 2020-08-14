import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
# from page_obj.scg.scg_def_physical_interface import *
# from page_obj.scg.scg_def_vlan_interface import *
# from page_obj.scg.scg_def_bridge import *
# from page_obj.common.rail import *
# from page_obj.scg.scg_def_log import *
# from page_obj.common.ssh import *
# from page_obj.scg.scg_def_dhcp import *
# from page_obj.scg.scg_dev import *
# from page_obj.scg.scg_def_ifname_OEM import *
# from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142898
# 先配置一个查询条件，包括时间日期、关键字，级别等，保存该查询条件，然后在reload处点击该条件，查询system log
# 可以根据查询条件查询system log
def test_c142898(browser):
    try:
        login_web(browser, url=dev1)
        # 配置查询条件并保存为“系统日志查询”
        advanced_query_save_system_log_lzy(browser, advanced="yes", ambiguous_search="",
                                           start_date="", start_time="", end_date="", end_time="",
                                           level="change", select_all="no", emerg="yes/no", alert="yes/no",
                                           critical="yes/no", error="yes/no", warning="yes/no", notice="yes",
                                           info="yes/no",
                                           debug="yes/no", module="change/unchange", modul_name="",
                                           save_as="yes", save_as_name="系统日志查询")
        # 点击该条件查询系统日志
        advanced_query_save_modify_admin_log_lzy(browser, log_type=系统日志, refresh="yes", refresh_name="系统日志查询",
                                                 delete="no")
        # 获取级别 判断为notice
        sleep(1)
        info1 = browser.find_element_by_xpath('//*[@id="levelarea0"]').text
        # print(info1)

        # 还原
        # 删除该查询条件
        advanced_query_save_modify_admin_log_lzy(browser, log_type=系统日志, refresh="yes", refresh_name="系统日志查询",
                                                 delete="yes")

        # 获取日志
        log1 =get_log(browser, 管理日志)
        # print(log1)



        try:
            assert "notice" in info1 and 'Delete' in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "notice" in info1 and 'Delete' in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
