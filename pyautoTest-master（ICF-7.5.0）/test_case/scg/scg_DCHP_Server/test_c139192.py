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

test_id = "139192"
def test_c139192(browser):
	try:
		login_web(browser, url=dev2)
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("ip address 192.165.12.2 255.255.255.0")
		a.execute("exit")
		dhcp_server_add_jyl(browser, interface=interface_name_5, dhcp_type="dhcp_server", dhcp_gw="192.165.12.1",
							dhcp_sm="24",
							ip_range1_1="192.165.12.4", ip_range1_2="192.165.12.20")
		time.sleep(2)
		# 点击编辑
		browser.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[7]/a[1]/img').click()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="ipfrom1"]').clear()
		# 清除默认输入
		browser.find_element_by_xpath('//*[@id="ipto1"]').clear()
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()


		loginfo = get_log(browser, 管理日志)
		# print(loginfo)
		a = Shell_SSH()
		a.connect(dev2)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("no ip address 192.165.12.2")
		a.execute("exit")
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert "设置DHCP成功" in loginfo
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "设置DHCP成功" in loginfo
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev2)
		assert False




if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])