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
from page_obj.scg.scg_def_ipsec import *

test_id = "141830"

def test_c141830(browser):
	try:
		login_web(browser, url=dev3)
		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("no ip address 13.1.1.3")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_2+".22")
		a.execute("ip address 13.1.1.3 24")
		a.execute("work-mode route")
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_2+".22")
		a.execute("no ip address 13.1.1.3")
		a.execute("work-mode transparent")
		a.execute("ip address 13.1.1.3 24")
		a.execute("exit")
		result1 = a.output()
		a.close()

		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_2+".22")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 13.1.1.3 24")
		a.execute("exit")
		a.close()

		time.sleep(1)
		try:
			assert "接口工作在透明模式" in result1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "接口工作在透明模式" in result1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])