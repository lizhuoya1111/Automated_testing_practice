
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_ospf import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 140888
def test_c140888(browser):
	try:
		login_web(browser, url=dev1)
		start_ospf_jyl(browser)
		time.sleep(0.5)
		ospf_general_jyl(browser, route_id="manual", manual_ip="192.168.1.1", save="yes")
		loginfo1 = get_log_info(browser, 管理日志)
		add_ospf_network_jyl(browser, network="192.165.16.3", mask="24", area_id="22", save="yes")
		loginfo2 = get_log_info(browser, 管理日志)
		edit_ospf_interface_jyl(browser, ospf_interface="br_0", auth_type="md5", message_digest_key="25", md5_key="12",
								save="yes")
		loginfo3 = get_log_info(browser, 管理日志)
		edit_ospf_interface_jyl(browser, ospf_interface="br_0", priority="1", hello_interval="10", dead_interval="40",
								auth_type="无", save="yes")
		delete_ospf_network_jyl(browser, ospf_neteork_ip="all")
		ospf_general_jyl(browser, route_id="auto", save="yes")
		time.sleep(0.5)
		# print(loginfo1)
		stop_ospf_jyl(browser)
		try:
			assert "成功设置" in loginfo1
			assert "成功添加" in loginfo2
			assert "成功修改" in loginfo3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功设置" in loginfo1
			assert "成功添加" in loginfo2
			assert "成功修改" in loginfo3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
