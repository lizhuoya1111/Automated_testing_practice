
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

test_id = "141160"

# 导入ip文件到指定的ISP里:导入目的为2.2.2.0/24的目的ip文件（UI、shell
# ip可以正常导入到指定ISP里，并正确显示


def test_c141160(browser):

    try:

        login_web(browser, url=dev1)
        # 添加ISP
        add_multi_isp_save_wxw(browser, name='lzy')

        # 导入IP
        import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='141160.txt')

        # 获取日志
        log1 = get_log(browser, 管理日志)

        # 删除ISP
        del_multi_isp_wxw(browser, name='lzy')



        try:
            assert "成功导入归属IP文件" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "成功导入归属IP文件" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])