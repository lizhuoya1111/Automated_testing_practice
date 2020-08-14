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
from page_obj.scg.scg_def import *


test_id = "130459"
def test_main(browser):
	try:
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ifconfig eth3 22.1.1.3 netmask 255.255.255.0')
		ssh.execute('route add -net 21.1.1.0/24 gw 22.1.1.2')
		# 关闭连接
		ssh.close()
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('route add -net 22.1.1.0/24 gw 21.1.1.1')
		# 关闭连接
		ssh.close()
		login_web(browser, url="10.2.2.81")
		# # 点击管理员
		# browser.find_element_by_xpath(网络).click()
		# # 点击接口设置
		# browser.find_element_by_xpath(接口设置).click()
		# # 点击物理接口
		# browser.find_element_by_xpath(物理接口).click()
		into_fun(browser, 物理接口)
		transparent_interface_change_physics_interface_jyl(browser, interface6=interface_name_6)
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("ip address 22.1.1.2 255.255.255.0")
		a.execute("exit")
		# browser.switch_to.default_content()
		# browser.switch_to.frame("lefttree")
		# # 点击网桥
		# browser.find_element_by_xpath(网桥).click()
		# # 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到内容frame
		# browser.switch_to.frame("content")
		# into_fun(browser, 网桥)
		# time.sleep(1)
		# bridge_add_jyl(browser, bridge_name="br_1", snat="yes", allow_ping="yes")
		# bridge_edit_interface_jyl(browser, interface=interface_name_5, bridge_interface="br_0")
		# bridge_edit_ip_add_jyl(browser, bridge_interface="br_0", address_mode="manual", ip="21.1.1.1", mask="255.255.255.0", )
		# a = Shell_SSH()
		# a.connect("10.2.2.81")
		# a.execute("en")
		# a.execute("conf t")
		a.execute("interface bridge br_0")
		a.execute("ip address 21.1.2.1 255.255.255.0")
		a.execute("ip address 21.1.3.1 255.255.255.0")
		a.execute("exit")
		time.sleep(1)
		ssh1 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh1.connect()
		ssh1.execute('	ifconfig '+server_pc_3_eth0+' 21.1.1.2 netmask 255.255.255.0')
		ssh1.execute('	 route add -net 22.1.1.0/24 gw 21.1.2.1')
		time.sleep(1)
		ssh2 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh2.connect()
		ssh2.execute('	 route add -net 21.1.2.0/24 gw 22.1.1.2')

		ssh3 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh3.connect()
		ssh3.execute(' ping 21.1.2.1 > /dev/null -c 500 &')

		ssh4 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh4.connect()
		ssh4.execute(' ping 21.1.2.2 > /dev/null -c 500 &')

		ssh5 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh5.connect()
		result1 = ssh5.execute('tcpdump -i '+server_pc_3_eth0+' -e -c 50')
		# print(result1)
		ssh5.close()

		ssh6 = SSH('10.1.1.213', 'root', 'root', 22)
		ssh6.connect()
		ssh6.execute('ifconfig eth3 21.1.1.3 netmask 255.255.255.0')
		# 关闭连接
		ssh.close()
		a = Shell_SSH()
		a.connect("10.2.2.81")
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_6)
		a.execute("no ip address 22.1.1.2")
		a.execute("exit")
		# delete_bridge_jyl(browser)
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# browser.switch_to.frame("lefttree")
		# time.sleep(3)
		# # 点击物理接口
		# browser.find_element_by_xpath(物理接口).click()
		into_fun(browser, 物理接口)
		time.sleep(2)
		physics_interface_change_transparent_interface(browser, interface6=interface_name_6)

		try:
			assert "21.1.2.1" in result1
			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "21.1.2.1" in result1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('reboot')
		time.sleep(15)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])