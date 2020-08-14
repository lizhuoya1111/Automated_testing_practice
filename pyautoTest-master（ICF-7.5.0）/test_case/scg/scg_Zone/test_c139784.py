import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139784"


def test_c139784(browser):

	try:
		login_web(browser, url=dev1)
		add_br(browser)
		into_fun(browser, Zone)
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
		select_zone1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		zone_list_object = select_zone1.options
		for x in zone_list_object:
			if x.text == "br_1":
				step1 = True
				break
		else:
			step1 = False

		add_vlan_inte(browser, physicl_interface=interface_name_4, vlan_id="66")
		into_fun(browser, Zone)
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="button_area"]/div/input[1]').click()
		select_zone1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		zone_list_object = select_zone1.options
		for x in zone_list_object:
			if x.text == interface_name_4 + ".66":
				step2 = True
				break
		else:
			step2 = False

		# print(step1, step2)
		time.sleep(5)


		try:
			assert step1 and step2
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert step1 and step2

		del_br_all(browser)
		del_vlan_inte_all(browser)


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])