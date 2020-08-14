import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_interface import *
from os.path import dirname, abspath
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = 143641


def test_c143641(browser):

	try:
		login_web(browser, url=dev1)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_4, ip="20.1.1.1")
		physics_interface_pppoe_set(browser, physical_interface=interface_name_4, pppoe_uesr="", pppoe_passwd="")
		info1 = browser.switch_to_alert().text
		browser.switch_to_alert().accept()
		# print(info1)
		try:

			assert "输入不能为空" in info1
			# assert True
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			# assert True
			assert "输入不能为空" in info1

		add_physical_interface_ip_wxw(browser, interface=interface_name_4, ip='20.1.1.1', mask='24')

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])