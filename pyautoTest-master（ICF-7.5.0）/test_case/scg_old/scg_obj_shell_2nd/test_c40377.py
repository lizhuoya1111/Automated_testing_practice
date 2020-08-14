import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_acl import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 40377
# 选择多条用户定义serv,删除,查看log


def test_obj_wxw(browser):

    try:
        login_web(browser, url="10.2.2.82")

        # 删除所有acl组，以防被引用导致的删除失败
        del_all_acl_group_wxw(browser)

        time.sleep(3)
        # 切换到默认frame
        browser.switch_to.default_content()
        # 切换到左侧frame
        browser.switch_to.frame("lefttree")
        # 点击对象
        browser.find_element_by_xpath(对象).click()
        # 点击ipv4
        browser.find_element_by_xpath(IPv4).click()
        # 点击服务
        browser.find_element_by_xpath(服务).click()
        # 点击自定义
        browser.find_element_by_xpath(自定义).click()

        # 先添加再删除
        for i in range(1, 6):
            add_obj_service_major_wxw(browser, name='obj_serv_377_' + str(i), desc='zhe是ge描shu',
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

        del_more_obj_service_wxw(browser, num=5)

        time.sleep(2)

        # 切换到默认frame
        browser.switch_to.default_content()

        get_log(browser, 管理日志)

        browser.switch_to.default_content()

        # 切换到左侧frame
        browser.switch_to.frame("content")

        loginfo = browser.find_element_by_xpath('//*[@id="namearea0"]').text

        try:
            assert "配置服务对象成功，删除内部对象 " in loginfo
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "配置服务对象成功，删除内部对象 " in loginfo

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        # reload(hostip="10.2.2.81")
        print(err)
        rail_fail(test_run_id, test_id)
        # time.sleep(70)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c40377.py"])