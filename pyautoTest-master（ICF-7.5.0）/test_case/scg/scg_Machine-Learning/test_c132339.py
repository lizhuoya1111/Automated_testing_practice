
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

test_id = "132339"

# 1.开始学习
# 3.开始学习后检查 ，SSH登录设备输入：show icf deeplearning 查看status
#
# 3.显示status:start
def test_c132339(browser):
    try:
        login_web(browser, url=dev1)
        # 进入到机器学习界面 开始机器学习
        start_learning(browser, learntime='5分钟')
        sleep(10)
        # 查看命令行
        ssh = Shell_SSH()
        ssh.connect(hostip=dev1)
        ssh.execute('en')
        ssh.execute('show icf deeplearning')
        t1 = ssh.output()
        print(t1)
        time.sleep(2)
        ssh.close()
        # 停止学习
        end_learning(browser)



        try:
            assert "status:start" in t1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "status:start" in t1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





