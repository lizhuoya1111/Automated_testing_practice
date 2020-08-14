import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141456"
# ADRT_ADD_STATIC_ROUTE_SUCCESS


def test_c141456(browser):

	try:
		login_web(browser, url=dev3)

		add_static_route_single_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2, gateway='13.1.1.1',
									enable='yes')

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		del_ipv4_static_route_bydestination(browser, destination='20.1.1.0/255.255.255.0')

		try:
			assert "添加静态路由对象成功"in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "添加静态路由对象成功" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])