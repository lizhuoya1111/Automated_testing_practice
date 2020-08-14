import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_log import *
from page_obj.scg.scg_def_mac import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139600"


def test_c139600(browser):

	try:
		login_web(browser, url=dev2)
		into_fun(browser, ARP列表)
		time.sleep(1.5)
		browser.find_element_by_xpath('//*[@id="tabs"]/li[2]').click()
		time.sleep(1.5)
		en_statu1 = browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').is_enabled()
		print(en_statu1)
		sy_status = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if sy_status is False:
			browser.find_element_by_xpath('//*[@id="status"]').click()
			browser.switch_to_alert().accept()
			time.sleep(1)
			browser.switch_to_alert().accept()
		time.sleep(1)
		en_statu = browser.find_element_by_xpath('//*[@id="set_to_static_arp"]').is_enabled()
		print(en_statu)

		try:
			assert en_statu is False
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert en_statu is False

		sy_status = browser.find_element_by_xpath('//*[@id="status"]').is_selected()
		if sy_status is True:
			browser.find_element_by_xpath('//*[@id="status"]').click()
			browser.switch_to_alert().accept()
			time.sleep(1)
			browser.switch_to_alert().accept()


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])