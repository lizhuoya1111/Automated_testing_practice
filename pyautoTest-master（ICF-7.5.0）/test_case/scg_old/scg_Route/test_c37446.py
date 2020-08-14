import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37446
# 输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256、


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_static_route_single_before_save_wxw(browser, ip='A.2.3.155', mask='24', out_device='ge0/2',
												gateway='13.1.1.1', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert1 = alert.text
		alert.accept()


		add_static_route_single_before_save_wxw(browser, ip='#.$.4.5', mask='24', out_device='ge0/2',
												gateway='13.1.1.1', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		alert = browser.switch_to_alert()
		time.sleep(1)
		# print(alert.text)
		alert2 = alert.text
		alert.accept()

		add_static_route_single_before_save_wxw(browser, ip='1.1.1.256', mask='24', out_device='ge0/2',
												gateway='13.1.1.1', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		alert = browser.switch_to_alert()
		time.sleep(1)
		# print(alert.text)
		alert3 = alert.text
		alert.accept()

		try:
			assert "IP格式输入错误，请重新输入" in alert1
			assert "IP格式输入错误，请重新输入" in alert2
			assert "IP格式输入错误，请重新输入" in alert3
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "IP格式输入错误，请重新输入" in alert1
			assert "IP格式输入错误，请重新输入" in alert2
			assert "IP格式输入错误，请重新输入" in alert3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.83")
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])