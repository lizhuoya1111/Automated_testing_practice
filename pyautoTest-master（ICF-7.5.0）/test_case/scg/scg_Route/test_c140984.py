import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.scg.scg_def_policy_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "140984"
# 添加20条路由条目，点击select all，然后点击delete all


def test_c140984(browser):

	try:

		login_web(browser, url=dev3)

		for n in range(1, 21):

			add_policy_route_single_wxw(browser, in_device=interface_name_3, src_ip='34.1.1.0', src_mask='24',
										dst_ip='12.'+str(n)+'.1.0', dst_mask='24', service='no', serv='any',
										service_grp='no', serv_grp='H323',
										out_device=interface_name_2, gateway='13.1.1.1', enable='yes', disnable='no',
										desc='maioshu')

		del_all_policy_route_lzy(browser)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		# for m in range(1, 6):
		#     del_policy_route_singele_wxw(browser, destination='12.'+str(m)+'.1.0/255.255.255.0')
		# for m in range(7, 11):
		#     del_policy_route_singele_wxw(browser, destination='12.' + str(m) + '.1.0/255.255.255.0')

		try:
			assert "删除策略路由对象成功" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "删除策略路由对象成功" in loginfo
		del_all_policy_route_lzy(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])