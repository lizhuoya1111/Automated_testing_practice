import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *

test_id = "21685"


def test_c21685(browser):

	login_web(browser)
	set_dns(browser)
	logo_info = get_log_info(browser, 管理日志)
	if "成功修改[dns]" in logo_info:
		ping = Shell_SSH()
		ping.connect("10.2.2.81")
		ping.execute("en")
		ping.execute("conf t")
		ping.execute("ip route 0.0.0.0/0 gateway 10.2.2.1")
		ping.execute("exit")
		ping.execute("ping www.163.com")
		time.sleep(3)
		ping_info = ping.output()
		print(ping_info)
		try:
			assert "Round-trip" in ping_info
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "Round-trip" in ping_info

		ping.execute("conf t")
		ping.execute("no ip route 0.0.0.0/0 gateway 10.2.2.1")
		print("删除默认路由完成")
		ping.execute("exit")
		ping.execute("exit")
	else:
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
