
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

test_id = "143985"

# 1.在接口上添加br_0,br_1，br_0的成员为ge0/2，br_1的成员为ge0/3
# 2.在acl的源接口引用br0，目的接口引用br1，其他为默认配置
# 3.pca接在ge0/2上，pcb接在ge0/3上面，从pca ping pcb

def test_c143985(browser):
	try:
		# 81#2#3变为透明模式
		login_web(browser, url=dev1)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.1")
		delete_physical_interface_ip_jyl(browser, interface=interface_name_3, ip="13.1.1.1")
		physics_interface_change_transparent_interface(browser, interface2=interface_name_2, interface3=interface_name_3)

		# 添加br_1（#2）   br_2（#3）
		bridge_add_jyl(browser, bridge_name="br_2")
		bridge_add_jyl(browser, bridge_name="br_3")
		bridge_edit_interface_jyl(browser, bridge_interface="br_2", interface=interface_name_2)
		bridge_edit_interface_jyl(browser, bridge_interface="br_3", interface=interface_name_3)
		bridge_ip_add(browser, bridge_interface="br_2", ip="12.1.1.1", mask="255.255.255.0")
		bridge_ip_add(browser, bridge_interface="br_3", ip="13.1.1.1", mask="255.255.255.0")
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
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface='br_3', dest_zone_interface='br_2')
		sleep(2)

		# 登录83，看能否ping通82
		login_web(browser, url=dev3)
		sleep(1)
		info1 = diag_ping(browser, ipadd="12.1.1.2", interface=interface_name_2)
		print(info1)
		sleep(2)

		# 还原
		# 删除ACL
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

		# 删网桥
		delete_bridge_byname(browser)

		# 接口改模式加ip
		transparent_interface_change_physics_interface_lzy(browser, interface2=interface_name_2, interface3=interface_name_3)
		add_physical_interface_ip_wxw(browser, interface=interface_name_2, ip='12.1.1.1', mask='255.255.255.0')
		add_physical_interface_ip_wxw(browser, interface=interface_name_3, ip='13.1.1.1', mask='255.255.255.0')
		# 用SSH方法转换工作模式加ip
		# shell_81 = Shell_SSH()
		# shell_81.connect(hostip=dev1)
		# shell_81.execute("en")
		# shell_81.execute("conf t")
		# shell_81.execute("interface gigabitethernet EXT")
		# shell_81.execute("work-mode route")
		# shell_81.execute("ip address 12.1.1.1 24")
		# shell_81.execute("exit")
		# shell_81.execute("interface gigabitethernet P0")
		# shell_81.execute("work-mode route")
		# shell_81.execute("ip address 13.1.1.1 24")
		# shell_81.close()

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





