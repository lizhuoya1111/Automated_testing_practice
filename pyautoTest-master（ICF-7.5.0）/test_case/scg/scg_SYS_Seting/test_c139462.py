import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "139462"



def test_c139462(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		set_dns(browser, dns2="202.103.24.68")
		dns_info = get_dns(browser)
		log_info = get_log_info(browser, 管理日志)

		try:
			assert "202.103.24.68" in log_info and "202.103.24.68" in dns_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "202.103.24.68" in log_info and "202.103.24.68" in dns_info

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False

	set_dns(browser, dns1="114.114.114.114")
	set_dns(browser, dns2=" ")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])