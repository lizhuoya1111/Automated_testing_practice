import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_vlan_interface import  *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
test_id = "26910"
def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		# 点击管理员
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到内容frame
		browser.switch_to.frame("content")
		bridge_add_jyl(browser, bridge_name="br_1",  allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface="ge0/5", bridge_interface="br_1")
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_1", address_mode="manual", ip="21.1.1.1", mask="24")

		bridge_add_jyl(browser, bridge_name="br_2", allow_ping="no")
		bridge_edit_interface_jyl(browser, interface="ge0/6", bridge_interface="br_2")
		bridge_edit_ip_add_jyl(browser, bridge_interface="br_2", address_mode="manual", ip="22.1.1.1", mask="24")

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 21.1.1.1 -c 8')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 21.1.1.1 -c 3')
		# print(result1)
		# 关闭连接
		ssh.close()

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 22.1.1.1 -c 8')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 22.1.1.1 -c 3')
		print(result2)
		# 关闭连接
		ssh.close()
		delete_bridge_jyl(browser)
		delete_bridge_jyl(browser)
		try:
			assert "100% packet loss" not in result1
			assert "100% packet loss" in result2

			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "100% packet loss" not in result1
			assert "100% packet loss" in result2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])