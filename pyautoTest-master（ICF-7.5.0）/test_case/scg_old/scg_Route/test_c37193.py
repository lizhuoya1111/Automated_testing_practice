import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37193
# 选择service
# 操作成功；shell先显示和UI一致；admin log正常


def test_route_wxw(browser):

	try:

		login_web(browser, url="10.2.2.83")

		for n in range(1, 5):

			add_multi_gateway_group_wxw(browser, name='mgg_193_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device='ge0/3', gateway='34.1.1.1'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		add_policy_route_multi_wxw(browser, in_device='ge0/3', src_ip='34.1.1.0', src_mask='24',
								   dst_ip='20.1.1.0', dst_mask='24', service='yes', serv='any',
								   service_grp='no', serv_grp='H323',
								   gw_group='1(GROUP_1)', grp_mem=["主用", "备份1", "备份2", "不选择"], enable='yes',
								   disable='no', desc='maioshu', save='yes', cancel='no')

		exist = is_policy_route_exist_wxw(browser, destination='20.1.1.0/255.255.255.0')
		# print(exist)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_policy_route_singele_wxw(browser, destination='20.1.1.0/255.255.255.0')

		del_multi_gateway_group_all(browser)

		try:
			assert "添加策略路由对象成功" in loginfo
			assert"服务为 [any]" in loginfo
			assert exist is True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加策略路由对象成功" in loginfo
			assert "服务为 [any]" in loginfo
			assert exist is True


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.83")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])