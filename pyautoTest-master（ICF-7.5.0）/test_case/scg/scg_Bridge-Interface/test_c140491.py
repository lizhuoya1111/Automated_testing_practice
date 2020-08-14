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


test_id = 140491
def test_c140491(browser):
	try:
		login_web(browser, url=dev1)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="33", work_mode="transparent")

		bridge_add_jyl(browser, bridge_name="br_1")

		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2)
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3+".33")

		loginfo1 = get_log_info(browser, 管理日志)
		print(loginfo1)

		delete_bridge_byname(browser, br_name="br_1")

		bridge_add_jyl(browser, bridge_name="br_1")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("work-mode route")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="transparent")

		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2+".22")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3+".33")

		loginfo2 = get_log_info(browser, 管理日志)
		print(loginfo2)

		delete_bridge_byname(browser, br_name="br_1")

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")
		del_vlan_inte_by_name(browser, interface_name=interface_name_3+".33")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.close()

		time.sleep(0.1)
		try:
			assert "修改 interface失败" in loginfo1
			assert "修改 interface失败" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "修改 interface失败" in loginfo1
			assert "修改 interface失败" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
