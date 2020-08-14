import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37204
# 对于只有ISP name的 条目，点击条目后面的edit 按钮
# 可修改ISP name 和description


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp204', desc='')

        edit_multi_isp_wxw(browser, name='isp204', newname='newisp204', newdesc='newmiaoshu')

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_multi_isp_byname(browser, name='newisp204')

        try:
            assert "修改ISP对象成功" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "修改ISP对象成功" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])