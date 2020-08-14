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

test_id = 140191

def test_c140191(browser):

	try:
		login_web(browser, url=dev2)
		add_ipsec_remote_gateway_gm(browser, name='test1', desc='miaoshu', status='enable', out_interface=interface_name_1,
                                remote_gateway='static', gateway='10.21.22.82',
                                localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
                                local='local_ip', local_ip='35.12.1.0/255.255.255.0',
                                 remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0', ipsec_super_net_switch="no",
                                 advanced='no', save='yes')

		result = True
		for en in ["null", "des", "3des", "aes128", "aes192", "aes256", "sm1", "sm4", "b91"]:
			for au in ["null", "md5", "sha1", "sha256", "sha384", "sha512", "sm3"]:
				if en != "null" and au != "null":
					edit_ipsec_remote_gateway_gm(browser, name='test1', advanced='yes',esp='yes',
					                             esp_encry_alg=en, esp_auth_alg=au, return1="yes", save='yes')
					out_en_au = get_ipesc_remote_gateway_en_au_gm(browser, name='test1', switch="阶段2")

					# print(en, au, "===", out_en_au)
					if (en, au) != out_en_au:
						result = False
						break

		try:
			assert result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result

		del_ipsec_remote_gateway_gm(browser, name='test1')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])