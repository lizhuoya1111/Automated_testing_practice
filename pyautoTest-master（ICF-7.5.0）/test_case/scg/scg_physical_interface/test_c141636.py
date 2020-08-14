import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141636
# 接口为路由模式，关闭此接口的Allow Ping功能，检查是否成功；shell下查看是否一致


def test_physical_interface_wxw(browser):

    try:
        login_web(browser, url=dev1)

        open_physical_interface_allowping_wxw(browser, interface=interface_name_4, allow_ping="close")

        # 切换到默认frame
        browser.switch_to.default_content()
        get_log(browser, 管理日志)
        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")
        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text
        # print(loginfo)

        ssh = SSH("10.1.1.202", 'root', 'root', 22)
        ssh.connect()
        result = ssh.execute('ping 20.1.1.1 -c 10 -i 0.1')
        # print(result)
        ssh.close()

        open_physical_interface_allowping_wxw(browser, interface=interface_name_4, allow_ping="open")

        try:
            assert "100% packet loss" in result
            assert "allow ping : no" in loginfo
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "100% packet loss" in result
            assert "allow ping : no" in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])