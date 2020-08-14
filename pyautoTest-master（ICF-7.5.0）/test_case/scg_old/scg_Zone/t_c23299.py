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

test_id = "23299"


def test_c23299(browser):

	try:
		login_web(browser, url='10.2.2.81')
		add_obj_zone(browser, "t23299", "d", ["ge0/4", "ge0/5"])
		add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:t23299',
		                          source_address_object='yes', s_address_object='A:any',
		                          d_address_object='A:any', dest_zone_interface='ge0/2', service='P:any',
		                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
		set_acl_to_top_byid(browser, "2", "default")
		login_web(browser, url='10.2.2.82')
		add_static_route_single_wxw(browser, "20.1.1.0", "24", "ge0/2", "12.1.1.1", "yes")

		to_ssh = Shell_SSH()
		to_ssh.connect("10.1.1.202", "root", "root")
		to_ssh.execute("route add -net 12.1.1.0/24 gw 20.1.1.1")
		to_ssh.execute("ping 12.1.1.2 -c 2")
		time.sleep(10)
		ssh_info = to_ssh.output()
		print(ssh_info)
		if "100% packet loss" in ssh_info:
			login_web(browser, url='10.2.2.81')
			del_ipv4_acl_byid(browser, "1", "default")
			del_obj_zone_byname(browser, "t23299")
			add_obj_zone(browser, "t23299", "d", ["ge0/3", "ge0/5"])
			add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:t23299',
			                          source_address_object='yes', s_address_object='A:any',
			                          d_address_object='A:any', dest_zone_interface='ge0/2', service='P:any',
			                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
			set_acl_to_top_byid(browser, "2", "default")
			to_ssh.connect("10.1.1.202", "root", "root")
			to_ssh.execute("ping 12.1.1.2 -c 3")
			time.sleep(2)
			ssh_info1 = to_ssh.output()
			print(ssh_info1)

			try:
				assert "ttl" in str(ssh_info1)
				rail_pass(test_run_id, test_id)

			except Exception as err1:
				print(err1)
				rail_fail(test_run_id, test_id)
				assert "ttl" in str(ssh_info1)

		else:
			rail_fail(test_run_id, test_id)
			reload()
			assert False

		del_ipv4_acl_byid(browser, "1", "default")
		del_obj_zone_byname(browser, "t23299")
		# add_physical_interface_ip_wxw(browser, interface="ge0/4", ip="20.1.1.1", mask="24")
		login_web(browser, url='10.2.2.82')
		del_ipv4_static_route_bydestination(browser, "20.1.1.0/255.255.255.0")
		to_ssh.execute("route del -net 12.1.1.0/24 gw 20.1.1.1")
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
