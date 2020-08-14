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

test_id = 142746


def test_c142746(browser):
	try:
		login_web(browser, url=dev1)
		add_log_server_jyl(browser, status="disenable", server_name="日志服务器", ip="192.165.12.3", port="151",
					   format="syslog", protocol="tcp", charset="UTF-8", save="yes")
		logs_info1 = get_logserver_info(browser, server_name="日志服务器")

		# print(logs_info1)
		try:
			assert '192.165.12.3' in logs_info1[0] and '151' in logs_info1[1] and 'syslog' in logs_info1[2] and \
			       'tcp' in logs_info1[3] and 'UTF-8' in logs_info1[4] and 'enable' in logs_info1[5]
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert '192.165.12.3' in logs_info1[0] and '151' in logs_info1[1] and 'syslog' in logs_info1[2] and \
			       'tcp' in logs_info1[3] and 'UTF-8' in logs_info1[4] and 'enable' in logs_info1[5]

		delete_log_server_jyl(browser, log_server="日志服务器")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
