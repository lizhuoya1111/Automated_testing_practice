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

test_id = "143926"
# 修改acl 1
# 1.添加一个分组，以interface为分组条件，其他为默认条件
# 2.添加acl，动作为drop
# 3.修改该acl的动作为accept
# 修改成功


def test_c143926(browser):

	try:
		login_web(browser, url=dev3)

		for y in range(0, 5):
			add_acl_group_complete(browser, name='acl_group_'+str(y), enable='yes', sour=interface_name_3, dest='Z:any',
		                       desc='miaoshu',
		                       save='yes', cancel='no')


		for x in range(0, 1):
			for i in range(0,5):
				add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_'+str(i), source_zone_interface=interface_name_4,
		                          toip='13.1.1.0', tonetmask='24', dest_zone_interface=interface_name_3)

		for z in range(6, 1, -1):
			move_ipc4_acl_group_simple(browser, group_id=str(z), move="up")
			time.sleep(3)


		group_name = get_groupname_byid(browser, group_id="1")
		# print(group_name)

		loginfo1 = get_log_info(browser, 管理日志)
		# print(loginfo1)


		try:
			assert "成功移动组" in loginfo1 and "acl_group_4" in group_name
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "成功移动组" in loginfo1 and "acl_group_4" in group_name

		for h in range(0, 5):
			del_acl_group_wxw(browser, name='acl_group_'+str(h))
			time.sleep(1)


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev3)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])