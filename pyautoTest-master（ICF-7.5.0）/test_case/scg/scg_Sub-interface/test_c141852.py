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

test_id = "141852"


def test_c141852(browser):
	try:

		login_web(browser, url=dev2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.2")
		add_vlan_inte(browser, physicl_interface=interface_name_2, vlan_id="20", work_mode="route")
		add_vlan_inte_add(browser, interface_name=interface_name_2 + ".20", ipadd="20.1.1.100", mask="24")
		switch_vlan_interface_snat(browser, vlan_interface=interface_name_2 + ".20", snat="open")


		# 切换到默认frame
		# browser.switch_to.default_content()
		# # 切换到左侧frame
		# browser.switch_to.frame("lefttree")
		# browser.find_element_by_xpath(防火墙).click()
		# browser.find_element_by_xpath(NAT).click()
		#
		# # 判断菜单是否展开，元素是否可见
		# if not browser.find_element_by_xpath(display_NAT).is_displayed():
		# 	# 如果不可见，点击加号，展开元素
		# 	browser.find_element_by_xpath(display_NAT).click()
		# browser.find_element_by_xpath(源NAT).click()
		# # 定位到默认frame
		# browser.switch_to.default_content()
		# # 定位到内容frame
		# browser.switch_to.frame("content")
		# # 获取目前有多少个SNAT
		into_fun(browser, 源NAT)
		time.sleep(1)
		snat_sum = int(browser.find_element_by_xpath('//*[@id="rules_count"]').text)
		# print(snat_sum)


		try:
			assert snat_sum == 0
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert snat_sum == 0

		del_vlan_inte_all(browser)
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.2', mask='24')



	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev2)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c"+str(test_id)+".py"])