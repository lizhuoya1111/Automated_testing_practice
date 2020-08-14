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

test_id = "139754"


def test_c139754(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t23246", "d", [interface_name_4, interface_name_5])
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[7]/a[1]').click()
		s1 = Select(browser.find_element_by_xpath('//*[@id="src_interface"]'))
		s1.select_by_visible_text(interface_name_1)
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[1]').click()
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		num_info1 = browser.find_element_by_xpath('//*[@id="interarea2"]').text
		# print(num_info1)

		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[7]/a[1]').click()
		s2 = Select(browser.find_element_by_xpath('//*[@id="dst_interface"]'))
		s2.select_by_visible_text(interface_name_1)
		browser.find_element_by_xpath('//*[@id="conftr_2"]/td[2]/table/tbody/tr[2]/td[2]/input[2]').click()
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[3]').click()
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		num_info2 = browser.find_element_by_xpath('//*[@id="interarea2"]').text
		# print(num_info2)

		try:
			assert num_info1 == interface_name_4+" "+interface_name_5+" "+interface_name_1 and num_info2 == interface_name_4+" "+interface_name_5
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert num_info1 == interface_name_4+" "+interface_name_5+" "+interface_name_1 and num_info2 == interface_name_4+" "+interface_name_5

		del_obj_zone_byname(browser, "t23246")


	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])