import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_route import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
test_id = "139568"
def test_c139568(browser):
	try:
		login_web(browser, url=dev1)
		set_language(browser, language_sw="繁体中文")
		time.sleep(1)
		set_language(browser, language_sw="英文")
		time.sleep(1)
		set_language(browser, language_sw="简体中文")
		info1 = diag_ping(browser, ipadd="13.1.1.3", packersize="40", count="10", ping_wait_time="2", interface=interface_name_3)
		try:
			assert "ms" in info1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "ms" in info1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])