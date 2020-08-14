import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139806"


def test_c139806(browser):

	try:
		login_web(browser, url=dev1)
		# add_obj_zone(browser, "abcabcabcabcabcabcabcabcabcabcab", "dabcabcabcabcabcabcabc", [interface_name_5, interface_name_6])
		add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:any',
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface=interface_name_2,
								  service='P:any', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no', save='yes', cancel='no')
		add_acl_loginfo = get_log_info(browser, 管理日志)

		add_snat(browser, name="snat_jia_1", desc="", src_inter_zone='Z:any', des_inter_zone=interface_name_3,
				 other_match_switch="no",
				 src_ipadd_switch="自定义", srcaddress_predefine="A:any", srcip_custom="12.1.1.0", srcmask_custom="24",
				 des_ipadd_switch="自定义", desaddress_predefine="A:any", desip_custom="13.1.1.0", desmask_custom="24",
				 server='P:any', trans_local_ip="yes", single_ip='no', ip_range_start='no', ip_range_end='no',
				 other_action_nomap='no', other_action_maplist="no", save='yes', cancel='no')
		add_sant_loginfo = get_log_info(browser, 管理日志)

		try:
			assert '配置过滤规则对象成功' in add_acl_loginfo
			assert '从区域端口 [any]' in add_acl_loginfo
			assert '配置SNAT对象成功' in add_sant_loginfo
			assert '从域/接口 [any]' in add_sant_loginfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert '配置过滤规则对象成功' in add_acl_loginfo
			assert '从区域端口 [any]' in add_acl_loginfo
			assert '配置SNAT对象成功' in add_sant_loginfo
			assert '从域/接口 [any]' in add_sant_loginfo

		del_acl_byid(browser, group_name="default", acl_id="2")
		del_snat_byname(browser, name="snat_jia_1")
		# del_obj_zone_byname(browser, "abcabcabcabcabcabcabcabcabcabcab")


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])