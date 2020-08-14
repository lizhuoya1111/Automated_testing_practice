import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ipsec import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
import random
sys.path.insert(0, dirname(dirname(abspath(__file__))))


test_id = 140203


# "测试用例没有问题，是告警信息不一致导致的，需要提单修改！"
def test_c140203(browser):
	try:
		login_web(browser, url=dev2)

		for i in range(0, 4):
			add_ipsec_remote_gateway_gm(browser, name='test'+str(i), desc='miaoshu', status='enable', out_interface=interface_name_1,
	                                remote_gateway='static', gateway='10.21.22.182',
	                                localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
	                                local='local_ip', local_ip='35.12.1.0/255.255.255.0',
	                                 remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0', ipsec_super_net_switch="no",
	                                 advanced='no', save='yes')

		del_all_ipsec_remote_gateway_gm(browser)
		loginfo3 = get_log_info(browser, 管理日志)

		try:
			assert "成功删除远程网关隧道" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功删除远程网关隧道" in loginfo3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
