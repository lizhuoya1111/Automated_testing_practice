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
from page_obj.scg.scg_def_acl import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144051"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143951(browser):

	try:
		login_web(browser, url=dev1)
		# 添加一个zone对象，名称为“哈哈哈哈哈哈哈”，成员为ge0/4，ge0/5
		add_obj_zone(browser, name="哈哈哈哈哈哈哈", zone_mem=[interface_name_4, interface_name_5])
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		# 添加规则
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface="Z:哈哈哈哈哈哈哈",
						source_address_object='no',
						dest_address_object='no', accept='yes', drop='no')
		move_ipc4_acl_group_simple(browser, group_id=2, move="up")

		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip="10.1.1.212", name="root", passwd="root", po=22)
		ssh_pc3.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')

		# ssh_pc2.execute('ping 21.1.1.2 -c 2 -i 0.2')
		# time.sleep(2)
		pc2topc3_ping_info = ssh_pc2.output()
		# print(pc2topc3_ping_info)

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(9)
		pc2topc3_ftp_info = ssh_pc2.output()
		# print(pc2topc3_ftp_info)

		ssh_pc2.execute('route del -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3.execute('route del -net 20.1.1.0/24 gw 21.1.1.1')
		ssh_pc2.close()
		ssh_pc3.close()


		try:
			# assert "ttl" in pc2topc3_ping_info
			assert "230 Login successful." in pc2topc3_ftp_info
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			# assert "ttl" in pc2topc3_ping_info
			assert "230 Login successful." in pc2topc3_ftp_info

		del_all_acl_group_lzy(browser)
		del_obj_zone_byname(browser, name="哈哈哈哈哈哈哈")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])