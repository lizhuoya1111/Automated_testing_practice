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

test_id = "143966"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143966(browser):

	try:
		login_web(browser, url=dev1)

		del_br_addr(browser, br_name="br_0", ipadd="21.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")

		transparent_interface_change_physics_interface_lzy(browser, intefacex=interface_name_5)

		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="2", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="2", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_4 + ".2", ipadd="20.1.1.1", mask="24")
		add_vlan_inte_add(browser, interface_name=interface_name_5 + ".2", ipadd="21.1.1.1", mask="24")

		ssh_81 = Shell_SSH()
		ssh_81.connect(hostip=dev1)
		ssh_81.execute("en")
		ssh_81.execute("conf t")
		ssh_81.execute("inte gigabitethernet "+interface_name_4)
		ssh_81.execute("switchmode access")
		ssh_81.execute("exit")
		ssh_81.execute("inte gigabitethernet "+interface_name_5)
		ssh_81.execute("switchmode access")
		ssh_81.execute("exit")
		ssh_81.close()

		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_wxw(browser, name='acl_group')
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group', source_zone_interface=interface_name_4 + ".2",
								  source_address_object='yes', s_address_object='A:any',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface="Z:any",
								  service='P:FTP', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no')
		# time.sleep(600)
		ssh_pc2 = Shell_SSH()
		ssh_pc2.connect(hostip="10.1.1.202", name="root", passwd="root", po=22)
		ssh_pc2.execute('route add -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3 = Shell_SSH()
		ssh_pc3.connect(hostip="10.1.1.212", name="root", passwd="root", po=22)
		ssh_pc3.execute('route add -net 20.1.1.0/24 gw 21.1.1.1')

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(3)
		ssh_pc2.execute('root')
		time.sleep(8)
		pc2topc3_ftp_info = ssh_pc2.output()
		ssh_pc2.execute('exit')
		# print('pc2topc3_ftp_info\n', pc2topc3_ftp_info)

		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_wxw(browser, name='acl_group')
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group', source_zone_interface=interface_name_4 + ".2",
								  source_address_object='yes', s_address_object='A:any',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface="Z:any",
								  service='P:FTP', schdule='-- 无 --',
								  accept='no', drop='yes',
								  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no')

		ssh_pc2.execute('ftp 21.1.1.2')
		time.sleep(1)
		ssh_pc2.execute('root')
		time.sleep(3)
		ssh_pc2.execute('root')
		time.sleep(8)
		pc2topc3_ftp_info_2nd = ssh_pc2.output()
		ssh_pc2.execute('exit')
		# print('pc2topc3_ftp_info_2nd\n', pc2topc3_ftp_info_2nd)

		ssh_81 = Shell_SSH()
		ssh_81.connect(hostip=dev1)
		ssh_81.execute("en")
		ssh_81.execute("conf t")
		ssh_81.execute("inte gigabitethernet "+interface_name_4)
		ssh_81.execute("switchmode trunk")
		ssh_81.execute("exit")
		ssh_81.execute("inte gigabitethernet "+interface_name_5)
		ssh_81.execute("switchmode trunk")
		ssh_81.execute("exit")
		ssh_81.close()

		try:
			assert "230 Login successful." in pc2topc3_ftp_info
			assert "230 Login successful." not in pc2topc3_ftp_info_2nd
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "230 Login successful." in pc2topc3_ftp_info
			assert "230 Login successful." not in pc2topc3_ftp_info_2nd

		del_all_acl_group_wxw(browser)
		del_vlan_inte_all(browser)
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_5)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		bridge_ip_add(browser, bridge_interface="br_0", address_mode="manual", ip="21.1.1.1", mask="24")

		ssh_pc2.execute('exit')
		ssh_pc2.execute('route del -net 21.1.1.0/24 gw 20.1.1.1')
		ssh_pc3.execute('route del -net 20.1.1.0/24 gw 21.1.1.1')
		ssh_pc2.close()
		ssh_pc3.close()

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1, switch="重启")
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])