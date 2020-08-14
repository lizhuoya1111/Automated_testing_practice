import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_reporter import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 139845


def test_c139845(browser):

	try:
		login_web(browser, url=dev1)
		reporter_switch(browser, interface="yes", traffic="yes", session="no", system="yes", action="保存")
		loginfo = get_log_info(browser, 管理日志, num=4)
		# print(loginfo)
		# time.sleep(60)
		try:
			assert "[reporter:interface ]对象成功 : [status:enable]" in loginfo
			assert "[reporter: traffic ]对象成功 : [status:enable]" in loginfo
			assert "[reporter: session ]对象成功 : [status:disable]" in loginfo
			assert "[reporter: system ]对象成功 : [status:enable]" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "[reporter:interface ]对象成功 : [status:enable]" in loginfo
			assert "[reporter: traffic ]对象成功 : [status:enable]" in loginfo
			assert "[reporter: session ]对象成功 : [status:disable]" in loginfo
			assert "[reporter: system ]对象成功 : [status:enable]" in loginfo

		reporter_switch(browser, interface="no", traffic="yes", session="yes", system="no", action="保存")
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])