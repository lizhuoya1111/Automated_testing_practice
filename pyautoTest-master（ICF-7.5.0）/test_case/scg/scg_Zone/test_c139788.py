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

test_id = "139788"


def test_c139788(browser):

	try:
		login_web(browser, url=dev1)
		delete_physical_interface_ip_wxw(browser, interface_name_2, "12.1.1.1")
		delete_physical_interface_ip_wxw(browser, interface_name_4, "20.1.1.1")
		scg = Shell_SSH()
		scg.connect(dev1)
		scg.execute("en")
		scg.execute("conf t")
		scg.execute("inte gigabitethernet "+interface_name_5)
		scg.execute("work-mode route")
		scg.execute("exit")
		scg.close()
		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="22", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="22", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="22", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		add_vlan_inte_add(browser, interface_name_2 + ".22", "12.1.1.1", "255.255.255.0")
		add_vlan_inte_add(browser, interface_name_4+".22", "20.1.1.1", "255.255.255.0")
		add_obj_zone(browser, "t23297", "d", [interface_name_4+".22", interface_name_5+".22", interface_name_3+".22", interface_name_2+".22"])

		# 进入命令行 设备ge0/4为access模式
		# 只修改到这。。。后续拓扑搭建后进行修改
		scg = Shell_SSH()
		scg.connect(dev1)
		scg.execute("en")
		scg.execute("conf t")
		scg.execute("inte gigabitethernet "+interface_name_4)
		scg.execute("switchmode  access")
		scg.execute("exit")
		scg.execute("in gigabitethernet "+interface_name_2)
		scg.execute("sw access")
		scg.close()
		# 删除默认的acl，让流量不通
		del_ipv4_acl_byid(browser, "1", "default")

		login_web(browser, url=dev2)
		add_static_route_single_wxw(browser, "20.1.1.0", "24", interface_name_2, "12.1.1.1", "yes")

		to_ssh = Shell_SSH()
		to_ssh.connect("10.1.1.202", "root", "root")
		to_ssh.execute("route add -net 12.1.1.0/24 gw 20.1.1.1")
		to_ssh.execute("ping 12.1.1.2 -c 2")
		time.sleep(10)
		ssh_info = to_ssh.output()
		# print(ssh_info)
		if "100% packet loss" in ssh_info:
			login_web(browser, url=dev1)
			add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:t23297',
			                          source_address_object='yes', s_address_object='A:any',
			                          d_address_object='A:any', dest_zone_interface=interface_name_2+".22", service='P:any',
			                          schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')
			add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:t23297',
			                          source_address_object='yes', s_address_object='A:any',
			                          d_address_object='A:any', dest_zone_interface='Z:t23297', service='P:any',
			                          schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')
			# set_acl_to_top_byid(browser, "2", "default")
			to_ssh.connect("10.1.1.202", "root", "root")
			to_ssh.execute("ping 12.1.1.2 -c 5")
			time.sleep(2)
			ssh_info1 = to_ssh.output()
			# print(ssh_info1)

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

		del_all_acl_group_wxw(browser)
		# add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:any',
		#                           source_address_object='yes', s_address_object='A:any',
		#                           d_address_object='A:any', dest_zone_interface='Z:any', service='P:any',
		#                           schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')
		del_obj_zone_byname(browser, "t23297")
		del_vlan_inte_all(browser)
		add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip="12.1.1.1", mask="24")
		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip="20.1.1.1", mask="24")
		scg = Shell_SSH()
		scg.connect(dev1)
		scg.execute("en")
		scg.execute("conf t")
		scg.execute("inte gigabitethernet "+interface_name_5)
		scg.execute("work-mode transparent")
		scg.execute("exit")
		scg.close()
		login_web(browser, url=dev2)
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
		reload([dev1, dev2])
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
