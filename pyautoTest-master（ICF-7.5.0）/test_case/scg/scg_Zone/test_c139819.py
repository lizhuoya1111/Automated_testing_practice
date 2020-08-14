import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139819"
# 检查zone name是否支持除< > ” ’ & \ ? $ #? 9个之外的所有字符

def test_c139819(browser):
    try:
        login_web(browser, url=dev1)

        # 添加zone name为lzy 检查description是否支持| ; #, $
        add_obj_zone(browser, "啊啊啊aaa111@",
                     "啊啊啊aaa111@/{}",
                     [interface_name_5, interface_name_6])
        sleep(1)
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 还原 //*[@id="layui-layer1"]/div[2]
        del_obj_zone_byname(browser, name='啊啊啊aaa111@/{}')


        try:
            assert '操作成功' in info1
            rail_pass(test_run_id, test_id)
        except Exception as err1:
            print(err1)
            rail_fail(test_run_id, test_id)
            assert '操作成功' in info1
    except Exception as err:
        # 如果上面的步骤有报错，重启设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + test_id + ".py"])