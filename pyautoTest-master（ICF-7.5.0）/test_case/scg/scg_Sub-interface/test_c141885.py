
import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "141885"

# 本测试用例包含"shell配置与UI配置的对比检查"


def test_c141885(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet P0")
		a.execute("no ip address 13.1.1.1")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="33", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_3+".33", ipadd="13.1.1.1", mask="24")

		login_web(browser, url=dev3)
		# 点击管理员
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet EXT")
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2+".22", ipadd="13.1.1.3", mask="24")

		login_web(browser, url=dev1)
		ping_info = diag_ping(browser, ipadd="13.1.1.3", packersize="100", count="5", ping_wait_time="2",
							  interface=interface_name_3+".33")

		# print(ping_info)
		del_vlan_inte_all(browser)

		login_web(browser, url=dev3)
		del_vlan_inte_all(browser)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet P0")
		a.execute("ip address 13.1.1.1 24")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet EXT")
		a.execute("ip address 13.1.1.3 24")
		a.execute("exit")
		a.close()

		try:
			assert "Destination" in ping_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Destination" in ping_info

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])