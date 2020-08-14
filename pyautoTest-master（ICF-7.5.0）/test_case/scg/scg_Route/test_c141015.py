import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141015"
# 对于只有ISP name的 条目，点击条目后面的delete 按钮


def test_c141015(browser):

    try:
        login_web(browser, url=dev1)

        add_multi_isp_save_wxw(browser, name='isp205', desc='miaoshu')

        del_multi_isp_byname(browser, name='isp205')

        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        try:
            assert "删除ISP对象成功"in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "删除ISP对象成功" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])