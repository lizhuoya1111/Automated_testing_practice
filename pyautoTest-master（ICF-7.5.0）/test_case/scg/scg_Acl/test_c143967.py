
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

test_id = "143967"

# 1.在子接口中添加ge0/2，vlanid 为2
# 2.在acl中设置源interface为GE0/3，source address选择custom，
#   目的接口选择ge0/2.2，service为all，其他为默认配置
# 来自source address的地址可以穿过DUT
# 63行新增删除默认规则的语句

def test_c143967(browser):
	try:
		login_web(browser, url=dev1)
		# 清除物理接口用到的ip
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev1)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("interface gigabitethernet "+interface_name_2)
		shell_82.execute("no ip address 12.1.1.1")
		shell_82.close()

		# 添加子接口
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="1", work_mode="route")
		sleep(2)
		# 添加子接口ip
		add_vlan_inte_add(browser, interface_name=interface_name_2+'.1', ipadd='12.1.1.1', mask='255.255.255.0')
		# 转换模式使子接口可用
		set_switchmode(hostip1=dev1, interface=interface_name_2, mode="access")

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
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface=interface_name_3,
						source_custom='yes', fromip='13.1.1.3', fromnetmask='255.255.255.0',
						source_address_object='no', dest_zone_interface=interface_name_2+'.1')
		sleep(2)


		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
		print(info1)
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

		# 删子接口
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("no interface vlan "+interface_name_2+".1")
		shell_81.close()

		# 还原物理接口ip
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("interface gigabitethernet "+interface_name_2)
		shell_81.execute("ip address 12.1.1.1 255.255.255.0")
		shell_81.close()

		try:
			assert 'ms' in info1
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert 'ms' in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=[dev1, dev2, dev3])
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])





