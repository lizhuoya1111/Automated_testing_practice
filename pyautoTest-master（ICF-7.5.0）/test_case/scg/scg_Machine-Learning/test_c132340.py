
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

test_id = "132340"

# 1.开始机器学习 ，学习时长设置5分钟
# 2.执行停止学习，ssh查看学习状态是否停止
# 3.等待学习时长5分钟结束后 ，ssh查看学习状态是否停止

def test_c132340(browser):
    try:
        login_web(browser, url=dev1)
        # 进入到机器学习界面 开始机器学习
        start_learning(browser, learntime='5分钟')
        sleep(20)
        # 查看命令行--start
        ssh1 = Shell_SSH()
        ssh1.connect(hostip=dev1)
        ssh1.execute('en')
        ssh1.execute('show icf deeplearning')
        t1 = ssh1.output()
        print(t1)
        time.sleep(2)
        ssh1.close()
        # 停止学习
        end_learning(browser)
        sleep(5)
        # 查看命令行--stop
        ssh2 = Shell_SSH()
        ssh2.connect(hostip=dev1)
        ssh2.execute('en')
        ssh2.execute('show icf deeplearning')
        t2 = ssh2.output()
        print(t2)
        time.sleep(2)
        ssh2.close()

        sleep(5)

        # 进入到机器学习界面 开始机器学习
        start_learning(browser, learntime='5分钟')
        sleep(20)
        # 查看命令行--start
        ssh3 = Shell_SSH()
        ssh3.connect(hostip=dev1)
        ssh3.execute('en')
        ssh3.execute('show icf deeplearning')
        t3 = ssh3.output()
        print(t3)
        time.sleep(2)
        ssh3.close()
        # 等待5分钟学习结束
        sleep(300)
        # 查看命令行--stop
        ssh4 = Shell_SSH()
        ssh4.connect(hostip=dev1)
        ssh4.execute('en')
        ssh4.execute('show icf deeplearning')
        t4 = ssh4.output()
        print(t4)
        time.sleep(2)
        ssh4.close()




        try:
            assert "status:start" in t1 and "status:stop" in t2 and "status:start" in t3 and "status:stop" in t4
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "status:start" in t1 and "status:stop" in t2 and "status:start" in t3 and "status:stop" in t4

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





