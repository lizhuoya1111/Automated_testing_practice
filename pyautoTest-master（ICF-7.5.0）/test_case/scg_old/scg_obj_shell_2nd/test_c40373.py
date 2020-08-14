import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40373
# 添加一个serv obj,在ACL中引用,验证serv obj中R是否有显示


def test_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.81")

        add_obj_service_wxw(browser, name='obj_serv_373', desc='zhe是ge描shu',
                            # tcp端口范围：(0-65535)； udp端口范围：(0-65535)；
                            # icmp(echo-reply;pong;destination-unreachable;network-unreachable;host-unreachable;protocol-unreachable;port-unreachable;
                            #      fragmentation-needed;source-route-failed;network-unknown;host-unknown;network-prohibited;host-prohibited;TOS-network-unreachable;
                            #      TOS-host-unreachable;communication;host-precedence-violation;precedence-cutoff;source-quench;redirect;network-redirect;host-redirect;
                            #      TOS-network-redirect;TOS-host-redirect;echo-request;ping;router-advertisement;router-solicitation;time-exceeded;ttl-exceeded;
                            #      ttl-zero-during-transit;ttl-zero-during-reassembly;parameter-problem;ip-header-bad;required-option-missing;timestamp-request;timestamp-reply;
                            #      address-mask-request)；
                            # ip协议号（0-255）
                            tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
                            udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
                            icmp='', item='ping',
                            ip='', number='85')

        time.sleep(2)
        acl_ref_service_obj_wxw(browser, gname='aclgroup_s373', service_obj='C:obj_serv_373')

        get_service_obj_ref_wxw(browser, name='obj_serv_373')

        # 获取引用
        ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

        try:
            assert ref == "acl-group"
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert ref == "acl-group"

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        time.sleep(70)
        assert False



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40373.py"])