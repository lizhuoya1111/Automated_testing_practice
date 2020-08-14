import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140484
def test_c140484(browser):
	try:
		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")
		loginfo1 = get_log(browser, 管理日志)

		bridge_ip_add(browser, bridge_interface="br_1", address_mode="manual", ip="192.165.12.2", mask="24")
		loginfo2 = get_log(browser, 管理日志)

		delete_bridge_byname(browser, br_name="br_1")
		loginfo3 = get_log(browser, 管理日志)

		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "成功" in loginfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
