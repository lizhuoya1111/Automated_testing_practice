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


test_id = "141783"

# 本测试用例包含"shell配置与UI配置的对比检查"


def test_c141783(browser):
	try:
		login_web(browser, url=dev1)
		# 点击管理员
		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode route")
		a.execute("exit")
		a.close()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="1", work_mode="route")
		loginfo1 = get_log_info(browser, 管理日志)

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="4094", work_mode="route")
		loginfo2 = get_log_info(browser, 管理日志)

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="0", work_mode="route")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info3 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="4095", work_mode="route")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info4 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="alksjdfskald", work_mode="route")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info5 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="#$%#$^$(_)", work_mode="route")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info6 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="", work_mode="route")
		alert = browser.switch_to_alert()
		# print(alert.text)
		web_info7 = alert.text
		# 接受告警
		browser.switch_to_alert().accept()

		add_vlan_inte(browser, physicl_interface=interface_name_5, vlan_id="1", work_mode="route")
		webinfo8 = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()

		del_vlan_inte_all(browser)

		a = Shell_SSH()
		a.connect(dev1)
		a.execute("en")
		a.execute("conf t")
		a.execute("interface gigabitethernet "+interface_name_5)
		a.execute("work-mode transparent")
		a.execute("exit")
		a.close()

		try:
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "输入数字错误，请重新输入" in web_info3
			assert "输入数字错误，请重新输入" in web_info4
			assert "输入数字错误，请重新输入" in web_info5
			assert "输入数字错误，请重新输入" in web_info6
			assert "输入数字错误，请重新输入" in web_info7
			assert "已经存在" in webinfo8
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "成功" in loginfo1
			assert "成功" in loginfo2
			assert "输入数字错误，请重新输入" in web_info3
			assert "输入数字错误，请重新输入" in web_info4
			assert "输入数字错误，请重新输入" in web_info5
			assert "输入数字错误，请重新输入" in web_info6
			assert "输入数字错误，请重新输入" in web_info7
			assert "已经存在" in webinfo8

		del_vlan_inte_all(browser)

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(hostip=dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])