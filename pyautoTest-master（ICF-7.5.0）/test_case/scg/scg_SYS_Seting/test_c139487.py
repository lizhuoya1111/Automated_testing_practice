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


test_id = "139487"


def test_c139487(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		set_ntpservers_default(browser, ntpserver='time.nist.gov')
		itest_ntpservers(browser, servers_option="default")
		time1 = get_time_time_lzy(browser)
		hour1 = time1[0:2]
		min1 = time1[3:5]
		second1 = time1[6:8]
		# print(time1, hour1, min1, second1)

		set_dns(browser, dns1="", dns2="")
		set_ntpservers_interval(browser, interval='1')
		time.sleep(61)
		time2 = get_time_time_lzy(browser)
		hour2 = time1[0:2]
		min2 = time2[3:5]
		second2 = time2[6:8]
		# print(time2, hour2, min2, second2)

		result = ""
		if int(hour2) < int(hour1):
			if int(min2) < int(min1):
				if int(second2) < int(second1):
					result = False
				else:
					result = True
			else:
				result = True
		else:
			result = True

		try:
			assert result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result

		set_dns(browser, dns1="114.114.114.114")
		set_ntpservers_disable(browser)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])