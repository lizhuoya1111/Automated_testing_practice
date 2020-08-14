import pytest
import time
import sys
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
from page_obj.scg.scg_def import *

test_id = 142881
# 先产生安全日志 再删除
def test_c142881(browser):
	try:
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
		diag_ping(browser, ipadd="12.1.1.1", interface=interface_name_2)

		# 登录Dev1
		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		# 获取安全日志总数 不为0
		num2 = get_log_counts_lzy(browser, log_type=安全日志)
		print(num2)

		# 删除安全日志
		delete_log(browser, log_type=安全日志)
		# 获取安全日志总数为0
		num1 = get_log_counts_lzy(browser, log_type=安全日志)
		print(num1)
		# 获取管理日志
		log1 = get_log(browser, 管理日志)

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
			assert "刪除日志成功" in log1 and num1 == 0 and num2 != 0

			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "刪除日志成功" in log1 and num1 == 0 and num2 != 0
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
