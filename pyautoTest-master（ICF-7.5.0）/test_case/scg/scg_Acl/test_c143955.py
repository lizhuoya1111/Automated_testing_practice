
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *

test_id = "143955"

# 根据源interface/zone、目的interface/zone、源地址、目的地址、服务、动作查找rule

def test_c143955(browser):
	try:
		login_web(browser, url=dev1)
		# 添加组
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		# 添加规则
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3,
						      source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0',
                              source_address_object='no', dest_zone_interface=interface_name_4,
                              dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0',
                              dest_address_object='no', service='P:SNMP', drop='yes')
		# 高级搜索
		find_ipv4acl_lzy(browser, source_zone_interface=interface_name_3, source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0',
					 source_address_object='no', dest_zone_interface=interface_name_4,
                     dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0', dest_address_object='no',
                     service='P:SNMP', action='yes', accept='no', drop='yes')
		sleep(10)
		# 获取信息
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		browser.switch_to.frame("iFrame1")
		# drop
		info1 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[5]/span').text
		print(info1)
		# SNMP
		info2 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[4]/a').text
		print(info2)
		# 14.1.1.1
		info3 = browser.find_element_by_xpath('//*[@id="storage_new_zone"]/div[1]/ul/li[3]/a[2]').text
		print(info3)
		# P0
		info4 = browser.find_element_by_xpath('//*[@id="fromezone0"]').text
		print(info4)


		# 还原
		del_all_acl_group_lzy(browser)
		sleep(2)

		try:
			assert 'drop' in info1 and 'SNMP' in info2 and '14.1.1.1' in info3 and interface_name_3 in info4
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert 'drop' in info1 and 'SNMP' in info2 and '14.1.1.1' in info3 and interface_name_3 in info4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





