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

test_id = "139607"


def test_c139607(browser):

	try:
		login_web(browser, url=dev2)
		bridge_add_jyl(browser, bridge_name="br_10")
		bridge_add_jyl(browser, bridge_name="br_11")
		inte_list = get_ipmac_set_interfaces(browser)

		try:
			assert "br_10" in inte_list and "br_11" in inte_list
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "br_10" in inte_list and "br_11" in inte_list

		delete_bridge_byname(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])