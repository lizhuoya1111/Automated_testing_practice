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
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_timeout_setting import *
test_id = 140148
# 查询没有符合条件的session，查询到0个session


def test_c140148(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 新建zone2
        add_obj_zone(browser, name='zone2', desc='1', zone_mem=[interface_name_2])
        # 添加名称为lzy的查询条件 源接口设置为zone2
        add_query_terms(browser, name='lzy', fromzone='Z:zone2')
        log1 = get_log(browser, 管理日志)
        # 查询没有符合条件的session
        query_Sessiontable_by_name(browser, name='lzy')
        # 查询到0个session
        num1 = catch_number_after_qurey_Sessiontable_by_name(browser)

        # 还原（删除查询条件）
        del_query_terms_by_name(browser, name='lzy')
        # 删除zone2
        del_obj_zone_byname(browser, name='zone2')


        try:
            assert '添加' in log1 and '0' in num1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert '添加' in log1 and '0' in num1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
