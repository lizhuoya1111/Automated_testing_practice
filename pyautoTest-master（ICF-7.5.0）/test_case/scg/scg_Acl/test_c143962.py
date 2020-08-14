import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "143962"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143962(browser):

	try:
		login_web(browser, url=dev1)

		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip="10.1.1.212", name="root", passwd="root", po=22)
		ssh_pc3.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')
		ssh_pc3.execute('echo arsenal > test')

		ssh_pc2.execute('ping 21.1.1.2 -c 3 -i 0.2')
		time.sleep(2)
		pc2topc3_ping_info = ssh_pc2.output()
		# print(pc2topc3_ping_info)

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(5)
		ssh_pc2.execute('get test')
		time.sleep(1)
		pc2topc3_ftp_info = ssh_pc2.output()
		ssh_pc2.execute('exit')
		time.sleep(1)
		# print(pc2topc3_ftp_info)

		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_wxw(browser, name='acl_group')
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group', source_zone_interface="Z:any",
								  source_address_object='yes', s_address_object='A:any',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface="Z:any",
								  service='P:any', schdule='-- 无 --',
								  accept='no', drop='yes',
								  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no')

		ssh_pc2.execute('ping 21.1.1.2 -c 3 -i 0.2')
		time.sleep(8)
		pc2topc3_ping_info_2nd = ssh_pc2.output()
		# print(pc2topc3_ping_info_2nd)

		ssh_pc2.execute('route del -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3.execute('route del -net 20.1.1.0/24 gw 21.1.1.1')
		ssh_pc3.execute('rm -rf test')
		ssh_pc2.close()
		ssh_pc3.close()


		try:
			assert "ttl" in pc2topc3_ping_info
			assert "226 Transfer complete" in pc2topc3_ftp_info
			assert "100% packet loss" in pc2topc3_ping_info_2nd
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in pc2topc3_ping_info
			assert "226 Transfer complete" in pc2topc3_ftp_info
			assert "100% packet loss" in pc2topc3_ping_info_2nd

		del_all_acl_group_wxw(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])