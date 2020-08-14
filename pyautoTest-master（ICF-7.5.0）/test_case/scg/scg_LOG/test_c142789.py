import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 142789
def test_c142789(browser):
	try:
		login_web(browser, url=dev1)
		into_fun(browser, 日志告警)
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/form/div/div[2]/div/input[2]').click()
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info = alert.text
		time.sleep(0.5)
		# 接受告警
		browser.switch_to_alert().accept()
		try:
			assert "密码不能为空" in web_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "密码不能为空" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
