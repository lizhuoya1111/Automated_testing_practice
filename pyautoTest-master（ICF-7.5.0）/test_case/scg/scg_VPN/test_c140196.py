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


test_id = 140196


def test_c140196(browser):
	try:
		login_web(browser, url=dev2)
		# ipsec_sa_lifetime='299'
		if oem_name == "SCG":
			add_ipsec_remote_gateway_gm(browser, name='test1', desc='miaoshu', status='enable', out_interface=interface_name_1,
									remote_gateway='static', gateway='10.21.22.82',
									localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
									local='local_ip', local_ip='35.12.1.0/255.255.255.0',
									 remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0', ipsec_super_net_switch="no",
									 advanced='yes', ipsec_sa="data", data='4999', save='yes')
			time.sleep(0.5)
			# 获取失败提示信息
			result1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			loginfo1 = ""
			if "无效的IPsec SA生存期" in result1:
				loginfo1 = get_log_info(browser, 管理日志)

			# ipsec_sa_lifetime='864001'
			add_ipsec_remote_gateway_gm(browser, name='test1', desc='miaoshu', status='enable',
										out_interface=interface_name_1,
										remote_gateway='static', gateway='10.21.22.82',
										localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
										local='local_ip', local_ip='35.12.1.0/255.255.255.0',
										remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0',
										ipsec_super_net_switch="no",
										advanced='yes', ipsec_sa="data", data='2147483648', save='yes')
			time.sleep(0.5)
			# 获取失败提示信息
			result2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			loginfo2 = ""
			if "数值大小超过有效范围[0~2147483647]" in result2:
				loginfo2 = get_log_info(browser, 管理日志)

			# ipsec_sa_lifetime在300-864000之间
			random_data_len = str(random.randint(5000, 2147483647))
			add_ipsec_remote_gateway_gm(browser, name='test1', desc='miaoshu', status='enable',
										out_interface=interface_name_1,
										remote_gateway='static', gateway='10.21.22.82',
										localid="CN=195.1.61.15", remoteid="CN=195.1.61.16", remote_cert_id_any_switch="no",
										local='local_ip', local_ip='35.12.1.0/255.255.255.0',
										remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0',
										ipsec_super_net_switch="no",
										advanced='yes', ipsec_sa="data", data=random_data_len, save='yes')
		elif oem_name == "ICF" or oem_name != "SCG":
			# add_ipsec_remote_gateway_gm(browser, name='test1', desc='miaoshu', status='enable',
			# 							out_interface=interface_name_1,
			# 							remote_gateway='static', gateway='10.21.22.82',
			# 							localid="CN=195.1.61.15", remoteid="CN=195.1.61.16",
			# 							remote_cert_id_any_switch="no",
			# 							local='local_ip', local_ip='35.12.1.0/255.255.255.0',
			# 							remote='remote_ip', remote_ip='25.12.1.0/255.255.255.0',
			# 							ipsec_super_net_switch="no",
			# 							advanced='yes', ipsec_sa="time", ipsec_sa_lifetime='119', save='yes')
			add_ipsec_remote_gateway_wxw(browser, name='test1', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 advanced='yes',
										 ipsec_sa='data', data='4999',
										 save='yes', cancel='')
			time.sleep(0.5)
			# 获取失败提示信息
			result1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			loginfo1 = ""
			if "无效的IPsec SA生存期" in result1:
				loginfo1 = get_log_info(browser, 管理日志)

			# ipsec_sa_lifetime='864001'
			add_ipsec_remote_gateway_wxw(browser, name='test1', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 advanced='yes',
										 ipsec_sa='data', data='2147483648',
										 save='yes', cancel='')
			time.sleep(0.5)
			# 获取失败提示信息
			result2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			loginfo2 = ""
			if "数值大小超过有效范围[0~2147483647]" in result2:
				loginfo2 = get_log_info(browser, 管理日志)

			# ipsec_sa_lifetime在300-864000之间
			random_data_len = str(random.randint(5000, 2147483647))
			add_ipsec_remote_gateway_wxw(browser, name='test1', desc='miaoshu', status='enable',
										 out_interface=interface_name_1,
										 remote_gateway='static', gateway='10.2.2.82', auth_method='预共享密钥',
										 password='123456',
										 local_ca='', remote_ca='',
										 local='local_ip', local_ip='30.1.1.0/255.255.255.0',
										 local_addr_obj='any',
										 remote='remote_ip', remote_ip='20.1.1.0/255.255.255.0',
										 remote_addr_obj='any',
										 advanced='yes',
										 ipsec_sa='time', data=random_data_len,
										 save='yes', cancel='')

		time.sleep(0.5)
		# 获取失败提示信息
		loginfo3 = get_log_info(browser, 管理日志)

		# print(loginfo1, loginfo2, loginfo3)
		try:
			assert "无效的IPsec SA生存期" in loginfo1 and "无效的IPsec SA生存期" in loginfo2 and "成功" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "无效的IPsec SA生存期" in loginfo1 and "无效的IPsec SA生存期" in loginfo2 and "成功" in loginfo3

		del_ipsec_remote_gateway_gm(browser, name='test1')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
