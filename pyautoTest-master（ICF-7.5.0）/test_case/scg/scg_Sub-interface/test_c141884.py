import pytest
import subprocess
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_def_bridge import *


test_id = "141884"




def test_c141884(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		# 配置相同的IP在相同的子接口
		add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="105.1.1.1", mask="24")
		add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="105.1.1.1", mask="24")
		info1 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
		# print(info1)
		if info1 == "IP地址已经存在于本系统":
			# 配置相同的IP不同的子网掩码在相同的子接口.
			add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="105.1.1.1", mask="32")
			info2 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
			if info2 == "IP地址已经存在于本系统":
				# 配置相同的IP在不同的子接口.
				add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="12", work_mode="route")
				time.sleep(20)
				add_vlan_inte_add(browser, interface_name=interface_name_5 + ".12", ipadd="105.1.1.1", mask="24")
				info3 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
				if info3 == "IP地址已经存在于本系统":
					# 配置相同的IP不同的子网掩码在不同的子接口.
					add_vlan_inte_add(browser, interface_name=interface_name_5 + ".12", ipadd="105.1.1.1", mask="32")
					info4 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
				else:
					assert False
			else:
				assert False

		else:
			assert False



		try:
			assert info4 == "IP地址已经存在于本系统"
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert info4 == "IP地址已经存在于本系统"

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])