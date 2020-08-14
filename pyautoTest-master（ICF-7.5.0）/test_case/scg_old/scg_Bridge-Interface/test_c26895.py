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
test_id = "26895"


def test_main(browser):
	try:
		login_web(browser,url="10.2.2.81")
		# 点击管理员
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 12.1.1.1")
		a.execute("exit")
		a.execute("interface gigabitethernet ge0/3")
		a.execute("no ip address 13.1.1.1")
		a.execute("exit")
		a.execute("interface gigabitethernet ge0/4")
		a.execute("no ip address 20.1.1.1")
		a.execute("exit")
		time.sleep(1)
		physics_interface_change_transparent_interface(browser, interface2="ge0/2")
		time.sleep(1)
		physics_interface_change_transparent_interface(browser,  interface3="ge0/3")
		time.sleep(1)
		physics_interface_change_transparent_interface(browser,  interface4="ge0/4")
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
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes")
		bridge_edit_interface_jyl(browser, interface="ge0/2", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/3", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/4", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/5", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/6", bridge_interface="br_1")
		a = Shell_SSH()
		a.connect("10.2.2.82")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 12.1.1.2")
		a.execute("ip address 21.1.1.6 255.255.255.0")
		a.execute("exit")
		time.sleep(1)

		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 13.1.1.3")
		a.execute("ip address 21.1.1.5 255.255.255.0")
		a.execute("exit")
		time.sleep(1)

		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('	ifconfig eth2 21.1.1.4 netmask 255.255.255.0')
		# 关闭连接

		ssh1 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh1.connect()
		ssh1.execute('ping 21.1.1.6 -c 8')
		ssh1.close()
		ssh2 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh2.connect()
		result1 = ssh2.execute('ping 21.1.1.6 -c 3')
		# print(result1)
		ssh2.close()

		ssh3 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh3.connect()
		ssh3.execute('ping 21.1.1.5 -c 8')
		ssh3.close()
		ssh4 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh4.connect()
		result2 = ssh4.execute('ping 21.1.1.5 -c 3')
		# print(result2)
		ssh4.close()

		ssh5 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh5.connect()
		ssh5.execute('ping 21.1.1.4 -c 8')
		ssh5.close()
		ssh6 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh6.connect()
		result3 = ssh6.execute('ping 21.1.1.4 -c 3')
		# print(result3)
		ssh6.close()

		ssh7 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh7.connect()
		ssh7.execute('ping 21.1.1.3 -c 8')
		ssh7.close()
		ssh8 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh8.connect()
		result4 = ssh8.execute('ping 21.1.1.3 -c 3')
		# print(result4)
		ssh8.close()

		ssh9 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh9.connect()
		ssh9.execute('ping 21.1.1.6 -c 8')
		ssh9.close()
		ssh10 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh10.connect()
		result5 = ssh10.execute('ping 21.1.1.6 -c 3')
		# print(result5)
		ssh10.close()

		ssh11 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh11.connect()
		ssh11.execute('ping 21.1.1.5 -c 8')
		ssh11.close()
		ssh12 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh12.connect()
		result6 = ssh12.execute('ping 21.1.1.5 -c 3')
		# print(result6)
		ssh12.close()

		ssh13 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh13.connect()
		ssh13.execute('ping 21.1.1.4 -c 8')
		ssh13.close()
		ssh14 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh14.connect()
		result7 = ssh14.execute('ping 21.1.1.4 -c 3')
		# print(result7)
		ssh14.close()

		ssh15 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh15.connect()
		ssh15.execute('ping 21.1.1.3 -c 8')
		ssh15.close()
		ssh16 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh16.connect()
		result8 = ssh16.execute('ping 21.1.1.3 -c 3')
		# print(result8)
		ssh16.close()
		time.sleep(1)

		a = Shell_SSH()
		a.connect("10.2.2.82")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 21.1.1.6")
		a.execute("ip address 12.1.1.2 255.255.255.0")
		a.execute("exit")
		time.sleep(1)

		a = Shell_SSH()
		a.connect("10.2.2.83")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("no ip address 21.1.1.5")
		a.execute("ip address 13.1.1.3 255.255.255.0")
		a.execute("exit")
		time.sleep(1)

		ssh = SSH('10.1.1.202', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('	ifconfig eth2 20.1.1.2 netmask 255.255.255.0')
		# 关闭连接
		delete_bridge_jyl(browser)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		time.sleep(3)
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		transparent_interface_change_physics_interface_jyl(browser, interface2="ge0/2")
		transparent_interface_change_physics_interface_jyl(browser, interface3="ge0/3")
		transparent_interface_change_physics_interface_jyl(browser, interface4="ge0/4")
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet ge0/2")
		a.execute("ip address 12.1.1.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface gigabitethernet ge0/3")
		a.execute("ip address 13.1.1.1 255.255.255.0")
		a.execute("exit")
		a.execute("interface gigabitethernet ge0/4")
		a.execute("ip address 20.1.1.1 255.255.255.0")
		a.execute("exit")


		try:
			assert "100% packet loss" not in result1
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result3
			assert "100% packet loss" not in result4
			assert "100% packet loss" not in result5
			assert "100% packet loss" not in result6
			assert "100% packet loss" not in result7
			assert "100% packet loss" not in result8
			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "100% packet loss" not in result1
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result3
			assert "100% packet loss" not in result4
			assert "100% packet loss" not in result5
			assert "100% packet loss" not in result6
			assert "100% packet loss" not in result7
			assert "100% packet loss" not in result8
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])