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
from page_obj.scg.scg_def_timeout_setting import *
test_id = 140071
# 在查询session的页面中，设置/修改 某个目的IP地址网段


def test_c140071(browser):
    try:
        # 登录设备
        login_web(browser, url=dev1)
        # 添加名称为lzy的查询条件 目的IP192.168.5.0/24 记得把默认的改成no
        add_query_terms(browser, name='lzy', destinationaddress='yes', dip='192.168.5.0', dipmask='24', destinationaddressobject='no')
        log1 = get_log(browser, 管理日志)
        # 点击修改目的IP192.168.6.0/24
        modify_query_terms_by_name(browser, name='lzy', destinationaddress='yes', dip='192.168.6.0', dipmask='24', destinationaddressobject='no')
        log2 = get_log(browser, 管理日志)
        # 还原（删除查询条件）
        del_query_terms_by_name(browser, name='lzy')


        try:
            assert '添加' in log1 and '修改' in log2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert '添加' in log1 and '修改' in log2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
