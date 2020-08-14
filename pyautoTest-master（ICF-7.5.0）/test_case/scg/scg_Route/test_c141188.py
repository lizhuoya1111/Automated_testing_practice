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

test_id = "141188"
# Route maitance group gateway 功能 15
# 网关组添加成功后显示在list里
# 显示和条目一致


def test_141188(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(4, 6):

			add_multi_gateway_group_wxw(browser, name='mgg_188_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_3, gateway='34.1.1.'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")
		exist1 = is_multi_gateway_group_exist_wxw(browser, name='mgg_188_4')
		# print(exist1)

		exist2 = is_multi_gateway_group_exist_wxw(browser, name='mgg_188_5')
		# print(exist2)

		del_multi_gateway_group_all(browser)

		try:
			assert exist1 is True
			assert exist2 is True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert exist1 is True
			assert exist2 is True

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])