
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

test_id = "155856"
# SSLVPN-安全站点-列表-增加
# 正确配置添加安全站点并保存
# 点击全选再取消全选
def test_c155856(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有安全站点（避免冲突）
        del_all_sslvpn_safe_site_lzy(browser)
        # 增加多个安全站点
        for x in range(1, 4):
            add_sslvpn_safe_site_complete_lzy(browser, sitename='lzy'+str(x), siteip=dev1, siteport='909'+str(x), enable='yes',
                                 enable_client_authentication='yes',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                 real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')

        # 全选安全站点
        select_or_unselect_all_sslvpn_safe_site_lzy(browser, select='yes')

        # 安全站点是否被全勾选，返回TRUE或者FALSE
        a1 = judge_select_or_unselect_all_sslvpn_safe_site_lzy(browser)

        # 单条安全站点是否被勾选
        a2 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='1')
        a3 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='2')
        a4 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='3')

        # 取消全选
        select_or_unselect_all_sslvpn_safe_site_lzy(browser, select='no')

        # 判断是否取消全选
        b1 = judge_select_or_unselect_all_sslvpn_safe_site_lzy(browser)

        # 单条安全站点是否被勾选
        b2 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='1')
        b3 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='2')
        b4 = judge_select_or_unselect_sslvpn_safe_site_lzy(browser, number='3')

        # 还原
        # 删除所有安全站点
        del_all_sslvpn_safe_site_lzy(browser)


        try:
            assert a1 == a2 == a3 == a4 == True and b1 == b2 == b3 == b4 == False
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert a1 == a2 == a3 == a4 == True and b1 == b2 == b3 == b4 == False



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





