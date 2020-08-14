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

test_id = 139694
def test_c139694(browser):
	try:
		login_web(browser, url=dev1)
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="open")
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="close")
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="open")
		synchronization_ip_mac_banding_and_static_arp_(browser, banding_static="close")
		loginfo1 = get_log(browser, 管理日志)
		try:
			assert "成功设置" in loginfo1

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功设置" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
