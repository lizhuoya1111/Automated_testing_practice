import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *

test_id = "141806"

def test_c141806(browser):
	try:
		login_web(browser, url=dev3)
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="22", work_mode="transparent")
		bridge_add_jyl(browser, bridge_name="br_1")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_2+".22") 
		del_vlan_inte_by_name(browser, interface_name=interface_name_2+".22")
		loginfo1 = get_log_info(browser, 管理日志)
		delete_bridge_byname(browser, br_name="br_1")

		try:
			assert "成功删除" in loginfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功删除" in loginfo1

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])