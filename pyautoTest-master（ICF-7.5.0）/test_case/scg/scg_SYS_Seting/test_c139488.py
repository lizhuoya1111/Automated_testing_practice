import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def import *

test_id = "139488"


# contact栏输入异常!@#/中文/英文/中文/123@111.com/123@111/www.222.com/123456，验证能否提交成功，查看log
# 不能提交
# 输入格式错误，不允许输入 & > < "  ? $ #


def test_c139488(browser):
    try:
        alert_info_list = []
        login_web(browser, url=dev5)
        # 点击管理员
        for x in ['!@#', '!@#中文/英文/中文', 0, 1441, '%@!#']:
            set_ntpservers_interval(browser, interval=str(x))
            alert = browser.switch_to_alert()
            alert_info_list.append(alert.text)
            time.sleep(0.5)
            alert.accept()
        # print(alert_info_list)

        try:
            assert "请输入号码" in alert_info_list or "数字超出允许范围" in alert_info_list
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "输入格式错误" in alert_info_list or "数字超出允许范围" in alert_info_list

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev5)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
