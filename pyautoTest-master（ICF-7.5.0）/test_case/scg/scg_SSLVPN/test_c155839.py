
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_sslvpn import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "155839"
# SSLVPN-安全站点-增加
# 输入正确站点端口，其余配置均正确，点击保存。
def test_c155839(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有安全站点（避免冲突）
        del_all_sslvpn_safe_site_lzy(browser)
        # 增加安全站点，站点端口为9090
        add_sslvpn_safe_site_complete_lzy(browser, sitename='lzy', siteip=dev1, siteport='9090', enable='yes',
                                 enable_client_authentication='no',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                    real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')

        # 获取安全站点总数为1
        num1 = get_count_sslvpn_safe_site_lzy(browser)
        print(num1)

        # 还原
        # 删除所有安全站点
        del_all_sslvpn_safe_site_lzy(browser)




        try:
            assert num1 == 1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert num1 == 1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





