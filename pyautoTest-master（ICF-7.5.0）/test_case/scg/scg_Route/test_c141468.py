import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_policy_route import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141468"
# ADRT_MODIFY_POLICY_ROUTE_FAIL


def test_c141468(browser):

	try:
		login_web(browser, url=dev3)

		add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
									dst_ip='12.1.1.0', dst_mask='24', service='no', serv='any',
									service_grp='no', serv_grp='H323',
									out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
									desc='maioshu')

		edit_policy_route_single_wxw(browser, destination='12.1.1.0/255.255.255.0', in_device=interface_name_2, src_ip='12.1.1.0',
									 src_mask='24',
									 dst_ip='24.1.1.0', dst_mask='24', service='no', serv='any',
									 service_grp='no', serv_grp='H323',
									 out_device=interface_name_3, gateway='10.2.2.0', enable='yes',
									 disnable='no', desc='maioshu')

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		del_policy_route_singele_wxw(browser, destination='12.1.1.0/255.255.255.0')


		try:
			assert "修改策略路由对象失败"in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "修改策略路由对象失败" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])