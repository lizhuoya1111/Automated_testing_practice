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
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 140215

def test_c140215(browser):

	try:
		login_web(browser, url=dev2)
		add_obj_address_wxw(browser, name='obj_add_339', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
		add_obj_address_wxw(browser, name='obj_add_338', desc='zhe是yi个描述1', subnetip='12.11.11.0', subnetmask='24')
		add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable', out_interface=interface_name_1,
								out_ip="default", auth_method='预共享密钥', password='123456', remote_ike_id_switch='no', ikeid_type="IP Address", remoteid_ipadd="5.5.5.5",
								pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="7.7.7.7", sencond_win="8.8.8.8",
								local='local_addr_obj', local_ip='30.1.1.0/255.255.255.0',
								local_addr_obj='obj_add_339',
								advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1',
								dh_group='2',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ip_compression='no', pfs='no', pfs_group='',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								return1='yes',
								save='yes', cancel='')
		loginfo1 = get_log_info(browser, 管理日志)
		del_ipsec_remote_access(browser, name='tt1')

		add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable', out_interface=interface_name_1,
								out_ip="default", auth_method='预共享密钥', password='123456', remote_ike_id_switch='no',
								ikeid_type="IP Address", remoteid_ipadd="5.5.5.5",
								pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="7.7.7.7", sencond_win="8.8.8.8",
								local='local_addr_obj', local_ip='30.1.1.0/255.255.255.0',
								local_addr_obj='obj_add_338',
								advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1',
								dh_group='2',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ip_compression='no', pfs='no', pfs_group='',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								return1='yes',
								save='yes', cancel='')
		loginfo2 = get_log_info(browser, 管理日志)
		del_ipsec_remote_access(browser, name='tt1')
		try:
			assert "成功添加" in loginfo1
			assert "成功添加" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功添加" in loginfo1
			assert "成功添加" in loginfo2
		del_obj_address_wxw(browser, name='obj_add_339')
		del_obj_address_wxw(browser, name='obj_add_338')
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])