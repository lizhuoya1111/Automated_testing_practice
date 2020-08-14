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

test_id = "23172"


def test_c23172(browser):

	try:
		login_web(browser, url='10.2.2.82')
		add_ipmac_list(browser, ipadd="24.1.1.4", inteface="ge0/3", mac="00:16:31:E5:7A:88")
		ip_mac_set(browser, "ge0/3", "yes", "no")
		ping = Shell_SSH()
		ping.connect("10.2.2.84")
		ping.execute("en")
		ping.output()
		ping.execute("ping 24.1.1.2")
		time.sleep(5)
		ping_info1 = ping.output()
		print(ping_info1)
		ping.execute("conf t")
		ping.execute("inte gigabitethernet ge0/3")
		ping.execute("no ip add 24.1.1.4")
		ping.execute("ip add 24.1.1.41 24")
		ping.execute("exit")
		ping.execute("exit")
		ping.output()
		ping.execute("ping 24.1.1.2")
		time.sleep(5)
		ping_info2 = ping.output()
		print(ping_info2)
		try:
			assert "Destination Host Unreachable" in str(ping_info2) and "Destination Host Unreachable" in str(ping_info1)
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "Destination Host Unreachable" in str(ping_info2) and "Destination Host Unreachable" in str(ping_info1)
		del_ipmac_list(browser, "24.1.1.4", "ge0/3", "00:16:31:E5:7A:88")
		time.sleep(2)
		ip_mac_set(browser, "ge0/3", "no", "yes")
		ping.execute("conf t")
		ping.execute("inte gigabitethernet ge0/3")
		ping.execute("no ip add 24.1.1.41")
		ping.execute("ip add 24.1.1.4 24")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])