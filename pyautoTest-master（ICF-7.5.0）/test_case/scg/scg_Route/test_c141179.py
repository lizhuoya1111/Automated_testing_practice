import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *
from page_obj.scg.scg_dev import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141179"
# Route maitance group gateway 功能 6
# 配置一个8网关的group
# 引用该group的路由条目可以正常使用，通信正常


def test_141179(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(4, 12):

			add_multi_gateway_group_wxw(browser, name='mgg_179_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_3, gateway='34.1.1.'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		add_static_route_multi_gateway_wxw(browser, ip='24.1.1.0', mask='24', gateway_grp='1(GROUP_1)', num=2,
										   grp_mem=["主用", "备份1"], enable="yes",
										   save='yes', cancel='no')
		# 在82上加去往83的路由
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 34.1.1.0/24 gateway 24.1.1.4")
		a.execute("exit")
		a.execute("exit")

		# 83ping82
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 24.1.1.4")
		time.sleep(5)
		result = a.output()
		# print(result)

		del_ipv4_static_route_bydestination(browser, destination='24.1.1.0/255.255.255.0')

		# 83ping82
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 24.1.1.4")
		time.sleep(5)
		result1 = a.output()
		# print(result1)

		del_multi_gateway_group_all(browser)

		# 给82删路由
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 34.1.1.0/24 gateway 24.1.1.4")
		a.execute("exit")

		try:
			assert "ms" in result
			assert "Destination Host Unreachable"in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result
			assert "Destination Host Unreachable" in result1


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev2, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])