import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_policy_route import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37679
# ADRT_MODIFY_GW_GROUP_SUCCESS


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.81")

		add_multi_gateway_group_wxw(browser, name='mgg_679', group="1(GROUP_1)", modify='yes/no', alias='',
									device='ge0/1', gateway='192.168.1.81', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		edit_multi_gateway_group_wxw(browser, name='mgg_679', group="1(GROUP_1)", modify='yes/no', alias='',
									 device='ge0/1', gateway='192.168.1.18', ping_server='192.168.1.18', ping='yes',
									 arp='no',
									 time_switch='17', ub="50000", db="50000")

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		del_multi_gateway_group_byname(browser, name='mgg_679')

		try:
			assert "修改网关组对象成功"in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "修改网关组对象成功" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])