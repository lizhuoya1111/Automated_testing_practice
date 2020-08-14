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
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 139250
def test_c139250(browser):
	try:
		login_web(browser, url=dev1)
		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_3)
		b.execute("no ip address 13.1.1.1")
		b.execute("work-mode transparent")
		b.execute("exit")
		dhcp_server_add(browser, interface=interface_name_3,
		                dhcp_type="dhcp_server", dhcp_gw="131.1.1.254", dhcp_sm="24",
		                dns_server1="114.114.114.114", wins_server1="115.115.115.115",
		                ip_range1_1="131.1.1.5", ip_range1_2="131.1.1.20")
		time.sleep(1)
		webinfo1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]/span').text.rstrip()
		# print(webinfo1)
		time.sleep(1)
		dhcp_server_edit_or_delete(browser, fuction="delete")
		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_3)
		b.execute("work-mode route")
		b.execute("ip address 13.1.1.1 24")
		b.execute("exit")
		try:
			assert "未定" == webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "未定" == webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
