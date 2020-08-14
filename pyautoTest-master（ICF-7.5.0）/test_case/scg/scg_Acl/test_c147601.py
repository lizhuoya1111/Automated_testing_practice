import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_physical_interface import *
from page_obj.common.ssh import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_policy_route import *


test_id = "147601"

# 1.添加一个组；
# 2.在“源区域/接口”的下拉框里面选择新建
# 3.新建完成后，是否默认选中该条zone
# 1.能跳转到创建zone的界面；
# 2.是

def test_c147601(browser):
    try:

        login_web(browser, url=dev1)
        # 删除默认ACL
        del_default_acl_group_lzy(browser)
        # 添加ACL组 源接口选择新建zone
        add_acl_group_and_choose_new(browser, name='lzy', enable='yes', snew='yes', szonename='zone1',
                                     szonedesc='新建', szonemember=[interface_name_2, interface_name_3],
                                     dest='Z:any', desc='miaoshu', save='yes')
        sleep(1)
        # 获取日志信息
        log1 = get_log(browser, 管理日志)
        print(log1)

        # 还原--删除ACL
        del_all_acl_group_lzy(browser)
        # 删除zone
        del_obj_zone_byname(browser, name='zone1')


        try:
            assert "区域端口 [zone1]" in log1
            rail_pass(test_run_id, test_id)
        except:
            rail_fail(test_run_id, test_id)
            assert "区域端口 [zone1]" in log1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        print(err)
        rail_fail(test_run_id, test_id)
        reload(dev1)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









