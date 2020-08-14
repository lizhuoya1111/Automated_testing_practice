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

test_id = "139661"


def test_c139661(browser):

	try:
		login_web(browser, url=dev1)
		add_ipmac_list(browser, ipadd="24.1.1.4", inteface=interface_name_3, mac="00:16:31:E5:7A:88")
		ip_mac_set(browser, interface_name_3, "no", "no")
		ping = Shell_SSH()
		ping.connect("10.2.2.84")
		ping.execute("en")
		ping.execute("ping 24.1.1.2")
		time.sleep(6)
		ping_info = ping.output()
		print(ping_info)
		try:
			assert "Round-trip" in str(ping_info)
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "Round-trip" in str(ping_info)
		del_ipmac_list(browser, "24.1.1.4", interface_name_3, "00:16:31:E5:7A:88")
		time.sleep(2)
		ip_mac_set(browser, interface_name_3, "no", "yes")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])