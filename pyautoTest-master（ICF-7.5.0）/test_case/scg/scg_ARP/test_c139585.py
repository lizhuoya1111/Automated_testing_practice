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

test_id = "139585"


def test_c139585(browser):

	try:
		mac1 = get_linux_host_mac_jyl(host_name="10.1.1.202", user="root", password="root", ip_add="20.1.1.2").lower()
		shell_cmd = Shell_SSH()
		shell_cmd.connect(hostip="10.1.1.202", name="root", passwd="root")
		shell_cmd.ping(ipadd="20.1.1.1")
		shell_cmd.close()
		login_web(browser, url=dev1)
		arp_list = get_dynamic_arp_all(browser)
		# print(arp_list)
		try:
			assert ['20.1.1.2', mac1, interface_name_4, ''] in arp_list
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert ['20.1.1.2', mac1, interface_name_4, ''] in arp_list


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		# reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])