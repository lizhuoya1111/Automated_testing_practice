import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_nat import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def_default_hole import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *

test_id = 132456
def test_c132456(browser):
	try:
		login_web(browser, url=dev1)
		get_into_default_hole_jyl(browser, full_selection_rule="diaenable")
		get_into_default_hole_jyl(browser)
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[5]/td[5]/input').click()
		get_into_default_hole_jyl(browser)
		webinfo1 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]/span').text.rstrip()
		get_into_default_hole_jyl(browser, full_selection_rule="diaenable")
		get_into_default_hole_jyl(browser)
		webinfo2 = browser.find_element_by_xpath('//*[@id="pagecmd"]/ul/li[6]/span').text.rstrip()

		try:
			assert "1" in webinfo1
			assert "0" in webinfo2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "1" in webinfo1
			assert "0" in webinfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
