import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_firewall import  *
from page_obj.scg.scg_def_bridge import *
test_id = "26944"
def test_main(browser):
	try:
		login_web(browser,url="10.2.2.81")
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击接口设置
		browser.find_element_by_xpath(接口设置).click()
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到内容frame
		browser.switch_to.frame("content")
		bridge_add_jyl(browser, bridge_name="br_1", allow_ping="yes",)
		bridge_edit_interface_jyl(browser, interface="ge0/5", bridge_interface="br_1")
		bridge_edit_interface_jyl(browser, interface="ge0/6", bridge_interface="br_1")
		time.sleep(1)
		del_all_acl_group_noadd_wxw(browser)
		time.sleep(1)
		add_acl_group_wxw(browser, name='tom')
		time.sleep(1)
		add_acl_rule_complete_wxw(browser, aclgroup_name='tom', source_zone_interface='ge0/5',
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface='ge0/6',
								  service='P:any', schdule='-- 无 --', accept='yes', drop='no', auth='-- 无 --', log='no')
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		ssh.execute('ping 21.1.1.3 -c 8')
		ssh.close()
		ssh1 = SSH('10.1.1.212', 'root', 'root', 22)
		ssh1.connect()
		result1=ssh1.execute('ping 21.1.1.3 -c 3')
		# print(result1)
		ssh1.close()
		# 关闭连接
		del_all_acl_group_wxw(browser)
		# 切换到默认frame
		browser.switch_to.default_content()
		# 切换到左侧frame
		browser.switch_to.frame("lefttree")
		time.sleep(1)
		# 点击网络
		browser.find_element_by_xpath(网络).click()
		# 点击网桥
		browser.find_element_by_xpath(网桥).click()
		delete_bridge_jyl(browser)

		try:
			assert "100% packet loss"not in result1
			rail_pass(206, test_id)
		except:
			rail_fail(206, test_id)
			assert "100% packet loss"not in result1
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip="10.2.2.81")
		print(err)
		rail_fail(test_run_id, test_id)
		time.sleep(70)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])