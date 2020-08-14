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
		num = 0
		for x in range(0, 10):
			num += 1
			print("本次管理/互联地址：60.1.1." + str(1))
			print("本次本地保护地址：172.16." + str(1) + ".1")
			input("回车")
			login_web(browser, url="192.168.1.1")
			# ge0/1 添加地址
			add_physical_interface_ip_wxw(browser, interface=interface_name_1, ip='60.1.1.'+str(num), mask='24')

			# ge0/6 添加地址
			add_physical_interface_ip_wxw(browser, interface=interface_name_6, ip='172.16.'+str(num)+'.1', mask='24')

			# 添加全通acl
			add_acl_rule_complete_wxw(browser, aclgroup_name='aaa', source_zone_interface='Z:any',
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface='Z:any')
			# 导入证书
			import_cert_gm(browser, cert_path="C:/Users/liubb/Desktop/")

			# 创建 ipsec
			add_ipsec_remote_gateway_gm(browser, name='ipsec_1to1', desc='miaoshu', status='enable',
			                            out_interface=interface_name_1,
			                            remote_gateway='static', gateway='60.1.1.100',
			                            localid="CN=195.1.61.15", remoteid="CN=195.1.61.16",
			                            advanced='yes', start_negotiation='yes', save='yes')

			# 添加路由
			add_static_route_single_wxw(browser, ip='0.0.0.0', mask='0.0.0.0', out_device=interface_name_1, gateway='60.1.1.100', enable='yes')



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])