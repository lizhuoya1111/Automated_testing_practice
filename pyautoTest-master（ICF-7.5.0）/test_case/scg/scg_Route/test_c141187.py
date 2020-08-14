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

test_id = "141187"
# Route maitance group gateway 功能 14
# gateway group引用link server 为相同的 ip或者域名；引用相同的outdevice的不同ip作为网关
# 可以正常判断server 状态，并且影响被引用的路由


def test_141187(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(4, 6):

			add_multi_gateway_group_wxw(browser, name='mgg_187_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_3, gateway='34.1.1.'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		status1 = get_multi_gateway_status_gateway_wxw(browser, name='mgg_187_4')
		# print(status1)

		add_static_route_multi_gateway_wxw(browser, ip='24.1.1.0', mask='24', gateway_grp='1(GROUP_1)', num=4,
										   grp_mem=["主用", "备份1"], enable="yes",
										   save='yes', cancel='no')

		gateway1 = get_static_route_gateway_wxw(browser, destination='24.1.1.0/255.255.255.0')
		# print(gateway1)

		edit_multi_gateway_group_wxw(browser, name='mgg_187_4', group="1(GROUP_1)", modify='yes/no', alias='',
									 device=interface_name_3, gateway='34.1.1.4', ping_server='144.1.1.4', ping='yes/no',
									 arp='yes/no',
									 time_switch='7', ub="100000", db="100000")

		time.sleep(5)

		gateway2 = get_static_route_gateway_wxw(browser, destination='24.1.1.0/255.255.255.0')
		# print(gateway2)

		status2 = get_multi_gateway_status_gateway_wxw(browser, name='mgg_187_4')
		# print(status2)

		del_ipv4_static_route_bydestination(browser, destination='24.1.1.0/255.255.255.0')

		del_multi_gateway_group_all(browser)

		try:
			assert "34.1.1.4:alive:active" in gateway1
			assert "34.1.1.4:unreachable:active"in gateway2
			assert "up"in status1
			assert "down"in status2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "34.1.1.4:alive:active" in gateway1
			assert "34.1.1.4:unreachable:active" in gateway2
			assert "up" in status1
			assert "down" in status2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])