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

test_id = "141318"
# 单、多网关路由描叙里英文符号中; $ #    //*[@id="box"]/div[3]/ul/li[2]   非法描述字串  //*[@id="link_but"]
# 无法配置成功，系统报错
# 策略路由



def test_c141318(browser):
    try:
        login_web(browser, url=dev1)
        # 添加策略路由单网关  描叙里输入; $ #
        add_policy_route_single_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='255.255.255.0',
								dst_ip='192.168.5.0', dst_mask='255.255.255.0', service='yes', serv='any',
								service_grp='no', serv_grp='H323',
								out_device=interface_name_1, gateway='192.168.1.2', enable='yes',
								disnable='no', desc='; $ #')

        # 获取提示信息 点击返回
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy', group="1(GROUP_1)", modify='no', alias='',
								device=interface_name_1, gateway='192.168.1.2', ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes', arp='no',
								time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_1, gateway='192.168.1.10',
                                    ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes', arp='no',
                                    time_switch='7', ub="100000", db="100000")

        # 添加策略路由 多网关 描叙里输入; $ #
        add_policy_route_multi_wxw(browser, in_device='全部', src_ip='1.1.1.0', src_mask='255.255.255.0',
							   dst_ip='192.168.5.0', dst_mask='255.255.255.0', service='yes', serv='any',
							   service_grp='no', serv_grp='H323',
							   gw_group='1(GROUP_1)',  grp_mem=["主用", "备份1"], enable='yes',
							   disable='no', desc='; $ #', save='yes', cancel='no')

        # 获取提示信息 点击返回
        info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        browser.find_element_by_xpath('//*[@id="link_but"]').click()

        # 删除多网关组
        del_multi_gateway_group_all(browser)


        try:
            assert "非法描述字串" in info1 and "非法描述字串" in info2
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "非法描述字串" in info1 and "非法描述字串" in info2
    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])