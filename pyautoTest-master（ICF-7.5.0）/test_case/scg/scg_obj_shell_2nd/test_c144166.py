import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144166"
# 选择全部serv grp,在unselected
# 可以选择


def test_c144166(browser):
    try:

        login_web(browser, url=dev1)
        # 先添加服务组lzy1-lzy5
        for x in range(1, 6):
            add_obj_serv_grp_wxw(browser, name='lzy'+str(x), serv_obj='P:any')
        # 全选服务组
        click_all_select_serv_group(browser)

        # 判断其中某个服务组是否被勾选
        judge1 = judge_if_select_obj_serv_group_ornot_by_name(browser, name='lzy2')

        # 取消全选
        cancel_all_select_serv_group(browser)

        # 判断其中某个服务组是否被勾选
        judge2 = judge_if_select_obj_serv_group_ornot_by_name(browser, name='lzy2')

        # 还原 删除全部服务组
        del_all_obj_serv_grp_wxw(browser)

        try:
            assert '被勾选' in judge1 and '未被勾选' in judge2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '被勾选' in judge1 and '未被勾选' in judge2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])