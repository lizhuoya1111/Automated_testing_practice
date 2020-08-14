import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *

test_id = 139268
def test_c139268(browser):
	try:
		login_web(browser, url=dev1)
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="22", work_mode="route")
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".22")
		a.execute("ip address 131.1.1.1 255.255.255.0")
		a.execute("exit")
		dhcp_server_add(browser, interface=interface_name_3+".22", dhcp_type="dhcp_rely", dhcp_rely_server1="131.1.1.6")
		time.sleep(3)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_3+".22")
		a.execute("exit")
		crtinfo = a.output()
		print(crtinfo)
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		time.sleep(1)
		del_vlan_inte_all(browser)
		time.sleep(1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".22")
		a.execute("no ip address 131.1.1.1 255.255.255.0")
		a.execute("exit")
		try:
			assert "接口不允许删除" in crtinfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "接口不允许删除"in crtinfo
	except Exception as err:
		# # 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
