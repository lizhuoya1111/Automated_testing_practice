import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *

test_id = "141841"

def test_c141841(browser):
	try:
		# 关闭85上的ge0/2，防止干扰，因为下面需要用到30.1.1.1
		login_web(browser, url=dev5)
		physical_interface_switch(browser, interface=interface_name_2, status="disable")

		login_web(browser, url=dev1)
		# 点击管理员
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")

		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="20", work_mode="route")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		add_vlan_inte_add(browser, interface_name=interface_name_4 + ".20", ipadd="20.1.1.1", mask="24")

		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="30", work_mode="route")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		add_vlan_inte_add(browser, interface_name=interface_name_4 + ".30", ipadd="30.1.1.1", mask="24")


		# 81的命令行,将4口设备为access模式
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  access")
		shell_81.close()

		# PC2上添加30.1.1.0的路由
		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route add -net 30.1.1.0/24 gw 20.1.1.1')
		shell_pc2.close()

		# PC1上添加20.1.1.0的路由
		shell_pc2 = SSH('10.1.1.230', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route add -net 20.1.1.0/24 gw 30.1.1.1')
		shell_pc2.close()

		# pc1 ping pc2
		shell_pc2 = SSH('10.1.1.230', 'root', 'root', 22)
		shell_pc2.connect()
		result = shell_pc2.execute('ping 20.1.1.2 -c 8 -i 0.1')
		shell_pc2.close()


		try:
			assert "ttl" in result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ttl" in result

		# 删除子接口
		del_vlan_inte_all(browser)
		# 还原物理接口地址
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')
		shell_81 = Shell_SSH()
		shell_81.connect(hostip=dev1)
		shell_81.execute("en")
		shell_81.execute("conf t")
		shell_81.execute("inte gigabitethernet " + interface_name_4)
		shell_81.execute("switchmode  trunk")
		shell_81.close()
		# 删除路由

		shell_pc2 = SSH('10.1.1.202', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route del -net 30.1.1.0/24 gw 20.1.1.1')
		shell_pc2.close()

		shell_pc2 = SSH('10.1.1.230', 'root', 'root', 22)
		shell_pc2.connect()
		shell_pc2.execute('route del -net 20.1.1.0/24 gw 30.1.1.1')
		shell_pc2.close()


		login_web(browser, url=dev5)
		physical_interface_switch(browser, interface=interface_name_2, status="enable")

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev5])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])