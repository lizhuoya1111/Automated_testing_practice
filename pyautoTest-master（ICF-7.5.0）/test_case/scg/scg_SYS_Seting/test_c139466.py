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


test_id = "139466"



def test_c139466(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员

		for x in ["ntp.fudan.edu.cn", 'pool.ntp.org', 'time.nist.gov', 'time.stdtime.gov.tw', 'time.windows.com' ]:
			set_ntpservers_default(browser, ntpserver=x)
			loginfo = get_log_info(browser, log_type=管理日志, num=5)
			# print(loginfo)
			if '成功修改[ntpserver1]' in loginfo or "no server suitable for synchronization found" in loginfo:
				result = True
			else:
				result = False
				break

		try:
			assert result
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert result

		set_ntpservers_disable(browser)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])