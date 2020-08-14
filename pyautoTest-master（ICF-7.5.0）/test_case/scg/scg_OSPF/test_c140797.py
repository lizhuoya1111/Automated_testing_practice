
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_ospf import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 140797
def test_c140797(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_4+".44")
		a.execute("exit")
		a.close()
		start_ospf_jyl(browser)
		time.sleep(0.5)
		web_info1 = get_ospf_interface_name_jyl(browser)
		print(web_info1)
		time.sleep(0.5)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_4+".44")
		a.execute("exit")
		a.close()
		stop_ospf_jyl(browser)
		# 诊断错误！等待修改
		try:
			assert ['br_0', '1', '10', '40', 'none'] and ['MGMT', '1', '10', '40', 'none'] \
				   and ['P1.44', '1', '10', '40', 'none'] in web_info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert ['br_0', '1', '10', '40', 'none'] and ['MGMT', '1', '10', '40', 'none'] \
				   and ['P1.44', '1', '10', '40', 'none'] in web_info1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
