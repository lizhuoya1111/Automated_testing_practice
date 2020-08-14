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

test_id = "141349"
# 网关组16个已满的情况下，添加或者导入新的网关组
# 无法配置成功，系统报错
def test_c141349(browser):

    try:
        # 81 上获取多网关组下拉列表
        login_web(browser, url=dev1)
        into_fun(browser, 多网关组)
        # 点击添加
        browser.find_element_by_xpath('//*[@id="button_area"]/div/input').click()
        # 获取多网关组列表
        s1 = browser.find_element_by_xpath('//*[@id="gateway_group"]')
        option_list1 = s1.find_elements_by_tag_name('option')
        for option1 in option_list1:
            info1 = option1.get_attribute('value')
            print('%s'%(info1))





        try:
            assert "16" in info1 and '17' not in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "16" in info1 and '17' not in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])