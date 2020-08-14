import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_ipv6 import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 141893
def test_c141893(browser):
	try:
		login_web(browser, url=dev1)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2002:48:3434:5689::", ipv6_mask="64",
						 add="no")
		edit_neighbor_discovery_jyl(browser, physical_interface=interface_name_4, retransmission_time="2000",
									base_reachable_time="40000", duolicate_add_retry_count="2", save="yes")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("show ipv6 address interface gigabitethernet "+interface_name_4)
		result1 = a.output()
		a.close()

		edit_neighbor_discovery_jyl(browser, physical_interface=interface_name_4, retransmission_time="1000",
									base_reachable_time="30000", duolicate_add_retry_count="1", save="yes")

		try:
			assert "2002:48:3434:5689::/64" not in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "2002:48:3434:5689::/64" not in result1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
