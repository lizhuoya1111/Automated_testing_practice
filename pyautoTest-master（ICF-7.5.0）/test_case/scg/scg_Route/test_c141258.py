import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141258"
# 输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256(静态单网关路由配置GW输入异常检测 1)


def test_c141258(browser):

	try:
		login_web(browser, url=dev3)

		add_static_route_single_before_save_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2,
												gateway='A.2.3.155', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(2)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert1 = alert.text
		alert.accept()


		add_static_route_single_before_save_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2,
												gateway='#.$.4.5', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		alert = browser.switch_to_alert()
		time.sleep(2)
		# print(alert.text)
		alert2 = alert.text
		alert.accept()

		add_static_route_single_before_save_wxw(browser, ip='20.1.1.0', mask='24', out_device=interface_name_2,
												gateway='1.1.1.256', enable='yes')
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		alert = browser.switch_to_alert()
		time.sleep(2)
		# print(alert.text)
		alert3 = alert.text
		alert.accept()

		try:
			assert "IP格式输入错误，请重新输入" in alert1
			assert "IP格式输入错误，请重新输入" in alert2
			assert "IP格式输入错误，请重新输入" in alert3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP格式输入错误，请重新输入" in alert1
			assert "IP格式输入错误，请重新输入" in alert2
			assert "IP格式输入错误，请重新输入" in alert3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])