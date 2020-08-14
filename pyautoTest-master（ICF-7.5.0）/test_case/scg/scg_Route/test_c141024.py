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

test_id = "141024"

# 点击add route，选择multi gw，选择网关group，选择不同的active、backup1、backup2 、not selected
# 操作成功；shell先显示和UI一致；admin log正常
#  添加时显示ISP没有导入IP ISP功能和配置还不了解--20190911


def test_c141024(browser):

    try:
        login_web(browser, url=dev1)

        # 添加多网关组
        add_multi_gateway_group_wxw(browser, name='lzy1', group="1(GROUP_1)", modify='no', alias='',
									device=interface_name_2, gateway='12.1.1.2', ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")
        add_multi_gateway_group_wxw(browser, name='lzy2', group="1(GROUP_1)", modify='no', alias='',
                                    device=interface_name_3, gateway='13.1.1.2',
                                    ping_server='119.75.213.61 [www.baidu.com(China Telecom)]', ping='yes',
                                    arp='no', time_switch='7', ub="100000", db="100000")

        # 添加一条ISP
        add_multi_isp_save_wxw(browser, name='lzy', desc='')

        # 添加ISP路由 多网关
        add_isp_route_lzy(browser, name='lzy', single_gateway='no', device='', gateway='',
                          multi_gateway='yes', gateway_group='1(GROUP_1)', grp_mem=["备份1", "主用"],
                          enable='yes', disable='no')

        # 获取提示信息
        info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
        print(info1)

        # 删除ISP
        del_multi_isp_wxw(browser, name='lzy')


        # 删除多网关组
        del_multi_gateway_group_all(browser)



        try:
            assert "ISP尚未导入IP" in info1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "ISP尚未导入IP" in info1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(hostip=dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])