
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
from page_obj.scg.scg_def_obj import *

test_id = "143972"

# 1.添加一个zone，名称为zone01，在其中选择几个物理接口
# 2.添加一个address对象，名称为obj1
# 3.在acl中设置源为zone，source address选择defined，目的地址选择all，
# service为all，动作为deny，其他为默认配置
# 来自该zone的地址不能穿过DUT

def test_c143972(browser):
	try:

		# 添加zone1
		login_web(browser, url=dev1)
		add_obj_zone(browser, name='zone1', desc='1', zone_mem=[interface_name_2, interface_name_3])

		# 添加地址对象
		add_obj_address_wxw(browser, name='a', subnetip='13.1.1.3')

		# 配路由使8283通
		# 82上添加经过81到83路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()

		# 83上添加经过81到82的路由
		shell_83 = Shell_SSH()
		shell_83.connect(hostip=dev3)
		shell_83.execute("en")
		shell_83.execute("conf t")
		shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		shell_83.close()

		# 删除默认规则
		del_default_acl_group_lzy(browser)
		sleep(2)
		# 添加组，添加规则
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface='Z:zone1',
						source_address_object='yes', s_address_object='A:a', drop='yes')
		sleep(2)

		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=10)
		print(info1)
		sleep(2)


		# 登录81，修改规则为accept
		login_web(browser, url=dev1)
		edit_acl_rule_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:zone1',
						source_address_object='yes', s_address_object='A:a')
		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info2 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=5)
		print(info2)
		sleep(2)

		# 还原
		# 删ACL
		login_web(browser, url=dev1)
		del_all_acl_group_lzy(browser)
		sleep(2)

		# 删82上路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()


		# 删83上路由
		shell_83 = Shell_SSH()
		shell_83.connect(hostip=dev3)
		shell_83.execute("en")
		shell_83.execute("conf t")
		shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		shell_83.close()

		# 删除zone和地址对象
		del_obj_zone_byname(browser, name='zone1')
		del_obj_address_wxw(browser, name='a')

		try:
			assert 'Destination Host Unreachable' in info1 and 'ms' in info2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert 'Destination Host Unreachable' in info1 and 'ms' in info2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=[dev1, dev2, dev3])
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





