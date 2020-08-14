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


test_id = 140490
def test_c140490(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface vlan "+interface_name_4+".44")
		a.execute("work-mode transparent")
		bri_edit_jyl(browser, bridge="br_0")
		# 选interface下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="interface_sel"]'))
		# 选interface下拉框内容
		s1.select_by_visible_text(interface_name_4+".44")
		# 点击移动
		browser.find_element_by_xpath('//*[@id="conftr_1"]/td[3]/input[1]').click()
		# 点击保存
		time.sleep(2)
		browser.find_element_by_xpath('//*[@id="container"]/div[2]/form/div[3]/div[2]/div/input[2]').click()
		webinfo1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("no interface vlan "+interface_name_4+".44")
		a.execute("exit")
		time.sleep(1)
		try:
			assert "错误成员列表" == webinfo1
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "错误成员列表" == webinfo1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
