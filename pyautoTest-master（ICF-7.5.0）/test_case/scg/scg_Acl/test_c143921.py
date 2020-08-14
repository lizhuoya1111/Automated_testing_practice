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

test_id = "143921"
# 根据分组添加规则 3
# 1.添加一个分组，以interface为分组条件
# 2.添加一条acl，源来自物理接口，源ip选择source address下拉框中，目的到达vlan，目的IP是custom，选择service，action是accept，点击confirm
# 可以正常添加，adminlog记录正常，shell下查看正常


def test_c143921(browser):

	try:
		login_web(browser, url=dev1)

		# 添加一个vlan
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("vlan 1")
		a.execute("exit")
		a.execute("exit")

		add_acl_group_complete(browser, name='acl_group_921', enable='yes', sour=interface_name_3, dest='Z:any', desc='miaoshu',
							   save='yes', cancel='no')

		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_921', source_zone_interface=interface_name_4,
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='yes', toip='13.1.1.0', tonetmask='24',
								  dest_address_object='no', d_address_object='A:any',
								  dest_zone_interface=interface_name_3+'.1',
								  service='P:any', schdule='-- 无 --',
								  accept='yes', drop='no',
								  auth='-- 无 --', icf='no', log='no')

		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)

		del_acl_group_wxw(browser, name='acl_group_921')

		# 删除一个vlan
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_3+".1")
		a.execute("vlan 1")
		a.execute("exit")
		a.execute("exit")


		try:
			assert "配置过滤规则对象成功" in loginfo
			assert "过滤操作为 [accept]"in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置过滤规则对象成功" in loginfo
			assert "过滤操作为 [accept]" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])