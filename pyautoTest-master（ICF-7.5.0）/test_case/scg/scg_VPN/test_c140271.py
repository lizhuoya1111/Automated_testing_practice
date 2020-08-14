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

test_id = 140271

def test_c140271(browser):

	try:
		login_web(browser, url=dev2)
		if oem_name == "ICF" or oem_name != "SCG":
			add_ipsec_remote_gateway_wxw(browser, name='to_81', desc='', status='enable',
										 out_interface=interface_name_1, out_ip="10.2.2.82",
										 remote_gateway='dynamic_ip', gateway='12.1.1.1', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 save='yes', cancel='')
			login_web(browser, url=dev1)
			add_ipsec_remote_gateway_wxw(browser, name='to_82', desc='', status='enable',
										 out_interface=interface_name_1, out_ip="10.2.2.81",
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='20.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='30.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 save='yes', cancel='')

		elif oem_name == "SCG":
			import_cert_gm(browser, cert_name="sm2-cert-15.zip")
			add_ipsec_remote_gateway_gm(browser, name='to_81', desc='miaoshu', status='enable',
										out_interface=interface_name_1, out_ip="10.2.2.82",
										remote_gateway='dynamic_ip', gateway='12.1.1.1', auth_method='证书',
										localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
										local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										local_addr_obj='any',
										remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										remote_addr_obj='any', ipsec_super_net_switch="no",
										advanced='yes',
										encry_alg_div='sm1', auth_alg='sm3',
										ike_sa_lifetime='86400',
										ah='no', ah_auth_alg='',
										esp='yes', esp_encry_alg='sm1', esp_auth_alg='sm3',
										ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										save='yes', cancel='no')

			login_web(browser, url=dev1)
			import_cert_gm(browser, cert_name="sm2-cert-16.zip")
			add_ipsec_remote_gateway_gm(browser, name='to_82', desc='miaoshu', status='enable',
										out_interface=interface_name_1, out_ip="10.2.2.81",
										remote_gateway='static', gateway='10.2.2.82', auth_method='证书',
										localid="CN=195.1.61.16", remoteid="CN=195.1.61.15",
										remote_cert_id_any_switch="no",
										local='local_ip', local_ip='20.1.1.0/255.255.255.0',
										local_addr_obj='any',
										remote='remote_ip', remote_ip='30.1.1.0/255.255.255.0',
										remote_addr_obj='any', ipsec_super_net_switch="no",
										advanced='yes',
										encry_alg_div='sm1', auth_alg='sm3',
										ike_sa_lifetime='86400',
										ah='no', ah_auth_alg='',
										esp='yes', esp_encry_alg='sm1', esp_auth_alg='sm3',
										ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										save='yes', cancel='no')

		login_web(browser, url=dev2)
		result = get_ipsec_station_byname(browser, ipsec_name="to_81")
		print(result)
		time.sleep(60)
		loginfo1 = get_log_info(browser, 管理日志)
		del_ipsec_remote_gateway_wxw(browser, name='to_81')
		login_web(browser, url=dev1)
		del_ipsec_remote_gateway_wxw(browser, name='to_82')
		try:
			assert "ipsec_jia_1" in result[1] and "10.2.2.81" in result[2] and "Established" in result[5]
			assert "成功添加" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ipsec_jia_1" in result[1] and "10.2.2.81" in result[2] and "Established" in result[5]
			assert "成功添加" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])