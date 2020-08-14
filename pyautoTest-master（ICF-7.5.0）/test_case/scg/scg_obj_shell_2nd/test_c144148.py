import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144148"
# 添加一个serv obj,在ACL中引用,验证serv obj中R是否有显示


def test_c144148(browser):

	try:
		login_web(browser, url=dev1)

		add_obj_service_wxw(browser, name='obj_serv_373', desc='zhe是ge描shu',
							tcp='', src_port_from='1', src_port_to='2', dest_port_from='3', dest_port_to='4',
							udp='yes', src_port_from1='1', src_port_to1='2', dst_port_from1='3', dst_port_to1='4',
							icmp='', item='ping',
							ip='', number='85')

		add_acl_group_wxw(browser, name='acl_group_373')

		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_373', source_zone_interface=interface_name_4,
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface=interface_name_2,
								  service='C:obj_serv_373', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no')

		get_service_obj_ref_wxw(browser, name='obj_serv_373')
		time.sleep(1)
		# 获取引用
		ref = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]').text

		del_acl_group_wxw(browser, name='acl_group_373')

		del_obj_service_wxw(browser, name='obj_serv_373')

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