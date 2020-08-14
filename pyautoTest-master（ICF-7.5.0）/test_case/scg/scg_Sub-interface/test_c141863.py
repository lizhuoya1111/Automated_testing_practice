import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141863

def test_c141863(browser):

	try:
		login_web(browser, url=dev1)

		# no掉物理接口的地址
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.1")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		a.close()

		# 添加子接口
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="route")
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="22", work_mode="route")

		# 子接口添加IP地址
		add_vlan_inte_add(browser, interface_name=interface_name_2+".22", ipadd="12.1.1.1", mask="24")
		add_vlan_inte_add(browser, interface_name=interface_name_3+".22", ipadd="13.1.1.1", mask="24")

		# 改变接口的转换模式
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("switchmode access")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("switchmode access")
		a.close()

		# 82上配置去往83的路由
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.close()

		# 83上配置去往82的路由
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 12.1.1.2")
		result1 = a.output()
		a.close()
		# print(result1)

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")
		del_vlan_inte_by_name(browser, interface_name=interface_name_3+".22")

		# no掉82上配置去往83的路由
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		a.close()

		# no掉83上配置去往82的路由
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		a.close()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 12.1.1.1 24")
		a.execute("exit")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("ip address 13.1.1.1 24")
		a.close()

		time.sleep(0.5)

		try:
			assert "ms" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=[dev1, dev2, dev3])
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])