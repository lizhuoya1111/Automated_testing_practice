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


test_id = "139470"


def test_c139470(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		set_ntpservers_user(browser, ntpserver1='ntp7.aliyun.com')
		itest_ntpservers(browser, servers_option="server1")
		loginfo = get_log_info(browser, log_type=管理日志, num=3)
		# print(loginfo)
		set_ntpservers_interval(browser, interval='1')
		time.sleep(61)
		loginfo1 = get_log_info(browser, log_type=管理日志)
		# print(loginfo1)
		try:
			assert '成功修改[date' in loginfo
			assert '成功修改[ntpserver2]为[ntp7.aliyun.com]' in loginfo
			assert "成功修改[date" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert '成功修改[date' in loginfo
			assert '成功修改[ntpserver2]为[ntp7.aliyun.com]' in loginfo
			assert "成功修改[date" in loginfo1

		set_ntpservers_disable(browser)
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])