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

test_id = "139643"


def test_c139643(browser):

	try:
		login_web(browser, url=dev1)
		add_static_arp_jyl(browser, ip="12.1.1.2", interface=interface_name_2, mac_add="auto_mac",
						   host_name="manual_host", host="主机82")
		loginfo = get_log(browser, 管理日志)
		delete_static_arp_jyl(browser, static_arp_ip="12.1.1.2")
		try:
			assert "成功" in loginfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])