
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
from page_obj.scg.scg_def_obj import *

test_id = "143956"


def test_c143956(browser):
	try:
		login_web(browser, url=dev2)
		# 添加zone
		add_obj_zone(browser, name="哈哈哈哈哈哈", zone_mem=[interface_name_1, interface_name_2])

		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		# 添加规则
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface="Z:哈哈哈哈哈哈",
						      source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0',
                              source_address_object='no', dest_zone_interface=interface_name_4,
                              dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0',
                              dest_address_object='no', service='P:SNMP', drop='yes')
		# 高级搜索
		find_ipv4acl_lzy(browser, source_zone_interface="Z:哈哈哈哈哈哈", source_custom='yes', fromip='13.1.1.1', fromnetmask='255.255.255.0',
					 source_address_object='no', dest_zone_interface=interface_name_4,
                     dest_custom='yes', toip='14.1.1.1', tonetmask='255.255.255.0', dest_address_object='no',
                     service='P:SNMP', action='yes', accept='no', drop='yes')
		sleep(10)
		# 获取信息
		browser.switch_to.default_content()
		browser.switch_to.frame("content")
		browser.switch_to.frame("iFrame1")

		# P0 //*[@id="fromezone0"]
		info4 = browser.find_element_by_xpath('//*[@id="fromezone0"]').text
		# print(info4)

		# 还原
		del_all_acl_group_lzy(browser)
		del_obj_zone_byname(browser, name="哈哈哈哈哈哈")

		try:
			assert '哈哈哈哈哈哈' in info4
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert '哈哈哈哈哈哈' in info4

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev2)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])


