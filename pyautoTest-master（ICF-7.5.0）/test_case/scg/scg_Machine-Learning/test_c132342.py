
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "132342"
# 1.设置学习时长“5分钟”，不开启“清除历史记录”开关，开始机器学习  等待5分钟
# 3.设置学习时长“5分钟”，开启“清除历史记录开关”，开始机器学习 等待5分钟
# 1.开启机器学习后，清除历史记录开关自动隐藏 5分钟后，清除历史记录开关自动复现，且开关保持“未开启”状态
# 3.开启机器学习后，清除历史记录开关自动隐藏 5分钟后，清除历史记录开关自动复现，且开关保持“未开启”状态
# 开关自动隐藏未验证
def test_c132342(browser):
    try:
        login_web(browser, url=dev1)
        # 学习时长5分钟，不开启清除历史记录 执行开始学习
        start_learning_complete(browser, learntime='5分钟', aotu_deploy='yes', clear_history='no')
        sleep(5)
        # 等待5分钟
        sleep(300)
        # 5分钟后查看清除历史记录开关 自动复现，且开关保持“未开启”状态
        clear_history2 = browser.find_element_by_xpath('//*[@id="clearhis"]').is_selected()
        print(clear_history2)
        # 学习时长5分钟，开启清除历史记录 执行开始学习
        start_learning_complete(browser, learntime='5分钟', aotu_deploy='yes', clear_history='yes')
        sleep(5)
        # 等待5分钟
        sleep(300)
        # 5分钟后查看清除历史记录开关 自动复现，且开关保持“未开启”状态
        clear_history3 = browser.find_element_by_xpath('//*[@id="clearhis"]').is_selected()
        print(clear_history3)

        try:
            assert clear_history2 == False and clear_history3 == False
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert clear_history2 == False and clear_history3 == False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





