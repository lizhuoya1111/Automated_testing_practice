import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def import *


test_id = 140575
def test_c140575(browser):
	try:
		login_web(browser, url=dev1)
		bridge_add_jyl(browser, bridge_name="br_1")

		bri_edit_jyl(browser, bridge="br_1")
		# 输入ip
		browser.find_element_by_xpath('//*[@id="ipaddress_tex"]').send_keys("A.加.#.?")
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="mask_tex"]').clear()
		# 输入掩码
		browser.find_element_by_xpath('//*[@id="mask_tex"]').send_keys("24")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info2 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("exit")

		try:
			assert "输入错误" in web_info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "输入错误" in web_info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
