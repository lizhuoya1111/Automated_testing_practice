import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.scg.scg_def_obj import *


test_id = "144188"


def test_c144188(browser):
	try:
		# 81添加一个子接口，选择ge0/5，id为2
		login_web(browser, url=dev1)
		# 在object中添加两个address group，分别为group1，group2，每个group中又包含group
		add_obj_address_wxw(browser, name='obj_add_source', subnetip='20.1.1.0', subnetmask='24')
		# add_obj_address_wxw(browser, name='obj_add_dest', subnetip='13.1.1.0', subnetmask='24')

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_source_p', addr_obj='A:obj_add_source')
		# add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_dest_p', addr_obj='A:obj_add_dest')

		add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_source', addr_obj='G:obj_grp_source_p')
		# add_obj_group_use_addr_obj_wxw(browser, name='obj_grp_dest', addr_obj='G:obj_grp_dest_p')

		# 添加ACL
		add_acl_group_complete(browser, name='lzy', enable='yes')
		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
								  s_address_object='G:obj_grp_source', d_address_object='A:any')
		# time.sleep(2000)
		add_ref = get_addr_obj_ref_wxw(browser, name='obj_add_source')
		# print(add_ref)
		add_g1_ref =get_grp_obj_ref_wxw(browser, name='obj_grp_source_p')
		# print(add_g1_ref)
		add_g2_ref = get_grp_obj_ref_wxw(browser, name='obj_grp_source')
		# print(add_g2_ref)

		modify_obj_add_grp_by_name(browser, name='obj_grp_source_p', dec='', add='yes', add_obj1='A:any')
		edit_log = get_log_info(browser, log_type=管理日志)
		# print(edit_log)

		try:
			assert "对象成功，修改内部对象 [obj_grp_source_p]" in edit_log and \
				'address-group' in add_ref and \
				'address-group' in add_g1_ref and \
				'acl' in add_g2_ref
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "对象成功，修改内部对象 [obj_grp_source_p]" in edit_log and \
			       'address-group' in add_ref and \
			       'address-group' in add_g1_ref and \
			       'acl' in add_g2_ref

		del_all_acl_group_wxw(browser)
		del_obj_grp_wxw(browser, name='obj_grp_source')
		del_obj_grp_wxw(browser, name='obj_grp_source_p')
		del_all_obj_address_wxw(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=[dev1, dev2, dev3])
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])









