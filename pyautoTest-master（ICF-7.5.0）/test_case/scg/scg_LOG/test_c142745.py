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

test_id = 142745


def test_c142745(browser):
	try:
		logfilter_info1_result = logfilter_info2_result = False
		login_web(browser, url=dev1)
		logfilter_info1 = get_logfilter_info(browser)
		for x in range(0, len(logfilter_info1)):
			if '日志服务器' not in logfilter_info1[x][1]:
				logfilter_info1_result = True

		add_log_server_jyl(browser, status="disenable", server_name="日志服务器", ip="192.165.12.3", port="151",
					   format="syslog", protocol="tcp", charset="UTF-8", save="yes")
		logfilter_info2 = get_logfilter_info(browser)
		for x in range(0, len(logfilter_info2)):
			if '日志服务器' in logfilter_info2[x][1]:
				logfilter_info2_result = True

		print(logfilter_info1, logfilter_info2)
		try:
			assert logfilter_info1_result and logfilter_info2_result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert logfilter_info1_result and logfilter_info2_result

		delete_log_server_jyl(browser, log_server="日志服务器")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
