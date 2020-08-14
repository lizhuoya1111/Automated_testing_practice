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

test_id = "140205"
# 网关接入基本配置2
# Local Interface 分别选择BR0 SP1 GE1 GE1.1的主ip和multi IP
# 可以设置成功,有日志记录


def test_c140205(browser):

	try:
		login_web(browser, url=dev1)
		# use br
		add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable', out_interface="br_0",
								out_ip="default", auth_method='预共享密钥', password='123456',
								pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="", sencond_win="",
								local='local_ip', local_ip='30.1.1.0/255.255.255.0',
								advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1',
								dh_group='2',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ip_compression='no', pfs='no', pfs_group='',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								save='yes', cancel='')

		exist = is_ipsec_remote_access_exist(browser, name='tt1')
		# print(exist)
		loginfo = get_log_info(browser, 管理日志)
		del_ipsec_remote_access(browser, name='tt1')

		# use ge6.1 primary ip
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="1", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_6+'.1', ipadd="141.1.1.2", mask="255.255.255.0")
		add_vlan_inte_add(browser, interface_name=interface_name_6 + '.1', ipadd="142.1.1.2", mask="255.255.255.0")

		add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable', out_interface=interface_name_6+'.1',
								out_ip="141.1.1.2", auth_method='预共享密钥', password='123456',
								pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="", sencond_win="",
								local='local_ip', local_ip='30.1.1.0/255.255.255.0',
								advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1',
								dh_group='2',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ip_compression='no', pfs='no', pfs_group='',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								save='yes', cancel='')

		exist1 = is_ipsec_remote_access_exist(browser, name='tt1')
		# print(exist)
		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo)
		del_ipsec_remote_access(browser, name='tt1')

		# use ge6.1 second ip
		add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable',
								out_interface=interface_name_6 + '.1',
								out_ip="142.1.1.2", auth_method='预共享密钥', password='123456',
								pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="", sencond_win="",
								local='local_ip', local_ip='30.1.1.0/255.255.255.0',
								advanced='no', mode='main/aggressive', encry_alg_div='3des', auth_alg='sha1',
								dh_group='2',
								ike_sa_lifetime='86400',
								ah='no', ah_auth_alg='',
								esp='yes', esp_encry_alg='aes128', esp_auth_alg='sha1',
								ip_compression='no', pfs='no', pfs_group='',
								ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
								tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
								save='yes', cancel='')

		exist2 = is_ipsec_remote_access_exist(browser, name='tt1')
		# print(exist)
		loginfo2 = get_log_info(browser, 管理日志)
		# print(loginfo)
		del_ipsec_remote_access(browser, name='tt1')

		try:
			assert exist is True and exist1 is True and exist2 is True
			assert "成功添加远程接入隧道" in loginfo and "成功添加远程接入隧道" in loginfo1 and "成功添加远程接入隧道" in loginfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert exist is True and exist1 is True and exist2 is True
			assert "成功添加远程接入隧道" in loginfo and "成功添加远程接入隧道" in loginfo1 and "成功添加远程接入隧道" in loginfo2

		del_vlan_inte_all(browser)
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_6)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])