import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_dev import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140961"
# 添加10条路由条目，点击删除按钮，删除第五条


def test_c140961(browser):

    try:

        login_web(browser, url=dev1)

        for n in range(1, 11):

            add_static_route_single_wxw(browser, ip='20.1.'+str(n)+'.0', mask='24', out_device=interface_name_2,
                                        gateway='12.1.1.2', enable='yes')

        del_ipv4_static_route_bydestination(browser, destination='20.1.6.0/255.255.255.0')
        exist = is_static_route_exist_wxw(browser, destination='20.1.6.0/255.255.255.0')
        loginfo = get_log_info(browser, 管理日志)
        # print(loginfo)

        for m in range(1, 6):
            del_ipv4_static_route_bydestination(browser, destination='20.1.' + str(m) + '.0/255.255.255.0')
        for m in range(7, 11):
            del_ipv4_static_route_bydestination(browser, destination='20.1.' + str(m) + '.0/255.255.255.0')

        try:
            assert "删除静态路由对象成功" in loginfo
            assert exist is False
            rail_pass(test_run_id, test_id)
        except:
            rail_pass(test_run_id, test_id)
            assert "删除静态路由对象成功" in loginfo
            assert exist is False

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])