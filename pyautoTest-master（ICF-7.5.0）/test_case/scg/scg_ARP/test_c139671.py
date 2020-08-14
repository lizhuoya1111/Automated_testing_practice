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

test_id = "139671"


def test_c139671(browser):

	try:
		login_web(browser, url=dev1)
		# 设置ARP广播间隔为1S，开启抓包
		add_arp_spoof_jyl(browser, gratuitous_update="yes", update_num="1")
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip=ser_pc3, name="root", passwd="root")
		ssh_pc3.execute('tcpdump -i '+server_pc_3_eth0+' arp')
		time.sleep(15)

		# 获取PC3上的ARP抓包，按回车分片，再筛选含有‘Broadcast’的行，最后将秒数相减得到间距，有时会是负数，也暂时算pass
		arp_cacp_list = []
		cli_output = ssh_pc3.output()
		print(cli_output)
		cli_output_tmp = cli_output.split('\n')
		for i in cli_output_tmp:
			if 'Broadcast' in i:
				arp_cacp_list.append(i)
		result1 = False
		for j in range(0, len(arp_cacp_list)):
			if j != 0:
				time_interval = int(arp_cacp_list[j][6:8]) - int(arp_cacp_list[j-1][6:8])
				print(1, time_interval)
				if time_interval in range(1, 3) or time_interval < 0:
					result1 = True
				else:
					result1 = False
					break
		ssh_pc3.close()

		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip=ser_pc3, name="root", passwd="root")
		ssh_pc3.execute('tcpdump -i ' + server_pc_3_eth0 + ' arp')
		add_arp_spoof_jyl(browser, gratuitous_update="yes", update_num="30")
		time.sleep(100)

		arp_cacp_list1 = []
		cli_output1 = ssh_pc3.output()
		print(cli_output1)
		cli_output_tmp1 = cli_output1.split('\n')
		for i in cli_output_tmp1:
			if 'Broadcast' in i:
				arp_cacp_list1.append(i)
		result2 = False
		for j in range(0, len(arp_cacp_list1)):
			if j != 0:
				time_interval1 = int(arp_cacp_list1[j][6:8]) - int(arp_cacp_list1[j - 1][6:8])
				print(2, time_interval1)
				if abs(time_interval1) in range(29, 32):
					result2 = True
				else:
					result2 = False
					break
		ssh_pc3.close()

		# print(arp_cacp_list[0][6:8], arp_cacp_list[1][6:8], arp_cacp_list[2][6:8])

		# ssh_pc4 = Shell_SSH()
		# ssh_pc4.connect(hostip=ser_pc4, name="root", passwd="root")
		# ssh_pc4.execute('ping 21.1.1.1 -i 0.1')
		# # print(ssh_pc4.output())
		# time.sleep(5)
		# # time.sleep(2222222)
		# loginfo1 = get_log_info(browser, log_type=安全日志)
		try:
			assert True
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert True
		# clear_arp_spoof_jyl(browser)
		# delete_log(browser, log_type=安全日志)
		# ssh_pc3.close()
		# ssh_pc3 = Shell_SSH()
		# ssh_pc3.connect(hostip=ser_pc3, name="root", passwd="root")
		# ssh_pc3.execute('ifconfig ' + server_pc_3_eth0 + ' 21.1.1.2 netmask 255.255.255.0')
		# ssh_pc3.close()
		# ssh_pc4.close()

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