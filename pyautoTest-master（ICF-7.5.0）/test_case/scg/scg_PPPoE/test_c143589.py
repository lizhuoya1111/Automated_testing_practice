import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 143589


def test_c143589(browser):

	try:
		login_web(browser, url=dev1)
		# 在81上添加去往188和10的静态路由，删掉指向10.2.2.1的默认路由
		add_static_route_single_wxw(browser, ip='192.168.188.0', mask='24', out_device=interface_name_1,
		                            gateway='10.2.2.1',
		                            enable='yes')
		add_static_route_single_wxw(browser, ip='10.1.1.0', mask='24', out_device=interface_name_1, gateway='10.2.2.1',
		                            enable='yes')
		del_ipv4_static_route_bydestination(browser, destination='0.0.0.0/0.0.0.0')
		connect_pc2 = Shell_SSH()
		connect_pc2.connect(hostip="10.1.1.202", name="root", passwd="root")
		connect_pc2.execute('pppoe-server -I eth5 -L 20.1.1.2 -R 20.1.1.100 -N 10')
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		physics_interface_pppoe_set(browser, physical_interface=interface_name_4, pppoe_uesr="test", pppoe_passwd="test", dns_renew="yes", idle_time="60")
		# 等待一段时间，让PPPOE接口获取到地址，然后去获取PPPOE地址，作为pc2的路由的下一跳使用
		time.sleep(7)
		ppp_info = get_physics_interface_pppoe_station(browser, physical_interface=interface_name_4)
		# print(ppp_info[1])
		# 去查看是否生产了一条默认路由
		default_gw_gw = return_static_route_gateway_by_destination(browser, destination='0.0.0.0/0.0.0.0')
		default_gw_outif = get_static_route_out_device_wxw(browser, destination='0.0.0.0/0.0.0.0')
		if '0.0.0.0' in default_gw_gw and interface_name_4 in default_gw_outif:
			physics_interface_pppoe_action(browser, physical_interface=interface_name_4, action="断开")
		else:
			rail_fail(test_run_id, test_id)
			assert False
		# print(default_gw_gw, default_gw_outif)
		# 给PC2添加去往82的回程路由
		connect_pc2.execute('route add -net 12.1.1.0/24 gw '+ppp_info[1])

		# 82上添加到20.1.1.0网段路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("ip route 20.1.1.0/24 gateway 12.1.1.1")
		login_web(browser, url=dev2)
		# 82 ping PC2
		result1 = diag_ping(browser, ipadd="20.1.1.2", packersize="100", count="5", ping_wait_time="4")
		# print(result1)

		try:
			assert 'ms' not in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert 'ms' not in result1

		login_web(browser, url=dev1)
		shell_82.execute("no ip route 20.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()
		connect_pc2.execute('route del -net 12.1.1.0/24 gw '+ppp_info[1])
		connect_pc2.close()
		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("ip route 0.0.0.0/0 gateway 10.2.2.1")
		shell_81.execute("no ip route 192.168.188.0/24 gateway 10.2.2.1")
		shell_81.execute("no ip route 10.1.1.0/24 gateway 10.2.2.1")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])