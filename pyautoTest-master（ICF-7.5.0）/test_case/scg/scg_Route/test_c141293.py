import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141293"
# 输入IP格式不对：A.2.3.155、#.$.4.5 、1.1.1.256、


def test_c141293(browser):

	try:
		login_web(browser, url=dev3)

		add_multi_gateway_group_wxw_before_save_wxw(browser, name='Abc', group="1(GROUP_1)", modify='no', alias='',
									device=interface_name_3, gateway='A.2.3.155', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()


		add_multi_gateway_group_wxw_before_save_wxw(browser, name='Abc', group="1(GROUP_1)", modify='no', alias='',
													device=interface_name_3, gateway='#.$.4.5', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		add_multi_gateway_group_wxw_before_save_wxw(browser, name='Abc', group="1(GROUP_1)", modify='no', alias='',
													device=interface_name_3, gateway='1.1.1.256', ping_server='34.1.1.4',
													ping='yes',
													arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert3)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()

		try:
			assert "网关IP地址格式错误" in alert1
			assert "网关IP地址格式错误" in alert2
			assert "网关IP地址格式错误" in alert3
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "网关IP地址格式错误" in alert1
			assert "网关IP地址格式错误" in alert2
			assert "网关IP地址格式错误" in alert3

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev3)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])