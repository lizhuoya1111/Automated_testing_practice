import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_physical_interface import *
from page_obj.scg.scg_def_vlan_interface import *
from page_obj.scg.scg_def_ipv6 import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *

test_id = 141891
def test_c141891(browser):
	try:
		login_web(browser, url=dev1)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2002:48:3434:5689::", ipv6_mask="64")
		loginfo1 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2002:ac12:402::1", ipv6_mask="32")
		loginfo2 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2452:48:3434:5689::", ipv6_mask="126")
		loginfo3 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2462:48:3434:5689::", ipv6_mask="127")
		loginfo4 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2172:48:3434:5689::", ipv6_mask="128")
		loginfo5 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2002::12ac:1::", ipv6_mask="64")
		loginfo6 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="2002:48:3434:5689::", ipv6_mask="64")
		loginfo7 = get_log(browser, 管理日志)
		add_ipv6_add_jyl(browser, physical_interface=interface_name_4, ipv6_add="", ipv6_mask="64")
		loginfo8 = get_log(browser, 管理日志)
		delete_ipv6_add_jyl(browser, physical_interface=interface_name_4, interface_add="2002:48:3434:5689::/64")
		delete_ipv6_add_jyl(browser, physical_interface=interface_name_4, interface_add="2002:ac12:402::1/32")
		delete_ipv6_add_jyl(browser, physical_interface=interface_name_4, interface_add="2452:48:3434:5689::/126")
		delete_ipv6_add_jyl(browser, physical_interface=interface_name_4, interface_add="2462:48:3434:5689::/127")
		delete_ipv6_add_jyl(browser, physical_interface=interface_name_4, interface_add="2172:48:3434:5689::/128")

		time.sleep(1)
		try:
			assert "添加IPv6地址成功" in loginfo1
			assert "添加IPv6地址成功" in loginfo2
			assert "添加IPv6地址成功" in loginfo3
			assert "添加IPv6地址成功" in loginfo4
			assert "添加IPv6地址成功" in loginfo5
			assert "添加IPv6地址失败" in loginfo6
			assert "添加IPv6地址失败" in loginfo7
			assert "添加IPv6地址失败" in loginfo8
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "添加IPv6地址成功" in loginfo1
			assert "添加IPv6地址成功" in loginfo2
			assert "添加IPv6地址成功" in loginfo3
			assert "添加IPv6地址成功" in loginfo4
			assert "添加IPv6地址成功" in loginfo5
			assert "添加IPv6地址失败" in loginfo6
			assert "添加IPv6地址失败" in loginfo7
			assert "添加IPv6地址失败" in loginfo8
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
