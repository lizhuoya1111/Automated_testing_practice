import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.scg.scg_def_obj import *


test_id = "143984"


def test_c143984(browser):
	try:
		# 81添加一个子接口，选择ge0/5，id为2
		login_web(browser, url=dev1)
		# 在object中添加两个address group，分别为group1，group2，每个group中又包含group
		add_obj_address_wxw(browser, name='obj_add_source', subnetip='20.1.1.0', subnetmask='24')
		add_obj_address_wxw(browser, name='obj_add_dest', subnetip='13.1.1.0', subnetmask='24')

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_source_p', addr_obj='A:obj_add_source')
		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_dest_p', addr_obj='A:obj_add_dest')

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_source', addr_obj='G:obj_grp_source_p')
		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_dest', addr_obj='G:obj_grp_dest_p')

		# 删除默认ACL
		del_default_acl_group_lzy(browser)
		# 添加ACL
		add_acl_group_complete(browser, name='lzy', enable='yes')
		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
								  s_address_object='G:obj_grp_source', d_address_object='G:obj_grp_dest')

		# PC2添加去往 13.1.1.0的路由、SCG3添加去往PC2的路由
		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 13.1.1.0/24 gw 20.1.1.1')

		ssh_83 = Shell_SSH()
		ssh_83.connect(hostip=dev3)
		ssh_83.execute('en')
		ssh_83.execute('conf t')
		ssh_83.execute('ip route 20.1.1.0/24 gateway 13.1.1.1')

		# 从pc2 ping 83，从pc2 ftp 83
		ssh_pc2.execute('ping 13.1.1.3 -c 10 -i 0.2')
		time.sleep(3)
		pc2to83_ping_info = ssh_pc2.output()
		print(pc2to83_ping_info)
		ssh_pc2.close()
		# print(pc2topc3_ftp_info1)
		# 修改ge0/4为桥模式，将他加入桥接口br_1中，修改acl rule的源接口为br_1，从pc2 ftp pc3

		try:
			assert "ms" in pc2to83_ping_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in pc2to83_ping_info

		del_all_acl_group_wxw(browser)
		del_obj_grp_wxw(browser, name='obj_grp_source')
		del_obj_grp_wxw(browser, name='obj_grp_dest')
		del_all_obj_group_wxw(browser)
		del_all_obj_address_wxw(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=[dev1, dev2, dev3])
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









