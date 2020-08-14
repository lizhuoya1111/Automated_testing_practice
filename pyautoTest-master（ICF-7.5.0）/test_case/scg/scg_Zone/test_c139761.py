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

test_id = "139761"


def test_c139761(browser):

	try:
		login_web(browser, url=dev1)
		for n in range(0, 10):
			add_obj_zone(browser, "t"+str(n), "d", [interface_name_4, interface_name_3])
		time.sleep(2)
		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		if info1 == "操作成功":
			zone_name = find_zone_byname(browser, "t0")
			if zone_name == interface_name_4+" "+interface_name_3:
				into_fun(browser, Zone)
				# 获取目前有多少个zone对象，而且要减去2，因为有两个默认存在的对
				time.sleep(2)
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				time.sleep(2)
				browser.find_element_by_xpath('//*[@id="btn_check_all"]').click()
				browser.find_element_by_xpath('//*[@id="button_area"]/div/input[2]').click()
				browser.switch_to_alert().accept()
				into_fun(browser, Zone)
				# browser.find_element_by_xpath('//*[@id="link_but"]').click()
				time.sleep(3)
				zone_num = browser.find_element_by_xpath('//*[@id="rules_count"]').text
				# print(zone_num)
				if zone_num == "12":
					try:
						assert zone_num == "12"
						rail_pass(test_run_id, test_id)

					except Exception as err1:
						print(err1)
						rail_fail(test_run_id, test_id)
						assert zone_num == "12"

				else:
					assert False
			else:
				assert False
		else:
			assert False

		del_zone_all_batch(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])