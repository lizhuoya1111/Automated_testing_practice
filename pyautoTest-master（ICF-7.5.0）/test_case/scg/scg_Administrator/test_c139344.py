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
test_id = 139344


def test_c139344(browser):
	try:
		# 登录函数
		login_web(browser, url=dev1)
		configuer(browser)
		time.sleep(2)
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
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


def configuer(browser):
	sys_set_jyl(browser, frozen_time="86400", expire_time="3600", retry="5")


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
