import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141274"
# 静态多网关路由配置GW输入异常检测 9
# 输入网关不可达（ip地址所在网段墙上没有的）


def test_c141274(browser):

	try:
		login_web(browser, url=dev1)

		add_multi_gateway_group_wxw(browser, name='mgg_464', group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_1, gateway='6.6.6.6', ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		alert1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert1)

		try:
			assert "网关不可达" in alert1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "网关不可达" in alert1


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])