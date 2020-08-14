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

test_id = "139637"


def test_c139637(browser):

	try:
		login_web(browser, url=dev1)
		# mac_5 = get_dut_interface_mac_jyl(dut_name=dev1, interface=interface_name_5).lower()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("bridge-member "+interface_name_5)
		a.execute("exit")
		a.close()
		mac_5 = get_dut_interface_mac_jyl(dut_name=dev1, interface=interface_name_5).lower()
		add_bri_mac_jyl(browser, bri_serch="open", bridge="br_0", mac_serach="open", mac=mac_5)
		webinfo = browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text.rstrip()
		# print(webinfo)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("no bridge-member "+interface_name_5)
		a.execute("exit")

		try:
			assert "00" in webinfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "00" in webinfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])