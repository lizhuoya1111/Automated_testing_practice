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

test_id = "141033"
# Route Mantiance 里的Multi-gateway group操作 5
# 点击Add后，添加新的网关，输入网关地址、link server 带宽
# 操作成功；shell先显示和UI一致；admin log正常


def test_c141033(browser):

	try:
		login_web(browser, url=dev3)


		add_multi_gateway_group_wxw(browser, name='mgg_033_4', group="1(GROUP_1)", modify='no', alias='',
									device=interface_name_3, gateway='34.1.1.4', ping_server='34.1.1.4',
									ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		add_multi_gateway_group_wxw(browser, name='mgg_033_5', group="1(GROUP_1)", modify='no', alias='',
									device=interface_name_3, gateway='34.1.1.5', ping_server='34.1.1.4',
									ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")
		exist = is_multi_gateway_group_exist_wxw(browser, name='mgg_033_5')
		# print(exist)

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_multi_gateway_group_all(browser)

		try:
			assert "添加网关对象到网关组成功" in loginfo
			assert exist is True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加网关对象到网关组成功" in loginfo
			assert exist is True

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s",  "test_c"+str(test_id)+".py"])