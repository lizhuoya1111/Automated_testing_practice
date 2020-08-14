import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_policy_route import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141484"
# ADRT_ADD_GW_GROUP_SUCCESS


def test_c141484(browser):

	try:
		login_web(browser, url=dev1)

		add_multi_gateway_group_wxw(browser, name='mgg_674', group="1(GROUP_1)", modify='yes/no', alias='',
									device=interface_name_1, gateway='192.168.1.81', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")


		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		del_multi_gateway_group_all(browser)

		try:
			assert "添加网关对象到网关组成功"in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "添加网关对象到网关组成功" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])