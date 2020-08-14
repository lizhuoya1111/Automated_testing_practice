
import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_ospf import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 140946
def test_c140946(browser):
	try:
		login_web(browser, url=dev1)
		start_ospf_jyl(browser)
		time.sleep(0.5)
		edit_ospf_interface_jyl(browser, ospf_interface="br_0", auth_type="md5",  message_digest_key="256", md5_key="#",
								save="yes")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info = alert.text
		# print(web_info)
		# 接受告警
		browser.switch_to_alert().accept()
		edit_ospf_interface_jyl(browser, ospf_interface="br_0", priority="1", hello_interval="10", dead_interval="40",
								auth_type="无", save="yes")
		stop_ospf_jyl(browser)
		try:
			assert "输入数字错误" in web_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "输入数字错误" in web_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
