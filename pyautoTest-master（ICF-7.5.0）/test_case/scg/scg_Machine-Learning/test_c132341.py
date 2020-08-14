
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

test_id = "132341"
# 1.设置开始时间，学习时长，勾选清除历史记录 执行开始学习 ，无流量
# 2.开始学习后, 查看页面变化，是否清除已学习规则列表
# 3.执行停止学习 ，查看已学习列表是否为空
# 2.规则列表被清空
# 3.停止学习后机器学习规则列表仍然为空
def test_c132341(browser):
    try:
        login_web(browser, url=dev1)
        # 进入到机器学习界面,获取页面规则总数
        num11 = get_rulescount(browser)
        num1 = int(num11)
        # 设置开始时间，学习时长，勾选清除历史记录 执行开始学习
        start_learning_complete(browser, learntime='5分钟', aotu_deploy='yes', clear_history='yes')
        sleep(5)
        # 看是学习后，获取页面规则总数
        num22 = get_rulescount(browser)
        num2 = int(num22)
        # 停止学习，获取页面规则总数
        end_learning(browser)
        num33 = get_rulescount(browser)
        num3 = int(num33)



        try:
            assert num1 >= 0 and num2 == 0 and num3 == 0
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert num1 >= 0 and num2 == 0 and num3 == 0

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





