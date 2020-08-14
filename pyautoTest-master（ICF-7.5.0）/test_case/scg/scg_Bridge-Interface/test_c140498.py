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


test_id = 140498
def test_c140498(browser):
	try:
		login_web(browser, url=dev1)
		i = 1
		gat_valu_list1 = []

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 13.1.1.1")
		while i <= 5:
			a.execute("work-mode transparent")
			browser.refresh()
			get_into_bri_jyl(browser)
			webinfo = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
			gat_valu_list1.append(webinfo)
			a.execute("work-mode route")
			# a.close()
			i += 1
		a.close()
		# print(gat_valu_list1)
		n = 1
		gat_valu_list2 = []

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		while n <= 5:
			a.execute("interface vlan "+interface_name_3+"."+str(n))
			a.execute("work-mode transparent")
			browser.refresh()
			get_into_bri_jyl(browser)
			webinfo = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
			gat_valu_list2.append(webinfo)
			a.execute("work-mode route")
			a.execute("exit")
			# a.close()
			n += 1
		a.close()
		# print(gat_valu_list2)
		n = 1
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		while n <= 5:
			a.execute("no interface vlan "+interface_name_3+"."+str(n))
			# print("del:interface vlan "+interface_name_3+"."+str(n))
			n += 1
			time.sleep(1)
		webinfo1 = gat_valu_list1[0]
		webinfo2 = gat_valu_list2[0]
		a.close()

		# print(webinfo1)
		# print(webinfo2)
		b = Shell_SSH()
		b.connect(dev1)
		b.execute("en")
		b.execute("conf t")
		b.execute("interface gigabitethernet "+interface_name_3)
		b.execute("ip address 13.1.1.1 24")
		b.execute("exit")
		b.close()

		try:
			assert interface_name_3 in webinfo1
			assert interface_name_5 in webinfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert interface_name_3 in webinfo1
			assert interface_name_5 in webinfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
