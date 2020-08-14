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


test_id = "141889"




def test_c141889(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route", describe=str_85_ch+"汉")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		info1 = browser.switch_to_alert().text
		browser.switch_to_alert().accept()
		if "描述格式输入错误，请重新输入" in info1:
			add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route",
			              describe=str_256_en + "A")
			info2 = get_vlan_interface_desc(browser, interface_name=interface_name_6+".11")
			# print(len(info2))
		else:
			assert False

		try:
			assert len(info2) == 256
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert len(info2) == 256

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])