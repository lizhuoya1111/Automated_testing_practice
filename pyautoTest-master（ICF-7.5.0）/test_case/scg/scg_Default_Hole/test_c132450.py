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

test_id = 132450
def test_c132450(browser):
	try:
		login_web(browser, url=dev1)
		get_into_default_hole_jyl(browser, next_page="yes", previous_page="yes")
		webinfo1 = browser.find_element_by_xpath('//*[@id="button_area"]/ul/li[3]/select').text.rstrip()

		try:
			assert "1" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "1" in webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
