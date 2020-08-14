
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

test_id = "155921"

# 创建真实服务端口不为HTTP端口
# 其余配置均正确
# 在服务器中访问“站点地址”+“站点端口”
# 不能访问真实服务器
def test_c155921(browser):
    try:
        login_web(browser, url=dev1)
        # 清空安全站点
        del_all_sslvpn_safe_site_lzy(browser)
        sleep(0.5)
        # 增加安全站点
        add_sslvpn_safe_site_complete_lzy(browser, sitename='lzy', siteip=dev1, siteport='9090', enable='yes', enable_client_authentication='no',
								infomation_transfer='no', client_real_address='yes/no', certificate_DN='yes/no',
                              real_service_address='47.93.52.230', real_service_port='801', save='yes', cancel='no')
        sleep(0.5)

        #
        sign_out_jyl(browser)
        get_into_safe_site__lzy(browser, siteip=dev1, siteport='801')
        sleep(0.5)

        # 获取页面信息
        info1 = browser.find_element_by_xpath('//*[@id="main-message"]/h1/span').text
        print(info1)

        # 还原
        sleep(0.5)
        login_web(browser, dev2)
        login_web(browser, dev1)

        # 删除安全站点
        del_all_sslvpn_safe_site_lzy(browser)



        try:
            assert '无法访问此网站' in info1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert '无法访问此网站' in info1



    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





