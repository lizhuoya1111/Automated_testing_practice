
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

test_id = "155853"
# SSLVPN-安全站点-列表-增加
# 正确配置添加安全站点并保存
# 安全站点界面右上方总数显示正确，与列表中数目一致
def test_c155853(browser):
    try:
        login_web(browser, url=dev1)
        # 删除所有安全站点（避免冲突）
        del_all_sslvpn_safe_site_lzy(browser)
        # 增加3个安全站点，输入正确真实服务端口
        for x in range(1, 4):
            add_sslvpn_safe_site_lzy(browser, sitename='lzy'+str(x), siteip=dev1, siteport='909'+str(x), enable='yes',
                                 enable_client_authentication='yes',
                                 infomation_transfer='yes/no', client_real_address='yes/no', certificate_DN='yes/no',
                                 real_service_address='47.93.52.230', real_service_port='80',
                                 save='yes', cancel='no')
            sleep(5)
            # 获取操作成功信息并返回
            info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
            print(info1)
            sleep(5)
            browser.find_element_by_xpath('//*[@id="link_but"]').click()
            sleep(0.5)
            sleep(5)
        sleep(5)
        # 获取安全站点列表条目数
        num2 = get_list_num_sslvpn_safe_site_lzy(browser, number='3')
        print(num2)
        sleep(5)

        # 获取安全站点总数
        num1 = get_count_sslvpn_safe_site_lzy(browser)
        print(num1)
        sleep(5)

        # 还原
        # 删除所有安全站点
        del_all_sslvpn_safe_site_lzy(browser)



        try:
            assert num1 == num2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert num1 == num2



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





