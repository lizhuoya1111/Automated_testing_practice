import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37216
# 添加10条ISP路由条目，点击删除按钮，删除第五条


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        for n in range(1, 11):
            add_multi_isp_save_wxw(browser, name='isp216_'+str(n), desc='miaoshu')
        del_multi_isp_byname(browser, name='isp216_6')

        exist = is_multi_isp_exist_wxw(browser, name='isp216_6')

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        for m in range(1, 6):
            del_multi_isp_byname(browser, name='isp216_'+str(m))
        for m in range(7, 11):
            del_multi_isp_byname(browser, name='isp216_' + str(m))

        try:
            assert exist is False
            assert "删除ISP对象成功" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist is False
            assert "删除ISP对象成功" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])