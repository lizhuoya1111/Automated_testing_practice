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


test_id = "141890"




def test_c141890(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		num = 10
		for x in ["|", ";", "#", "$", ","]:
			# print(x)
			num += 1
			add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id=str(num), work_mode="route", describe=x)
			info1 = browser.switch_to_alert().text
			browser.switch_to_alert().accept()
			if "描述格式输入错误，请重新输入。" not in info1:
				info1 = False
				break

		try:
			assert info1 is not False
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert info1 is not False

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])