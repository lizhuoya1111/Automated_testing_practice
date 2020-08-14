import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_bridge import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141864

def test_c141864(browser):

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
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="transprent")
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="22", work_mode="transprent")

		# 添加网桥
		bridge_add_jyl(browser, bridge_name="br_1")

		# 添加网桥接口
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2+".22")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_3+".22")

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

		# no掉物理接口的地址
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 12.1.1.2")
		a.execute("ip address 13.1.1.5 24")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.5")
		time.sleep(5)
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("ping 13.1.1.5")
		time.sleep(5)
		result1 = a.output()
		a.close()
		print(result1)

		delete_bridge_byname(browser, br_name="br_1")

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")
		del_vlan_inte_by_name(browser, interface_name=interface_name_3+".22")

		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.5")
		a.execute("ip address 12.1.1.2 24")
		a.execute("exit")
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