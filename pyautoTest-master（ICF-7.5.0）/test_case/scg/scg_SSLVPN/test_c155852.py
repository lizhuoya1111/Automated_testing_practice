
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

test_id = "155852"
# SSLVPN-安全站点-列表-增加
# 正确配置添加安全站点并保存
# 安全站点列表信息显示正确（索引、站点名称、站点地址、站点端口、真实服务地址、真实服务端口、启用、操作）
def test_c155852(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有安全站点（避免冲突）
        del_all_sslvpn_safe_site_lzy(browser)
        # 增加安全站点，输入正确真实服务端口
        add_sslvpn_safe_site_lzy(browser, sitename='lzy', siteip=dev1, siteport='9090', enable='yes',
                                 enable_client_authentication='yes',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                 real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')
        # 获取操作成功信息并返回
        info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info2)
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 获取安全站点总数为1
        num1 = get_count_sslvpn_safe_site_lzy(browser)
        print(num1)

        # 获取安全站点列表信息
        info1 = get_list_info_sslvpn_safe_site_lzy(browser)

        # 还原
        # 删除所有安全站点
        del_all_sslvpn_safe_site_lzy(browser)




        try:
            assert "操作成功" in info2 and "lzy" in info1 and "10.2.2.102" in info1 and "9090" in info1 and "47.93.52.230" in info1 and "80" in info1 and num1 == 1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "操作成功" in info2 and "lzy" in info1 and "10.2.2.102" in info1 and "9090" in info1 and "47.93.52.230" in info1 and "80" in info1 and num1 == 1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





