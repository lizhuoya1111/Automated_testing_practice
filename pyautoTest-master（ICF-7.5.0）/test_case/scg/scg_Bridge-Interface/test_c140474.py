import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = "140474"
def test_c140474(browser):
	try:
		login_web(browser, url=dev4)
		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("exit")
		a.close()
		bridge_add_jyl(browser, bridge_name="br_1")
		b = Shell_SSH()
		b.connect(dev4)
		b.execute("en")
		b.execute("conf t")
		b.execute("access-list group name acl1 5 src-zone br_1")
		b.execute("exit")
		b.close()
		bridge_ip_add(browser, bridge_interface="br_1", address_mode="manual", ip="192.165.12.2", mask="24")
		loginfo1 = get_log(browser, 管理日志)
		delete_bridge_byname(browser, br_name="br_1")
		loginfo2 = get_log(browser, 管理日志)

		a = Shell_SSH()
		a.connect(dev4)
		a.execute("en")
		a.execute("conf t")
		a.execute("no access-list group  name acl1")
		a.execute("exit")
		time.sleep(2)
		delete_bridge_byname(browser, br_name="br_1")
		try:
			assert "成功" in loginfo1
			assert "失败" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "失败" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev4)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
