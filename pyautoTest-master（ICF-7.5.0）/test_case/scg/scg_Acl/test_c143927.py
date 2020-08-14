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

test_id = "143927"
# 添加分组 3
# 添加一个组，名字为字母开头的32位字符，以zone/interface当作分组条件，点击confirm


def test_c143927(browser):

	try:
		login_web(browser, url=dev1)
		for x in range(0, 10):
			add_acl_group_complete(browser, name='test'+str(x), enable='yes', sour='Z:any', dest='Z:any',
								   desc='miaoshu', save='yes', cancel='no')
		for y in range(0, 10):
			for i in range(0, 10):
				add_acl_rule_complete_wxw(browser, aclgroup_name='test' + str(i),
										  source_zone_interface=interface_name_4,
										  toip='13.1.1.0', tonetmask='24', dest_zone_interface=interface_name_3)
		del_acl_group_wxw(browser, name='test9')
		loginfo = get_log_info(browser, 管理日志)
		# print(loginfo)
		# del_acl_group_wxw(browser, name='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
		# del_all_acl_group_wxw(browser)

		try:
			assert "配置过滤规则对象成功，删除内部对象" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置过滤规则对象成功，删除内部对象" in loginfo

		del_all_acl_group_wxw(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])