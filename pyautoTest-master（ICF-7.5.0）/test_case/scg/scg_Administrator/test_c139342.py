import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_button import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
test_id = 139342
# 未通过测试

def test_c139342(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		configuer(browser)
		loginfo = get_log(browser, 管理日志)
		# print(loginfo)

		try:
			assert "修改" in loginfo
			assert "设置成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "修改" in loginfo
			assert "设置成功" in loginfo

		sys_set_jyl(browser)
		for x in range(1, 5):
			browser.refresh()
		login_web(browser, url=dev1)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		reload(hostip=dev1, port=33)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	sys_set_jyl(browser, ssh_port="33", ssh_timeout="86400", https_port="446", https_timeout="86400",
	            telent_port="23", telent_timeout="86400", console_timeout="86400", frozen_time="600",
	            expire_time="600", retry="3")
	# time.sleep(30)
	for x in range(1, 5):
		browser.refresh()
	time.sleep(2)
	login_web(browser, url=dev1+str(":446"))


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])