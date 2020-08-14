import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "143923"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143923(browser):

	try:
		login_web(browser, url=dev3)

		add_acl_group_complete(browser, name='acl_group_923', enable='yes', sour=interface_name_3, dest='Z:any', desc='miaoshu',
							   save='yes', cancel='no')

		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_923', source_zone_interface=interface_name_4,
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='13.1.1.0', tonetmask='24',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface=interface_name_3,
								  service='P:any', schdule='-- 无 --',
								  accept='no', drop='yes',
								  auth='-- 无 --', icf='no', log='no')
		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)

		edit_acl_rule_wxw(browser, aclgroup_name='acl_group_923', accept='yes', drop='no')

		loginfo2 = get_log_info(browser, 管理日志)
		# print(loginfo2)

		del_acl_group_wxw(browser, name='acl_group_923')


		try:
			assert "配置过滤规则对象成功，添加内部对象" in loginfo1
			assert "过滤操作为 [drop]" in loginfo1
			assert "配置过滤规则对象成功，修改内部对象" in loginfo2
			assert "过滤操作为 [accept]"in loginfo2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置过滤规则对象成功，添加内部对象" in loginfo1
			assert "过滤操作为 [drop]" in loginfo1
			assert "配置过滤规则对象成功，修改内部对象" in loginfo2
			assert "过滤操作为 [accept]" in loginfo2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev3)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])