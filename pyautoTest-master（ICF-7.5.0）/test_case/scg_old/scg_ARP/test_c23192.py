import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "23192"


def test_c23192(browser):

	try:
		# 不加任何策略，直连路由能不能通 p1 ms
		login_web(browser, url='10.2.2.84')
		add_static_route_single_wxw(browser, "12.1.1.0", "24", 'ge0/3', "24.1.1.2", "yes")
		login_web(browser, url='10.2.2.81')
		add_static_route_single_wxw(browser, "24.1.1.0", "24", 'ge0/2', "12.1.1.2", "yes")
		ping = Shell_SSH()
		ping.connect("10.2.2.84")
		ping.execute("en")
		ping.output()
		ping.execute("ping 12.1.1.1")
		time.sleep(5)
		ping_info1 = ping.output()
		print("--------------ping1--------------------")
		print(ping_info1)
		# 添加不匹配IPMAC绑定，期望不通 p2 un
		if "ms" in ping_info1:
			login_web(browser, url='10.2.2.82')
			add_ipmac_list(browser, ipadd="24.1.1.4", inteface="ge0/3", mac="00:16:31:E5:7A:88")
			ip_mac_set(browser, "ge0/3", "yes", "yes")
			ping.execute("ping 12.1.1.1")
			time.sleep(8)
			ping_info2 = ping.output()
			print("--------------ping2--------------------")
			print(ping_info2)
			# 将ipmac绑定修改为匹配，期望通 p3 ms
			if "Destination Host Unreachable" in ping_info2:
				del_ipmac_list(browser, ipadd="24.1.1.4", inteface="ge0/3", mac="00:16:31:E5:7A:88")
				add_ipmac_list(browser, ipadd="24.1.1.4", inteface="ge0/3", mac="00:16:31:E5:7A:42")
				ping.execute("ping 12.1.1.1")
				time.sleep(5)
				ping_info3 = ping.output()
				print("--------------ping3--------------------")
				print(ping_info3)
				# 修改84设备的IP，期望可以通 p4 ms
				if "ms" in ping_info3:
					ping.execute("conf t")
					ping.execute("inte gigabitethernet ge0/3")
					ping.execute("no ip add 24.1.1.4")
					ping.execute("ip add 24.1.1.100 24")
					ping.execute("exit")
					ping.execute("exit")
					ping.output()
					ping.execute("ping 12.1.1.1")
					time.sleep(5)
					ping_info4 = ping.output()
					print("--------------ping4--------------------")
					print(ping_info4)
					try:
						assert "ms" in str(ping_info4)
						rail_pass(test_run_id, test_id)

					except Exception as err1:
						print(err1)
						rail_fail(test_run_id, test_id)
						assert "ms" in str(ping_info4)

					del_ipmac_list(browser, "24.1.1.4", "ge0/3", "00:16:31:E5:7A:42")
					time.sleep(2)
					ip_mac_set(browser, "ge0/3", "no", "yes")
					ping.execute("conf t")
					ping.execute("inte gigabitethernet ge0/3")
					ping.execute("no ip add 24.1.1.100")
					ping.execute("ip add 24.1.1.4 24")
					login_web(browser, url='10.2.2.84')
					del_ipv4_static_route_bydestination(browser, "12.1.1.0/255.255.255.0")
					login_web(browser, url='10.2.2.81')
					del_ipv4_static_route_bydestination(browser, "24.1.1.0/255.255.255.0")

			else:
				del_ipmac_list(browser, "24.1.1.4", "ge0/3", "00:16:31:E5:7A:42")
				ip_mac_set(browser, "ge0/3", "no", "yes")
				print("if_2 err")
				rail_fail(test_run_id, test_id)
				reload()
				assert False
		else:
			print("if_1 err")
			rail_fail(test_run_id, test_id)
			reload()
			assert False


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload()
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])