
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

test_id = "143935"

# 添加多条acl，选择其中一条，点击“clone”，然后对克隆出来的acl再次点击“clone”

def test_c143935(browser):
	try:
		login_web(browser, url=dev1)
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		for x in range(1, 6):
			add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_2, dest_zone_interface=interface_name_2)
			sleep(1)

		add_acl_rule_complete_wxw(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3, dest_zone_interface=interface_name_3)
		sleep(2)
		clone_ipv4acl_lzy(browser, group_name='lzy', aclnum='6')
		sleep(2)
		clone_ipv4acl_lzy(browser, group_name='lzy', aclnum='7')
		log1 = get_log(browser, 管理日志)
		# print(log1)

		# 还原
		del_all_acl_group_lzy(browser)
		sleep(2)

		try:
			assert "配置过滤规则对象成功" in log1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "配置过滤规则对象成功" in log1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])






