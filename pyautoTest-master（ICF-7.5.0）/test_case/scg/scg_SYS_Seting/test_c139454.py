import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "139454"



def test_c139454(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		edit_sysinfo(browser, hostname="防火墙")
		# time.sleep(1)
		result1 = get_sys_info_hostname(browser)

		edit_sysinfo(browser, hostname="firewall")
		# time.sleep(1)
		result2 = get_sys_info_hostname(browser)

		edit_sysinfo(browser, hostname="firewall-1")
		# time.sleep(1)
		result3 = get_sys_info_hostname(browser)

		edit_sysinfo(browser, hostname="firewall_1")
		# time.sleep(1)
		result4 = get_sys_info_hostname(browser)

		edit_sysinfo(browser, hostname="防火墙防火墙防火墙防")
		# time.sleep(1)
		result5 = get_sys_info_hostname(browser)

		edit_sysinfo(browser, hostname="123abcabcabcabcabcabcabcabcabcab")
		# time.sleep(1)
		result6 = get_sys_info_hostname(browser)
		loginfo = get_log_info(browser, 管理日志)

		try:
			assert result1 == "防火墙" and result2 == "firewall" and result3 == "firewall-1" and result4 == "firewall_1" and result5 == "防火墙防火墙防火墙防" and result6 == "123abcabcabcabcabcabcabcabcabcab" and "123abcabcabcabcabcabcabcabcabcab" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result1 == "防火墙" and result2 == "firewall" and result3 == "firewall-1" and result4 == "firewall_1" and result5 == "防火墙防火墙防火墙防" and result6 == "123abcabcabcabcabcabcabcabcabcab" and "123abcabcabcabcabcabcabcabcabcab" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])