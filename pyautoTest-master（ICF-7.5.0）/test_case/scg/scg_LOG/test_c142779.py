import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *

test_id = 142779


def test_c142779(browser):
	try:
		login_web(browser, url=dev1)
		edit_log_filter(browser, index=1, level=["alert", "critical"])
		logfilter_info1 = get_logfilter_info(browser)
		# print(logfilter_info1)
		edit_log_filter(browser, index=9, level='全部')
		logfilter_info2 = get_logfilter_info(browser)
		# print(logfilter_info2)

		try:
			assert "critical alert" in logfilter_info1[0][3] and "all" in logfilter_info1[1][3]
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "critical alert" in logfilter_info1[0][3] and "all" in logfilter_info1[1][3]

		edit_log_filter(browser, index=1, level='全部')
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
