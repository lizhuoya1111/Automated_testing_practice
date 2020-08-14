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

test_id = "139691"

def test_c139691(browser):

	try:
		login_web(browser, url=dev3)
		add_ip_mac_binding_jyl(browser, ip="192.165.12.3", interface=interface_name_5, mac_add="manual_mac",
						   mac="00:16:31:e5:7a:23", host_name="manual_host", host="主机1")
		add_ip_mac_binding_jyl(browser, ip="192.165.12.3", interface=interface_name_5, mac_add="manual_mac",
						   mac="00:16:89:e5:7a:23", host_name="manual_host", host="主机2")
		loginfo = get_log_info(browser, log_type=管理日志)
		del_bindinglist(browser, index_list="all")

		try:
			assert "失败" in loginfo
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "失败" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])