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
test_id = "26898"


def test_main(browser):
	try:
		login_web(browser, url="10.2.2.81")
		# 点击管理员
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		transparent_interface_change_physics_interface_jyl(browser, interface5="ge0/5")
		transparent_interface_change_physics_interface_jyl(browser, interface6="ge0/6")
		time.sleep(2)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击子接口接口
		browser.find_element_by_xpath(子接口).click()
		vlan_add_jyl(browser, physicl_interface="ge0/5", vlan_id="55", work_mode="transparent")
		vlan_add_jyl(browser, physicl_interface="ge0/6", vlan_id="55", work_mode="transparent")
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
		bridge_edit_interface_jyl(browser, interface="ge0/5.55", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/6.55", bridge_interface="br_1")
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 114.114.114.114 -c 5')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result2 = ssh.execute('ping 114.114.114.114 -c 3')
		# print(result2)
		# 关闭连接
		ssh.close()
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		result3 = ssh.execute('ping 114.114.114.114 -c 5')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.213', 'root', 'root', 22)
		ssh.connect()
		result4 = ssh.execute('ping 114.114.114.114 -c 3')
		# print(result4)
		# 关闭连接
		ssh.close()
		delete_bridge_jyl(browser)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		# 点击子接口接口
		browser.find_element_by_xpath(子接口).click()
		vlan_delete_jyl(browser)
		time.sleep(5)
		vlan_delete_jyl(browser)
		# 定位到默认frame
		browser.switch_to.default_content()
		browser.switch_to.frame("lefttree")
		time.sleep(3)
		# 点击物理接口
		browser.find_element_by_xpath(物理接口).click()
		physics_interface_change_transparent_interface(browser, interface5="ge0/5")
		time.sleep(1)
		physics_interface_change_transparent_interface(browser, interface6="ge0/6")
		time.sleep(1)
		try:
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result4
			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "100% packet loss" not in result2
			assert "100% packet loss" not in result4
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])