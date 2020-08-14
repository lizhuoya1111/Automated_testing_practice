import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "139411"

# 1.添加32个admin profile，然后再添加32个管理员用户分别引用这32个profile
# 2.反复修改这32个admin profile
# 新增自定义Profile只能新增29个，且被引用的profile不允许修改或删除
def test_c139411(browser):
    try:
        # 添加adminprofile
        scg = Shell_SSH()
        scg.connect(hostip=dev1)
        scg.execute("en")
        scg.execute("con t")
        for x in range(1, 30):
            scg.execute("privilege profile lzy" + str(x))
        time.sleep(1)
        # 添加admin user
        for x in range(1, 30):
            scg.execute("admin user lzy" + str(x) + " privilege lzy" + str(x))
        for x in range(30, 33):
            scg.execute("admin user lzy" + str(x))
        time.sleep(1)
        scg.close()
        # output = scg.output()
        # print(output)


        login_web(browser, url=dev1)
        # 获取adminname
        name1 = get_admin_name(browser)
        print(name1)

        # 还原
        # 删除admin
        scg = Shell_SSH()
        scg.connect(hostip=dev1)
        scg.execute("en")
        scg.execute("con t")
        for x in range(1, 33):
            scg.execute("no admin user lzy" + str(x))
        time.sleep(1)
        # 添加admin profile
        for x in range(1, 30):
            scg.execute("no privilege profile lzy" + str(x))
        time.sleep(1)
        scg.close()
        # output = scg.output()
        # print(output)


        try:
            assert "lzy1" in name1
            rail_pass(test_run_id, test_id)

        except:
            rail_fail(test_run_id, test_id)
            assert "lzy1" in name1

    except Exception as err:
        # 如果上面的步骤有报错，重新设备，恢复配置
        reload(hostip=dev1)
        print(err)
        rail_fail(test_run_id, test_id)
        assert False


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])







