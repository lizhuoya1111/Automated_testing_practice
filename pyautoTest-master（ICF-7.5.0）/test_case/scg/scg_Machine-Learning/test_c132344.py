


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

test_id = "132344"
# 1.机器开始学习 ，回放数据产生一条规则
# 2.点击“刷新” 查看页面右上角 规则总数是否显示1
# 3.再次回放数据 产生1条规则
# 4.点击“刷新”查看页面右上角 规则总数是否增加1
def test_c132344(browser):
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
        # 进入机器学习界面，查看总数为1
        refresh(browser)
        sleep(1)
        num1 = get_rulescount(browser)
        print(num1)
        # 重放报文
        icf_replay(pcap_type="WhiteList_SIP")
        sleep(60)
        # 进入机器学习界面，查看总数为2
        refresh(browser)
        sleep(1)
        num2 = get_rulescount(browser)
        print(num2)
        # 结束学习
        end_learning(browser)

        sleep(1)

        # 还原
        del_all_acl_group_lzy(browser)


        try:
            assert "1" in num1 and "2" in num2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "1" in num1 and "2" in num2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





