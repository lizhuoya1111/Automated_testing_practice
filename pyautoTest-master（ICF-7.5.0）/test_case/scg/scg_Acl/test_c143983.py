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


test_id = "143983"


def test_c143983(browser):
	try:
		# 81添加一个子接口，选择ge0/5，id为2
		login_web(browser, url=dev1)
		del_br_addr(browser, br_name="br_0", ipadd="21.1.1.1")
		transparent_interface_change_physics_interface_lzy(browser, intefacex=interface_name_5)
		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="2", work_mode="route")
		sleep(2)
		add_vlan_inte_add(browser, interface_name_5+'.2', "21.1.1.1", '255.255.255.0')
		# 子接口转换模式
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet " + interface_name_5)
		a.execute("switchmode access")
		a.close()
		# 添加一个zone，名称为 zone02，包含ge0/4，ge0/5.2
		add_obj_zone(browser, name="zone02", zone_mem=[interface_name_4, interface_name_5+".2"])

		# 删除默认ACL
		del_default_acl_group_lzy(browser)

		# 添加ACL
		add_acl_group_complete(browser, name='lzy', enable='yes')
		# print("111")
		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_4,
								  source_custom='yes', fromip='20.1.1.2', fromnetmask='255.255.255.0',
								  dest_zone_interface='Z:zone02')
		# print("222")
		# 从pc2 ftp pc3
		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip="10.1.1.212", name="root", passwd="root", po=22)
		ssh_pc3.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')

		# ssh_pc2.execute('ping 21.1.1.2 -c 2 -i 0.2')
		# time.sleep(2)
		# pc2topc3_ping_info = ssh_pc2.output()
		# print(pc2topc3_ping_info)

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(9)
		pc2topc3_ftp_info1 = ssh_pc2.output()
		ssh_pc2.close()
		# print(pc2topc3_ftp_info1)
		# 修改ge0/4为桥模式，将他加入桥接口br_1中，修改acl rule的源接口为br_1，从pc2 ftp pc3
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_4)
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface=interface_name_4, bridge_interface="br_1")
		bridge_ip_add(browser, bridge_interface="br_1", ip="20.1.1.1", mask="255.255.255.0")

		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_complete(browser, name='lzy', enable='yes')
		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface="br_1",
								  source_custom='yes', fromip='20.1.1.2', fromnetmask='255.255.255.0',
								  dest_zone_interface='Z:zone02')

		# time.sleep(300)
		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		time.sleep(1)
		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(9)
		pc2topc3_ftp_info2 = ssh_pc2.output()
		# print(pc2topc3_ftp_info2)
		ssh_pc2.close()

		# 修改acl rule的源接口为zone02，其他不变，从pc2 ftp pc3
		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_complete(browser, name='lzy', enable='yes')
		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface="Z:zone02",
								  source_custom='yes', fromip='20.1.1.2', fromnetmask='255.255.255.0',
								  dest_zone_interface='Z:zone02')

		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(9)
		pc2topc3_ftp_info3 = ssh_pc2.output()
		ssh_pc2.close()
		ssh_pc3.close()
		# print(pc2topc3_ftp_info3)

		try:
			assert "230 Login successful." in pc2topc3_ftp_info1 and \
				 	"230 Login successful." in pc2topc3_ftp_info2 and \
					 "230 Login successful." in pc2topc3_ftp_info3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "230 Login successful." in pc2topc3_ftp_info1 and \
				   "230 Login successful." in pc2topc3_ftp_info2 and \
				   "230 Login successful." in pc2topc3_ftp_info3

		del_all_acl_group_wxw(browser)
		del_zone_all_batch(browser)
		delete_bridge_byname(browser, br_name="all")
		del_vlan_inte_all(browser)
		transparent_interface_change_physics_interface_lzy(browser, intefacex=interface_name_4)
		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='255.255.255.0')
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_5)
		bridge_ip_add(browser, bridge_interface="br_0", ip="21.1.1.1", mask="255.255.255.0")


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=[dev1, dev2, dev3])
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









