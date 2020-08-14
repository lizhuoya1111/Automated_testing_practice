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

test_id = "139634"


def test_c139634(browser):

	try:
		login_web(browser, url=dev1)
		into_fun(browser, 桥MAC表)
		browser.switch_to.default_content()
		# 定位到
		browser.switch_to.frame("header")
		webinfo = browser.find_element_by_xpath('//*[@id="header_postion_span"]').text.rstrip()
		print(webinfo)
		try:
			assert "桥MAC表" == webinfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "桥MAC表" == webinfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])