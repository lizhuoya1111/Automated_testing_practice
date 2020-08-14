import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139713"

def test_c139713(browser):

	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_3+".22")
		a.execute("exit")
		get_into_edit_ip_mac_binding_rule_jyl(browser)
		time.sleep(2)
		n = 2
		# 选择接口
		getname1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname1)
		while getname1 != interface_name_3+".22":
			n = n + 1
			getname1 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
			print(getname1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_1")
		a.execute("exit")
		get_into_edit_ip_mac_binding_rule_jyl(browser)
		time.sleep(2)
		n = 2
		# 选择接口
		getname2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
		print(getname2)
		while getname2 != "br_1":
			n = n + 1
			getname2 = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(n) + ']/td[2]').text.rstrip()
			print(getname2)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_3+".22")
		a.execute("no interface bridge br_1")
		a.execute("exit")

		try:
			assert interface_name_3+".22" in getname1
			assert "br_1" in getname2
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert interface_name_3+".22" in getname1
			assert "br_1" in getname2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])