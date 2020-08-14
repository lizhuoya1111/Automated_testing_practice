import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_firewall import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144129"
# 添加一个addr obj,在ACL中引用,验证obj中R是否有显示


def test_c144129(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_address_wxw(browser, name='obj_add_354', desc='zhe是yi个描述1', subnetip='11.11.11.0', subnetmask='24')

		time.sleep(0.5)

		add_acl_group_wxw(browser, name='acl_group_354')

		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_354', source_zone_interface=interface_name_4,
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:obj_add_354',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:obj_add_354',
								  dest_zone_interface=interface_name_2,
								  service='P:any', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no')


		get_addr_obj_ref_wxw(browser, name='obj_add_354')
		time.sleep(1)

		# 获取引用
		ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text
		# print(ref)

		del_acl_group_wxw(browser, name='acl_group_354')

		del_obj_address_wxw(browser, name='obj_add_354')

		try:
			assert ref == "acl"
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert ref == "acl"

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])