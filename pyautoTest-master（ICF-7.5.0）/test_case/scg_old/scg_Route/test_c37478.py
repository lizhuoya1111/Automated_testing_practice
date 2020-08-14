import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37478
# 输入中文字符(多网关组)


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_multi_gateway_group_wxw(browser, name='中文', group="1(GROUP_1)", modify='no', alias='',
									device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4', ping='yes',
									arp='no',
									time_switch='7', ub="100000", db="100000")

		exist = is_multi_gateway_group_exist_wxw(browser, name='中文')

		del_multi_gateway_group_byname(browser, name='中文')

		try:
			assert exist is True
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert exist is True


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.83")
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])