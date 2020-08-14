import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_multi_gateway_group import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141035"
# Route Mantiance 里的Multi-gateway group操作 7
# 添加10条路由网关条目，点击删除按钮，删除第五条
# 操作成功；shell先显示和UI一致；admin log正常


def test_c141035(browser):

	try:
		login_web(browser, url=dev3)

		for n in range(1, 10):
			if n == 3:
				continue
			add_multi_gateway_group_wxw(browser, name='mgg_035_'+str(n), group="1(GROUP_1)", modify='no', alias='',
										device=interface_name_3, gateway='34.1.1.'+str(n), ping_server='34.1.1.4',
										ping='yes', arp='no', time_switch='7', ub="100000", db="100000")

		for n in range(10, 12):
			add_multi_gateway_group_wxw(browser, name='mgg_035_'+str(n), group="2(GROUP_2)", modify='no', alias='',
										device=interface_name_3, gateway='34.1.1.'+str(n), ping_server='34.1.1.4',
										ping='yes', arp='no', time_switch='7', ub="100000", db="100000")

		del_multi_gateway_group_byname(browser, name='mgg_035_6')
		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)
		exist = is_multi_gateway_group_exist_wxw(browser, name='mgg_035_6')
		print(exist)

		del_multi_gateway_group_all(browser)


		try:
			assert "从网关组删除网关对象成功" in loginfo
			assert exist is False
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "从网关组删除网关对象成功" in loginfo
			assert exist is False

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])