
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

test_id = "143974"

# DUT上filter rule配置为默认，源mac地址为非PC机的网卡mac地址。
# 验证PC机无法ping通server。

def test_c143974(browser):
	try:

		login_web(browser, url=dev1)

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
		# 添加组，添加规则（mac非PC机的网卡mac地址）
		add_ipv4_aclgroup_lzy(browser, group_name='lzy')
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', mac='00:16:31:EE:03:22')
		sleep(2)

		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=10)
		# print(info1)
		sleep(2)

		# 登录81，mac为正确地址
		login_web(browser, url=dev1)
		edit_acl_rule_wxw(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
						  mac=mac_dev3_interface_2, dest_zone_interface='Z:any')

		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info2 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2, timesleep=5)
		# print(info2)
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





