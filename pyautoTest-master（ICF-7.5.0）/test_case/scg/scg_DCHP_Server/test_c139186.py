import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *


test_id = "139186"
def test_c139186(browser):
	try:
		login_web(browser, url=dev2)
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("ip address 131.1.1.1 255.255.255.0")
		a.execute("exit")
		dhcp_server_add_jyl(browser, interface=interface_name_3, dhcp_type="dhcp_rely",
							dhcp_rely_server1="115.115.115.115")
		time.sleep(2)
		loginfo1 = get_log(browser, 管理日志)
		into_fun(browser, DHCP设定)
		# 点击终止
		browser.find_element_by_xpath('//*[@id="net_dhcp_setting"]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		time.sleep(2)
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		loginfo2 = get_log(browser, 管理日志)
		# print(loginfo2)
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("no ip address 131.1.1.1")
		a.execute("exit")
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert "启动DHCP成功" in loginfo1
			assert "终止DHCP成功" in loginfo2
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "启动DHCP成功" in loginfo1
			assert "终止DHCP成功" in loginfo2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])