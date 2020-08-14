import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 141657

def test_c141657(browser):

	try:
		login_web(browser, url=dev3)
		edit_interface_senior_jyl(browser, interface=interface_name_4, negotiation="强制", speed="1000", duplex="全双工",
							  force_mtu="1397")
		loginfo1 = get_log_info(browser, log_type=管理日志)
		edit_interface_senior_jyl(browser, interface=interface_name_4, negotiation="自动", anto_mtu="1500")

		try:
			assert "成功修改" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功修改" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev3)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])