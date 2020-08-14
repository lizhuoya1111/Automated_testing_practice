import pytest
import time
import sys
from os.path import dirname, abspath
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_static_route import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_interface import *
from page_obj.scg.scg_def_ipv4acl import *
from page_obj.common.rail import *
from page_obj.common.telnet import *
from page_obj.common.ssh import *
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "139762"


def test_c139762(browser):

	try:
		login_web(browser, url=dev1)
		add_obj_zone(browser, "t23296", "d", [interface_name_5])
		add_acl_rule_complete_wxw(browser, aclgroup_name='default', source_zone_interface='Z:t23296',
		                          source_address_object='yes', s_address_object='A:any',
		                          d_address_object='A:any', dest_zone_interface=interface_name_2, service='P:any',
		                          schdule='-- 无 --', accept='no', drop='yes', auth='-- 无 --', log='no')
		del_obj_zone_byname(browser, "t23296")
		del_info = browser.find_element_by_xpath('//*[@id="box"]/div[3]/ul/li[2]').text.rstrip()
		# print(del_info)

		try:
			assert "对象正在使用" == str(del_info)
			rail_pass(test_run_id, test_id)

		except Exception as err1:
			print(err1)
			rail_fail(test_run_id, test_id)
			assert "对象正在使用" == str(del_info)

		del_ipv4_acl_byid(browser, "1", "default")
		del_obj_zone_byname(browser, "t23296")


	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		print(err)
		rail_fail(test_run_id, test_id)
		reload(dev1)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + test_id + ".py"])
