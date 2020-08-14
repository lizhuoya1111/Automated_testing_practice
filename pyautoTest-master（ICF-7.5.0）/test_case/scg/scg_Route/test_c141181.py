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

test_id = "141181"
# Route maitance group gateway 功能 8
# 在一个网关组里删除已添加好的网关


def test_141181(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(1, 3):

			add_multi_gateway_group_wxw(browser, name='mgg_181_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_3, gateway='34.1.1.1'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")


		del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

		del_multi_gateway_group_all(browser)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		try:
			assert "从网关组删除网关对象成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "从网关组删除网关对象成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])