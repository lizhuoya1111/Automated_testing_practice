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

test_id = "140200"
# 网关接入基本配置3
# 填写正确的remote gateway 网关
# 可以设置成功,有日志记录


def test_c140200(browser):

	try:
		login_web(browser, url=dev1)
		add_loginfo = edit_loginfo = del_loginfo = ""
		if oem_name == "ICF" or oem_name != "SCG":
			add_ipsec_remote_gateway_wxw(browser, name='ttl', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 advanced='no', xauth='server/client/no', user='', user_name='', user_password='',
										 mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1', dh_group='2',
										 ike_sa_lifetime='86400',
										 ah='no', ah_auth_alg='',
										 esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										 ip_compression='no', pfs='no', pfs_group='',
										 ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										 tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										 save='yes', cancel='')
			add_loginfo = get_log_info(browser, 管理日志)
			edit_ipsec_remote_gateway_wxw(browser, name='ipsec', desc='miao', status='enable/unmodify',
										  save='yes', cancel='')
			edit_loginfo = get_log_info(browser, 管理日志)

			del_ipsec_remote_gateway_wxw(browser, name='ttl')
			del_loginfo = get_log_info(browser, 管理日志)

		elif oem_name == "SCG":
			add_ipsec_remote_gateway_gm(browser, name='ttl', desc='miaoshu', status='enable',
										out_interface=interface_name_1,
										remote_gateway='static', gateway='10.2.2.82', auth_method='证书',
										localid="CN=127.0.0.1", remoteid="CN=127.0.0.2", remote_cert_id_any_switch="no",
										local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										local_addr_obj='any',
										remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										remote_addr_obj='any', ipsec_super_net_switch="no",
										advanced='no',
										encry_alg_div='3des', auth_alg='sha1',
										ike_sa_lifetime='86400',
										ah='no', ah_auth_alg='',
										esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
										ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
										tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
										save='yes', cancel='no')
			add_loginfo = get_log_info(browser, 管理日志)
			edit_ipsec_remote_gateway_gm(browser, name='ttl', desc='miaoshu/unmodify', status='enable/unmodify',
								 out_interface="/unmodify", out_ip="default/unmodify",
								 remote_gateway='static/dynamic_ip/unmodify', gateway='10.2.2.82/unmodify',
								 auth_method='证书/unmodify',
								 localid="CN=127.0.0.3", remoteid="127.0.0.1/unmodify", save='yes')
			edit_loginfo = get_log_info(browser, 管理日志)

			del_ipsec_remote_gateway_wxw(browser, name='ttl')
			del_loginfo = get_log_info(browser, 管理日志)


		try:
			assert "成功添加远程网关隧道，具体属性 : Name= [ttl]" in add_loginfo
			assert "成功修改远程网关隧道，具体属性 : Name= [ttl]" in edit_loginfo
			assert "成功删除远程网关隧道，具体属性 : Name= [ttl]" in del_loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功添加远程网关隧道，具体属性 : Name= [ttl]" in add_loginfo
			assert "成功修改远程网关隧道，具体属性 : Name= [ttl]" in edit_loginfo
			assert "成功删除远程网关隧道，具体属性 : Name= [ttl]" in del_loginfo


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])