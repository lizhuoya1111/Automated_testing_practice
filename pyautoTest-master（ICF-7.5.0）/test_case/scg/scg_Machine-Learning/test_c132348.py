
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

test_id = "132348"
# 1.点击列表“详情”
# 2.查看列表详情内容（序号，规则名，操作码，事件处理，启用状态）
def test_c132348(browser):
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
        # 进入机器学习界面，结束学习
        into_fun(browser, 安全事件)
        end_learning(browser)
        # 获取页面信息

        info1 = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/table/tbody/tr[2]/td[4]').text
        print(info1)
        sleep(1)

        # 点击详情
        browser.find_element_by_xpath('//*[@id="0"]').click()
        sleep(1)
        info2 = browser.find_element_by_xpath('/html/body/div[1]/div[2]/form/div/table/tbody/tr[3]/td/div/table/tbody/tr[2]/td[3]').text
        print(info2)
        # # 输出详情内容
        # info3 = browser.find_element_by_xpath('').text
        # print(info3)



        # 还原
        del_all_acl_group_lzy(browser)


        try:
            assert "PROFINET-IO" in info1 and 'profinetio' in info2
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "PROFINET-IO" in info1 and 'profinetio' in info2

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        reload(hostip=dev1)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





