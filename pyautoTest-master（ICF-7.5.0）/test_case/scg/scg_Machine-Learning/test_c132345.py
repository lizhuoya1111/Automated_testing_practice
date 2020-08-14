


import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_machine_learning import *

test_id = "132345"
# 1.开启机器学习，按照顺序回放modbus，mms，DNP3
# 2.查看学习到的规则列表排序是否按照发包先后顺序
# 2.学习到列表按照学习先后顺序排序
def test_c132345(browser):
    try:
        login_web(browser, url=dev1)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)
        # 添加组，添加规则
        add_ipv4_aclgroup_lzy(browser, group_name='lzy')
        add_ipv4acl_lzy(browser, aclgroup_name='lzy', icf='yes')

        # 学习时长5分钟，执行开始学习
        start_learning_complete(browser, learntime='5分钟', aotu_deploy='yes', clear_history='yes')
        sleep(10)
        # 重放报文
        icf_replay(pcap_type="9bao")
        sleep(5)
        icf_replay(pcap_type="WhiteList_SIP")
        sleep(5)
        icf_replay(pcap_type="ProtocolAudit_SNMP")
        sleep(5)
        refresh(browser)
        sleep(1)
        end_learning(browser)
        # 获取页面信息
        info1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text
        print(info1)
        info2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[4]').text
        print(info2)
        info3 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[4]').text
        print(info3)
        sleep(1)

        # 还原
        del_all_acl_group_lzy(browser)


        try:
            assert "SNMP" in info1 and "SIP" in info2 and "PROFINET-IO" in info3
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "SNMP" in info1 and "SIP" in info2 and "PROFINET-IO" in info3

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





