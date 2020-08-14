import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139598"


def test_c139598(browser):

	try:
		login_web(browser, url=dev2)
		set_arp_dyn_to_static(browser, ipadd="10.2.2.1")
		edit_static_arp_byipadd(browser, ipadd_index="10.2.2.1", ipadd="10.2.2.11")
		loginfo = get_log_info(browser, log_type=管理日志)
		del_static_arp(browser)
		try:
			assert "成功修改静态条目" in loginfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功修改静态条目" in loginfo


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])