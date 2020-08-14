import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "23311"


def test_c23311(browser):

	try:

		login_web(browser, url='10.2.2.81')
		add_obj_zone(browser, "zone1", "d", ["br_0"])
		add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:zone1',
		                          source_address_object='yes', s_address_object='A:any',
		                          d_address_object='A:any', dest_zone_interface='Z:any', service='P:any',
		                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
		set_acl_to_top_byid(browser, "2", "default")
		# 进入命令行 设备ge0/4为access模式
		# scg = Shell_SSH()
		# scg.connect("10.2.2.81")
		# scg.execute("en")
		# scg.execute("conf t")
		# scg.execute("inte gigabitethernet ge0/4")
		# scg.execute("switchmode  access")
		# scg.execute("exit")
		# scg.execute("exit")
		# to_ssh_202 = Shell_SSH()
		# to_ssh_202.connect("10.1.1.202", "root", "root")
		# to_ssh_202.execute("route add -net 21.1.1.0/24 gw 20.1.1.1")

		to_ssh = Shell_SSH()
		to_ssh.connect("10.1.1.212", "root", "root")
		to_ssh.execute("route add -net 20.1.1.0/24 gw 21.1.1.1")
		to_ssh.execute("ping 20.1.1.1 -c 5 -i 0.1")
		time.sleep(2)
		ssh_info = to_ssh.output()
		print(ssh_info)
		if "ttl" in ssh_info:
			r1 = True
			del_ipv4_acl_byid(browser, "1", "default")
			add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:zone1',
			                          source_address_object='yes', s_address_object='A:any',
			                          d_address_object='A:any', dest_zone_interface='Z:zone1', service='P:any',
			                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
			set_acl_to_top_byid(browser, "2", "default")
			to_ssh.connect("10.1.1.212", "root", "root")
			to_ssh.execute("ping 21.1.1.3 -c 3 -i 0.1")
			time.sleep(9)
			ssh_info1 = to_ssh.output()
			print(ssh_info1)
			if "100% packet loss" in ssh_info1:
				r2 = True

				del_ipv4_acl_byid(browser, "1", "default")
				add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='ge0/5',
				                          source_address_object='yes', s_address_object='A:any',
				                          d_address_object='A:any', dest_zone_interface='ge0/6', service='P:any',
				                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
				set_acl_to_top_byid(browser, "2", "default")
				to_ssh.connect("10.1.1.212", "root", "root")
				to_ssh.execute("ping 21.1.1.3 -c 3 -i 0.1")
				time.sleep(9)
				ssh_info2 = to_ssh.output()
				print(ssh_info2)
				if "100% packet loss" in ssh_info2:
					r3 = True
					try:
						assert r1 is True and r2 is True and r3 is True
						rail_pass(test_run_id, test_id)

					except Exception as err1:
						print(err1)
						rail_fail(test_run_id, test_id)
						assert r1 is True and r2 is True and r3 is True
				else:
					assert False

			else:
				assert False
		else:
			assert False

		del_ipv4_acl_byid(browser, "1", "default")
		del_obj_zone_byname(browser, "zone1")
		to_ssh.execute("route del -net 20.1.1.0/24 gw 21.1.1.1")
		# dhcp_server_edit_or_delete(browser, fuction="delall")
		# login_web(browser, url='10.2.2.84')
		# change_addrmod_physical_inte(browser, "ge0/3", "静态")
		# add_net_ineterface(browser, "24.1.1.4", "255.255.255.0", "ge0/3")

	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
