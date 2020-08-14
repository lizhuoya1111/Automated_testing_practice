import pytest
import time
import sys
import math
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_log import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *

test_id = 142906
# 根据时间日期查询security日志
# 1.设置为同一天查询日志
# 2.起始日期小于终止日期查询

def test_c142906(browser):
	try:
		# 登录admin
		login_web(browser, url=dev1)
		# 安全日志过滤级别改为all
		edit_log_filter_lzy(browser, index="3", all='yes', debug='yes/no', info='yes/no', notice='yes/no',
							warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no")

		# IPMac绑定
		add_ip_mac_binding_jyl(browser, ip="12.1.1.2", interface=interface_name_2, mac_add="auto_mac")
		# 设置
		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_2, source_mac_binding="enable",
									 policy_for_undefined_host="alert")
		# 登录Dev2 修改2接口ip
		sign_out_jyl(browser)
		login_web(browser, url=dev2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.2")
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.3', mask='24')
		# 82 ping 12.1.1.1
		sleep(1)
		info1 = diag_ping(browser, ipadd="12.1.1.1", interface=interface_name_2)
		print(info1)

		# 登录Dev1
		sign_out_jyl(browser)
		login_web(browser, url=dev1)

		# 获取系统当前日期
		date1 = get_time_date_lzy(browser)
		print(date1)

		# 设置为同一天查询日志
		query_security_or_traffic_log_lzy(browser, log_type=安全日志, ambiguous_search="",
									  from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="", to_port="",
									  protocol="", exclude_protocol="", start_date=date1, start_time="", end_date=date1, end_time="")


		# 获取页面信息
		info1 = browser.find_element_by_xpath('//*[@id="datearea0"]').text
		print(info1)


		# 起始时间设置为固定日期
		date2 = '2000-01-01'
		print(date2)

		# 起始日期小于终止日期查询
		query_security_or_traffic_log_lzy(browser, log_type=安全日志, ambiguous_search="",
										  from_ip="", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="",
										  to_port="", protocol="", exclude_protocol="", start_date=date2, start_time="",
										  end_date=date1, end_time="")
		# 获取页面信息 //*[@id="datearea0"]
		info2 = browser.find_element_by_xpath('//*[@id="datearea0"]').text
		print(info2)

		# 还原
		# 还原安全日志过滤级别error critical alert emerg
		edit_log_filter_lzy(browser, index="3", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
							warning='yes/no', error='yes', critical='yes', emerg='yes', alert="yes")
		# 删除IPMac绑定
		delete_ip_mac_banding_jyl(browser, ip="12.1.1.2")
		# 恢复IPMac设置
		edit_ip_mac_binding_rule_jyl(browser, interface=interface_name_2, source_mac_binding="disenable",
									 policy_for_undefined_host="allow")
		# 82 接口2改IP
		sign_out_jyl(browser)
		login_web(browser, url=dev2)
		delete_physical_interface_ip_jyl(browser, interface=interface_name_2, ip="12.1.1.3")
		add_physical_interface_static_ip_jyl(browser, interface=interface_name_2, ip='12.1.1.2', mask='24')

		try:
			assert date1 in info1 and date1 in info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert date1 in info1 and date1 in info2

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False

if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
