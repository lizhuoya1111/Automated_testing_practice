
import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_multi_isp import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141159"

# 验证添加ISP name、description 生效：创建名字为test、description为test的ISP对象
# 该功能可以生效


def test_c141159(browser):

    try:

        login_web(browser, url=dev1)
        # 添加ISP
        add_multi_isp_save_wxw(browser, name='test', desc='test的ISP对象')

        # 获取日志
        log1 = get_log(browser, 管理日志)
        # print(log1)

        # 删除ISP
        del_multi_isp_wxw(browser, name='test')



        try:
            assert "成功" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "成功" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])