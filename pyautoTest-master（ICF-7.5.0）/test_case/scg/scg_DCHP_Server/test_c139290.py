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

test_id = 139290
def test_c139290(browser):
	try:
		login_web(browser, url=dev1)
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("ip address 131.1.1.1 255.255.255.0")
		a.execute("exit")

		into_fun(browser, DHCP设定)
		# 选interface下拉框
		s1 = Select(browser.find_element_by_xpath('//*[@id="interface"]'))
		# 选interface下拉框内容
		s1.select_by_visible_text(interface_name_3)
		# 点击增加
		browser.find_element_by_xpath('//*[@id="totalrules"]/input').click()
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		# 点击dhcp_server
		browser.find_element_by_xpath('//*[@id="work_mode_0"]').click()
		# 输入dhcp网关
		browser.find_element_by_xpath('//*[@id="gateway"]').send_keys("131.1.1.254")
		# 输入dhcp子网掩码
		browser.find_element_by_xpath('//*[@id="netmask"]').send_keys("24")
		# 清除dhcp 默认租约时间
		browser.find_element_by_xpath('//*[@id="day"]').clear()
		# 输入dhcp 租约时间
		browser.find_element_by_xpath('//*[@id="minute"]').send_keys("200")
		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div/form/div[2]/div[2]/div/input[2]').click()
		time.sleep(2)
		webinfo = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		time.sleep(2)
		# 点击返回
		browser.find_element_by_xpath('//*[@id="link_but"]').click()
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_3)
		a.execute("no ip address 131.1.1.1")
		a.execute("exit")
		dhcp_server_edit_or_delete(browser, fuction="delete")
		try:
			assert webinfo == "默认租约时间不能小于最小租约时间(5分钟)"
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert webinfo == "默认租约时间不能小于最小租约时间(5分钟)"
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])