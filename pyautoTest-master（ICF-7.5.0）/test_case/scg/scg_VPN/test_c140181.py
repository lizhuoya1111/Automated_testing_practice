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

test_id = "140181"


# 网关接入基本配置3
# 填写正确的remote gateway 网关
# 可以设置成功,有日志记录


def test_c140181(browser):
	try:
		exist1 = exist2 = exist3 = exist4 = ""
		loginfo1 = loginfo2 = loginfo3 = loginfo4 = ""
		login_web(browser, url=dev1)
		add_obj_address_wxw(browser, name='obj_add_339', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')
		add_obj_address_wxw(browser, name='obj_add_338', desc='zhe是yi个描述1', subnetip='12.11.11.0', subnetmask='24')

		if oem_name == "ICF" or oem_name != "SCG":
			add_ipsec_remote_gateway_wxw(browser, name='ttl', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_addr_obj', local_ip='obj_add_339',
										 local_addr_obj='obj_add_339',
										 remote='remote_addr_obj', remote_ip='obj_add_338',
										 remote_addr_obj='obj_add_338',
										 advanced='no', xauth='server/client/no', user='', user_name='',
										 user_password='',
										 mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1', dh_group='2',
										 ike_sa_lifetime='86400',
										 ah='no', ah_auth_alg='',
										 esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										 ip_compression='no', pfs='no', pfs_group='',
										 ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										 tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										 save='yes', cancel='')
			exist1 = is_ipsec_remote_gateway_exist_wxw(browser, name='ttl')
			# print(exist)

			loginfo1 = get_log_info(browser, 管理日志)
			# print(loginfo)
			del_ipsec_remote_gateway_wxw(browser, name='ttl')

			add_ipsec_remote_gateway_wxw(browser, name='ttl', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_addr_obj', local_ip='obj_add_338',
										 local_addr_obj='obj_add_338',
										 remote='remote_addr_obj', remote_ip='obj_add_339',
										 remote_addr_obj='obj_add_339',
										 advanced='no', xauth='server/client/no', user='', user_name='',
										 user_password='',
										 mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1', dh_group='2',
										 ike_sa_lifetime='86400',
										 ah='no', ah_auth_alg='',
										 esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										 ip_compression='no', pfs='no', pfs_group='',
										 ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										 tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										 save='yes', cancel='')
			exist2 = is_ipsec_remote_gateway_exist_wxw(browser, name='ttl')
			# print(exist)

			loginfo2 = get_log_info(browser, 管理日志)
			# print(loginfo)
			del_ipsec_remote_gateway_wxw(browser, name='ttl')

		elif oem_name == "SCG":
			add_ipsec_remote_gateway_gm(browser, name='ttl', desc='miaoshu', status='enable',
										out_interface=interface_name_1,
										remote_gateway='static', gateway='10.2.2.82', auth_method='证书',
										localid="CN=127.0.0.1", remoteid="CN=127.0.0.2", remote_cert_id_any_switch="yes",
										local='local_addr_obj', local_ip='obj_add_339',
										local_addr_obj='obj_add_339',
										remote='remote_addr_obj', remote_ip='obj_add_338',
										remote_addr_obj='obj_add_338', ipsec_super_net_switch="no",
										advanced='no',
										encry_alg_div='3des', auth_alg='sha1',
										ike_sa_lifetime='86400',
										ah='no', ah_auth_alg='',
										esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										save='yes', cancel='no')
			exist3 = is_ipsec_remote_gateway_exist_wxw(browser, name='ttl')
			# print(exist)

			loginfo3 = get_log_info(browser, 管理日志)
			# print(loginfo)
			del_ipsec_remote_gateway_wxw(browser, name='ttl')

			add_ipsec_remote_gateway_gm(browser, name='ttl', desc='miaoshu', status='enable',
										out_interface=interface_name_1,
										remote_gateway='static', gateway='10.2.2.82', auth_method='证书',
										localid="CN=127.0.0.1", remoteid="CN=127.0.0.2",
										remote_cert_id_any_switch="yes",
										local='local_addr_obj', local_ip='obj_add_339',
										local_addr_obj='obj_add_338',
										remote='remote_addr_obj', remote_ip='obj_add_338',
										remote_addr_obj='obj_add_339', ipsec_super_net_switch="no",
										advanced='no',
										encry_alg_div='3des', auth_alg='sha1',
										ike_sa_lifetime='86400',
										ah='no', ah_auth_alg='',
										esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										save='yes', cancel='no')
			exist4 = is_ipsec_remote_gateway_exist_wxw(browser, name='ttl')
			# print(exist)

			loginfo4 = get_log_info(browser, 管理日志)
			# print(loginfo)
			del_ipsec_remote_gateway_wxw(browser, name='ttl')

		try:
			assert (exist1 is True and exist2 is True) or (exist3 is True and exist4 is True)
			assert ("成功添加远程网关隧道" in loginfo1 and "成功添加远程网关隧道" in loginfo2) or ("成功添加远程网关隧道" in loginfo3 and "成功添加远程网关隧道" in loginfo4)
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert (exist1 is True and exist2 is True) or (exist3 is True and exist4 is True)
			assert ("成功添加远程网关隧道" in loginfo1 and "成功添加远程网关隧道" in loginfo2) or (
						"成功添加远程网关隧道" in loginfo3 and "成功添加远程网关隧道" in loginfo4)

		del_obj_address_wxw(browser, name='obj_add_339')
		del_obj_address_wxw(browser, name='obj_add_338')
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])