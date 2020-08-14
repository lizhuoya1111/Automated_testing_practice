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


test_id = "141781"

# 本测试用例包含"shell配置与UI配置的对比检查"


def test_c141781(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route", check_workmode="no")
		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()

		try:
			assert "错误工作模式" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "错误工作模式" in webinfo1

		del_vlan_inte_all(browser)
		physics_interface_change_transparent_interface(browser, intefacex=interface_name_6)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])