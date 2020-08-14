import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141328"
# 输入字符串长度超过256（英文字符）（中文字符一个占三个字符位）
# 英文可以配置成功 中文会产生告警
# ISP 描述


def test_c141328(browser):
    try:
        login_web(browser, url=dev3)
        # 添加ISP 描述 长度超过中文字符
        add_multi_isp_save_wxw(browser, name='lzy', desc='啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不不拜拜便便啛啛喳喳错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错李李李李李')
        # 获取告警信息并接受告警
        alert1 = browser.switch_to_alert().text
        print(alert1)
        browser.switch_to_alert().accept()
        # 添加ISP 描述 长度超过英文字符
        add_multi_isp_save_wxw(browser, name='lzy', desc='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
        # 获取日志
        log1 = get_log(browser, 管理日志)

        # 还原
        del_all_multi_isp_wxw(browser)


        try:
            assert "描述格式输入错误" in alert1 and "李" not in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "描述格式输入错误" in alert1 and "李" not in log1
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev3)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])