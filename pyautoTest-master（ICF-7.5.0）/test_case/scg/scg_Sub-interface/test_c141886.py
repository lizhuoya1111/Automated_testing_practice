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

# 包含141887 141888
test_id = "141886"
test_id1 = "141887"
test_id2 = "141888"



def test_c141886(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		add_vlan_inte(browser, physicl_interface=interface_name_6, vlan_id="11", work_mode="route")
		# result1 = find_vlan_interface_byname(browser, interface_name_6+".11")
		# A.2.3.155
		add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="A.2.3.155", mask="24")
		info1 = browser.switch_to_alert().text
		browser.switch_to_alert().accept()
		# print(info1)
		if info1 == "IP格式输入错误，请重新输入。":
			# #.$.4.5
			add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="#.$.4.5", mask="24")
			info2 = browser.switch_to_alert().text
			browser.switch_to_alert().accept()
			if info2 == "IP格式输入错误，请重新输入。":
				# 1.1.1.256
				add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="1.1.1.256", mask="24")
				info3 = browser.switch_to_alert().text
				browser.switch_to_alert().accept()
				if info3 == "IP格式输入错误，请重新输入。":
					# 中文
					add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="中文", mask="24")
					info4 = browser.switch_to_alert().text
					browser.switch_to_alert().accept()
					if info4 == "IP格式输入错误，请重新输入。":
						# 英文
						add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="eng",
						                  mask="24")
						info5 = browser.switch_to_alert().text
						browser.switch_to_alert().accept()
						if info5 == "IP格式输入错误，请重新输入。":
							# ！@！#！@￥、：“”
							add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="！@！#！@￥、：“”",
							                  mask="24")
							info6 = browser.switch_to_alert().text
							browser.switch_to_alert().accept()
							if info6 == "IP格式输入错误，请重新输入。":
								# 255.255.255.255
								add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11", ipadd="255.255.255.255",
								                  mask="24")
								info7 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text
								if info7 == "IP地址无效":
									# 1.1.1.1/255.255.256.255
									add_vlan_inte_add(browser, interface_name=interface_name_6 + ".11",
									                  ipadd="1.1.1.1",
									                  mask="255.255.256.255")
									info8 = browser.switch_to_alert().text
									browser.switch_to_alert().accept()
								else:
									assert False
							else:
								assert False
						else:
							assert False
					else:
						assert False
				else:
					assert False
			else:
				assert False
		else:
			assert False



		try:
			assert info8 == "掩码格式输入错误，请重新输入。"
			rail_pass(test_run_id, test_id)
			rail_pass(test_run_id, test_id1)
			rail_pass(test_run_id, test_id2)
		except:
			rail_fail(test_run_id, test_id)
			rail_fail(test_run_id, test_id1)
			rail_fail(test_run_id, test_id2)
			assert info8 == "掩码格式输入错误，请重新输入。"

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])