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

test_id = "141782"

def test_c141782(browser):
	try:
		login_web(browser, url=dev3)
		add_vlan_inte(browser, physicl_interface=interface_name_3, vlan_id="33", work_mode="route")
		loginfo = get_log_info(browser, 管理日志)
		del_vlan_inte_by_name(browser, interface_name=interface_name_3+".33")

		try:
			assert "成功添加" in loginfo
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功添加" in loginfo

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])