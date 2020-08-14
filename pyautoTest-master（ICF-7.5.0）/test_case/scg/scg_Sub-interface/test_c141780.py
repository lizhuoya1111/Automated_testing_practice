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


test_id = "141780"
test_id1 = "141825"

# 本测试用例包含"shell配置与UI配置的对比检查"


def test_c141780(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route")
		result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		loginfo = get_log_info(browser, 管理日志)
		scg_shell = Shell_SSH()
		scg_shell.connect(hostip=dev1)
		scg_shell.execute("en")
		scg_shell.execute("show inte vlan")
		shell_info = scg_shell.output()
		scg_shell.close()
		try:
			assert result1 is True and " 成功添加 interface" in loginfo and interface_name_6+".11" in shell_info
			rail_pass(test_run_id, test_id)
			rail_pass(test_run_id, test_id1)
		except:
			rail_fail(test_run_id, test_id)
			rail_fail(test_run_id, test_id1)
			assert result1 is True and " 成功添加 interface" in loginfo and interface_name_6+".11" in shell_info

		del_vlan_inte_all(browser)
		physics_interface_change_transparent_interface(browser, interface6=interface_name_6)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		rail_fail(test_run_id, test_id1)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])