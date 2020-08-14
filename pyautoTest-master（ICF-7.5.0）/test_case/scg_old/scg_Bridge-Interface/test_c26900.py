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
test_id = "26900"


def test_main(browser):
	try:
		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('	ifconfig eth2 21.1.1.4 netmask 255.255.255.0')
		# 关闭连接
		ssh.close()
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/4")
		a.execute("no ip address 20.1.1.1")
		a.execute("exit")
		login_web(browser, url="10.2.2.81")
		# 点击管理员
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		physics_interface_change_transparent_interface(browser, interface4="ge0/4")
		time.sleep(1)
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到内容frame
		browser.switch_to.frame("content")
		time.sleep(1)
		bridge_add_jyl(browser, bridge_name="br_1", bridge_describe="", snat="", allow_ping="yes",block_intra_bridge_traffic="")
		bridge_edit_interface_jyl(browser, interface="ge0/5", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/6", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/4", bridge_interface="br_1")

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 21.1.1.3 -c 8')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 21.1.1.3 -c 3')
		print(result1)
		# 关闭连接
		ssh.close()

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 21.1.1.4 -c 8')
		# 关闭连接
		ssh.close()
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 21.1.1.4 -c 3')
		print(result2)
		# 关闭连接
		ssh.close()

		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 21.1.1.4 -c 8')
		# 关闭连接
		ssh.close()
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		result3 = ssh.execute('ping 21.1.1.4 -c 3')
		print(result3)
		# 关闭连接
		ssh.close()

		delete_bridge_jyl(browser)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		time.sleep(3)
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		transparent_interface_change_physics_interface_jyl(browser, interface4="ge0/4")
		time.sleep(1)

		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/4")
		a.execute("ip address 20.1.1.1 255.255.255.0")
		a.execute("exit")


		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('	ifconfig eth2 20.1.1.2 netmask 255.255.255.0')
		# 关闭连接
		ssh.close()

		try:
			assert "100% packet loss" not in result1
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result3
			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "100% packet loss" not in result1
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result3
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])