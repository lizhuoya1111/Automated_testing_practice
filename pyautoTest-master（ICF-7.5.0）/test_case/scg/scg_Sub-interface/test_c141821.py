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

test_id = "141821"

def test_c141821(browser):
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
		a.execute("exit")
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("show interface vlan "+interface_name_2+".22")
		a.execute("exit")
		result = a.output()
		a.close()

		a = Shell_SSH()
		a.connect(dev3)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan EXT.22")
		a.execute("interface gigabitethernet "+interface_name_2)
		a.execute("ip address 13.1.1.3 24")
		a.execute("exit")
		a.close()
		time.sleep(1)
		try:
			assert "Work-mode: route" and "inet-addr:13.1.1.3/255.255.255.0" in result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Work-mode: route" and "inet-addr:13.1.1.3/255.255.255.0" in result

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])