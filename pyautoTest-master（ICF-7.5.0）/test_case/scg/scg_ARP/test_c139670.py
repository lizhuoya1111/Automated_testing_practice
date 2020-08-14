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

test_id = "139670"


def test_c139670(browser):

	try:
		login_web(browser, url=dev1)
		add_arp_spoof_jyl(browser, arp_reverse="yes")
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip=ser_pc3, name="root", passwd="root")
		ssh_pc3.execute('ifconfig '+server_pc_3_eth0+' 21.1.1.3 netmask 255.255.255.0')
		ssh_pc3.execute('ping 21.1.1.1 -i 0.1')
		# print(ssh_pc3.output())

		ssh_pc4 = Shell_SSH()
		ssh_pc4.connect(hostip=ser_pc4, name="root", passwd="root")
		ssh_pc4.execute('ping 21.1.1.1 -i 0.1')
		# print(ssh_pc4.output())
		time.sleep(5)
		# time.sleep(2222222)
		loginfo1 = get_log_info(browser, log_type=安全日志)
		try:
			assert '附加消息=[ip [21.1.1.3] 的mac异常' in loginfo1
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert '附加消息=[ip [21.1.1.3] 的mac异常' in loginfo1
		clear_arp_spoof_jyl(browser)
		delete_log(browser, log_type=安全日志)
		ssh_pc3.close()
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip=ser_pc3, name="root", passwd="root")
		ssh_pc3.execute('ifconfig ' + server_pc_3_eth0 + ' 21.1.1.2 netmask 255.255.255.0')
		ssh_pc3.close()
		ssh_pc4.close()

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		ssh_pc33 = Shell_SSH()
		ssh_pc33.connect(hostip=ser_pc3, name="root", passwd="root")
		ssh_pc33.execute('reboot')
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])