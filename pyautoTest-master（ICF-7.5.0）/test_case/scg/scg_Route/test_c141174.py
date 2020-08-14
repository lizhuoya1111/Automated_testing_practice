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

test_id = "141174"
# Route maitance group gateway 功能 1
# 填入Group的name
# 成功添加到group里，可被路由成功引用


def test_141174(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(1, 5):

			add_multi_gateway_group_wxw(browser, name='mgg_174_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_3, gateway='34.1.1.1'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)
		add_static_route_multi_gateway_wxw(browser, ip='20.1.1.0', mask='24', gateway_grp='1(GROUP_1)', num=4,
										   grp_mem=["主用", "备份1", "备份2", "不选择"], enable="yes",
										   save='yes', cancel='no')

		loginfo2 = get_log_info(browser, 管理日志)
		# print(loginfo2)

		del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

		del_multi_gateway_group_all(browser)

		try:
			assert "网关包括 [mgg_174_4" in loginfo1
			assert "添加静态路由对象成功" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "网关包括 [mgg_174_4" in loginfo1
			assert "添加静态路由对象成功" in loginfo2


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])