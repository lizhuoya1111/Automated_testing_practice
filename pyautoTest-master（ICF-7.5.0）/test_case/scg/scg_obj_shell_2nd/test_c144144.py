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

test_id = "144144"
# 添加一个obj grp,在ACL中引用,验证obj grp中R是否有显示


def test_c144144(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_369', desc='zhe是yi个描述1', addr_obj='A:any')

		add_acl_group_wxw(browser, name='acl_group_369')

		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_369', source_zone_interface=interface_name_4,
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='G:obj_grp_369',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='G:obj_grp_369',
								  dest_zone_interface=interface_name_2,
								  service='P:any', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no')

		get_grp_obj_ref_wxw(browser, name='obj_grp_369')

		# 获取引用
		time.sleep(1)
		ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

		del_acl_group_wxw(browser, name='acl_group_369')

		del_obj_grp_wxw(browser, name='obj_grp_369')

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
