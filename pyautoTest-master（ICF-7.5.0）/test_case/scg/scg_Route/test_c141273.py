import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141273"
# 静态多网关路由配置GW输入异常检测 8
# 网关group里有多网关，所有网关都选择back up（backup1，backupe2）


def test_c141273(browser):

	try:
		login_web(browser, url=dev1)

		for n in range(1, 3):

			add_multi_gateway_group_wxw(browser, name='mgg_463_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_1, gateway='192.168.1.8'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		add_static_route_multi_gateway_wxw(browser, ip='192.168.188.3', mask='32', gateway_grp='1(GROUP_1)',
													   num=4, grp_mem=["备份1", "备份2"], enable="no", save='yes', cancel='no')

		time.sleep(5)
		exist = is_static_route_exist_wxw(browser, destination='192.168.188.3/255.255.255.255')
		# print(exist)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_multi_gateway_group_all(browser)
		del_ipv4_static_route_bydestination(browser, destination='192.168.188.3/255.255.255.255')

		try:
			assert exist is True
			assert "添加静态路由对象成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert exist is True
			assert "添加静态路由对象成功" in loginfo



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])