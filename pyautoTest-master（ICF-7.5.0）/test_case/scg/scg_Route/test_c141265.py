import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141265"
# 静态多网关路由配置IP输入异常检测 2
# 输入不合法IP、掩码：255.255.255.255、1.1.1.1/255.255.255.256、1.1.1.1/32


def test_c141265(browser):

	try:
		login_web(browser, url=dev1)

		for n in range(1, 5):

			add_multi_gateway_group_wxw(browser, name='mgg_455_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_1, gateway='192.168.1.8'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		add_static_route_multi_gateway_wxw(browser, ip='255.255.255.255', mask='32', gateway_grp='1(GROUP_1)', num=4,
										   grp_mem=["主用", "不选择", "备份1", "备份2"], enable="yes", save='yes', cancel='no')

		alert1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(alert1)

		add_static_route_multi_gateway_before_save_wxw(browser, ip='1.1.1.1', mask='255.255.255.256', gateway_grp='1(GROUP_1)',
													   num=4, grp_mem=["主用", "不选择", "备份1", "备份2"], enable="no")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
		# 获取警告框信息
		alert = browser.switch_to_alert()
		time.sleep(2)
		alert2 = alert.text
		# print(alert2)
		alert.accept()

		del_multi_gateway_group_all(browser)

		try:
			assert "IP地址为D/E类地址" in alert1
			assert "掩码格式输入错误，请重新输入。" in alert2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "IP地址为D/E类地址" in alert1
			assert "掩码格式输入错误，请重新输入。" in alert2


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])