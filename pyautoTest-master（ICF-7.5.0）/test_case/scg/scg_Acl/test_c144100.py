import pytest
import time
import sys
from page_obj.scg.scg_def import *
from page_obj.scg.scg_def_obj import *
from page_obj.scg.scg_def_log import *
from page_obj.common.rail import *
from page_obj.scg.scg_dev import *
from page_obj.scg.scg_def_firewall import *
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

test_id = "144100"
# 输入非法参数 4
# 配置一条Filter rule，源IP地址使用错误格式，非法的掩码地址。如2.2.2.0、33其他配置为默认配置。


def test_c144100(browser):

	try:
		login_web(browser, url=dev1)

		add_acl_group_complete(browser, name='acl_grp_100', enable='yes', sour='Z:any', dest='Z:any', desc='miaoshu', save='yes')

		add_acl_rule_before_save_wxw(browser, aclgroup_name='acl_grp_100', source_zone_interface=interface_name_4,
									 source_custom='yes', fromip='2.2.2.0', fromnetmask='33',
									 source_address_object='no', s_address_object='A:any',
									 mac='',
									 dest_custom='no', toip='', tonetmask='',
									 dest_address_object='yes', d_address_object='A:any',
									 dest_zone_interface=interface_name_2,
									 service='P:any', schdule='-- 无 --',
									 accept='yes', drop='no',
									 auth='-- 无 --', icf='no', log='no')

		# 点击保存
		browser.find_element_by_xpath('//*[@id="container"]/div[1]/form/div[2]/div[2]/div/input[6]').click()

		alert = browser.switch_to_alert().text
		# print(alert)
		browser.switch_to_alert().accept()

		del_acl_group_wxw(browser, name='acl_grp_100')


		try:
			assert "格式输入错误，请重新输入" in alert
			rail_pass(test_run_id, test_id)

		except:
			rail_fail(test_run_id, test_id)
			assert "格式输入错误，请重新输入" in alert

	except Exception as err:
		# 如果上面的步骤有报错，重新设备，恢复配置
		reload(hostip=dev1)
		print(err)
		rail_fail(test_run_id, test_id)
		assert False


if __name__ == '__main__':
	pytest.main(["-v", "-s", "test_c" + str(test_id) + ".py"])