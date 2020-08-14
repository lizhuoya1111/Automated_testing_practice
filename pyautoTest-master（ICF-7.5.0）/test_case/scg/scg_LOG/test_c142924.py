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
from page_obj.scg.scg_def_acl import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.scg.scg_def_sys import *
from page_obj.scg.scg_def import *


test_id = 142924
# 在traffic日志中，设置include条件为源ip，查询该源ip产生的所有日志
#
def test_c142924(browser):
	try:
		# 登录admin
		login_web(browser, url=dev1)
		# 删除默认ACL
		del_default_acl_group_lzy(browser)

		# 添加ACL 全通开log
		add_acl_group_complete(browser, name='lzy', enable='yes')
		add_ipv4acl_lzy(browser, aclgroup_name='lzy', source_zone_interface='Z:any',
						source_custom='no', fromip='', fromnetmask='',
						source_address_object='yes', s_address_object='A:any',
						mac='', dest_zone_interface='Z:any',
						dest_custom='no', toip='', tonetmask='',
						dest_address_object='yes', d_address_object='A:any',
						service='P:any', schdule='-- 无 --',
						accept='yes', drop='no',
						auth='-- 无 --', icf='no', log='yes', save='yes', cancel='no')

		# 添加82到83 与83到82的路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("ip route 13.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()

		shell_83 = Shell_SSH()
		shell_83.connect(hostip=dev3)
		shell_83.execute("en")
		shell_83.execute("conf t")
		shell_83.execute("ip route 12.1.1.0/24 gateway 13.1.1.1")
		shell_83.close()

		# 流量日志过滤级别改为all
		edit_log_filter_lzy(browser, index="4", all='yes', debug='yes/no', info='yes/no', notice='yes/no',
							warning='yes/no', error='yes/no', critical='yes/no', emerg='yes/no', alert="yes/no")

		# 删除日志
		delete_log(browser, log_type=流量日志)

		# 先用82ping83  使本条流量日志源地址=[12.1.1.2]
		sign_out_jyl(browser)
		login_web(browser, url=dev2)
		sleep(1)
		info1 = diag_ping(browser, ipadd="13.1.1.3", interface=interface_name_2)
		# print(info1)

		sign_out_jyl(browser)
		login_web(browser, url=dev1)
		# 查询日志
		query_security_or_traffic_log_lzy(browser, log_type=流量日志, ambiguous_search="",
										  from_ip="12.1.1.2", exclude_from_ip="", to_ip="", exclude_to_ip="", from_port="",
										  to_port="",
										  protocol="", exclude_protocol="", start_date="", start_time="", end_date="",
										  end_time="")


		# 获取信息
		sleep(0.5)
		info2 = browser.find_element_by_xpath('//*[@id="src_portarea0"]').text
		# print(info2)

		# 还原
		# 删除ACL
		del_all_acl_group_lzy(browser)
		# 还原流量日志过滤级别error critical alert emerg
		edit_log_filter_lzy(browser, index="4", all='yes/no', debug='yes/no', info='yes/no', notice='yes/no',
							warning='yes/no', error='yes', critical='yes', emerg='yes', alert="yes")
		# 删除日志
		delete_log(browser, log_type=流量日志)
		# 删82上路由
		shell_82 = Shell_SSH()
		shell_82.connect(hostip=dev2)
		shell_82.execute("en")
		shell_82.execute("conf t")
		shell_82.execute("no ip route 13.1.1.0/24 gateway 12.1.1.1")
		shell_82.close()
		# 删83上路由
		shell_83 = Shell_SSH()
		shell_83.connect(hostip=dev3)
		shell_83.execute("en")
		shell_83.execute("conf t")
		shell_83.execute("no ip route 12.1.1.0/24 gateway 13.1.1.1")
		shell_83.close()

		try:
			assert '12.1.1.2' in info2
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert '12.1.1.2' in info2
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=[dev1, dev2, dev3])
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
