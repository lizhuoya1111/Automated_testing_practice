import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def import *


test_id = "141870"




def test_c141870(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")

		change_physical_interface_workmode_wxw(browser, interface=interface_name_3,
		                                       route="no", trans='yes')
		bridge_add_jyl(browser, bridge_name="br_2")
		bri_edit_interface(browser, interface=interface_name_3, bridge_interface="br_2")
		bridge_ip_add(browser, bridge_interface="br_2", ip="13.1.1.1", mask="24")

		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="11", work_mode="route")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		add_vlan_inte_add(browser, interface_name=interface_name_2 + ".11", ipadd="12.1.1.1", mask="24")

		add_multi_gateway_group_wxw(browser, name='test1', group="1(GROUP_1)", modify='no',
		                            device='br_2', gateway='13.1.1.3', ping_server='13.1.1.3', ping='yes',
		                            arp='no')
		add_multi_gateway_group_wxw(browser, name='test2', group="1(GROUP_1)", modify='no',
		                            device=interface_name_2 + ".11", gateway='12.1.1.2', ping_server='12.1.1.2', ping='yes',
		                            arp='no')
		add_static_route_multi_gateway_wxw(browser, ip='172.16.1.0', mask='24', gateway_grp='1(GROUP_1)', grp_mem=["主用", "备份1"],
		                                   save='yes')
		physical_interface_switch(browser, interface=interface_name_3, status="disable")


		# 给82、83的ge0/1添加172.16.1.3的地址，并添加回程路由
		login_web(browser, url=dev2)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_1, ip='172.16.1.3', mask='24')
		add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='12.1.1.1',
		                            enable='yes')
		login_web(browser, url=dev3)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_1, ip='172.16.1.3', mask='24')
		add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='13.1.1.1',
		                            enable='yes')




		# 81的命令行,将2口设备为access模式
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_2)
		shell_81.execute("switchmode  access")
		shell_81.close()

		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route add -net 172.16.1.0/24 gw 20.1.1.1')
		result2 = shell_pc2.execute('ping 172.16.1.3 -c 5 -i 0.5')
		print(result2)
		shell_pc2.close()

		login_web(browser, url=dev1)
		physical_interface_switch(browser, interface=interface_name_2, status="disable")
		physical_interface_switch(browser, interface=interface_name_3, status="enable")

		# 等待接口启用
		time.sleep(8)
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		result4 = shell_pc2.execute('ping 172.16.1.3 -c 20 -i 0.5')
		print(result4)
		result3 = shell_pc2.execute('ping 172.16.1.3 -c 5 -i 0.5')
		print(result3)
		shell_pc2.close()


		try:
			assert "ttl" in result2 and "ttl" in result3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result2 and "ttl" in result3

		physical_interface_switch(browser, interface=interface_name_2, status="enable")
		# time.sleep(800)
		del_ipv4_static_route_bydestination(browser, destination='172.16.1.0/255.255.255.0')
		del_multi_gateway_group_all(browser)
		# 删除子接口
		del_vlan_inte_all(browser)
		# 还原物理接口地址
		delete_bridge(browser)
		change_physical_interface_workmode_wxw(browser, interface=interface_name_3,
		                                       route="yes", trans='no')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_3, ip='13.1.1.1', mask='24')
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.1', mask='24')

		login_web(browser, url=dev2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_1, ip="172.16.1.3")
		# del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

		login_web(browser, url=dev3)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_1, ip="172.16.1.3")
		# del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')


		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_3)
		shell_81.execute("switchmode  trunk")
		shell_81.execute("exit")
		shell_81.execute("inte gigabitethernet " + interface_name_2)
		shell_81.execute("switchmode  trunk")
		shell_81.close()
		# 删除路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("no ip route 20.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()

		shell_83 = Shell_SSH()
		shell_83.connect(hostip=dev3)
		shell_83.execute("en")
		shell_83.execute("conf t")
		shell_83.execute("no ip route 20.1.1.0/24 gateway 13.1.1.1")
		shell_83.close()

		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route del -net 172.16.1.0/24 gw 20.1.1.1')
		shell_pc2.close()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])