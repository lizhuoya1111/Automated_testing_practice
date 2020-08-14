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

test_id = "139758"


def test_c139758(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t1", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t2", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t3", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t4", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t5", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t6", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t7", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t8", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t9", "d", [interface_name_5, interface_name_6])
		add_obj_zone(browser, "t0", "d", [interface_name_5, interface_name_6])
		time.sleep(1.5)
		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		if info1 == "操作成功":
			zone_name = find_zone_byname(browser, "t5")
			if zone_name == interface_name_5 + ' ' + interface_name_6:
				del_obj_zone_byname(browser, "t5")
				resalt1 = find_zone_byname(browser, "t23246")
				# print(resalt1, )
				if resalt1 is None:
					loginfo = get_log_info(browser, 管理日志)
					# print("日志："+loginfo)
					try:
						assert "成功，删除内部对象" in str(loginfo)
						rail_pass(test_run_id, test_id)

					except Exception as err1:
						print(err1)
						rail_fail(test_run_id, test_id)
						assert "成功，删除内部对象" in str(loginfo)

				else:
					assert False
			else:
				assert False
		else:
			assert False

		del_obj_zone_byname(browser, "t1")
		del_obj_zone_byname(browser, "t2")
		del_obj_zone_byname(browser, "t3")
		del_obj_zone_byname(browser, "t4")
		del_obj_zone_byname(browser, "t6")
		del_obj_zone_byname(browser, "t7")
		del_obj_zone_byname(browser, "t8")
		del_obj_zone_byname(browser, "t9")
		del_obj_zone_byname(browser, "t0")


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])