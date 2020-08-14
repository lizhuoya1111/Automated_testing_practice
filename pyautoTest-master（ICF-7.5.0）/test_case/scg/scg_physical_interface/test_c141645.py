
import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141645

def test_c141645(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("work-mode route")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="33", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="66", work_mode="route")

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("switchmode  trunk")
		a.execute("native-vlan 33")
		a.close()
		loginfo1 = get_log(browser, 管理日志)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("switchmode  trunk")
		a.execute("native-vlan 66")
		a.close()
		loginfo2 = get_log(browser, 管理日志)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_6+".33")
		a.execute("no interface vlan "+interface_name_6+".66")
		a.close()

		try:
			assert "成功" and "vlan id : 33" in loginfo1
			assert "成功" and "vlan id : 66" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" and "vlan id : 33" in loginfo1
			assert "成功" and "vlan id : 66" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])