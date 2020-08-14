import pytest
import time
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page_obj.scg.scg_def_ipv4acl import  *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_bridge import *
from page_obj.common.rail import *
from page_obj.scg.scg_def_physical_interface import  *
from page_obj.common.ssh import *
from page_obj.scg.scg_def_dhcp import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_ifname_OEM import *
from page_obj.common.ssh import *
from page_obj.scg.scg_def import *


test_id = 140560
def test_c140560(browser):
	try:
		login_web(browser, url=dev1)
		del_all_acl_group_noadd_wxw(browser)
		add_acl_group_wxw(browser, name='acl_group_jia_1')
		add_acl_rule_complete_wxw(browser, aclgroup_name='acl_group_jia_1', source_zone_interface="Z:any",
								  source_custom='no', fromip='', fromnetmask='',
								  source_address_object='yes', s_address_object='A:any',
								  mac='',
								  dest_custom='no', toip='', tonetmask='',
								  dest_address_object='yes', d_address_object='A:any',
								  dest_zone_interface='Z:any',
								  service='P:any', schdule='-- 无 --', accept='yes', drop='yes', auth='-- 无 --', log='no')

		to_ssh = Shell_SSH()
		to_ssh.connect("10.1.1.212", "root", "root")
		to_ssh.execute("ping 21.1.1.3 -c 2")
		time.sleep(5)
		ssh_info = to_ssh.output()
		print(ssh_info)

		del_all_acl_group_wxw(browser)

		try:
			assert "Unreachable" or "100% packet loss" in ssh_info
			rail_pass(test_run_id, test_id)
		except:
			rail_fail(test_run_id, test_id)
			assert "Unreachable" or "100% packet loss" in ssh_info
	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		reload(hostip=dev1)
		rail_fail(test_run_id, test_id)
		assert False



if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])
