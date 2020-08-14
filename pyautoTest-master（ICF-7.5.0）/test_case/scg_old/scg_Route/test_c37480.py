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

test_id = 37480
# 检查大小写敏感
# 大小写不敏感，输入Abc之后，不允许输入abc，但显示必需显示成Abc


def test_route_wxw(browser):

	try:
		login_web(browser, url="10.2.2.83")

		add_multi_gateway_group_wxw(browser, name='Abc', group="1(GROUP_1)", modify='no', alias='',
									device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		add_multi_gateway_group_wxw_before_save_wxw(browser, name='abc', group="1(GROUP_1)", modify='no', alias='',
									device='ge0/3', gateway='34.1.1.4', ping_server='34.1.1.4', ping='yes',
									arp='no', time_switch='7', ub="100000", db="100000")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()

		time.sleep(1)
		alert = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert)
		del_multi_gateway_group_byname(browser, name='Abc')

		try:
			assert "网关名称已经存在" in alert
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "网关名称已经存在" in alert


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip="10.2.2.83")
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])