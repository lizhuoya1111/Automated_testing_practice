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

test_id = 140220

def test_c140220(browser):

	try:
		# loginfo_list = []
		login_web(browser, url=dev2)
		for x in ('null', 'des', '3des', 'aes128', 'aes192', 'aes256', 'sm1', 'sm4', 'b91'):
			for y in ('null', 'md5', 'sha1', 'sha256', 'sha384', 'sha512', 'sm3'):
				if x != 'null' and y!= 'null':
					add_ipsec_remote_access(browser, name='tt1', desc='miaoshu', status='enable', out_interface=interface_name_1,
											out_ip="default", auth_method='预共享密钥', password='123456', remote_ike_id_switch='no', ikeid_type="IP Address", remoteid_ipadd="5.5.5.5",
											pri_dns="5.5.5.5", sencond_dns="6.6.6.6", pri_win="", sencond_win="",
											local='local_ip', local_ip='30.1.1.0/255.255.255.0',
											advanced='yes', mode='main', encry_alg_div='3des', auth_alg='sha1',
											dh_group='2',
											ike_sa_lifetime='86400',
											ah='no', ah_auth_alg='',
											esp='yes', esp_encry_alg=x, esp_auth_alg=y,
											ip_compression='no', pfs='no', pfs_group='',
											ipsec_sa='time/data', ipsec_sa_lifetime='86400', data='',
											tunnel='yes/no', tunnel_pl='', start_negotiation='yes', return1='yes',
											save='yes', cancel='')
					loginfo1 = get_log_info(browser, 管理日志)
					# loginfo_list.append(loginfo1)
					print(x,y)
					del_ipsec_remote_access(browser, name='tt1')
					try:
						assert "成功添加" in loginfo1
						rail_pass(test_run_id, test_id)
					except:
						rail_fail(test_run_id, test_id)
						assert "成功添加" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])