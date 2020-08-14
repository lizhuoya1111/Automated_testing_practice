import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_multi_isp import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_firewall import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_sys import *

test_id = "23246"


def test_c23246(browser):

	try:
		reload(dev3)
		print("ssss")
		# browser.switch_to.default_content()
		# # 定位到默认frame
		#
		# browser.switch_to.frame("lefttree")
		# # 登入后，定位到左侧frame nav_net_interface
		# browser.find_element_by_name("network").click()
		# if not browser.find_element_by_name(接口设置).is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_name(接口设置).click()
		# # browser.find_element_by_name("nav_net_interface").click()
		# browser.find_element_by_name("net_interface").click()

	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[4]/header/a').click()
	# 	# 点击”虚拟专网“
	#
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[4]/div/ul/li[4]/span/a').click()
	# 	time.sleep(5)
	# # 点击”远程网关“ //*[@id="menu"]/div[1]/header/a
	# 	browser.find_element_by_xpath('//*[@id="menu"]/div[1]/header/a').click()
	# 	browser.find_element_by_name('sys_status').click()
		time.sleep(5)

	except Exception as err:
		# 如果上面的步骤有报错，重启设备，恢复配置
		print(err)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_test1.py"])