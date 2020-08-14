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
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *
from page_obj.scg.scg_def import *

test_id = "140510"


def test_c140510(browser):
	try:
		login_web(browser, url=dev1)
		# # 点击管理员
		# browser.find_element_by_xpath(网络).click()
		# # 点击接口设置
		# browser.find_element_by_xpath(接口设置).click()
		# # 点击网桥
		# browser.find_element_by_xpath(网桥).click()
		# # 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到内容frame
		# browser.switch_to.frame("content")
		into_fun(browser, 网桥)
		bridge_add_jyl(browser, bridge_name="br_1", bridge_describe="", snat="", allow_ping="yes", block_intra_bridge_traffic="")
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_5)
		bridge_edit_interface_jyl(browser, bridge_interface="br_1", interface=interface_name_6)

		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result1 = ssh.execute('ping 21.1.1.3 -c 5')
		# 关闭连接
		ssh.close()
		time.sleep(5)
		ssh = SSH('10.1.1.212', 'root', 'root', 22)
		ssh.connect()
		result = ssh.execute('ping 21.1.1.3 -c 3')
		time.sleep(2)
		print(result)
		# 关闭连接
		ssh.close()
		delete_bridge_jyl(browser)

		try:
			assert "100% packet loss" not in result
			rail_pass(test_run_id, test_id)
		except:
			rail_pass(test_run_id, test_id)
			assert "100% packet loss" not in result
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])