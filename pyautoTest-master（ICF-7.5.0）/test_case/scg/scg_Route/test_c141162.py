
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

test_id = "141162"

# 验证在指定的ISP条目里添加路由功能，路由里选取单网关：
# 可以正常添加路由，并且数据匹配该路由走正确的网关

def test_c141162(browser):

    try:

        login_web(browser, url=dev1)
        # 81上添加ISP
        add_multi_isp_save_wxw(browser, name='lzy')

        # 导入IP (目的网段）
        import_ip_config_file_wxw(browser, name='lzy', save='yes', cancel='no', file='34.1.1.0.txt')

        # 添加路由
        add_isp_route_lzy(browser, name='lzy', single_gateway='yes', device=interface_name_3, gateway='13.1.1.3',
                          multi_gateway='no', enable='yes', disable='no')

        # 84上添加到13.1.1.0网段路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()

        # 81 ping 84
        result1 = diag_ping(browser, ipadd="34.1.1.4", packersize="100", count="5", ping_wait_time="2",
                            interface=interface_name_3)
        # print(result1)

        # 删除ISP
        del_multi_isp_wxw(browser, name='lzy')
        # 84上删除到13.1.1.0网段路由
        shell_84 = Shell_SSH()
        shell_84.connect(hostip=dev4)
        shell_84.execute("en")
        shell_84.execute("conf t")
        shell_84.execute("no ip route 13.1.1.0/24 gateway 34.1.1.3")
        shell_84.close()



        try:
            assert "ms" in result1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ms" in result1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=[dev1, dev4])
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])