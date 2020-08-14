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

test_id = "141807"

def test_c141807(browser):
	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2+".22", ipadd="13.1.1.3", mask="24")

		add_static_route_single_wxw(browser, ip='12.1.1.0', mask='24', out_device=interface_name_2+".22", gateway='13.1.1.1',
									enable='yes')

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")
		loginfo1 = get_log_info(browser, 管理日志)

		del_ipv4_static_route_bydestination(browser, destination='12.1.1.0/255.255.255.0')
		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 13.1.1.3 24")
		a.execute("exit")
		a.close()

		try:
			assert "删除 interface失败" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "删除 interface失败" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])