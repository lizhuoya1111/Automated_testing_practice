
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

test_id = "132338"
# 1.自管理设备正常启动，并且以admin登录
#   学习时长下拉菜单固定配置:5min，30min，1h，2h，10h，16h，1D,3D,1W，2W,1M,3M
# 2.开始时间设置为系统时间之后 设置学习时长为 5m ，执行开始学习。
# 3.检查学习时长是否为5分钟，等待5分钟结束后是否停止学习---学习时长为5分钟，时间结束后学习停止，学习时长同配置相同
# 4.开始时间设置为系统时间之后 设置学习时长分别为 1小时，1天 ，一周，执行开始学习。检查学习时长是否同配置相同----------未完成
# 5.学习时长下拉菜单固定配置:5min，30min，1h，2h，10h，16h，1D,3D,1W 2W,1M,3M---学习时长下拉菜单显示正确
def test_c132338(browser):
    try:
        login_web(browser, url=dev1)
        # 进入到机器学习界面
        get_into_machinelearning(browser)
        # 获取学习时长下拉菜单
        learntime = get_learntime_menu(browser)
        # 设置学习时长为 5m ，执行开始学习
        start_learning(browser, learntime='5分钟')
        sleep(20)
        # 获取‘剩余学习时间’
        info1 = browser.find_element_by_xpath('//*[@id="timers"]').text
        print(info1)
        # 停止学习
        end_learning(browser)



        try:
            assert "5分钟" in learntime and "3个月" in learntime and '剩余学习时间：0: 04' in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "5分钟" in learntime and "3个月" in learntime and '剩余学习时间：0: 04' in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





