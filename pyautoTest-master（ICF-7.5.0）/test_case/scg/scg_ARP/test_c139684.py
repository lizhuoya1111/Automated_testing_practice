import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139684"

def test_c139684(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(3)
		a.execute("exit")
		a.close()
		result1 = a.output()
		print(result1)

		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_3, source_mac_binding="enable",
									 policy_for_undefined_host="block")
		add_ip_mac_binding_jyl(browser, ip="13.1.1.3", interface=interface_name_3, mac_add="auto_mac",
							   host_name="manual_host", host="主机83")
		edit_ip_mac_banding_jyl(browser, banding_ip="13.1.1.3", ip="13.1.1.3", interface=interface_name_3,
								mac_add="manual_mac", mac="00:16:89:ee:03:69")

		del_dynamic_arp(browser, index_list="all")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(3)
		a.execute("exit")
		a.close()
		result2 = a.output()
		print(result2)

		edit_ip_mac_banding_jyl(browser, banding_ip="13.1.1.3", ip="13.1.1.3", interface=interface_name_3,
								mac_add="manual_mac", mac="00:16:31:ee:03:23")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(3)
		a.execute("exit")
		a.close()
		result3 = a.output()
		print(result3)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("ip address 13.1.1.5 24")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		time.sleep(3)
		a.execute("exit")
		a.close()
		result4 = a.output()
		print(result4)

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.5")
		a.execute("ip address 13.1.1.3 24")
		a.close()

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.close()
		del_bindinglist(browser, index_list="all")
		del_static_arp(browser, index_list="all")
		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_3, source_mac_binding="disenable",
									 policy_for_undefined_host="allow")
		try:
			assert "ms" in result1
			assert "Unreachable" in result2
			assert "ms" in result3
			assert "Unreachable" in result4
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "ms" in result1
			assert "Unreachable" in result2
			assert "ms" in result3
			assert "Unreachable" in result4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])