
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

test_id = "132349"
# 1.DPI启动正常
# 2.一台设备GOOSE协议学习到很多规则
# 1.查看规则是否按照学习时间先后顺序排序
# 1.学习到的规则按照先后正确顺序
def test_c132349(browser):
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
        icf_replay(pcap_type="ProtocolAudit_S7")
        sleep(5)
        # 进入机器学习界面，结束学习
        into_fun(browser, 安全事件)
        end_learning(browser)
        # 获取页面信息
        info1 = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[4]').text
        print(info1)
        sleep(1)
        # 比较规则详情中第一条和最后一条的时间 返回True
        a = compare_rules_time_machine_learning(browser, protocol_name='S7')
        print(a)

        # 还原
        del_all_acl_group_lzy(browser)


        try:
            assert "S7" in info1 and a == True
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "S7" in info1 and a == True

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        # reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





