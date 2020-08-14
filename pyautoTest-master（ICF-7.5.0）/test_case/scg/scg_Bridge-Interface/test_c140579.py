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


test_id = 140579
def test_c140579(browser):
	try:
		login_web(browser, url=dev1)
		bri_add_jyl(browser)
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="name"]').clear()
		# 输入网桥名称
		browser.find_element_by_xpath('//*[@id="name"]').send_keys("br_12345678加")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(webinfo1)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface bridge br_1")
		a.execute("exit")

		try:
			assert "无效网桥名称" in webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "无效网桥名称" in webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
