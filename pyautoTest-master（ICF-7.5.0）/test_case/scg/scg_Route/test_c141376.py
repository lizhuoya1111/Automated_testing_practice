import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_dev import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141376"

# ISP name中输入超过32个字符；description超过100个字符
# 无法配置成功，系统报错
# name输入本身有限制 description最大长度改为256 且英文输入有限制 中文有错误提示


def test_c141376(browser):
    try:
        login_web(browser, url=dev1)
        # 添加ISP路由
        add_multi_isp_save_wxw(browser, name='aaaaaaaaaabbbbbbbbbbccccccccccddddd', desc='啦啦啦啦啦啦啦啦绿绿绿绿啦啦啦啦啦啦啦啦绿绿啦啦啦啦啦啦啦啦绿绿啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿啦啦啦啦啦啦啦啦绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿李李李')
        # 获取告警信息 并接受告警
        alert1 = browser.switch_to_alert().text
        print(alert1)
        browser.switch_to_alert().accept()

        try:
            assert "描述格式输入错误" in alert1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "描述格式输入错误" in alert1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])