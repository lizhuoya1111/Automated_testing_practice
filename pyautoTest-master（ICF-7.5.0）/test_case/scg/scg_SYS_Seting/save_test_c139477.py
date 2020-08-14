import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139477"


def test_c139477(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t23246", "d", [interface_name_4, interface_name_5])
		reload(dev1, switch="重启")
		login_web(browser, url=dev1)
		zone_info_nosave = find_zone_byname(browser, "t23246")
		zone_info_save = ""

		if zone_info_nosave is None:
			add_obj_zone(browser, "t23246", "d", [interface_name_4, interface_name_5])
			save_configer(browser)
			reload(dev1, switch="重启")
			login_web(browser, url=dev1)
			zone_info_save = find_zone_byname(browser, "t23246")
			flag1 = zone_info_save
			while flag1 is not None:
				del_obj_zone_byname(browser, "t23246")
				save_configer(browser)
				flag1 = find_zone_byname(browser, "t23246")
		try:
			assert interface_name_4+" "+interface_name_5 in zone_info_save
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			zone_info_nosave = find_zone_byname(browser, "t23246")
			while zone_info_nosave is not None:
				del_obj_zone_byname(browser, "t23246")
				zone_info_nosave = find_zone_byname(browser, "t23246")
			save_configer(browser)
			print(err1)
			rail_fail(test_run_id, test_id)
			assert interface_name_4+" "+interface_name_5 in zone_info_save



	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		zone_info_nosave = find_zone_byname(browser, "t23246")
		while zone_info_nosave is not None:
			del_obj_zone_byname(browser, "t23246")
			zone_info_nosave = find_zone_byname(browser, "t23246")
		save_configer(browser)
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])