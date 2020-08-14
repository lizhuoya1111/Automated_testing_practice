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

test_id = 148130

def test_c148130(browser):

	try:
		login_web(browser, url=dev2)
		add_ipsec_remote_gateway_wxw(browser, name='ipsec_jia_1', desc='', status='enable',
									 out_interface=interface_name_2,
									 remote_gateway='static', gateway='12.1.1.1', auth_method='预共享密钥',
									 password='123456',
									 local_ca='', remote_ca='',
									 local='local_ip', local_ip='24.1.1.0/255.255.255.0',
									 local_addr_obj='any',
									 remote='remote_ip', remote_ip='13.1.1.0/255.255.255.0',
									 remote_addr_obj='any',
									 save='yes', cancel='')

		loginfo1 = get_log_info(browser, 管理日志)
		add_ipsec_remote_gateway_wxw(browser, name='ipsec_jia_2', desc='', status='enable',
									 out_interface=interface_name_2,
									 remote_gateway='static', gateway='12.1.1.1', auth_method='预共享密钥',
									 password='123456',
									 local_ca='', remote_ca='',
									 local='local_ip', local_ip='24.1.1.6.9/255.255.255.0',
									 local_addr_obj='any',
									 remote='remote_ip', remote_ip='13.1.1.9.85/255.255.255.0',
									 remote_addr_obj='any',
									 save='yes', cancel='')

		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		del_ipsec_remote_gateway_wxw(browser, name='ipsec_jia_1')

		try:
			assert "成功添加" in loginfo1
			assert "无效的本地保护子网" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功添加" in loginfo1
			assert "无效的本地保护子网" in webinfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])