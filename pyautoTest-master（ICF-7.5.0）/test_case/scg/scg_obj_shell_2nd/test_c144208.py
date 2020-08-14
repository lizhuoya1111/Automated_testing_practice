import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_firewall import *
from page_obj.scg.scg_dev import *
from page_obj.common.ssh import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144208"

def test_c144208(browser):

	try:
		login_web(browser, url=dev3)
		# 添加一个addr
		add_obj_address_wxw(browser, name='@_@', desc='zhe是yi个描述1', subnetip='13.1.1.0', subnetmask='24')
		add_log = get_log_info(browser, log_type=管理日志)

		try:
			assert "对象成功，添加内部对象 [@_@]"in add_log
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "对象成功，添加内部对象 [@_@]"in add_log

		# 恢复配置
		del_obj_address_wxw(browser, name='@_@')
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])