import pytest
import time
import sys
from page_obj.common.rail import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_multi_gateway_group import *

sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "141270"
# 静态多网关路由配置GW输入异常检测 5
# 网关group里只有两个网关，一个选active，一个选unselect


def test_c141270(browser):

	try:
		login_web(browser, url=dev1)

		for n in range(1, 3):

			add_multi_gateway_group_wxw(browser, name='mgg_460_'+str(n), group="1(GROUP_1)", modify='no', alias='',
									    device=interface_name_1, gateway='192.168.1.8'+str(n), ping_server='34.1.1.4', ping='yes',
									    arp='no', time_switch='7', ub="100000", db="100000")

		add_static_route_multi_gateway_before_save_wxw(browser, ip='192.168.188.3', mask='32', gateway_grp='1(GROUP_1)',
													   num=4, grp_mem=["主用", "不选择"], enable="no")

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[2]').click()
		# 获取警告框信息
		alert = browser.switch_to_alert()
		time.sleep(2)
		alert1 = alert.text
		# print(alert1)
		alert.accept()

		del_multi_gateway_group_all(browser)

		try:
			assert "必须选择2个以上的网关。" in alert1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "必须选择2个以上的网关。" in alert1


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])