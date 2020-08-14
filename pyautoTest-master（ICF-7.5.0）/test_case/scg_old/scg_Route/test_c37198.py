import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37198
# 点击“add”按钮，输入ISP name、Description，点击save


def test_route_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        add_multi_isp_save_wxw(browser, name='isp198', desc='miaoshu')

        exist = is_multi_isp_exist_wxw(browser, name='isp198')
        # print(exist)

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        del_multi_isp_wxw(browser, name='isp198')

        try:
            assert exist is True
            assert "添加ISP对象成功" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert exist is True
            assert "添加ISP对象成功" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        # print(err)
        rail_fail(test_run_id, test_id)
        reload()
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])