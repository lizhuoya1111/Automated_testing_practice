import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141279"
# 网关输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256
# 无法配置成功，系统报错
# 策略路由单网关


def test_c141279(browser):
    try:
        login_web(browser, url=dev1)
        # 添加策略路由单网关 网关IP A.2.3.155
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='24',
                                                            dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                                            serv='any', out_device=interface_name_1, gateway='A.2.3.155')
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        # 添加策略路由单网关 网关IP #.$.4.5
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='24',
                                    dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                    serv='any', out_device=interface_name_1, gateway='#.$.4.5')
        info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        # 添加策略路由单网关 网关IP 1.1.1.256
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='24',
                                    dst_ip='192.168.5.0', dst_mask='24', service='yes',
                                    serv='any', out_device=interface_name_1, gateway='1.1.1.256')
        info3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text



        try:
            assert "非法IP地址" in info1 and "非法IP地址" in info2 and "非法IP地址" in info3
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "非法IP地址" in info1 and "非法IP地址" in info2 and "非法IP地址" in info3
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])