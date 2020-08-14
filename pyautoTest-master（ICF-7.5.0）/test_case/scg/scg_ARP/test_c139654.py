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

test_id = "139654"

def test_c139654(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 10.2.2.81 count 10")
		a.execute("exit")
		set_dynamic_arp_to_static_arp_jyl(browser, dynamic_arp_ip="10.2.2.83")
		edit_static_arp_jyl(browser, edit_arp_ip="10.2.2.83", ip="10.2.2.83", interface=interface_name_1,
							mac_add="manual_mac", mac="00:16:31:ee:03:29", host_name="manual_host",
							host="主机83")
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 10.2.2.81")
		a.execute("exit")
		result1 = a.output()
		delete_static_arp_jyl(browser, static_arp_ip="10.2.2.83")

		try:
			assert "ms" not in result1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "ms" not in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])