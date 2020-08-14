import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 37481
# 输入空格;',./:"标点符号
# .和/可以正确输入


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_multi_gateway_group_wxw_before_save_wxw(browser, name=' ', group="1(GROUP_1)", modify='no', alias='',
									device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		print(alert.text)
		alert1 = alert.text
		alert.accept()

		add_multi_gateway_group_wxw_before_save_wxw(browser, name=" ;", group="1(GROUP_1)", modify='no', alias='',
													device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert2 = alert.text
		alert.accept()

		add_multi_gateway_group_wxw_before_save_wxw(browser, name="'", group="1(GROUP_1)", modify='no', alias='',
													device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert3 = alert.text
		alert.accept()

		add_multi_gateway_group_wxw_before_save_wxw(browser, name=",", group="1(GROUP_1)", modify='no', alias='',
													device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert4 = alert.text
		alert.accept()



		add_multi_gateway_group_wxw_before_save_wxw(browser, name="/", group="1(GROUP_1)", modify='no', alias='',
													device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert6 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)


		add_multi_gateway_group_wxw_before_save_wxw(browser, name='"', group="1(GROUP_1)", modify='no', alias='',
													device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.switch_to_alert()
		# print(alert.text)
		alert8 = alert.text
		alert.accept()


		try:
			assert "对象名输入错误，请重新输入" in alert1
			assert "对象名输入错误，请重新输入" in alert2
			assert "对象名输入错误，请重新输入" in alert3
			assert "对象名输入错误，请重新输入" in alert4
			assert "网关名称包含非法字符" in alert6
			assert "对象名输入错误，请重新输入" in alert8
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "对象名输入错误，请重新输入" in alert1
			assert "对象名输入错误，请重新输入" in alert2
			assert "对象名输入错误，请重新输入" in alert3
			assert "对象名输入错误，请重新输入" in alert4
			assert "网关名称包含非法字符" in alert6
			assert "对象名输入错误，请重新输入" in alert8


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.83")
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])